import winsound
import time

# Define the frequency (Hz) and duration (ms) of the beep
frequency = 2000  # Frequency in Hz
duration = 1200   # Duration in milliseconds

# Produce the beep sound
winsound.Beep(frequency, duration)

# Optionally, you can add a delay before the beep to create a pause
time.sleep(1)  # Sleep for 1 second

# You can also play multiple beeps in a loop or sequence
for _ in range(3):
    winsound.Beep(frequency, duration)
    time.sleep(0.5)  # Sleep for 0.5 seconds between beeps
