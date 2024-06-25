import time
import requests

# Desk API endpoints
DESK_API_URL = 'http://desk.local/control'
DESK_SIT_POSITION = 50  # Example position value for sitting
DESK_STAND_POSITION = 120  # Example position value for standing

def set_desk_position(position):
    """Sets the desk position via API."""
    response = requests.post(DESK_API_URL, json={'position': position})
    if response.status_code == 200:
        print(f"Desk moved to position {position}")
    else:
        print(f"Failed to move desk: {response.content}")

def alternate_desk_position():
    """Alternates desk position between sitting and standing every hour."""
    sitting = True
    while True:
        if sitting:
            print("Switching to standing position.")
            set_desk_position(DESK_STAND_POSITION)
        else:
            print("Switching to sitting position.")
            set_desk_position(DESK_SIT_POSITION)
        
        sitting = not sitting
        time.sleep(3600)  # Wait for one hour

if __name__ == "__main__":
    alternate_desk_position()
