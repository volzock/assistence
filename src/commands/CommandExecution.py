from src.commands.commands.DisableWIFICommand import DisableWIFICommand
from src.commands.commands.SumCommand import SumCommand
from src.commands.commands.ExitCommand import ExitCommand
from src.commands.commands.OpenSettingsCommand import OpenSettingsCommand
from src.commands.commands.EthernetSearchCommand import EthernetSearchCommand
from src.commands.commands.OpeningHostsFileCommand import OpenHostsFileCommand
from src.commands.commands.TaskManagerOpeningCommand import TaskManagerOpeningCommand


class CommandExecution:
    commands = [
        DisableWIFICommand(),
        SumCommand(),
        ExitCommand(),
        OpenSettingsCommand(),
        EthernetSearchCommand(),
        OpenHostsFileCommand(),
        TaskManagerOpeningCommand()
    ]
    print("Список комманд: ")
    print("\n".join(list(map(str, commands))))

    def execute(self, string:str):
        print(f"Пользователь сказал: {string}")
        for command in self.commands:
            if command.isThisCommand(string):
                print(f"Выполняется {command}")
                command.executeCommand()
                break

