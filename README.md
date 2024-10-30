🚀 Voice Assistant using Groq & Llama 3 🗣🤖

Welcome to the Voice Assistant project! This project is built using Python's speech recognition, text-to-speech, and the Groq API for conversational AI. The assistant listens to specific commands and processes them using Llama 3 models via the Groq API.

🌟 Features

Voice Command Recognition: Uses your microphone to listen for commands.

Wake Words Detection: Activates with phrases like "Hey Yuktha" or "Hey Bujji".

Conversational AI Integration: Processes user input using the Groq API with a Llama 3 model.

Text-to-Speech Responses: Provides spoken responses to recognized commands.


🛠 Setup and Installation

Step 1: Prerequisites 📋

Python 3.x installed on your machine.

Groq API Key (get yours from the Groq platform).

Microphone for audio input.


Step 2: Clone the Repository 📂

git clone https://github.com/your-username/voice-assistant-groq.git
cd voice-assistant-groq

Step 3: Install Required Packages 📦

Install all necessary Python packages using:

pip install -r requirements.txt

The requirements.txt file should include:

SpeechRecognition
pyttsx3
groq

Step 4: Obtain and Set Groq API Key 🔑

Get your API key from the Groq dashboard and replace "gsk_your_api_key" with your actual key:

client = Groq(api_key="gsk_your_api_key")

Step 5: Run the Script 🏃‍♂

Execute the following command:

python main.py

📝 How It Works

1. Initialization: The script initializes the recognizer, TTS engine, and Groq API client.


2. Listening for Commands: The assistant continuously listens for wake words like "Hey Yuktha" or "Hey Bujji".


3. Processing User Input: After activation, it processes the user’s command and generates a response using the Llama 3 model.


4. Speaking the Response: The assistant speaks the generated response.



Example Commands 📣

"Hey Yuktha, tell me a joke!"

"Hey Bujji, what's the weather today?"


📂 Project Structure

voice-assistant-groq/
│
├── main.py            # Main script to run the assistant
├── README.md          # This beautiful documentation 😍
└── requirements.txt   # Required dependencies for the project

🐛 Troubleshooting

1. No Input Detected: Ensure your microphone is properly connected.


2. Speech Not Recognized: Adjust the microphone sensitivity or reduce background noise.


3. API Error: Double-check your Groq API key and model name.



🤝 Contributing

Feel free to fork this repository and submit pull requests! For major changes, open an issue first to discuss what you would like to change.

📄 License

Distributed under the MIT License. See LICENSE for more information.

🌐 Connect with Me

GitHub: https://github.com/yukthagithub?tab=repositories

LinkedIn: www.linkedin.com/in/yuktha-boggavarapu-640a0b286



---

This README file integrates the steps for setting up, running, and understanding the project, along with troubleshooting and contribution guidelines.
