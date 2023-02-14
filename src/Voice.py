import speech_recognition as sr
#------------------------------
class Voice:
    def __init__(self):
        self.text = None
    def audio_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio_text = recognizer.listen(source)
            try:
                self.text = recognizer.recognize_google(audio_text,language="pl-PL")
                print(self.text)
            except:
                print("Run again")
