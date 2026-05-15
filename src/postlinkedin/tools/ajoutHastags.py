from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import re


class HashtagGeneratorInput(BaseModel):
    text: str = Field(..., description="Le contenu du post LinkedIn")


class HashtagGeneratorTool(BaseTool):
    name: str = "LinkedIn Hashtag Generator Tool"
    description: str = (
        "Génère des hashtags LinkedIn pertinents "
        "à partir du contenu d’un post."
    )

    args_schema: Type[BaseModel] = HashtagGeneratorInput

    def _run(self, text: str) -> str:
        """
        Génération simple de hashtags intelligents
        à partir des mots-clés du texte.
        """

        # Nettoyage du texte
        text = text.lower()

        # Suppression caractères spéciaux
        text = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", "", text)

        # Mots ignorés
        stop_words = {
            "le", "la", "les", "de", "des", "du", "un", "une",
            "et", "ou", "en", "dans", "pour", "avec", "sur",
            "par", "plus", "que", "qui", "est", "au", "aux",
            "ce", "ces", "cette", "son", "ses", "leur", "leurs",
            "the", "and", "for", "with", "this", "that"
        }

        # Extraction des mots
        words = text.split()

        # Filtrage des mots utiles
        keywords = []

        for word in words:
            if len(word) > 4 and word not in stop_words:
                keywords.append(word)

        # Suppression des doublons
        keywords = list(dict.fromkeys(keywords))

        # Limite hashtags
        keywords = keywords[:10]

        # Création hashtags
        hashtags = [f"#{word.replace(' ', '')}" for word in keywords]

        if not hashtags:
            return "Aucun hashtag pertinent trouvé."

        return "\n".join(hashtags)
    

from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from collections import Counter
import re


class KeywordResearchInput(BaseModel):
    text: str = Field(
        ...,
        description="Texte du post LinkedIn à analyser"
    )


class KeywordResearchTool(BaseTool):
    name: str = "Keyword Research Tool"

    description: str = (
        "Analyse un texte et extrait les mots-clés "
        "les plus importants pour le SEO LinkedIn."
    )

    args_schema: Type[BaseModel] = KeywordResearchInput

    def _run(self, text: str) -> str:

        # Nettoyage du texte
        text = text.lower()

        # Suppression caractères spéciaux
        text = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", "", text)

        # Stop words français + anglais
        stop_words = {
            "le", "la", "les", "de", "des", "du", "un", "une",
            "et", "ou", "en", "dans", "pour", "avec", "sur",
            "par", "plus", "que", "qui", "est", "au", "aux",
            "ce", "ces", "cette", "son", "ses", "leur", "leurs",
            "the", "and", "for", "with", "this", "that", "from",
            "your", "vous", "nous", "ils", "elles", "être",
            "avoir", "comme", "mais", "donc"
        }

        # Découpage des mots
        words = text.split()

        # Filtrage intelligent
        keywords = []

        for word in words:
            if (
                len(word) > 4
                and word not in stop_words
                and not word.isdigit()
            ):
                keywords.append(word)

        # Comptage fréquence
        keyword_counts = Counter(keywords)

        # Top mots-clés
        top_keywords = keyword_counts.most_common(10)

        # Construction résultat
        result = []

        result.append("Top Keywords Detected:\n")

        for keyword, count in top_keywords:
            result.append(
                f"- {keyword} → fréquence : {count}"
            )

        # Suggestions SEO LinkedIn
        result.append("\nSEO Suggestions:\n")

        for keyword, _ in top_keywords[:5]:
            result.append(
                f"- Utiliser '{keyword}' dans le hook "
                f"et les hashtags."
            )

        return "\n".join(result)
    
