import re

from src.commands.commands.BaseCommand import BaseCommand


class SumCommand(BaseCommand):
    command = r"(((слож[а-я]{0,4})|(суммирова[а-я]{0,3}))\s\d{1,10}((\s)|(\,)|(\sи\s))\d{1,10})"
    a, b = 0, 0

    def isThisCommand(self, string: str) -> bool:
        try:
            self.a, self.b = map(int, re.findall(self.command, string)[0][0]
                                 .replace("и", "")
                                 .replace(",", "")
                                 .split()[1:3])
            return True
        except:
            return False

    def executeCommand(self) -> None:
        print(self.a + self.b)

    def __str__(self):
        return "Сложить число1 число2"

    def __repr__(self):
        return self.__str__()
