#🌤️ #Advanced Weather Dashboard
A Streamlit web app that shows live weather data, a 3-day forecast, interactive charts, and lets you download reports as CSV & PDF.
Built using wttr.in for weather scraping — no API keys required!

🔥 Features
✅ Live current weather:

Temperature, humidity, wind speed, weather condition

Emoji icons based on weather description

✅ 3-day forecast:

Displays date, max/min temperatures, sky condition in a clean table

✅ Interactive line chart:

Plots temperature trends over the forecast period using Plotly

✅ Download reports:

Download forecast as CSV or PDF with a single click

✅ Dark/Light theme toggle:

Switch themes directly in the app for better viewing

🛠 Tech stack & libraries used
Tool	What it does
🐍 Python	Base language
🚀 Streamlit	Interactive web app framework
🌐 Requests	To scrape weather data from wttr.in
🐼 Pandas	For structured forecast tables & CSV export
📊 Plotly	For plotting temperature trends
📝 FPDF2	For generating downloadable PDF reports
🖌 CSS	Used via st.markdown to apply dynamic dark/light themes

⚙ How it works
Fetches weather data for the specified city using:

perl
Copy
Edit
https://wttr.in/<city>?format=j1
Parses JSON to get current conditions & forecast.

Displays data in Streamlit widgets and Plotly charts.

Generates downloadable CSV & PDF reports.

Theme toggle changes page styles on the fly.

🚀 Getting started
🔧 Installation
Clone this repo and install dependencies:

bash
Copy
Edit
git clone https://github.com/yourusername/weather-dashboard
cd weather-dashboard
pip install -r requirements.txt
▶️ Run locally
bash
Copy
Edit
streamlit run weather_project.py
🌐 Deploy on Streamlit Cloud
Push your project to GitHub.

Go to streamlit.io/cloud.

Click "New app from GitHub", select your repo and branch, set weather_project.py as the main file.

🚀 Done — your app is live!

📷 Screenshots
Current Weather & Forecast Table	Interactive Chart & Downloads
