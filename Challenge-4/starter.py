"""
Challenge 4: The Full Agent — Tools + Memory + Streaming
Model: Amazon Nova Pro via Bedrock
"""

import os
import requests

os.environ["BYPASS_TOOL_CONSENT"] = "true"

from datetime import date, datetime

from strands import Agent, tool
from strands_tools import calculator, mem0_memory

MODEL = "us.amazon.nova-pro-v1:0"


# ============================================================
# Streaming Callback Handler
# ============================================================

def stream_callback(**kwargs):

    if "data" in kwargs:
        print(kwargs["data"], end="", flush=True)

    elif (
        "current_tool_use" in kwargs
        and kwargs["current_tool_use"].get("name")
    ):
        print(
            f"\n🔧 Using tool: "
            f"{kwargs['current_tool_use']['name']}"
        )


# ============================================================
# Real Weather Tool using wttr.in API
# ============================================================

@tool
def weather(city: str) -> str:
    """Get real-time weather information for a city.

    Args:
        city: Name of the city
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

        return f"❌ Unable to fetch weather for {city}: {str(e)}"


# ============================================================
# Age Calculator Tool
# ============================================================

@tool
def age_calculator(birth_date: str) -> str:
    """Calculate age from birth date.

    Args:
        birth_date: Date in YYYY-MM-DD format
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

    return f"🎂 The person is {age} years old."


# ============================================================
# Motivation Tool
# ============================================================

@tool
def motivation(topic: str) -> str:
    """Provide motivational advice.

    Args:
        topic: Topic for motivation
    """

    return (
        f"🚀 Keep learning {topic}! "
        f"Every project you build improves your skills "
        f"and brings you closer to becoming an expert engineer."
    )


# ============================================================
# Full AI Agent
# ============================================================

agent = Agent(

    model=MODEL,

    tools=[
        calculator,
        weather,
        age_calculator,
        motivation,
        mem0_memory
    ],

    callback_handler=stream_callback,

    system_prompt="""
    You are a fun and intelligent AI assistant powered by Amazon Nova Pro 🤖🚀

    Your capabilities:
    - Perform calculations 🧮
    - Provide real-time weather 🌤️
    - Calculate age 🎂
    - Remember user preferences 🧠
    - Motivate users 🚀

    Rules:
    - Be friendly and professional
    - Use emojis naturally
    - Keep responses concise
    - Use tools whenever required
    - Never expose internal reasoning or thinking process
    """
)


# ============================================================
# Interactive Chat Loop
# ============================================================

print("=" * 70)
print("🤖 Full AI Agent Initialized")
print("=" * 70)

print("\n💡 Example Prompts:")
print("- What's the weather in Madurai?")
print("- How old is someone born on 2002-04-26?")
print("- What is 365 * 24?")
print("- Motivate me to become a GenAI Engineer")
print("- Remember that my favorite AWS service is Bedrock")
print("- What is my favorite AWS service?")

print("\nType 'quit' to exit.\n")


while True:

    try:

        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in (
            "quit",
            "exit",
            "q"
        ):

            print("\n👋 Session ended successfully.")
            break

        print("\nAgent: ", end="")

        agent(user_input)

        print("\n")

    except KeyboardInterrupt:

        print("\n\n👋 Session interrupted.")
        break

    except Exception as e:

        print(f"\n❌ Error: {str(e)}")


print("\n✅ Challenge 4 complete! 🏆")