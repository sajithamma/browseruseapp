import streamlit as st
from langchain_openai import ChatOpenAI
from browser_use import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig
from browser_use.controller.service import Controller
import asyncio
from dotenv import load_dotenv

load_dotenv()

browser = Browser(
	config=BrowserConfig(
		
	)
)

context = BrowserContext(browser=browser)

async def run_agent(task):
    agent = Agent(
        task=task,
        browser_context=context,
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    return result

async def format_result_to_markdown(raw_result):
    llm = ChatOpenAI(model="gpt-4o")
    prompt = f"""
    Convert this JSON data into clean markdown without code blocks. Follow these rules:
    1. Use headers, lists, and links
    2. Format images as markdown images
    3. Never use triple backticks
    4. Keep dates bolded

    Input:
    {raw_result}

    Markdown:
    """
    formatted_result = await llm.agenerate([prompt])
    return formatted_result.generations[0][0].text.strip()

def main():
    st.title("Task Execution with Streamlit")
    task = st.text_input("Enter the task you want to execute:")
    
    if st.button("Execute Task") and task:
        result_placeholder = st.empty()
        with st.spinner("🚀 Executing task..."):
            try:
                # Get raw result
                raw_result = asyncio.run(run_agent(task))
                with st.expander("Raw Result"):
                    st.write(raw_result)
                
                # Format to markdown
                with st.spinner("🎨 Formatting results..."):
                    formatted_result = asyncio.run(format_result_to_markdown(raw_result))
                
                # Display final output
                result_placeholder.markdown("---")
                st.subheader("Final Result")
                st.markdown(formatted_result, unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
            finally:
                # Ensure the browser is closed even if an error occurs
                asyncio.run(browser.close())

if __name__ == "__main__":
    main()