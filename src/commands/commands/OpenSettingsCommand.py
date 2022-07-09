import os

from src.commands.commands.BaseCommand import BaseCommand


class OpenSettingsCommand(BaseCommand):
    command = r"откр[а-я]{0,4}\sнастро[а-я]{0,3}(\sос){0,1}(\sоперационной системы){0,1}"

    def executeCommand(self) -> None:
        os.system('open "x-apple.systempreferences:"')

    def __str__(self):
        return "Открытие настроек операционной системы"

    def __repr__(self):
        return self.__str__()