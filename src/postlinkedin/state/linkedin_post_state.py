from pydantic import BaseModel
from typing import Optional


class LinkedinPostState(BaseModel):
    # INPUT UTILISATEUR
    topic: Optional[str] = None

    # research
    research_result: Optional[str] = None

    #writer
    write_result: Optional[str] = None

    #SEO
    seo_result: Optional[str] = None

    #Final editor
    final_post: Optional[str] = None

    # FLOW STATUS
    current_step: Optional[str] = None

    flow_status: Optional[str] = "initialized"

    error_message: Optional[str] = None