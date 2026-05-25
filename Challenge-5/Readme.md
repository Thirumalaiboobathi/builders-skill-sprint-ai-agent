# Challenge 5 - AgriNova AI Assistant 🌾🚜

## Overview

AgriNova AI Assistant is an advanced AI-powered smart farming assistant built using:

- Amazon Bedrock
- Amazon Nova Pro
- Strands Agents SDK
- MCP (Model Context Protocol)
- FAISS Memory
- Real-Time APIs
- Streaming Responses

The assistant helps farmers using AI-driven agriculture guidance and intelligent tool orchestration.

---

## Features

The AgriNova AI Assistant combines multiple agricultural intelligence capabilities:

| Capability | Description |
|------------|-------------|
| 🌤️ Real-Time Weather Intelligence | Live weather insights using APIs |
| 🌧️ Rainfall Prediction | Rain probability for irrigation planning |
| 🌱 Soil Health Analysis | Soil type, pH and crop recommendations |
| 💧 Water Management Intelligence | River / Well / Pond / Rainfed planning |
| 🚜 Irrigation Advisor | Crop irrigation guidance |
| 💰 Government Market Price Engine | Live mandi prices with market-level details |
| 🌾 Multi-Crop Planner | Intercropping suggestions |
| 🧪 Fertilizer Calculator | Fertilizer estimation |
| 🏛️ Government Scheme Discovery | Central + Tamil Nadu schemes |
| ✅ Scheme Eligibility Engine | Farmer eligibility analysis |
| 🚜 Equipment Subsidy Discovery | Government equipment subsidies |
| 🤝 Equipment Rental Ecosystem | Government / PPP / Private rentals |
| 📅 Crop Calendar Planner | Crop lifecycle planning |
| 📈 Farm Profit Calculator | Revenue and expense estimation |
| 🧠 Persistent Farmer Memory | Mem0 + FAISS |
| ⚡ Streaming Responses | Callback streaming |
| ☁️ AWS Documentation MCP | AWS guidance integration |
| 🇮🇳 Tamil + English Support | Multilingual interaction |
| 🛡️ AI Safety Guardrails | Safe agriculture workflows |

---
# 🌤️ Real-Time Weather Tool

Fetch live weather information using the wttr.in API.

Provides:
- Temperature
- Humidity
- Wind speed
- Weather conditions

---

# 🌧️ Rainfall Prediction Tool

Predicts rainfall probability for better irrigation planning and farming decisions.

---

# 🌱 Soil Health Analysis

Analyze:
- Soil type
- Soil pH
- Moisture level

Suggest suitable crops for farming.

---

# 💧 Smart Irrigation Advisor

Provides irrigation recommendations based on weather conditions.

---

# 💰 Live Market Price Tool

Fetch live mandi market prices using the Government of India Agmarknet API.

Provides:
- Market name
- State
- Min / Max / Modal prices

---

# 🌾 Multi-Cropping Planner

Suggests companion crops and intercropping strategies.

---

# 🧪 Fertilizer Calculator

Estimate fertilizer requirements based on farm area.

---

# 🏛️ Government Scheme Discovery Engine

AgriNova AI includes structured agricultural datasets covering both **Central Government** and **Tamil Nadu Government** schemes.

## Central Government Schemes

| Scheme | Category |
|---------|-----------|
| PM-KISAN | Income Support |
| PMFBY | Crop Insurance |
| PMKSY | Irrigation |
| MIDH | Horticulture |
| SMAM | Mechanization |
| eNAM | Market Access |
| Soil Health Card | Soil Health |
| Agricultural Infrastructure Fund | Infrastructure |

---

## Tamil Nadu Government Schemes

| Scheme | Category |
|---------|-----------|
| TN Micro Irrigation Scheme | Irrigation |
| Uzhavar Sandhai | Market |
| Tamil Nadu Millet Mission | Millets |
| Coconut Development Programme | Plantation |
| Collective Farming Programme | Agriculture |
| Precision Farming Development | Horticulture |

---

Example:

```text
Schemes for coconut farming
```

Output:

```text
Central:

PMKSY

MIDH

Tamil Nadu:

Coconut Development Programme

TN Micro Irrigation Scheme
```

---

# 💧 Water Intelligence Layer

AgriNova AI supports water-aware agricultural planning by considering both **water source** and **water availability**.

Supported ecosystems:

| Water Source | Planning Support |
|--------------|------------------|
| River Irrigation | Flood / controlled irrigation |
| Well Irrigation | Water conservation planning |
| Pond Irrigation | Storage-based irrigation |
| Rainfed Farming | Drought crop guidance |

---

Example:

```text
Crop:
Rice

Water Source:
Well Irrigation

Water Availability:
Low
```

Output:

