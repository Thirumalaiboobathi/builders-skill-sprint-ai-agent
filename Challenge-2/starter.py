"""
Challenge 2: Adding Tools to Your Agent
Give your agent a calculator, weather tool, and age calculator.
Model: Amazon Nova Pro via Bedrock
"""

import os
import requests

os.environ["BYPASS_TOOL_CONSENT"] = "true"

from datetime import date, datetime
from strands import Agent, tool
from strands_tools import calculator

MODEL = "us.amazon.nova-pro-v1:0"


# ============================================================
# Weather Tool using Real-Time API
# ============================================================

@tool
def weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: The name of the city.
    """

    try:

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]

        description = current["weatherDesc"][0]["value"]

        humidity = current["humidity"]

        wind_speed = current["windspeedKmph"]

        return (
            f"🌤️ Weather in {city}:\n"
            f"Condition: {description}\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} km/h"
        )

    except Exception as e:

        return f"❌ Unable to fetch weather data: {str(e)}"


# ============================================================
# Age Calculator Tool
# ============================================================

@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from a birth date.

    Args:
        birth_date: Date of birth in YYYY-MM-DD format.
    """

    birth = datetime.strptime(
        birth_date,
        "%Y-%m-%d"
    ).date()

    today = date.today()

    age = (
        today.year
        - birth.year
        - (
            (today.month, today.day)
            < (birth.month, birth.day)
        )
    )

    return f"The person is {age} years old."


# ============================================================
# Create Agent with All Tools
# ============================================================

agent = Agent(

    model=MODEL,

    tools=[
        calculator,
        weather,
        age_calculator
    ],

    system_prompt="""
    You are an AWS and Generative AI assistant.

    Help users with:
    - mathematical calculations
    - weather information
    - age calculations

    Respond in a friendly and helpful way.
    """
)


# ============================================================
# Test the Agent
# ============================================================

# Math Test
print("🧮 Math test:")

response = agent("What is 42 * 17?")

print(response)


# Weather Test
print("\n🌤️ Weather test:")

response = agent("What's the weather in Chennai?")

print(response)


# Age Test
print("\n🎂 Age test:")

response = agent(
    "How old is someone born on 2000-05-15?"
)

print(response)


print("\n✅ Challenge 2 complete!")