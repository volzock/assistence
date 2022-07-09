from src.commands.commands.BaseCommand import BaseCommand

import os


class OpenHostsFileCommand(BaseCommand):
    command = r"откр[а-я]{0,3}\sфайл\shosts{0,1}\sв\sблокноте{0,1}"

    def executeCommand(self) -> None:
        os.system("open /etc/hosts")

    def __str__(self):
        return "Открыть файл hosts в блокноте"

    def __repr__(self):
        return self.__str__()