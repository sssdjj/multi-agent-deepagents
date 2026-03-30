"""Base agent class defining the interface for all agents."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from multi_agent.tools.base import BaseTool


class BaseAgent(ABC):
    """Base class for all agents."""

    def __init__(
        self,
        name: str,
        description: str = "",
        tools: Optional[List[BaseTool]] = None,
    ):
        self.name = name
        self.description = description
        self.tools = tools or []
        self.conversation_history: List[Dict[str, Any]] = []

    @abstractmethod
    async def run(self, input: str) -> str:
        """Run the agent with the given input."""
        pass

    def add_to_history(self, role: str, content: str) -> None:
        """Add a message to the conversation history."""
        self.conversation_history.append({
            "role": role,
            "content": content,
        })

    def get_tools(self) -> List[BaseTool]:
        """Get all tools available to this agent."""
        return self.tools

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r})"