```text
Recommendation:

SRI Method

Water Saving Practices:

Alternate irrigation

Mulching
```

---

Example crop recommendations:

| Crop | Water Source | Water Availability | Recommendation | Technique |
|-------|--------------|--------------------|---------------|-----------|
| Rice | River | High | Controlled flooding | AWD |
| Rice | Well | Medium | SRI | Alternate irrigation |
| Millets | Rainfed | Low | Drought crops | Mulching |
| Coconut | Pond | Medium | Drip irrigation | Micro irrigation |
| Banana | Well | Low | Water scheduling | Drip |

---

# 🚜 Farm Equipment Ecosystem

AgriNova AI supports both **equipment subsidy discovery** and **equipment rental ecosystems**.

## Equipment Subsidy Discovery

| Equipment | Central Scheme | State Scheme |
|-----------|----------------|--------------|
| Tractor | SMAM | Farm Mechanization Scheme |
| Rotavator | SMAM | TN Mechanization Support |
| Harvester | SMAM | State Subsidy |
| Drone | Precision Agriculture | TN Pilot Programs |
| Seed Drill | SMAM | State Support |

---

Example:

```text
Subsidy for tractor
```

Output:

```text
Central:

SMAM

State:

Farm Mechanization Scheme
```

---

## Equipment Rental Ecosystem

AgriNova AI supports rental discovery through:

| Provider Type |
|---------------|
| Government Centers |
| PPP Providers |
| Farmer Producer Organizations (FPO) |
| Private Operators |

Example:

```text
Rental for harvester
```

---

# 📅 Crop Calendar Planner

AgriNova AI includes crop lifecycle planning and activity scheduling.

Example:

```text
Crop calendar for rice
```

Output:

| Stage | Duration | Activity |
|--------|-----------|-----------|
| Sowing | 0–20 days | Nursery preparation |
| Vegetative | 20–60 days | Fertilizer application |
| Flowering | 60–90 days | Water management |
| Harvest | 100–120 days | Harvest |

---

Example crop calendar datasets:

| Crop | Stage | Duration Days | Activity |
|------|--------|---------------|-----------|
| Rice | Sowing | 0–20 | Nursery preparation |
| Rice | Vegetative | 20–60 | Fertilizer application |
| Banana | Planting | 0–30 | Pit preparation |
| Coconut | Maintenance | Monthly | Fertilizer + irrigation |

---

# 🚜 Farm Equipment Ecosystem

AgriNova AI supports both **equipment subsidy discovery** and **equipment rental ecosystems**.

## Equipment Subsidy Discovery

| Equipment | Central Scheme | State Scheme |
|-----------|----------------|--------------|
| Tractor | SMAM | Farm Mechanization Scheme |
| Rotavator | SMAM | TN Mechanization Support |
| Harvester | SMAM | State Subsidy |
| Drone | Precision Agriculture | TN Pilot Programs |
| Seed Drill | SMAM | State Support |

---

Example:

```text
Subsidy for tractor
```

Output:

```text
Central:

SMAM

State:

Farm Mechanization Scheme
```

---

## Equipment Rental Ecosystem

AgriNova AI supports rental discovery through:

| Provider Type |
|---------------|
| Government Centers |
| PPP Providers |
| Farmer Producer Organizations (FPO) |
| Private Operators |

Example:

```text
Rental for harvester
```

---

# 📅 Crop Calendar Planner

AgriNova AI includes crop lifecycle planning and activity scheduling.

Example:

```text
Crop calendar for rice
```

Output:

| Stage | Duration | Activity |
|--------|-----------|-----------|
| Sowing | 0–20 days | Nursery preparation |
| Vegetative | 20–60 days | Fertilizer application |
| Flowering | 60–90 days | Water management |
| Harvest | 100–120 days | Harvest |

---

Example crop calendar datasets:

| Crop | Stage | Duration Days | Activity |
|------|--------|---------------|-----------|
| Rice | Sowing | 0–20 | Nursery preparation |
| Rice | Vegetative | 20–60 | Fertilizer application |
| Banana | Planting | 0–30 | Pit preparation |
| Coconut | Maintenance | Monthly | Fertilizer + irrigation |

---

# 📚 Agricultural Knowledge Layer

AgriNova AI uses structured datasets to power agricultural intelligence workflows.

Training datasets:

```text
training_data/

TN_Schemes.csv

central gov schemes.xlsx

water_management.xlsx

farm_equipment_subsidy.xlsx

farm_equipment_rental.xlsx

crop_calendar.xlsx

scheme_eligibility.xlsx
```

---

Dataset overview:

