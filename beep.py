# # Only run this once to generate the voice alert
# import pyttsx3

# engine = pyttsx3.init()
# engine.save_to_file("Elevator full. Please wait.", "beep.mp3")
# engine.runAndWait()

# import pyttsx3

# engine = pyttsx3.init()
# engine.say("Testing voice")
# engine.runAndWait()

# import pyttsx3
# import os

# engine = pyttsx3.init()

# # Show available voices
# voices = engine.getProperty('voices')
# for i, voice in enumerate(voices):
#     print(f"{i}: {voice.name} - {voice.id}")

# # Set a voice (optional)
# engine.setProperty('voice', voices[0].id)  # 0 or 1 depending on system

# # Save the file
# file_path = os.path.abspath("alert.mp3")
# print("Saving to:", file_path)

# engine.save_to_file("Elevator full. Please wait.", file_path)
# engine.runAndWait()


from playsound import playsound
playsound("beep_sound.wav")  # Run this alone
