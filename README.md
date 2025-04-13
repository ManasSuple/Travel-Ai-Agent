
---

# 🌍 AI-Powered Travel Assistant

This project is an intelligent **Travel Planning Agent** built using **LangChain**, **Gemini API**, and real-time data tools. It helps you plan a trip by generating:

- Local weather reports  
- Top attractions  
- Daily budget estimates  
- Flight information from Mumbai  
- Travel tips – all in one place!

### 🚀 Features

- 🌤️ Real-time weather via WeatherAPI
- 🏛️ Top 5 attractions from Tavily Search
- 💰 Daily cost breakdown (budget to luxury)
- ✈️ Simulated flight suggestions from Mumbai
- 📋 Full travel report with formatting
- ⚙️ Simple CLI app – just run and input your destination

---

## 🔮 Future Improvements

- ✅ Add real flight API (Skyscanner, Amadeus, etc.)
- ✅ Add hotel suggestions
- ✅ Interactive Streamlit front-end
- ✅ Save multiple reports
- ✅ Travel plan export as PDF

---

## 🛠️ Setup

### 1. Install Dependencies

```bash
pip install langchain langchain_google_genai langchain_community requests google-generativeai
```

---

## 🔑 API Keys Configuration

Set your API keys inside the script or via environment variables:

```python
os.environ["GOOGLE_API_KEY"] = "your-gemini-key"
os.environ["TAVILY_API_KEY"] = "your-tavily-key"
WEATHER_API_KEY = "your-weatherapi-key"
```

---

## 🧱 Project Structure

```
.
├── final_travel_agent.py     # Main script to generate the travel report
└── README.md                 # This documentation file
```

---

## 🧠 How It Works

1. User enters a destination
2. App fetches:
   - 🌀 Live weather
   - 🏛️ Attractions
   - 💸 Budget estimates (simulated)
   - ✈️ Flights from Mumbai (simulated)
3. Compiles a **well-formatted travel report**
4. Adds bonus travel tips

---

## ▶️ Run the App

Just run the script:

```bash
python final_travel_agent.py
```

Sample interaction:

```
Enter a destination you'd like to visit: Tokyo

Processing your request...
🌍 TRAVEL REPORT FOR TOKYO 🌍
🌤️ CURRENT WEATHER...
🏛️ TOP ATTRACTIONS...
💰 ESTIMATED COSTS...
✈️ FLIGHTS FROM MUMBAI...
✨ TRAVEL TIPS...
```

---

## 🧠 Tech Stack

- **LangChain** — Tool chaining and agent logic  
- **Google Gemini** — Intelligent content generation  
- **WeatherAPI** — Real-time weather data  
- **Tavily Search** — Tourist info and cost data  
- **Python CLI** — Lightweight interaction

---

## 📈 Example Report Sections

- Weather:
  ```
  Temperature: 25°C / 77°F
  Condition: Clear sky
  Wind: 10 kph
  ```

- Attractions:
  ```
  1. Tokyo Tower
     Tokyo’s iconic landmark offering panoramic views...
  ```

- Cost:
  ```
  Budget: $80/day | Mid: $150/day | Luxury: $300/day
  ```

- Flights:
  ```
  Air India | ₹23,000 | Duration: 9h 20m | Direct
  ```

---

## 🤝 Contributing

Fork the repo and improve it — add APIs, UX, or local caching!

---

## 📫 Contact

Feel free to connect with me on GitHub.  
Suggestions, ideas, and pull requests are welcome!

---

## 📜 License

MIT License — free to use and modify.

---
