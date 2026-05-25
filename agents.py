from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

def run_swarm(user_input):
    search_tool = SerperDevTool()
    
    # Define your agent
    analyst = Agent(
        role='Analyst',
        goal='Research the topic provided',
        backstory='Expert researcher.',
        tools=[search_tool]
    )

    task = Task(
        description=user_input, 
        expected_output='A detailed summary.',
        agent=analyst
    )

    crew = Crew(agents=[analyst], tasks=[task], process=Process.sequential)
    return crew.kickoff()
