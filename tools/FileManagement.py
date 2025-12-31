from langchain_community.agent_toolkits import FileManagementToolkit
rootDir = "./sandbox"

fileToolKit = FileManagementToolkit(root_dir=rootDir)
fileTools = fileToolKit.get_tools()