from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool

serper = GoogleSerperAPIWrapper()

webSearchTool = Tool(
    name="webSearchTool",
    func=serper.run,
    description="Search web to get latest information"
)
