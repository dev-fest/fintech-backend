import openai
from typing import Dict, Any

class LLMReportGenerator:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generer_rapport(self, donnees: Dict[str, Any], titre: str) -> str:
        """
        Envoie les données au modèle LLM pour générer un rapport.
        :param donnees: Données sous forme de dictionnaire.
        :param titre: Titre du rapport.
        :return: Texte du rapport généré.
        """
        prompt = self.construire_prompt(donnees, titre)
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-instant",
                messages=[{"role": "system", "content": "Tu es un générateur de rapports."},
                          {"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1000
            )
            rapport = response.choices[0].message['content']
            return rapport
        except Exception as e:
            return f"Erreur lors de la génération du rapport : {e}"

    def construire_prompt(self, donnees: Dict[str, Any], titre: str) -> str:
        """
        Construit le prompt pour envoyer au LLM.
        :param donnees: Données brutes sous forme de dictionnaire.
        :param titre: Titre du rapport.
        :return: Prompt formaté.
        """
        contenu = "\n".join([f"- {cle}: {valeur}" for cle, valeur in donnees.items()])
        prompt = (
            f"Génère un rapport intitulé '{titre}'. Voici les données à analyser :\n"
            f"{contenu}\n\n"
            "Présente une analyse détaillée, identifie les tendances et propose des recommandations."
        )
        return prompt
