from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool,ScrapeWebsiteTool,BrowserbaseLoadTool
from langchain_groq import ChatGroq
import os

# Initialisation du modèle Groq (ex: Llama 3 en version 70b pour plus de puissance)
llm_groq = ChatGroq(
    temperature=0, 
    groq_api_key=os.environ.get("GROQ_API_KEY"), 
    model_name='groq/llama-3.3-70b-versatile'
)



@CrewBase
class Recherchepost():
    """Recherchepost crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

 
    @agent
    def researcherPost(self) -> Agent:
        return Agent(
            config=self.agents_config['researcherPost'], # type: ignore[index]
            verbose=True,
            allow_delegation=False,
            tools=[SerperDevTool(),ScrapeWebsiteTool()],
            llm='groq/llama-3.3-70b-versatile',
        )



    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task_post'], # type: ignore[index]
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Recherchepost crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
