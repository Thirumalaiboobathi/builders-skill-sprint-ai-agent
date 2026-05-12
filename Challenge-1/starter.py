"""
Challenge 1: Your First AI Agent
Build a simple agent using Strands SDK + Ollama (runs locally!)
"""

from strands import Agent
from strands.models.ollama import OllamaModel


# Create Ollama model
ollama_model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.2:3b"
)


# Create Pirate AI Agent 🏴‍☠️
agent = Agent(
    model=ollama_model,
    tools=[],
    system_prompt="""
    You are Captain BlackByte, a funny pirate AI assistant.
    Always respond like a pirate.
    Use pirate words like:
    - Ahoy!
    - Matey!
    - Arrr!
    - Ye!
    Keep responses short, fun, and entertaining.
    """
)


# Ask multiple questions
questions = [
    "Tell me a fact about AWS Cost Optimization",
    "How does Amazon Bedrock help in Generative AI applications?",
    "Why is cloud computing important for AI and Machine Learning?",
    "What are the benefits of using AWS Lambda in serverless applications?",
    "How can I become a successful GenAI Engineer using AWS services?"
]


print("🏴‍☠️ Pirate AI Agent Started!\n")

for i, question in enumerate(questions, start=1):
    print(f"🧑 Question {i}: {question}")

    response = agent(question)

    print(f"🤖 Pirate Agent: {response}")
    print("-" * 60)


print("\n✅ Bonus Challenge Complete!")