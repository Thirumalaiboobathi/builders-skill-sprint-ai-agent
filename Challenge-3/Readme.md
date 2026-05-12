# Challenge 3 - Persistent Memory AI Agent using FAISS 

## Overview

This project demonstrates how to build an AI Agent with persistent memory using:

- Amazon Bedrock
- Amazon Nova Pro
- Strands SDK
- mem0 Memory Tool
- FAISS Vector Storage

The agent can remember user preferences and personal information across multiple sessions using vector-based memory storage.

---

## Features

- Persistent AI Memory
- Memory survives application restarts
- FAISS-based vector storage
- AI-powered conversational memory
- Amazon Nova Pro integration
- Interactive memory chat interface

---

## Technologies Used

- Python
- Amazon Bedrock
- Amazon Nova Pro
- Strands SDK
- mem0 Memory
- FAISS
- AWS CLI

---

## Project Structure

```text
Challenge-3/
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
pip install mem0ai
pip install faiss-cpu
pip install opensearch-py
pip install boto3
```

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

## Add IAM Permission

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

## Example Interactions

### Store User Information

```text
Remember that my name is Boobathi and I love biryani
```

```text
Remember that I want to become a GenAI Engineer
```

```text
Remember that my favorite AWS service is Bedrock
```

---

### Retrieve Information

```text
What is my name?
```

```text
What career goal did I mention?
```

```text
What is my favorite AWS service?
```

---

## Screenshots

### Memory Storage Demo

![Memory Storage](screenshots/ss1.png)

![Memory Retrieval](screenshots/ss2.png)

---

## Learning Outcomes

Through this challenge, I learned:

- How persistent memory works in AI agents
- Basics of vector databases and FAISS
- How AI agents store and retrieve semantic memories
- Integration of Amazon Bedrock with memory systems
- Conversational AI memory workflows
- AI agent continuity across sessions

---

## Notes

Persistent memory storage using mem0 + FAISS was successfully integrated.

Some memory retrieval operations showed compatibility limitations with the current Bedrock provider setup during retrieval operations.

---

