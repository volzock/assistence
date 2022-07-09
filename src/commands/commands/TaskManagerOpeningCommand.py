import os

from src.commands.commands.BaseCommand import BaseCommand


class TaskManagerOpeningCommand(BaseCommand):
    command = r"откр[а-яА-Я]{0,4}\sдиспетчер[а-яА-Я]{0,1}\sзадач"

    def executeCommand(self) -> None:
        os.system("open /System/Applications/Utilities/Activity\ Monitor.app")

    def __str__(self):
        return "Открыть диспетчер задач"

    def __repr__(self):
        return self.__str__()
