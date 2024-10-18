from abc import ABC, abstractmethod

class Observer(ABC):
    """Interface de base pour l'observateur."""
    @abstractmethod
    def update(self, message: str):
        pass


class ConcreteObserver(Observer):
    """Observateur concret qui réagit aux notifications."""
    def update(self, message: str):
        print(f"[Notification] {message}")
