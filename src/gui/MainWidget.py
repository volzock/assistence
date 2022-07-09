from PyQt6.QtCore import QThread
from PyQt6.QtWidgets import QPushButton, QWidget, QLabel, QVBoxLayout

from src.gui.RecognizerWorker import RecognizerWorker
from src.recognition.Recognizer import Recognizer


class MainWidget(QWidget):
    recognizer = Recognizer()

    def __init__(self):
        super().__init__()

        self.worker = RecognizerWorker()
        self.thread = QThread()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.changeText)
        self.worker.finished.connect(self.stopThread)
        self.worker.finished.connect(self.stopThread)

        self.label_states = ["Нажмите на кнопку для начала распознования",
                             "Подождите информацию о старте прослушки, посмотрите в терминал"]
        self.button_status = False

        self.button = QPushButton("Кнопка")
        self.text = QLabel("Нажмите на кнопку")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.mainButtonClickHandler)

    def changeText(self):
        self.button_status = not self.button_status
        self.text.setText(self.label_states[self.button_status])

    def stopThread(self):
        self.thread.quit()
        self.thread.wait()

    def mainButtonClickHandler(self):
        if not self.button_status:
            print("Пользователь инициировал запуск модуля")
            self.changeText()
            self.thread.start()
        else:
            print("Пользователь нажал без причины")



