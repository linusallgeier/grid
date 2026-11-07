import serial
import time

connection_arduino = None

def connect():
    global connection_arduino

    try:
        connection_arduino = serial.Serial('/dev/cu.usbmodem11201', 9600, timeout=0.1)
        time.sleep(2)
        print("Verbindung wurde erfolgreich hergestellt.")
    except:
        connection_arduino= None
        print("Verbindung wurde fehlgeschlagen.")

def send_values(steps_elbow, steps_shoulder): 

    if  connection_arduino is None:
        return

    message = f"{steps_elbow},{steps_shoulder}\n"

    try:
        connection_arduino.write(bytes(message, 'utf-8'))

        response = connection_arduino.readline()
        print("Antwort: ", response.decode('utf_8'))
    except:
        print("Fehler beim Senden.")
