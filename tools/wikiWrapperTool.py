from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_core.tools import Tool

__wikiWrapper = WikipediaAPIWrapper()
wiki_tool = WikipediaQueryRun(api_wrapper=__wikiWrapper)