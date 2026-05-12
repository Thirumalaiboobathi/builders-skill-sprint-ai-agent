"""
Challenge 3: Agent with Persistent Memory
Give your agent memory that survives restarts using FAISS.
Model: Amazon Nova Pro via Bedrock
"""

import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent
from strands_tools import mem0_memory

MODEL = "us.amazon.nova-pro-v1:0"


# ============================================================
# Create an agent with mem0_memory tool
# ============================================================

agent = Agent(
    model=MODEL,
    tools=[mem0_memory],
    system_prompt="""
        You are an intelligent AI memory assistant powered by Amazon Nova Pro.

        Responsibilities:
        - Remember important user preferences and personal details
        - Recall stored memories accurately
        - Maintain conversational continuity across sessions

        Rules:
        - Do not expose internal thinking or tool execution.
        - Do not mention errors related to memory tools unless absolutely necessary.
        - Respond naturally and professionally.
        - When memory retrieval succeeds, answer directly.

        Examples:
        User: Remember that my name is Ravi and I love biryani
        Assistant: ✅ I'll remember that!

        User: What's my name and what food do I like?
        Assistant: Your name is Ravi and you love biryani.
        """
)


# ============================================================
# Interactive loop — chat with the memory agent
# ============================================================

print("🧠 Memory Agent Ready!")
print("Try: 'Remember that my name is Boopathi and I love biryani'")
print("Then: 'What's my name and what food do I like?'")
print("Type 'quit' to exit.\n")

while True:
    try:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "q"):
            print("Bye! 👋")
            break

        # Send user input to the agent
        response = agent(user_input)

        print(f"Agent: {response}")

    except KeyboardInterrupt:
        print("\nBye! 👋")
        break

print("\n✅ Challenge 3 complete!")