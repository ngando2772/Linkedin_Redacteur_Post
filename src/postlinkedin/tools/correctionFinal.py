from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import re
from collections import Counter


class FinalContentOptimizerInput(BaseModel):
    text: str = Field(
        ...,
        description="Le contenu final du post LinkedIn"
    )


class FinalContentOptimizerTool(BaseTool):

    name: str = "Final Content Optimizer Tool"

    description: str = (
        "Analyse, corrige et optimise un post LinkedIn : "
        "grammaire, lisibilité, ton, répétitions, CTA "
        "et mise en forme."
    )

    args_schema: Type[BaseModel] = FinalContentOptimizerInput

    def _run(self, text: str) -> str:

        original_text = text

        # =====================================================
        # 1. GRAMMAR TOOL (corrections simples)
        # =====================================================

        grammar_fixes = {
            " sa ": " ça ",
            " ces ": " ses ",
            " a la ": " à la ",
            " a le ": " au ",
            " probléme ": " problème ",
            " developpement ": " développement ",
            " inteligence ": " intelligence ",
        }

        corrected_text = f" {text} "

        for wrong, correct in grammar_fixes.items():
            corrected_text = corrected_text.replace(
                wrong,
                correct
            )

        corrected_text = corrected_text.strip()

        # =====================================================
        # 2. READABILITY TOOL
        # =====================================================

        readability_suggestions = []

        sentences = re.split(r"[.!?]", corrected_text)

        long_sentences = [
            s for s in sentences
            if len(s.split()) > 25
        ]

        if long_sentences:
            readability_suggestions.append(
                "- Certaines phrases sont longues. "
                "Essayez de les raccourcir."
            )

        if "\n\n" not in corrected_text:
            readability_suggestions.append(
                "- Ajouter des espaces entre paragraphes "
                "pour améliorer la lecture."
            )

        # =====================================================
        # 3. TONE ANALYZER TOOL
        # =====================================================

        motivational_words = [
            "succès",
            "opportunité",
            "innovation",
            "croissance",
            "avenir",
            "impact"
        ]

        tone_detected = "Professionnel"

        if any(
            word in corrected_text.lower()
            for word in motivational_words
        ):
            tone_detected = "Professionnel et motivant"

        # =====================================================
        # 4. REPETITION CHECKER TOOL
        # =====================================================

        cleaned_words = re.findall(
            r"\b[a-zA-ZÀ-ÿ]{4,}\b",
            corrected_text.lower()
        )

        word_counts = Counter(cleaned_words)

        repetitions = []

        for word, count in word_counts.items():
            if count >= 4:
                repetitions.append(
                    f"- '{word}' apparaît {count} fois."
                )

        # =====================================================
        # 5. CTA OPTIMIZER TOOL
        # =====================================================

        cta_present = any(
            expression in corrected_text.lower()
            for expression in [
                "qu'en pensez-vous",
                "votre avis",
                "partagez",
                "commentaire",
                "dites-moi"
            ]
        )

        cta_suggestion = ""

        if not cta_present:
            cta_suggestion = (
                "\nCTA Suggestion:\n"
                "- Ajouter une question engageante comme :\n"
                "\"Qu’en pensez-vous ?\""
            )

        # =====================================================
        # 6. FORMATTING TOOL
        # =====================================================

        formatted_text = corrected_text

        # Ajouter espaces après emojis si besoin
        formatted_text = re.sub(
            r"([🔥🚀💡📌👉])([^\s])",
            r"\1 \2",
            formatted_text
        )

        # Découpage léger des gros blocs
        formatted_text = formatted_text.replace(". ", ".\n\n")

        # =====================================================
        # RAPPORT FINAL
        # =====================================================

        report = []

        report.append(
            "=============================="
        )
        report.append(
            "LINKEDIN FINAL CONTENT REPORT"
        )
        report.append(
            "==============================\n"
        )

        # Texte optimisé
        report.append("FINAL OPTIMIZED POST:\n")
        report.append(formatted_text)

        # Ton détecté
        report.append("\n\nTONE ANALYSIS:\n")
        report.append(f"- Ton détecté : {tone_detected}")

        # Lisibilité
        report.append("\nREADABILITY SUGGESTIONS:\n")

        if readability_suggestions:
            report.extend(readability_suggestions)
        else:
            report.append(
                "- Bonne lisibilité globale."
            )

        # Répétitions
        report.append("\nREPETITION ANALYSIS:\n")

        if repetitions:
            report.extend(repetitions)
        else:
            report.append(
                "- Aucune répétition excessive détectée."
            )

        # CTA
        if cta_suggestion:
            report.append(cta_suggestion)
        else:
            report.append(
                "\nCTA ANALYSIS:\n"
                "- CTA engageant détecté."
            )

        return "\n".join(report)