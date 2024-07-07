import win32com.client
import speech_recognition as sr
import VIC

speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Voice = speaker.GetVoices().Item(1)


def say(w):
    speaker.Speak(w)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(
            device_index=sr.Microphone.list_microphone_names().index('Headset (realme Buds T300)')) as mic:
        r.pause_threshold = 1
        audio = r.listen(mic)
        try:
            print("Recognizing...")
            q = r.recognize_google(audio, language="en-in")
            print(f"User said: {q}")
            say(q)
            return q
        except Exception as e:
            print(f"Some error occurred please try again..{e}")


if __name__ == "__main__":
    say("Initiating Script")
    while True:
        print("Listening...")
        query = takeCommand()
        if query:
            query = query.lower()
            if "hp" in query:
                if "lock" in query:
                    VIC.lock_windows()
