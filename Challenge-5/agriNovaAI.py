"""
Challenge 5 - AgriNova AI Assistant 🌾🚜
Advanced Smart Farming AI Agent

Built using:
- Amazon Nova Pro
- Strands Agents SDK
- MCP Server
- Memory
- Streaming
- Real-Time APIs
- Government Market Price API

Features:
✅ Real-time Weather
✅ Rainfall Prediction
✅ Soil Health Analysis
✅ Smart Irrigation Advisor
✅ Live Market Price API
✅ Multi-Crop Planning
✅ Fertilizer Calculator
✅ Farmer Memory
✅ Tamil + English Support
✅ AWS Agriculture Guidance using MCP
"""

import os
import requests

os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent, tool
from strands.tools.mcp import MCPClient

from strands_tools import (
    calculator,
    mem0_memory
)

from mcp import (
    StdioServerParameters,
    stdio_client
)

MODEL = "us.amazon.nova-pro-v1:0"

# ============================================================
# Government API Key
# ============================================================




# ============================================================
# Streaming Callback
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
# Real-Time Weather Tool
# ============================================================

@tool
def weather(city: str) -> str:
    """
    Get real-time weather information.

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

        return f"❌ Unable to fetch weather: {str(e)}"


# ============================================================
# Rainfall Prediction Tool
# ============================================================

@tool
def rainfall_prediction(city: str) -> str:
    """
    Predict rainfall possibility.

    Args:
        city: City name
    """

    try:

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        data = response.json()

        forecast = data["weather"][0]

        rain_chance = forecast["hourly"][0]["chanceofrain"]

        if int(rain_chance) > 60:

            return (
                f"🌧️ High chance of rainfall in {city} "
                f"today ({rain_chance}%). "
                f"Avoid irrigation and fertilizer spraying."
            )

        else:

            return (
                f"☀️ Low rainfall chance in {city} "
                f"today ({rain_chance}%). "
                f"Irrigation can be planned."
            )

    except Exception as e:

        return f"❌ Unable to predict rainfall: {str(e)}"


# ============================================================
# Soil Health Advisor
# ============================================================

@tool
def soil_health_advisor(
    soil_type: str,
    ph: float,
    moisture: str
) -> str:
    """
    Analyze soil and recommend crops.

    Args:
        soil_type: Soil type
        ph: Soil pH
        moisture: Moisture level
    """

    soil = soil_type.lower()

    crops = []

    if "black" in soil:

        crops = [
            "Cotton",
            "Soybean",
            "Groundnut"
        ]

    elif "red" in soil:

        crops = [
            "Millets",
            "Groundnut",
            "Pulses"
        ]

    elif "clay" in soil:

        crops = [
            "Rice",
            "Broccoli",
            "Cabbage"
        ]

    elif "sandy" in soil:

        crops = [
            "Watermelon",
            "Coconut",
            "Groundnut"
        ]

    else:

        crops = [
            "Rice",
            "Maize",
            "Vegetables"
        ]

    if ph < 5.5:

        ph_advice = (
            "⚠️ Soil is acidic. "
            "Add lime or organic compost."
        )

    elif ph > 7.5:

        ph_advice = (
            "⚠️ Soil is alkaline. "
            "Use organic manure."
        )

    else:

        ph_advice = (
            "✅ Soil pH is suitable for farming."
        )

    return (
        f"🌱 Soil Analysis Result:\n"
        f"Soil Type: {soil_type}\n"
        f"Soil pH: {ph}\n"
        f"Moisture: {moisture}\n\n"
        f"Recommended Crops:\n"
        f"- " + "\n- ".join(crops) + "\n\n"
        f"{ph_advice}"
    )


# ============================================================
# Smart Irrigation Advisor
# ============================================================

@tool
def irrigation_advisor(
    crop: str,
    weather_condition: str
) -> str:
    """
    Suggest irrigation advice.

    Args:
        crop: Crop name
        weather_condition: Weather condition
    """

    weather_condition = weather_condition.lower()

    if "rain" in weather_condition:

        return (
            f"🌧️ Rain expected.\n"
            f"Avoid irrigating the {crop} crop today."
        )

    elif "sunny" in weather_condition:

        return (
            f"☀️ Sunny climate detected.\n"
            f"Moderate irrigation is recommended "
            f"for {crop} crops."
        )

    else:

        return (
            f"💧 Monitor soil moisture carefully "
            f"before irrigating {crop}."
        )


# ============================================================
# Live Market Price Tool
# ============================================================

@tool
def market_price(
    crop: str,
    district: str = "",
    state: str = "Tamil Nadu"
) -> str:
    """
    Fetch live mandi market prices.

    Args:
        crop: Commodity/crop name
        district: District name
        state: State name
    """

    try:

        # ====================================================
        # Clean Input
        # ====================================================

        crop = crop.replace("?", "").strip().title()

        district = (
            district
            .replace("?", "")
            .strip()
            .title()
        )

        state = (
            state
            .replace("?", "")
            .strip()
            .title()
        )

        BASE_URL = (
            "https://api.data.gov.in/resource/"
            "9ef84268-d588-465a-a308-a864a43d0070"
        )

        params = {

            "api-key": DATA_GOV_API_KEY,

            "format": "json",

            "limit": 10,

            "filters[commodity]": crop
        }

        if district:

            params["filters[district]"] = district

        if state:

            params["filters[state]"] = state

        headers = {

            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64)"
            ),

            "Accept": "application/json"
        }

        

       

        response = requests.get(

            BASE_URL,

            params=params,

            headers=headers
        )

       
        

        

        data = response.json()

        records = data.get("records", [])

        if not records:

            return (
                f"❌ No market price data found "
                f"for {crop} in {district}."
            )

        result = (
            f"💰 {crop} Prices in "
            f"{district}:\n\n"
        )

        for item in records[:5]:

            market = item.get(
                "market",
                "Unknown"
            )

            market = (
                market
                .replace("(Uzhavar Sandhai )", "")
                .strip()
            )

            result += (

                f"📍 Market : {market}\n"
                
                 f"📊 Variety : "
                f"₹{item.get('variety')}\n"

                f"📊 Modal Price : "
                f"₹{item.get('modal_price')}\n"

                f"⬇️ Min Price : "
                f"₹{item.get('min_price')}\n"

                f"⬆️ Max Price : "
                f"₹{item.get('max_price')}\n"

                f"{'-' * 35}\n"
            )

        return result

    except Exception as e:

        return f"❌ Error: {str(e)}"
# ============================================================
# Multi-Crop Planner
# ============================================================

@tool
def multicrop_planner(crop: str) -> str:
    """
    Suggest multi-cropping ideas.

    Args:
        crop: Main crop
    """

    crop = crop.lower()

    if "rice" in crop:

        return (
            "🌾 Rice Multi-Cropping Ideas:\n"
            "- Rice + Pulses\n"
            "- Rice + Fish Farming\n"
            "- Rice + Vegetables"
        )

    elif "coconut" in crop:

        return (
            "🌴 Coconut Multi-Cropping Ideas:\n"
            "- Coconut + Banana\n"
            "- Coconut + Pepper\n"
            "- Coconut + Pineapple"
        )

    else:

        return (
            "🌱 General Multi-Cropping Suggestions:\n"
            "- Main crop + Pulses\n"
            "- Main crop + Vegetables"
        )


# ============================================================
# Fertilizer Calculator
# ============================================================

@tool
def fertilizer_calculator(area: float) -> str:
    """
    Estimate fertilizer requirement.

    Args:
        area: Farm area in acres
    """

    fertilizer = area * 50

    return (
        f"🧪 Estimated fertilizer needed "
        f"for {area} acres is approximately "
        f"{fertilizer} kg."
    )


# ============================================================
# Farming Tip Tool
# ============================================================

@tool
def farming_tip(crop: str) -> str:
    """
    Provide farming guidance.

    Args:
        crop: Crop name
    """

    return (
        f"🌱 Farming Tip for {crop}:\n"
        f"Use proper irrigation, monitor pests regularly, "
        f"and maintain soil nutrients for better yield."
    )


# ============================================================
# AWS Documentation MCP
# ============================================================

aws_docs_mcp = MCPClient(

    lambda: stdio_client(

        StdioServerParameters(
            command="awslabs.aws-documentation-mcp-server"
        )
    )
)


# ============================================================
# Main Application
# ============================================================

with aws_docs_mcp:

    mcp_tools = aws_docs_mcp.list_tools_sync()

    agent = Agent(

        model=MODEL,

        tools=[
            calculator,
            weather,
            rainfall_prediction,
            soil_health_advisor,
            irrigation_advisor,
            market_price,
            multicrop_planner,
            fertilizer_calculator,
            farming_tip,
            mem0_memory,
            *mcp_tools
        ],

        callback_handler=stream_callback,

        system_prompt="""
            You are AgriNova AI Assistant 🌾🚜

            Responsibilities:
            - Help farmers using smart agriculture guidance
            - Analyze soil and recommend crops
            - Suggest irrigation strategies
            - Predict rainfall and weather impacts
            - Provide live crop market prices
            - Support sustainable farming
            - Explain AWS smart farming technologies
            - Remember farmer preferences

            Language Support:
            - Support Tamil and English
            - Reply in the same language as the user

            Safety Guardrails:
            - Only provide agriculture and farming related guidance
            - Never provide harmful, illegal, violent, or unsafe instructions
            - Never suggest dangerous chemical misuse
            - Never generate hateful, abusive, or toxic content
            - If the user asks unrelated harmful questions, politely refuse
            - Avoid medical, political, or illegal advice
            - Always encourage safe and sustainable farming practices

            Behavior Rules:
            - Be practical and supportive
            - Use emojis naturally
            - Keep responses concise
            - Use tools whenever required
            - Never expose internal reasoning
            - Never expose API keys or secrets
            """
    )

    print("=" * 90)
    print("🌾 AgriNova AI Assistant Initialized")
    print("=" * 90)

    print("\n💡 Example Questions:")
    print("- What's the weather in Madurai?")
    print("- Will it rain in Madurai today?")
    print("- Soil type is black soil, pH 6.5")
    print("- Suggest crops for red soil")
    print("- Market price of tomato")
    print("- Current onion mandi price")
    print("- Should I irrigate rice crops during rainy weather?")
    print("- Fertilizer needed for 5 acres")
    print("- Explain IoT in smart farming")
    print("- என் நிலம் கரிசல் மண். எந்த பயிர் நல்லா வளரும்?")

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

            print("\nAgriNova: ", end="")

            agent(user_input)

            print("\n")

        except KeyboardInterrupt:

            print("\n\n👋 Session interrupted.")
            break

        except Exception as e:

            print(f"\n❌ Error: {str(e)}")


print("\n✅ Challenge 5 complete! 🏆")