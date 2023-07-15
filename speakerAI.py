import openai
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
listener = sr.Recognizer()
openai.api_key = "Enter Your Account API Key"

def process_speech():
    with sr.Microphone() as source:
        print("What can I help you with?")
        print("Now speak...")
        listener.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = listener.listen(source)

    try:
        data = listener.recognize_google(audio)
        print("Question you said to me:", data)

        if "exit" in data:
            return False

        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=data,
            max_tokens=1024,
            temperature=0.5,
            n=1,
            stop=None
        )

        response = completion.choices[0].text.strip()
        print("Response:", response)
        engine.say(response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I could not understand your question.")
    except sr.RequestError:
        print("Sorry, speech recognition service is currently unavailable.")

    return True

while True:
    if not process_speech():
        break
