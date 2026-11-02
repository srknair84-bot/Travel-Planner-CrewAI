# ✈️ Travel Planner with CrewAI

A small command-line example of a single [CrewAI](https://www.crewai.com/) agent. Enter a city and a "Travel Planner" agent suggests three places to visit there, each described in one line.

## How it works

1. The script loads your API key and model name from a `.env` file.
2. It asks which city you want to travel to.
3. A **Travel Planner** agent is given a task to suggest 3 places to visit, each with a one-line description and a tip.
4. A `Crew` with that one agent and task runs, and the result is printed in the terminal.

The agent has no tools, so suggestions come from the language model's own knowledge.

## Tech stack

Python · CrewAI · OpenAI · python-dotenv

## Getting started

### Prerequisites

- Python 3.10 or newer
- An [OpenAI API key](https://platform.openai.com/)

### Install

```bash
git clone https://github.com/srknair84-bot/Travel-Planner-CrewAI.git
cd Travel-Planner-CrewAI
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install crewai python-dotenv
```

### Configure

Create a `.env` file in the project folder:

```env
OPENAI_API_KEY=your-openai-key
OPENAI_MODEL_NAME=gpt-4o-mini
```

### Run

```bash
python travel_planner.py
```

Example:

```
Enter the city you want to travel to?: Jaipur
```

The agent then prints three suggestions for that city.

## Project structure

```
travel_planner.py   agent, task, crew and command-line prompt
```

## Ideas for next steps

- Add a web search tool so suggestions use current information
- Add more agents, such as a budget planner and an itinerary writer
- Ask for trip length, budget and interests
- Add a Streamlit interface
