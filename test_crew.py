import os
from dotenv import load_dotenv
from src.postlinkedin.crews.recherchepost.recherchepost import Recherchepost

# Charger les clés API
load_dotenv()

def run_test():
    print("--- Lancement du Test : recherchePost ---")
    inputs = {
        'topic': 'L’IA et CrewAI pour automatiser LinkedIn',
        'target_audience': 'Développeurs Python'
    }
    
    try:
        # Initialisation du Crew
        # Note: On utilise le chemin d'import relatif au projet
        result = Recherchepost().crew().kickoff(inputs=inputs)
        print("\n--- RÉSULTAT DU TEST ---")
        print(result.raw)
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    run_test()
