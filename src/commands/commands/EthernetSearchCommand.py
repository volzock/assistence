import os
import re

from src.commands.commands.BaseCommand import BaseCommand


class EthernetSearchCommand(BaseCommand):
    command = r"((пои[а-я]{2})|(найди))(\sв\sинтернете){0,1}"
    search = []

    def isThisCommand(self, string: str) -> bool:
        query = re.split(self.command, string)
        if query:
            self.search = query[-1].rstrip().split()
        return query[0] != string

    def executeCommand(self) -> None:
        os.system(f'open "https://www.google.com/search?q={"+".join(self.search)}" ')

    def __str__(self):
        return "Поиск в интернете {что хочешь найти}"

    def __repr__(self):
        return self.__str__()