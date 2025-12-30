# Compliance Testing of Large Language Model Personality Prompts Under Pressure

## Project Overview

This project, also known as **Islanders**, is a simulation environment designed to test the compliance and personality consistency of Large Language Models (LLMs) under pressure. It features a "Desert Island Survival" scenario where AI-driven NPCs interact, gather resources, and strive to survive.

The simulation is built using Python and Pygame, with NPCs powered by the Aliyun Bailian (DashScope) API.

## Features

- **AI-Driven NPCs**: Three distinct characters (Kai, Elara, Jax) with unique personalities and memory systems.
- **Survival Simulation**: NPCs manage energy levels and gather resources (Water, Fish, Fruit) with inventory limits.
- **Social Interaction**: NPCs can engage in dialogue, share information, and form relationships.
- **Memory System**: 
  - Individual NPC memory streams.
  - Global "Chronicle" to record major events.
- **Visual Interface**: Real-time visualization of the island, NPC movements, and status using Pygame.

## Project Structure

```text
.
├── Islanders-main/          # Main source code directory
│   ├── main.py              # Entry point of the application
│   ├── game.py              # Main game loop and logic
│   ├── npc.py               # NPC class and behavior definitions
│   ├── ai_client.py         # Aliyun Bailian API client
│   ├── world.py             # World generation and management
│   ├── ui.py                # User Interface rendering
│   ├── memory_system.py     # Memory and chronicle management
│   ├── dialog_system.py     # Dialogue management
│   └── config.py            # Configuration settings
├── data/                    # Data storage for memories and logs
├── LICENSE
└── README.md
```

## Prerequisites

- Python 3.8+
- Aliyun Bailian API Key (DashScope)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cheung20050509-prog/Compliance_Testing_of_Large_Language_Model_Personality_Prompts_Under_Pressure.git
   ```

2. Install the required Python packages:
   ```bash
   pip install pygame dashscope
   ```

## Usage

1. **Configure API Key**:
   Open `Islanders-main/main.py` (or `ai_client.py`) and ensure your Aliyun Bailian API key is correctly configured.
   *Note: The current codebase may have hardcoded placeholders. It is recommended to use environment variables for security.*

2. **Run the Simulation**:
   Navigate to the project root and run:
   ```bash
   python Islanders-main/main.py
   ```

3. **Controls**:
   - The simulation runs automatically.
   - You can observe NPC interactions and status through the UI.

## Research Context

This tool is intended for researching how LLM-based agents maintain their assigned personas (personalities) when faced with survival pressures (scarcity of resources, competition). It analyzes:
- **Compliance**: Do they stick to their character instructions?
- **Social Dynamics**: How do they cooperate or compete?
- **Memory Usage**: How do past events influence current decisions?

## License

See the [LICENSE](LICENSE) file for details.
