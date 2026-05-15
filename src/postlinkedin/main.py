from crewai.flow.flow import Flow, start, listen

from .state.linkedin_post_state import LinkedinPostState

from .crews.recherchepost.recherchepost import Recherchepost
from .crews.recherchepost.recherchepost import Recherchepost
from .crews.redacteurpost.redacteurpost import Redacteurpost
from .crews.ajouthashtags.ajouthashtags import Ajouthashtags
from .crews.correctionfinal.correctionfinal import Correctionfinal


class LinkedinPostAutomatisationFlow(Flow[LinkedinPostState]):

    @start()
    def get_topic(self):

        print("\n===================================")
        print(" LINKEDIN AI CONTENT SYSTEM ")
        print("===================================\n")

        topic = input("Entrez le sujet du post : ")

        self.state.topic = topic
        self.state.current_step = "research"

        return topic


    @listen(get_topic)
    def run_research(self, topic):

        print("\n[1/4] RESEARCH AGENT RUNNING...\n")

        result = Recherchepost().crew().kickoff(
            inputs={"topic": topic}
        )

        research_text = result.raw[:1000]  # limite tokens

        self.state.research_result = research_text
        self.state.current_step = "writer"

        return research_text


    @listen(run_research)
    def run_writer(self, research_result):

        print("\n[2/4] WRITER AGENT RUNNING...\n")

        result = Redacteurpost().crew().kickoff(
            inputs={"research_result": research_result}
        )

        writer_text = result.raw[:1000]

        self.state.write_result = writer_text
        self.state.current_step = "seo"

        return writer_text


    @listen(run_writer)
    def run_seo(self, write_result):

        print("\n[3/4] SEO AGENT RUNNING...\n")

        result = Ajouthashtags().crew().kickoff(
            inputs={"write_result": write_result}
        )

        seo_text = result.raw[:1000]

        self.state.seo_result = seo_text
        self.state.current_step = "final editing"

        return seo_text


    @listen(run_seo)
    def run_final_editor(self, seo_result):

        print("\n[4/4] FINAL EDITOR AGENT RUNNING...\n")

        result = Correctionfinal().crew().kickoff(
            inputs={"seo_result": seo_result}
        )

        final_text = result.raw

        self.state.final_post = final_text
        self.state.current_step = "completed"
        self.state.flow_status = "Success"

        return final_text


    @listen(run_final_editor)
    def final_flow(self, final_result):

        print("\n===================================")
        print(" FINAL LINKEDIN POST ")
        print("===================================\n")

        print(final_result.raw if hasattr(final_result, "raw") else final_result)

        print("\n===================================")
        print(" FLOW STATUS : SUCCESS ")
        print("===================================\n")

        return final_result


def kickoff():
    flow = LinkedinPostAutomatisationFlow()
    flow.kickoff()


if __name__ == "__main__":
    kickoff()