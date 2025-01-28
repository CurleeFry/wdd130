import time

from pysinewave import SineWave

# Create a sine wave, with a starting pitch of 12, and a pitch change speed of 10/second.
sinewave = SineWave(pitch = 12, pitch_per_second = 10)

# # Turn the sine wave on.
# sinewave.play()

# # Sleep for 2 seconds, as the sinewave keeps playing.
# time.sleep(2)

# # Set the goal pitch to -5.
# sinewave.set_pitch(-5)

# # Sleep for 3 seconds, as the sinewave smoothly slides its pitch down from 12 to -5, and stays there.
# time.sleep(3)

b = sinewave.set_pitch(493.88)
c = sinewave.set_pitch(261.63)
d = sinewave.set_pitch(293.66)
e = sinewave.set_pitch(329.63)
f_sharp = sinewave.set_pitch(369.99)

b.play()
time.sleep(1)