# Challenge 2 - AI Agent with Tools using Amazon Nova Pro 🚀

## Overview

This project demonstrates how to build an AI Agent with tool-calling capabilities using:

- Amazon Bedrock
- Amazon Nova Pro
- Strands SDK
- Custom Python Tools

The AI agent can intelligently decide when to use tools such as:

- Calculator Tool
- Weather Tool
- Age Calculator Tool

This challenge introduces the concept of AI Tool Calling Agents used in modern Generative AI systems.

---

## Features

- AI Agent powered by Amazon Nova Pro
- Tool Calling using Strands SDK
- Custom Weather Tool
- Custom Age Calculator Tool
- Mathematical Calculations using Calculator Tool
- AWS Bedrock Integration

---

## Technologies Used

- Python
- Amazon Bedrock
- Amazon Nova Pro
- Strands SDK
- Strands Agents Tools
- AWS CLI

---

## Project Structure

```text
Challenge-2/
│
├── starter.py
├── README.md
└── screenshots/
    ├── ss1.png
    └── ss2.png
```

---

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

---

### 2. Activate Virtual Environment

#### Windows CMD

```bash
venv\Scripts\activate
```

#### Git Bash

```bash
source venv/Scripts/activate
```

---

### 3. Install Dependencies

```bash
pip install strands-agents
pip install strands-agents-tools
pip install boto3
```

---

## AWS Configuration

### 1. Configure AWS CLI

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

### 2. Enable Amazon Bedrock Access

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

### 3. Add IAM Permission

Attach the following policy to the IAM user:

```text
AmazonBedrockFullAccess
```

---

## Run the Project

```bash
python starter.py
```

---

## Sample Questions

### Calculator Tool

- What is 42 * 17?

### Weather Tool

- What's the weather in Chennai?

### Age Calculator Tool

- How old is someone born on 2000-05-15?

---

## Screenshots


### Successful Output

![Successful Output](screenshots/image.png)

---

## Learning Outcomes

Through this challenge, I learned:

- How AI agents use tools dynamically
- How Amazon Bedrock works
- How to integrate Amazon Nova Pro with Python
- Basics of Tool Calling AI Agents
- AWS authentication and IAM permissions
- Building custom tools using Strands SDK

---

