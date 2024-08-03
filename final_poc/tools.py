from tavily import TavilyClient
import os

search_tool = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])