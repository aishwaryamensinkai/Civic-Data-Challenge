from flask import Flask, render_template, request
import folium
import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import openai

app = Flask(__name__)

# Set up OpenAI API
openai.api_key = ''

def generate_crime_summary(location):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Generate a crime summary for the location: {location}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def geocode_address(address, retries=3):
    geolocator = Nominatim(user_agent="civic_data_challenge")
    for attempt in range(retries):
        try:
            location = geolocator.geocode(address, timeout=10)
            if location:
                return (location.latitude, location.longitude)
            else:
                return (None, None)
        except GeocoderTimedOut:
            if attempt < retries - 1:
                continue
            else:
                raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crime_summary', methods=['POST'])
def crime_summary():
    location = request.form['location']
    summary = generate_crime_summary(location)
    return render_template('summary.html', location=location, summary=summary)

if __name__ == '__main__':
    # Generate the crime map
    data = pd.read_csv('./data/Part1.csv')
    crime_map = folium.Map(location=[43.0481, -76.1474], zoom_start=12)
    for index, row in data.iterrows():
        # Example address; replace with actual column names if necessary
        address = row['ADDRESS']
        lat, lon = geocode_address(address)
        if lat and lon:
            folium.Marker([lat, lon], popup=row['CODE_DEFINED']).add_to(crime_map)
    crime_map.save('static/crime_map.html')
    
    app.run(debug=True)
