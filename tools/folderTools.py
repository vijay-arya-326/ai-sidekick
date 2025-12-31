import os
from langchain_core.tools import StructuredTool

rootDir = "./sandbox/"

def create_folder(path: str) -> str:
    """
    Create a folder if it does not exist.
    """
    try:
        print("Create folder called")
        os.makedirs(path, exist_ok=True)
        return f"Folder created successfully: {path}"
    except Exception as e:
        return f"Error creating folder: {str(e)}"


create_folder_tool = StructuredTool.from_function(
    name="create_folder",
    func=create_folder,
    description="Create a folder at the given path in root dir only"
)