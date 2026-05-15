from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from postlinkedin.tools.ajoutHastags import KeywordResearchTool, HashtagGeneratorTool
from crewai import LLM

# Configuration pour Llama 3 local via Ollama
local_llm = LLM(
    model="ollama/mistral",
    base_url="http://localhost:11434"
)

@CrewBase
class Ajouthashtags():
    """Ajouthashtags crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

   
    @agent
    def seo_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_agent'], # type: ignore[index]
            tools=[KeywordResearchTool(), HashtagGeneratorTool()],
            llm=local_llm,
        )

    @task
    def seo_agent_task(self) -> Task:
        return Task(
            config=self.tasks_config['seo_agent_task'], # type: ignore[index]
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Ajouthashtags crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
