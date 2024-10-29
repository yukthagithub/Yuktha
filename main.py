import os
import speech_recognition as sr
import pyttsx3
from groq import Groq

# Initialize speech recognition and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak out text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize voice input
def listen_for_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.WaitTimeoutError:
            print("No input detected. Waiting for 'Hey Bujji'...")
            return None
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
            return None

# Initialize the API client (Make sure you have your Groq API key)
client = Groq(api_key="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")

def activate_assistant():
    speak("Hey there! I'm ready when you are.")
    while True:
        try:
            command = listen_for_command()
            if command and ("hey yuktha" in command or "hey yuktha" in command or "yuktha" in command or "hey bujji" in command):
                speak("How can I assist you?")
                user_prompt = listen_for_command()  
                if user_prompt:
                    try:
                        print(f"Processing: {user_prompt}")
                        chat_completion = client.chat.completions.create(
                            messages=[{"role": "user", "content": user_prompt}],
                            model="llama3-8b-8192",  # Or your chosen Llama 3 model
                        )
                        response = chat_completion.choices[0].message.content
                        print(f"Assistant's response: {response}")
                        speak(response)
                    except Exception as e:
                        print(f"An error occurred: {e}")
                        speak("Sorry, I encountered an error processing your request.")
        except KeyboardInterrupt:
            print("\nExiting the assistant...")
            break

if __name__ == "__main__":
    activate_assistant()
