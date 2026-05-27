Let me read the relevant files first to give you a grounded review.

Now let me also check the WA review steering/skill files for the proper framework:

I have everything I need. Here is the full Well-Architected review of AgriNova AI.

---

# AgriNova AI — AWS Well-Architected Review

**Workload:** AgriNova AI Assistant (Challenge 5)
**Model:** Amazon Nova Pro via Amazon Bedrock
**Stack:** Strands Agents SDK · MCP · Mem0/FAISS · wttr.in · data.gov.in APIs · Local Excel/CSV datasets
**Lens applied:** ML/AI Workload + Standard 6-pillar WA Framework
**Finding counts:** 🔴 5 HRI · 🟡 6 MRI · 🟢 5 Improvements

---

## 🔴 High Risk Issues (HRI)

### HRI-1 — Security: API Key Hardcoded / Exposed at Runtime

**Finding:** `DATA_GOV_API_KEY` is referenced directly in the `market_price` tool and loaded from a `.env` file with no secret rotation, no scoping, and `BYPASS_TOOL_CONSENT = "true"` disables all tool-use guardrails.

**Impact:** If the `.env` file is committed or the process is inspected, the key leaks. Bypassing tool consent removes the last human-in-the-loop safety check for all tool calls.

**Recommendation:**
- Store secrets in **AWS Secrets Manager** or **AWS Systems Manager Parameter Store** and fetch at startup.
- Remove `BYPASS_TOOL_CONSENT = "true"` or gate it behind an environment flag that is `false` by default in production.
- Add `.env` to `.gitignore` (verify it is already there).

**Effort:** Low | **AWS Services:** Secrets Manager, SSM Parameter Store

---

### HRI-2 — Security: No Authentication or Authorization on the Agent

**Finding:** The agent runs as a bare CLI loop with no user identity, no session isolation, and no access control. Any process that can reach the terminal can query the agent and trigger live API calls and memory writes.

**Impact:** Unauthorized use, data poisoning of the Mem0/FAISS memory store, and uncontrolled API spend.

**Recommendation:**
- Wrap the agent behind **Amazon Cognito** + **API Gateway** if exposing as a service.
- For CLI use, add a simple session token or farmer ID that scopes memory reads/writes.
- Apply **IAM least-privilege** to the Bedrock invocation role — scope it to `bedrock:InvokeModel` on the specific model ARN only.

**Effort:** Medium | **AWS Services:** Cognito, API Gateway, IAM

---

### HRI-3 — Reliability: No Error Handling or Retry Logic on External APIs

**Finding:** Both `weather()` and `rainfall_prediction()` call `wttr.in` with a bare `requests.get()` and a single broad `except Exception`. `market_price()` does the same against `data.gov.in`. There are no timeouts, no retries, and no fallback.

**Impact:** A transient API failure silently returns an error string to the farmer with no retry. A slow response blocks the entire synchronous agent loop.

**Recommendation:**
- Add `timeout=` to all `requests.get()` calls (e.g., 5–10 seconds).
- Use **exponential backoff with jitter** (the `tenacity` library or manual retry loop).
- Cache last-known-good responses in **Amazon ElastiCache** or a local TTL dict so the agent can serve stale-but-useful data during outages.

**Effort:** Low | **AWS Services:** ElastiCache (optional), Lambda (if moving to serverless)

---

### HRI-4 — Security: Training Data Loaded from Local Filesystem at Startup

**Finding:** Seven Excel/CSV files are loaded with `pd.read_excel()` / `pd.read_csv()` using relative paths at module import time. There is no integrity check, no schema validation, and no access control on these files.

**Impact:** A corrupted or tampered dataset silently poisons all scheme, eligibility, and water management recommendations. A missing file crashes the entire agent at startup.

**Recommendation:**
- Store training data in **Amazon S3** with versioning and server-side encryption (SSE-S3 or SSE-KMS).
- Add schema validation (e.g., `pandera`) after loading.
- Wrap each `pd.read_*` in a try/except with a graceful degradation message rather than a hard crash.

