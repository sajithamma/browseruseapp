import streamlit as st
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def run_agent(task):
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    return result

def main():
    st.title("Task Execution with Streamlit")
    
    # Input for the task
    task = st.text_input("Enter the task you want to execute:")
    
    if st.button("Execute Task"):
        if task:
            # Use a placeholder for the result
            result_placeholder = st.empty()
            
            # Show a loading spinner while the task is running
            with st.spinner("Executing task..."):
                try:
                    # Run the async task
                    result = asyncio.run(run_agent(task))
                    # Display the result
                    result_placeholder.success("Task executed successfully!")
                    result_placeholder.write("Result:")
                    result_placeholder.write(result)
                except Exception as e:
                    result_placeholder.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a task.")

if __name__ == "__main__":
    main()