import os
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize Gemini (This is your Brain)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", # Fast and capable
    google_api_key=os.environ.get("AIzaSyAxLFrgc_vlVPuCPP_0Hd256y3oMiWvPIw")
)

# Search tool
search_tool = DuckDuckGoSearchRun()

def run_swarm(user_input):
    analyst = Agent(
        role='Analyst',
        goal='Research the topic provided',
        backstory='Expert researcher.',
        tools=[search_tool],
        llm=llm
    )

    task = Task(
        description=user_input, 
        expected_output='A detailed summary.',
        agent=analyst
    )

    crew = Crew(agents=[analyst], tasks=[task], process=Process.sequential)
    return crew.kickoff()
