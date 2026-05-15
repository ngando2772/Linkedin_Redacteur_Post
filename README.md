# 🚀 LinkedIn Content & Video Factory (Multi-Agent RAG System)

Bienvenue dans le moteur de croissance de contenu de nouvelle génération. Ce projet utilise la puissance de **CrewAI**, de l'**IA Agentique** et du **RAG** pour transformer une simple idée ou un document technique en une stratégie multicanale complète (Post LinkedIn + Script Vidéo optimisé).

---

## 🎯 Vision du Projet
L'objectif est d'automatiser le flux de travail d'une agence de marketing digital. Le système ne se contente pas de générer du texte ; il recherche, rédige, optimise pour les algorithmes et prépare la déclinaison vidéo pour garantir une portée maximale.

---

## 🧠 Architecture du Système (The Crew)

Le projet repose sur une équipe d'agents spécialisés :

1.  **Analyste Technologique (Researcher) :** Explore le sujet en profondeur, extrait les données clés et assure la crédibilité technique.
2.  **Copywriter Stratégique (Writer) :** Transforme les données brutes en un récit captivant (storytelling) adapté à l'audience LinkedIn.
3.  **Spécialiste SEO & Algorithmes (SEO Agent) :** Optimise la visibilité, sélectionne les hashtags et structure le format pour le "scroll-stopping".
4.  **Réalisateur Vidéo (Video Agent) :** Convertit le post final en un script dynamique pour Shorts/Reels (Visuels + Voix Off).

---

## 🛠 Stack Technique

*   **Framework :** [CrewAI](https://www.crewai.com/) (Orchestration multi-agents)
*   **Gestionnaire de Paquets :** `uv` (Ultra-fast Python package installer)
*   **Modèles LLM :** Support de modèles locaux via **Ollama** (Llama 3, Mistral) ou via API (Groq, OpenAI).
*   **Environnement :** Python 3.13 / Ubuntu Linux.
*   **Outils RAG :** Intégration prévue pour le traitement de fichiers PDF, Word et bases de données SQL.

---

## 📂 Structure du Projet

```text
postlinkedin/
├── src/
│   └── postlinkedin/
│       ├── config/              # Fichiers YAML (Agents & Tasks)
│       ├── crews/               # Définition des différentes équipes
│       ├── main.py              # Point d'entrée (Flows & Logic)
│       └── tools/               # Outils personnalisés (RAG, API)
├── .env                         # Variables d'environnement (Clés API)
└── pyproject.toml               # Configuration du projet via uv

