from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool,BraveSearchTool
from langchain_groq import ChatGroq
import os

# Initialisation du modèle Groq (ex: Llama 3 en version 70b pour plus de puissance)
llm_groq = ChatGroq(
    temperature=0, 
    groq_api_key=os.environ.get("GROQ_API_KEY"), 
    model_name='groq/llama-3.3-70b-versatile'
)

from crewai import LLM

# Configuration pour Llama 3 local via Ollama
local_llm = LLM(
    model="ollama/mistral",
    base_url="http://localhost:11434"
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
            tools=[SerperDevTool()],
            llm=local_llm,
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
