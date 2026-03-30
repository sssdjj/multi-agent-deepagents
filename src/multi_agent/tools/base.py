"""Base tool class defining the interface for all tools."""

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseTool(ABC):
    """Base class for all tools that agents can use."""

    name: str
    description: str

    @abstractmethod
    async def run(self, **kwargs) -> Dict[str, Any]:
        """Execute the tool with the given parameters."""
        pass

    def get_schema(self) -> Dict[str, Any]:
        """Get the JSON schema for this tool's parameters."""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self._get_parameters_schema(),
        }

    def _get_parameters_schema(self) -> Dict[str, Any]:
        """Override to provide parameters schema."""
        return {}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r})"
