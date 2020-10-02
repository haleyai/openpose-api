from abc import ABC, abstractmethod
from typing import List
from app.schemas.pose import Pose


class Engine(ABC):
    @abstractmethod
    def infer_image(self, image) -> List[Pose]:
        return []
