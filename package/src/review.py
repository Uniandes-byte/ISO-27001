from enum import Enum
from typing import List
from package.src.parameter import Parameter

class Review:
    def __init__(self):
        self._organizational_controls: List[Parameter] = []
        self._people_controls: List[Parameter] = []
        self._physical_controls: List[Parameter] = []
        self._technological_controls: List[Parameter] = []

    @property
    def get_organizational_controls(self) -> None:
        return self._organizational_controls

    @property
    def get_people_controls(self) -> None:
        return self._people_controls
    
    @property
    def get_physical_controls(self) -> None:
        return self._physical_controls
    
    @property
    def get_physical_controls(self) -> None:
        return self._technological_controls
    
    @property
    def set_organizational_controls(self, parameter:Parameter) -> List[Parameter]:
        return self._organizational_controls.append(parameter)
    
    @property
    def set_people_controls(self, parameter:Parameter) -> List[Parameter]:
        return self._people_controls.append(parameter)
    
    @property
    def set_physical_controls(self, parameter:Parameter) -> List[Parameter]:
        return self._physical_controls.append(parameter)

    @property
    def set_physical_controls(self, parameter:Parameter) -> List[Parameter]:
        return self._technological_controls.append(parameter)