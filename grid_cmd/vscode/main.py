import visualizer
import serial_communication
import math

def on_visualize(steps_elbow, steps_shoulder):
    if steps_elbow is None or steps_shoulder is None: 
        return;

    print(steps_elbow, steps_shoulder)
    serial_communication.send_values(steps_elbow, steps_shoulder)

serial_communication.connect()

visualizer.l1 = 5.0
visualizer.l2 = 4.0
visualizer.on_visualize = on_visualize

visualizer.visualize()