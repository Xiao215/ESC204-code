```python
'''
ESC204 2023S Prototypingx
Task: Light up onboard LED on button press.
'''
# Import libraries needed for blinking the LED
import board
import digitalio
# Configure the internal GPIO connected to the LED as a digital output

# red light is connected to port 14
red = digitalio.DigitalInOut(board.GP14)
red.direction = digitalio.Direction.OUTPUT

# blue light is connected to port 15
blue = digitalio.DigitalInOut(board.GP15)
blue.direction = digitalio.Direction.OUTPUT

# green light is connected to port 16
green = digitalio.DigitalInOut(board.GP16)
green.direction = digitalio.Direction.OUTPUT

# Configure the internal GPIO connected to the button as a digital input
button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP  # Set the internal resistor to pull-up
# Print a message on the serial console
print('Hello! My code is running.')
# counter 0 -> model 1, OFF
# counter 1 -> model 2, RED and BLUE
# counter 2 -> model 3, ALL THREE
counter = 0
past_button = True
# Loop so the code runs continuously
while True:
    # Only do change on every negative edge, or each time button change from True to False
    if (past_button == True and button.value == False):
        past_button = False
        if (counter == 0):
            # Model 2
            red.value = True
            blue.value = True
        elif (counter == 1):
            # Model 3
            green.value = True
        elif (counter == 2):
            # Model 1
            red.value = False
            blue.value = False
            green.value = False
            counter = -1
        else:
            testlight.value = True
        # Increment the counter, where counter value of -1 becomes 0
        counter += 1
    elif (button.value == True and past_button == False):
        past_button = True
```
