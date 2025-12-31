import subprocess
import os

from langchain_core.tools import Tool

working_dir = os.getcwd()+"/sandbox"

def runCommand(command: str):
    print("===Called this tool for running shell command===")
    updatedCommand = f"cd {working_dir} && "+ command
    print(updatedCommand)
    return subprocess.run(updatedCommand, shell=True, capture_output=True, text=True).stdout or "Done"


runCommandTool = Tool(
    name="runCommand",
    func=runCommand,
    description="run shell command, do not use this tool for any files and folder",
)
