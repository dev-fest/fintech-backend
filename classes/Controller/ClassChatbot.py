import requests
from typing import Dict, Any

class ChatBotClient:
    def __init__(self, base_url: str):
        """
        Initialise le client avec l'URL de base du chatbot.
        :param base_url: L'URL de l'API du chatbot.
        """
        self.base_url = base_url

    def envoyer_question(self, question: str) -> str:
        """
        Envoie une question au chatbot et récupère la réponse.
        :param question: La question à poser.
        :return: La réponse du chatbot.
        """
        try:
            response = requests.post(f"{self.base_url}/repondre", json={"question": question})
            response.raise_for_status()  # Gère les erreurs HTTP.
            return response.json().get("reponse", "Aucune réponse reçue.")
        except requests.RequestException as e:
            return f"Erreur lors de la communication avec le chatbot : {e}"

    def apprendre(self, question: str, reponse: str) -> str:
        """
        Envoie une nouvelle paire question-réponse au chatbot pour l'apprentissage.
        :param question: La question à ajouter.
        :param reponse: La réponse associée.
        :return: Message de confirmation ou d'erreur.
        """
        try:
            data = {"question": question, "reponse": reponse}
            response = requests.post(f"{self.base_url}/apprendre", json=data)
            response.raise_for_status()
            return response.json().get("message", "Apprentissage réussi.")
        except requests.RequestException as e:
            return f"Erreur lors de l'apprentissage : {e}"

    def charger_connaissances(self, fichier: str) -> str:
        """
        Envoie une requête pour charger une base de connaissances depuis un fichier.
        :param fichier: Nom du fichier JSON à charger sur le chatbot.
        :return: Message de confirmation ou d'erreur.
        """
        try:
            response = requests.post(f"{self.base_url}/charger", json={"fichier": fichier})
            response.raise_for_status()
            return response.json().get("message", "Connaissances chargées.")
        except requests.RequestException as e:
            return f"Erreur lors du chargement des connaissances : {e}"

    def sauvegarder_connaissances(self, fichier: str) -> str:
        """
        Envoie une requête pour sauvegarder la base de connaissances dans un fichier.
        :param fichier: Nom du fichier JSON pour sauvegarder.
        :return: Message de confirmation ou d'erreur.
        """
        try:
            response = requests.post(f"{self.base_url}/sauvegarder", json={"fichier": fichier})
            response.raise_for_status()
            return response.json().get("message", "Connaissances sauvegardées.")
        except requests.RequestException as e:
            return f"Erreur lors de la sauvegarde des connaissances : {e}"
