from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from postlinkedin.tools.correctionFinal import FinalContentOptimizerTool

@CrewBase
class Correctionfinal():
    """Correctionfinal crew"""

    agents: list[BaseAgent]
    tasks: list[Task]


    @agent
    def correcteurFinal(self) -> Agent:
        return Agent(
            config=self.agents_config['correcteurFinal'], # type: ignore[index]
            verbose=True,
            tools=[FinalContentOptimizerTool()],
            llm='groq/llama-3.3-70b-versatile',
        )

 

    @task
    def correcteurFinal_task(self) -> Task:
        return Task(
            config=self.tasks_config['correcteurFinal_task'], # type: ignore[index]
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Correctionfinal crew"""
      

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
