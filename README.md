# Gemini ADK Travel Concierge

## Problem & Solution
See writeup above. Architecture: Multi-agent with personalization loop.

## Setup
1. `pip install -r requirements.txt`
2. `.env` with GEMINI_API_KEY
3. `python main.py`

## Key Features
- **Personalization**: Handles age, health (respiratory, mobility), cleanliness, food, weather, sleep.
- **Optimization Loop**: Iterates plans until under budget (max 3x).
- **Hotel Vetting**: Real Places API queries for ratings/amenities.
- **Visual Catalog**: Markdown with image placeholders (extend with Imagen API).
- **Observability**: Logs tool calls, events, metrics (cost, iterations).

## Diagrams
See architecture Mermaid above.

## Evaluation
- **Multi-Agent**: Parallel/Sequential/Loop.
- **Tools**: Custom budget + Google Places.
- **Memory**: Session state persists profile.
- **Observability**: Logging + tracing.
- **Context**: Compaction in prompts.

Demo: Run with sample input for Italy trip output.