| Dataset | Purpose |
|----------|----------|
| TN_Schemes.csv | Tamil Nadu government schemes |
| central gov schemes.xlsx | Central government schemes |
| water_management.xlsx | Water planning intelligence |
| farm_equipment_subsidy.xlsx | Equipment subsidy engine |
| farm_equipment_rental.xlsx | Rental ecosystem |
| crop_calendar.xlsx | Crop lifecycle planning |
| scheme_eligibility.xlsx | Farmer eligibility rules |

---

# 💡 Example Prompts

## Weather

```text
What's the weather in Madurai?
```

```text
Will it rain in Chennai today?
```

---

## Market Intelligence

```text
What is today's tomato price in Madurai?
```

```text
Tomato price in Usilampatti
```

---

## Government Schemes

```text
Schemes for coconut farming
```

---

## Scheme Eligibility

```text
Small farmer

3 acres

Banana
```

---

## Equipment Subsidy

```text
Subsidy for tractor
```

---

## Equipment Rental

```text
Rental for harvester
```

---

## Water Planning

```text
Rice

Well irrigation

Low water availability
```

---

## Crop Calendar

```text
Crop calendar for rice
```

---

## Profit Calculation

```text
Farm profit for banana cultivation
```

---


# 🧠 Persistent Farmer Memory

Store and recall:
- Farmer preferences
- Crop interests
- Farm locations

Using:
- mem0
- FAISS vector memory

---

# ⚡ Streaming AI Responses

Displays AI responses in real time using callback handlers.

---

# ☁️ AWS MCP Integration

Integrated with:
- AWS Documentation MCP Server

Allows the assistant to explain:
- AWS IoT
- Smart farming architectures
- Cloud-based agriculture solutions
- AI-powered farming systems

---

# 🛡️ AI Safety Guardrails

AgriNova AI Assistant includes basic AI safety guardrails implemented through system-level response constraints.

The assistant is designed to:

- Provide only agriculture and farming-related guidance
- Avoid harmful, illegal, or unsafe instructions
- Prevent toxic or abusive responses
- Encourage safe and sustainable farming practices
- Protect sensitive information such as API keys and secrets

These guardrails help ensure responsible AI interactions while supporting practical farming use cases.

---


## AWS Configuration

### Configure AWS CLI

```bash
aws configure
```
Provide:

```text
AWS Access Key ID
AWS Secret Access Key
Default region: us-east-1
Default output format: json
```

---


## Enable Amazon Bedrock

- Open AWS Console
- Navigate to Amazon Bedrock
- Select region:

```text
us-east-1
```

- Enable access for:

```text
Amazon Nova Pro
```

---

## IAM Permission

Attach the following policy to your IAM user:

```text
AmazonBedrockFullAccess
```

---

## Run the Project

```bash
python starter.py
```

---

## Screenshots

### Memory Storage Demo

![Full Agent Demo](screenshots/SS1.png)

![Full Agent Demo](screenshots/SS2.png)

![Full Agent Demo](screenshots/SS3.png)

---

# 💡 Example Prompts

## 🌤️ Weather

```text
What's the weather in Madurai?
```

```text
Will it rain in Chennai today?
```

---

## 🌱 Soil Analysis

```text
My soil type is black soil with pH 6.5
```

```text
Suggest crops for red soil
```

---

## 💰 Market Prices

```text
What is the market price of tomato?
```

```text
Current onion mandi price
```

```text
Rice market price in India
```

---

## 💧 Irrigation

```text
Should I irrigate rice crops during rainy weather?
```

---

## 🌾 Multi-Cropping

```text
Suggest multi-cropping ideas for coconut farming
```

---

## 🧪 Fertilizer Calculator

```text
Fertilizer needed for 5 acres
```

---

## 🧠 Memory

```text
Remember that my farm is in Madurai
```

```text
What is my farm location?
```

---

## 🇮🇳 Tamil Questions

```text
மதுரையில் இன்று மழை வருமா?
```

```text
தக்காளி சந்தை விலை என்ன?
```

```text
எந்த பயிர் நல்லா வளரும்?
```

---

# 🧠 Learning Outcomes

| Topic | Learning |
|---------|-----------|
| AI Agents | Strands Agents SDK |
| Foundation Model | Amazon Nova Pro |
| Memory | Mem0 + FAISS |
| MCP | AWS Documentation MCP |
| APIs | Weather + Government Market APIs |
| Agriculture Intelligence | Schemes + Water + Equipment |
| Knowledge Layer | CSV + Excel datasets |
| Multilingual AI | Tamil + English |
| Real-world AI | Smart farming workflows |

---

# 📝 Notes

- Weather data is fetched using wttr.in API
- Market prices use Government Agmarknet APIs
- Memory is implemented using Mem0 + FAISS
- AWS Documentation MCP enables AWS guidance
- Agricultural intelligence uses structured datasets
- Tamil language support is powered through Amazon Nova Pro multilingual capabilities

---