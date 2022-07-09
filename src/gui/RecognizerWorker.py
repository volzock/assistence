from PyQt6.QtCore import QObject, pyqtSignal

from src.recognition.Recognizer import Recognizer
from src.commands.CommandExecution import CommandExecution


class RecognizerWorker(QObject):
    finished = pyqtSignal()
    recognizer = Recognizer()
    commandExecution = CommandExecution()

    def run(self):
        self.commandExecution.execute(self.recognizer.start())
        self.finished.emit()