**Effort:** Medium | **AWS Services:** S3, KMS

---

### HRI-5 — Reliability: Single-Process, Stateful, Blocking Architecture

**Finding:** The entire agent — MCP client, memory, all tools, and the chat loop — runs in a single Python process with a synchronous `while True` loop. The `with aws_docs_mcp:` context manager means MCP is torn down if the process crashes.

**Impact:** Any unhandled exception kills the session and all in-flight state. No horizontal scaling is possible. One slow tool call (e.g., a hanging API request) blocks all other interactions.

**Recommendation:**
- Move to an **async architecture** using `asyncio` or migrate tools to **AWS Lambda** functions invoked via **Amazon Bedrock Agents** action groups.
- Use **Amazon SQS** to decouple farmer queries from tool execution.
- Persist session state externally (DynamoDB) so crashes are recoverable.

**Effort:** High | **AWS Services:** Lambda, Bedrock Agents, SQS, DynamoDB

---

## 🟡 Medium Risk Issues (MRI)

### MRI-1 — Performance Efficiency: No Response Caching

**Finding:** Every query to `weather`, `rainfall_prediction`, and `market_price` makes a live HTTP call regardless of how recently the same data was fetched. Weather data changes at most hourly; market prices are updated once daily.

**Recommendation:** Add a simple TTL cache (Python `cachetools.TTLCache` or Redis/ElastiCache). Weather: 30-min TTL. Market prices: 6-hour TTL. This also reduces external API quota consumption.

**Effort:** Low | **AWS Services:** ElastiCache for Redis

---

### MRI-2 — Cost Optimization: No Token Budget or Model Tiering

**Finding:** Every query — including simple ones like "fertilizer for 5 acres" — invokes Amazon Nova Pro, the highest-capability (and highest-cost) model in the Nova family.

**Recommendation:**
- Route simple, deterministic queries (fertilizer calculator, crop calendar lookup) to **Amazon Nova Lite** or handle them as pure tool calls without LLM inference.
- Use **prompt caching** (Bedrock prompt caching feature) for the system prompt, which is long and repeated on every turn.
- Set a `max_tokens` budget per turn to prevent runaway responses.

**Effort:** Low–Medium | **AWS Services:** Amazon Bedrock (Nova Lite, prompt caching)

---

### MRI-3 — Operational Excellence: No Observability

**Finding:** There is no logging beyond `print()` statements, no metrics, no tracing, and no alerting. The `stream_callback` only prints to stdout.

**Recommendation:**
- Integrate **Amazon CloudWatch Logs** for structured logging (tool invocations, latencies, errors).
- Use **AWS X-Ray** for distributed tracing across Bedrock calls and tool executions.
- Define SLOs: e.g., p95 response time < 5s, tool error rate < 1%.
- Add a CloudWatch alarm for API error spikes.

**Effort:** Medium | **AWS Services:** CloudWatch, X-Ray, CloudWatch Alarms

---

### MRI-4 — Reliability: Mem0/FAISS Memory Has No Backup or Persistence Guarantee

**Finding:** FAISS is an in-memory vector index. If the process restarts, all farmer memory (preferences, farm location, crop history) is lost unless Mem0 is configured to persist to disk or a managed store.

**Recommendation:**
- Configure Mem0 to back the vector store with **Amazon OpenSearch Serverless** or **Amazon Aurora pgvector**.
- Alternatively, periodically snapshot the FAISS index to **S3**.

**Effort:** Medium | **AWS Services:** OpenSearch Serverless, Aurora PostgreSQL (pgvector), S3

---

### MRI-5 — Security: No Input Validation or Prompt Injection Defense

**Finding:** User input flows directly into tool parameters (e.g., `crop`, `city`, `district`) and into the agent's context without sanitization. The system prompt guardrails are soft — they instruct the model to refuse, but do not enforce at the code level.

**Recommendation:**
- Validate and sanitize tool inputs (length limits, allowlisted characters for city/crop names).
- Use **Amazon Bedrock Guardrails** to enforce topic restrictions, PII redaction, and content filtering at the API level — not just via system prompt instructions.
- Consider **AWS WAF** if the agent is exposed via API Gateway.

