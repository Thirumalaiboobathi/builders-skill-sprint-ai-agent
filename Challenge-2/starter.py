"""
Challenge 2: Adding Tools to Your Agent
Give your agent a calculator, weather tool, and age calculator.
Model: Amazon Nova Pro via Bedrock
"""

import os
os.environ["BYPASS_TOOL_CONSENT"] = "true"

from datetime import date, datetime
from strands import Agent, tool
from strands_tools import calculator

MODEL = "us.amazon.nova-pro-v1:0"


# ============================================================
# TODO 1: Create a custom weather tool
# ============================================================

@tool
def weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: The name of the city.
    """

    return f"The weather in {city} is sunny, 28°C."


# ============================================================
# TODO 2: Create a custom age calculator tool
# ============================================================

@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from a birth date.

    Args:
        birth_date: Date of birth in YYYY-MM-DD format.
    """

    birth = datetime.strptime(birth_date, "%Y-%m-%d").date()

    today = date.today()

    age = (
        today.year
        - birth.year
        - ((today.month, today.day) < (birth.month, birth.day))
    )

    return f"The person is {age} years old."


# ============================================================
# TODO 3: Create an agent with all tools
# ============================================================

agent = Agent(
    model=MODEL,
    tools=[calculator, weather, age_calculator],
    system_prompt="""
    You are an AWS and Generative AI assistant.
    Help users with calculations, weather information,
    and age calculations in a friendly way.
    """
)


# ============================================================
# TODO 4: Test the agent with different questions
# ============================================================

# Test math
print("🧮 Math test:")
response = agent("What is 42 * 17?")
print(response)

# Test weather
print("\n🌤️ Weather test:")
response = agent("What's the weather in Chennai?")
print(response)

# Test age
print("\n🎂 Age test:")
response = agent("How old is someone born on 2000-05-15?")
print(response)


print("\n✅ Challenge 2 complete!")