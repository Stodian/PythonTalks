import schedule
import time
import pyttsx3
import pandas as pd
from datetime import datetime

# Load the readings from the CSV file
readings_df = pd.read_csv('readings.csv')

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def read_bible_readings():
    today = datetime.now().strftime('%Y-%m-%d')
    reading = readings_df[readings_df['Date'] == today]
    
    if not reading.empty:
        reading1 = reading.iloc[0]['Reading1']
        reading2 = reading.iloc[0]['Reading2']
        reading3 = reading.iloc[0]['Reading3']
        
        engine.say(f"Today's Bible readings are:")
        engine.say(reading1)
        engine.say(reading2)
        engine.say(reading3)
        engine.runAndWait()
    else:
        engine.say("No readings found for today.")
        engine.runAndWait()

# Schedule the readings at 10 PM every day
schedule.every().day.at("22:00").do(read_bible_readings)

print("Script running. Waiting for scheduled readings...")

while True:
    schedule.run_pending()
    time.sleep(1)