**Effort:** Medium | **AWS Services:** Bedrock Guardrails, WAF

---

### MRI-6 — Cost Optimization: Local Excel Files Reloaded on Every Process Start

**Finding:** All seven training datasets are loaded into memory at startup unconditionally, even if only one tool is called. For large datasets this wastes memory and startup time.

**Recommendation:**
- Use **lazy loading** — load each DataFrame only when its tool is first called.
- For production, move to **Amazon DynamoDB** or **Aurora Serverless** for structured lookups, which also enables partial queries instead of full in-memory scans.

**Effort:** Low | **AWS Services:** DynamoDB, Aurora Serverless

---

## 🟢 Improvement Opportunities

### IMP-1 — Sustainability: No Scale-to-Zero

The agent runs continuously even when idle. Moving to **AWS Lambda** (event-driven) or **Amazon ECS Fargate** with scale-to-zero eliminates idle compute cost and carbon footprint.

---

### IMP-2 — Performance Efficiency: MCP Server Startup Latency

The `aws_docs_mcp` client starts a subprocess via `stdio_client` on every run. This adds cold-start latency. Consider keeping the MCP server as a persistent sidecar or using the HTTP transport variant if available.

---

### IMP-3 — Operational Excellence: No CI/CD or IaC

There is no deployment pipeline, no infrastructure-as-code, and no automated tests. Add **AWS CDK** or **SAM** for infrastructure, and a **GitHub Actions** or **AWS CodePipeline** workflow with at least a smoke test before deployment.

---

### IMP-4 — Reliability: Soil Health Advisor Uses Hardcoded Rules

The `soil_health_advisor` tool uses a simple `if/elif` chain with hardcoded crop lists. This is brittle and not extensible. Consider backing it with the training data layer (a soil-crop mapping dataset) for consistency and maintainability.

---

### IMP-5 — Sustainability: No Data Lifecycle Policy on Training Data

Training datasets in S3 (once migrated) should have **S3 Lifecycle policies** to transition older versions to S3 Glacier and expire stale data, reducing storage cost and carbon impact.

---

## Prioritized Remediation Plan

| Priority | Finding | Effort | Impact |
|---|---|---|---|
| 1 | HRI-1 — Secrets in .env / bypass tool consent | Low | 🔴 Critical |
| 2 | HRI-3 — No timeouts/retries on external APIs | Low | 🔴 High |
| 3 | MRI-1 — No response caching | Low | 🟡 Medium |
| 4 | MRI-2 — No token budget / model tiering | Low | 🟡 Medium |
| 5 | HRI-4 — Local training data, no validation | Medium | 🔴 High |
| 6 | MRI-3 — No observability | Medium | 🟡 Medium |
| 7 | HRI-2 — No auth/authz | Medium | 🔴 High |
| 8 | MRI-5 — No input validation / Bedrock Guardrails | Medium | 🟡 Medium |
| 9 | MRI-4 — FAISS memory not persisted | Medium | 🟡 Medium |
| 10 | HRI-5 — Blocking single-process architecture | High | 🔴 High |

---

## Next Steps

1. **This week (quick wins):** Fix secrets management (Secrets Manager), add request timeouts, add TTL caching for weather/market APIs, and set `max_tokens`.
2. **This sprint:** Enable Bedrock Guardrails, add CloudWatch structured logging, migrate training data to S3 with schema validation.
3. **Next sprint:** Introduce async architecture (Lambda + SQS or Bedrock Agents), add Cognito auth, persist memory to OpenSearch or pgvector.
4. **Ongoing:** Set up CDK/SAM IaC, CI/CD pipeline, and SLO dashboards in CloudWatch.

---

**Overall assessment:** AgriNova AI is a well-featured prototype with strong domain coverage. The core risks are in Security (secrets, no auth, no guardrails enforcement) and Reliability (no retries, blocking loop, ephemeral memory). The good news is the top-priority fixes are all low-effort and can be done without restructuring the application.