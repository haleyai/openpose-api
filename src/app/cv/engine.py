from abc import ABC, abstractmethod
from typing import List
from app.schemas.pose import Person


class Engine(ABC):
    @abstractmethod
    def infer_image(self, image) -> List[Person]:
        return []
