import schedule
import time

# Function to roll up the blind
def roll_up_blind():
    print("Rolling up the blind...")

# Schedule the blind to roll up every morning at 5:30 AM
schedule.every().day.at("05:30").do(roll_up_blind)

# Schedule the blind to roll up every evening at 6:00 PM
schedule.every().day.at("18:00").do(roll_up_blind)

# Keep the script running to maintain the schedule
while True:
    schedule.run_pending()
    time.sleep(1)
