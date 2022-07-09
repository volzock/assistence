import os

from src.commands.commands.BaseCommand import BaseCommand


class DisableWIFICommand(BaseCommand):
    command = r"выключи[а-я]{0,2}\swi-{0,1}fi"

    def executeCommand(self) -> None:
        os.system("networksetup -setairportpower airport off")

    def __str__(self):
        return "Выключить wifi"

    def __repr__(self):
        return self.__str__()