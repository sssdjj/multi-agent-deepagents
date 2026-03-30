# multi-agent

A flexible multi-agent framework for building collaborative AI systems.

## Features

- Modular agent architecture
- Easy-to-use tool system
- Communication between agents
- Extensible base classes

## Installation

```bash
pip install multi-agent
```

Or using uv:

```bash
uv add multi-agent
```

## Quick Start

```python
from multi_agent.agents.base import BaseAgent
from multi_agent.tools.web_search import WebSearchTool

# Create your agents and tools
# Build collaborative AI systems
```

## Project Structure

```
multi-agent/
├── src/
│   └── multi_agent/
│       ├── agents/          # Agent implementations
│       ├── tools/           # Tool definitions
│       └── utils/           # Utility functions
├── tests/                   # Test files
└── examples/                # Example usage
```

## License

MIT
