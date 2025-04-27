import streamlit as st
import os
import requests
import datetime
import random
from typing import Dict, Any, List
from langchain_community.tools.tavily_search import TavilySearchResults

# Set API keys from Streamlit secrets
os.environ["TAVILY_API_KEY"] = st.secrets["TAVILY_API_KEY"]
WEATHER_API_KEY = st.secrets["WEATHER_API_KEY"]

# Function: Get current weather using WeatherAPI
def get_weather(location: str) -> Dict[str, Any]:
    try:
        base_url = "http://api.weatherapi.com/v1/current.json"
        params = {"key": WEATHER_API_KEY, "q": location, "aqi": "no"}
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "location": f"{data['location']['name']}, {data['location']['country']}",
            "temperature_c": data['current']['temp_c'],
            "temperature_f": data['current']['temp_f'],
            "condition": data['current']['condition']['text'],
            "humidity": data['current']['humidity'],
            "wind_kph": data['current']['wind_kph'],
            "last_updated": data['current']['last_updated']
        }
    except Exception as e:
        return {"error": f"Failed to get weather data: {str(e)}"}

# Function: Get top attractions using Tavily Search
def get_attractions(location: str) -> List[str]:
    try:
        tavily = TavilySearchResults()
        query = f"Top 5 tourist attractions in {location}"
        results = tavily.run(query)
        return results if results else ["No attractions found."]
    except Exception as e:
        return [f"Error fetching attractions: {str(e)}"]

# Function: Generate simulated cost estimates
def get_cost_estimates(location: str) -> Dict[str, str]:
    try:
        return {
            "Hotel": f"${random.randint(30, 150)} per night",
            "Food": f"${random.randint(10, 50)} per day",
            "Transport": f"${random.randint(5, 20)} per day",
            "Attractions": f"${random.randint(20, 100)} for tickets/tours"
        }
    except Exception as e:
        return {"error": f"Failed to generate cost data: {str(e)}"}

# Function: Simulate flight data from Mumbai
def get_flights_from_mumbai(destination: str) -> List[Dict[str, str]]:
    try:
        airlines = ["IndiGo", "Air India", "SpiceJet", "Vistara", "Go First"]
        flights = []
        today = datetime.date.today()
        for _ in range(3):
            date = today + datetime.timedelta(days=random.randint(1, 15))
            flights.append({
                "airline": random.choice(airlines),
                "departure": f"Mumbai",
                "arrival": destination,
                "date": str(date),
                "price": f"${random.randint(150, 800)}"
            })
        return flights
    except Exception as e:
        return [{"error": f"Failed to get flight data: {str(e)}"}]

# Formatters for Streamlit output
def format_weather_info(weather: Dict[str, Any]) -> str:
    if "error" in weather:
        return weather["error"]
    return (
        f"📍 Location: {weather['location']}\n"
        f"🌡️ Temperature: {weather['temperature_c']}°C / {weather['temperature_f']}°F\n"
        f"🌤️ Condition: {weather['condition']}\n"
        f"💧 Humidity: {weather['humidity']}%\n"
        f"💨 Wind: {weather['wind_kph']} km/h\n"
        f"🕒 Last Updated: {weather['last_updated']}"
    )

# def format_attractions_info(attractions: List[str], location: str) -> str:
#     if not attractions:
#         return "No attractions found."
#     return "\n".join([f"{i+1}. {place}" for i, place in enumerate(attractions)])
def format_attractions_info(attractions: List[Dict[str, Any]], location: str) -> str:
    if not attractions:
        return "No attractions found."

    formatted_list = []
    for i, place in enumerate(attractions[:5]):  # Show only top 5
        title = place.get('title', 'Unknown Attraction')
        url = place.get('url')
        if url:
            formatted_list.append(f"{i+1}. [{title}]({url})")
        else:
            formatted_list.append(f"{i+1}. {title}")
    
    return "\n".join(formatted_list)

def format_cost_info(costs: Dict[str, str]) -> str:
    if "error" in costs:
        return costs["error"]
    return "\n".join([f"{k}: {v}" for k, v in costs.items()])

def format_flight_info(flights: List[Dict[str, str]]) -> str:
    if "error" in flights[0]:
        return flights[0]["error"]
    return "\n\n".join([
        f"✈️ Airline: {f['airline']}\n🛫 From: {f['departure']} → 🛬 To: {f['arrival']}\n📅 Date: {f['date']}\n💵 Price: {f['price']}"
        for f in flights
    ])

# Streamlit App UI
st.set_page_config(page_title="Travel AI", page_icon="🌍")
st.title("🌍 Travel AI Assistant")
st.write("Get a personalized travel report including weather, attractions, cost, and flight info.")

destination = st.text_input("Enter a destination you'd like to explore:")

if st.button("Generate Travel Report") and destination:
    with st.spinner("Gathering information..."):
        weather = get_weather(destination)
        attractions = get_attractions(destination)
        cost = get_cost_estimates(destination)
        flights = get_flights_from_mumbai(destination)

        st.subheader("☁️ Weather")
        st.text(format_weather_info(weather))

        st.subheader("🏛️ Attractions")
        st.text(format_attractions_info(attractions, destination))

        st.subheader("💰 Cost Estimates")
        st.text(format_cost_info(cost))

        st.subheader("✈️ Flight Options")
        st.text(format_flight_info(flights))
