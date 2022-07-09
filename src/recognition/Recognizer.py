import speech_recognition as sr


class Recognizer:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def start(self) -> str:
        with self.microphone:
            recognized_data = ""

            self.recognizer.adjust_for_ambient_noise(self.microphone, duration=5)

            try:
                print("Начинаю слушать, у вас 5 секурд")
                audio = self.recognizer.listen(self.microphone, 5, 5)
            except sr.WaitTimeoutError:
                print("Включите микрофон пожалуйста")
                return ""

            try:
                print("Начато распознование")
                recognized_data = self.recognizer.recognize_google(audio, language="ru").lower()
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Проверьте пожалуйста подключение к интернету")

            return recognized_data

