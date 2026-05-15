from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Redacteurpost():
    """Redacteurpost crew"""

    agents: list[BaseAgent]
    tasks: list[Task]


    @agent
    def redacteur(self) -> Agent:
        return Agent(
            config=self.agents_config['redacteur'],
            verbose=True,
            reasoning=True,
            max_reasoning_attempts=3,
            llm='groq/llama-3.3-70b-versatile',
        )
    
    @task
    def redacteur_task(self) -> Task:
        return Task(
            config=self.agents_config['redacteur_task']
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Redacteurpost crew"""
       

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            memory=True
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
