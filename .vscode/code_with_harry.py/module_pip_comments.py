# import pyjokes

# joke =pyjokes.get_joke()
# print(joke)
# print("""
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.
# """
# )

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I am studying plz don't disturb me")
engine.runAndWait()
