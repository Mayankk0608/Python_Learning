import cv2
import pytesseract
import time
import tkinter as tk
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

camera_url = "http://192.168.1.21:8080/video"

def detect_vehicle_number(frame):
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        
        vehicle_number = pytesseract.image_to_string(thresh, config='--psm 8').strip()

        return vehicle_number
    except Exception as e:
        print(f"Error in detecting vehicle number: {e}")
        return None

def calculate_fare(entry_time, exit_time):
    time_parked = exit_time - entry_time
    fare = (time_parked // 3600) * 20 
    return fare

cap = cv2.VideoCapture(camera_url)

if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

vehicle_data = {}  
is_parked = False
entry_time = None
vehicle_number = None

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture image.")
        break

    cv2.imshow("Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        vehicle_number = detect_vehicle_number(frame)
        if vehicle_number:
            print(f"Detected Vehicle Number: {vehicle_number}")
            if vehicle_number not in vehicle_data:
                vehicle_data[vehicle_number] = {'entry_time': time.time()}
                print(f"Entry recorded for {vehicle_number} at {time.ctime(vehicle_data[vehicle_number]['entry_time'])}")
                is_parked = True
                entry_time = vehicle_data[vehicle_number]['entry_time']
            else:
                print("This vehicle is already parked.")
        else:
            print("Unable to detect vehicle number.")
    
    if cv2.waitKey(1) & 0xFF == ord('x') and is_parked:
        exit_time = time.time()
        fare = calculate_fare(entry_time, exit_time)
        print(f"Exit recorded for {vehicle_number} at {time.ctime(exit_time)}")
        print(f"Total parking fare for vehicle {vehicle_number}: ₹{fare}")
        is_parked = False
        entry_time = None
        vehicle_data.pop(vehicle_number, None)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

def update_parking_status():
    """
    Updates the parking lot status dynamically.
    """
    global parking_lot
    parking_lot = np.random.choice([0, 1], size=(3, 3)) 
    refresh_display()

def refresh_display():
    """
    Refreshes the GUI display with the updated parking status.
    """
    for i in range(len(parking_lot)):
        for j in range(len(parking_lot[i])):
            status = "Available" if parking_lot[i][j] == 0 else "Occupied"
            color = "green" if parking_lot[i][j] == 0 else "red"
            labels[i][j].config(text=status, bg=color)

def on_parking_spot_click(i, j):
    """
    Called when a parking spot is clicked. If the spot is available, it returns the position.
    """
    if parking_lot[i][j] == 0:
        print(f"Parking spot selected: Row {i+1}, Column {j+1}", "Thank you!!")
    else:
        print(f"Parking spot at Row {i+1}, Column {j+1} is occupied.", "Thank you!!")

parking_lot = np.random.choice([0, 1], size=(3, 3))

root = tk.Tk()
root.title("Smart Parking System")

labels = []
for i in range(3):
    row_labels = []
    for j in range(3):
        status = "Available" if parking_lot[i][j] == 0 else "Occupied"
        color = "green" if parking_lot[i][j] == 0 else "red"
        label = tk.Label(root, text=status, bg=color, width=12, height=4)
        label.grid(row=i, column=j, padx=5, pady=5)

        label.bind("<Button-1>", lambda event, i=i, j=j: on_parking_spot_click(i, j))

        row_labels.append(label)
    labels.append(row_labels)

update_button = tk.Button(root, text="Update Status", command=update_parking_status)
update_button.grid(row=4, column=1, pady=10)

root.mainloop()