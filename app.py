from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig
from browser_use.controller.service import Controller
load_dotenv()

browser = Browser(
	config=BrowserConfig(
		#chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
	)
)

context = BrowserContext(browser=browser)

async def main():
    agent = Agent(
        browser_context=context,
        task="Search Sajith Amma LinkedIn and Google and get the link and check what he is currently doing",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())