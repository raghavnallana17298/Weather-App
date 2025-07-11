import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from fpdf import FPDF

# ----------------------------
# Function to get weather data
# ----------------------------
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# -----------------------------------
# Function to map descriptions to emojis
# -----------------------------------
def get_weather_icon(description):
    desc = description.lower()
    if "sunny" in desc or "clear" in desc:
        return "☀️"
    elif "cloud" in desc:
        return "☁️"
    elif "rain" in desc:
        return "🌧️"
    elif "thunder" in desc:
        return "⛈️"
    elif "snow" in desc:
        return "❄️"
    else:
        return "🌡️"

# -----------------------------
# Function to create PDF from DataFrame
# -----------------------------
def create_pdf(forecast_df, city):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Weather Forecast for {city.capitalize()}", ln=True, align='C')
    pdf.ln(10)

    # Table header
    pdf.cell(40, 10, "Date", 1)
    pdf.cell(40, 10, "Max Temp (°C)", 1)
    pdf.cell(40, 10, "Min Temp (°C)", 1)
    pdf.cell(70, 10, "Condition", 1)
    pdf.ln()

    # Table rows
    for _, row in forecast_df.iterrows():
        pdf.cell(40, 10, row["Date"], 1)
        pdf.cell(40, 10, str(row["Max Temp (°C)"]), 1)
        pdf.cell(40, 10, str(row["Min Temp (°C)"]), 1)
        pdf.cell(70, 10, row["Condition"], 1)
        pdf.ln()
    
    # Convert bytearray to bytes
    return bytes(pdf.output(dest='S'))

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("🌤️ Weather App")
st.write("Get live weather updates, 3-day forecast, and download reports!")

city = st.text_input("Enter City Name:", value="Lucknow")

if st.button("Get Weather"):
    with st.spinner("Fetching weather data..."):
        data = get_weather(city)
    if data:
        # Current weather
        current = data["current_condition"][0]
        temp_c = current["temp_C"]
        desc = current["weatherDesc"][0]["value"]
        icon = get_weather_icon(desc)
        humidity = current["humidity"]
        wind = current["windspeedKmph"]

        st.header(f"Current Weather in {city.capitalize()}")
        st.metric("🌡 Temperature (°C)", temp_c)
        st.write(f"{icon} **Condition:** {desc}")
        st.write(f"💧 **Humidity:** {humidity}%")
        st.write(f"🌬 **Wind Speed:** {wind} km/h")

        # Forecast table
        st.subheader("📅 3-Day Forecast")
        days = []
        max_temps = []
        min_temps = []
        conditions = []

        for day in data["weather"]:
            days.append(day["date"])
            max_temps.append(int(day["maxtempC"]))
            min_temps.append(int(day["mintempC"]))
            conditions.append(day["hourly"][4]["weatherDesc"][0]["value"])

        forecast_df = pd.DataFrame({
            "Date": days,
            "Max Temp (°C)": max_temps,
            "Min Temp (°C)": min_temps,
            "Condition": conditions
        })

        st.table(forecast_df)

        # Download CSV
        csv = forecast_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Forecast as CSV",
            data=csv,
            file_name=f"{city}_forecast.csv",
            mime='text/csv'
        )

        # Download PDF
        pdf_data = create_pdf(forecast_df, city)
        st.download_button(
            label="📄 Download Forecast as PDF",
            data=pdf_data,
            file_name=f"{city}_forecast.pdf",
            mime='application/pdf'
        )

        # Line chart
        fig = px.line(forecast_df, x="Date", y=["Max Temp (°C)", "Min Temp (°C)"],
                      markers=True, title=f"Temperature Trend for {city.capitalize()}")
        st.plotly_chart(fig)
    else:
        st.error("Could not fetch weather data. Please check city name or try again later.")
