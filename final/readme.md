
# Controllable robotic arm based on speech recognition
------
# Functions

> * Control the front, back, up, down, left and right of the robotic arm through voice recognition or GUI
> * Control the robotic arm for palletizing action through voice recognition
> * Let the robotic arm write some simple words and numbers through voice recognition

# Instructions

First of all, prepare the hardware you need: Raspberry Pi, pre-written STM32 and MCU, the robotic arm we made, various data cables, monitors, sound cards, keyboards, mice, headsets with microphones.

> * First, connect the motors that control the three axis directions on the robotic arm to the corresponding control lines on the STM32.
> * Connect the Raspberry Pi to STM32, sound card, monitor, mouse keyboard, earphone and turn it on, then connect STM32 to the microcontroller.
> * View the Raspberry Pi on the monitor, control it with the mouse and keyboard, and run the main.py file. Then a GUI which contains several buttons and input boxes appears. You can control the robotic arms to move by inputing parameters and clicking buttons.
> * Move the robotic arm to the preset initialization position, hold it by hand, and click POWERON on the UI to supply power to the motor. After that, the robotic arm can be suspended and can be controlled through UI or voice recognition.
> * View the Raspberry Pi on the monitor, control it with the mouse and keyboard, and run the app.py file. Firstly, power the motor. You can see a GUI used for speech recognition. When it says it is listening , you can say where you want the arm to move. And you can see the sentence that the system recognizes. After that, the arm moves correctly.
