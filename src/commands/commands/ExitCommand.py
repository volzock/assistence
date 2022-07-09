from src.commands.commands.BaseCommand import BaseCommand


class ExitCommand(BaseCommand):
    command = r"закр[а-яА-я]{0,4}\sголосов[а-яА-я]{0,3}\sас{1,2}истент[а-яА-я]{0,1}"

    def executeCommand(self) -> None:
        exit(0)

    def __str__(self):
        return "Закрыть голосовой ассистент"

    def __repr__(self):
        return self.__str__()
