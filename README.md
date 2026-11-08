# Grid

Grid is a Scara (Selective compliance assembly robot arm) project build for home-usage.

## Core Features 🚀

- **Inverse Kinematics:** Real-time joint angle and stepper motor position calculation for X/Y coordinates.
- **Graphical UI:** Built-in live arm preview and coordinate selection.
- **Custom Hardware:** A single dual-layer PCB combines logic and power supply.
- **Precise Motion:** Using SilentStepStick TMC 2209 with 16x microstepping for stepper motor control.

## Usage 💻

### Requirements
Ensure your system runs Python 3 and you have the Arduino IDE installed.

### Installation
Install the required dependencies:
```bash
pip install matplotlib pyserial
```

### Getting Started
1. Flash the microcontroller firmware (`stepper_control.ino`) onto the Arduino Nano.
2. Connect your PC to the PCB via micro USB.
3. Update the configuration inside `serial_communication.py` (Default: `/dev/cu.usbmodem11201`).
4. Run the `main.py` program.
