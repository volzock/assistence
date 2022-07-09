import re


class BaseCommand:
    command = r"" # regular expression string

    def isThisCommand(self, string: str) -> bool:
        if re.match(self.command, string):
            return True
        return False

    def executeCommand(self) -> None:
        pass
