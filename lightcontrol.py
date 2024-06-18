import requests
import time
import RPi.GPIO as GPIO

# Home Assistant configuration
HA_URL = "http://localhost:8123/api"
HA_TOKEN = "YOUR_LONG_LIVED_ACCESS_TOKEN"

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json"
}

def set_light_brightness(entity_id, brightness):
    url = f"{HA_URL}/services/light/turn_on"
    payload = {
        "entity_id": entity_id,
        "brightness": brightness
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    return response.json()

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start_time = time.time()
    stop_time = time.time()

    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    return distance

# Setup GPIO
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

light_entity_id = "light.your_light_entity_id"

try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance:.1f} cm")

        # Assuming max distance of 200 cm, and min brightness of 10
        if distance < 200:
            brightness = max(10, int((200 - distance) * (255 / 200)))
            set_light_brightness(light_entity_id, brightness)
            print(f"Setting brightness to {brightness}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()
