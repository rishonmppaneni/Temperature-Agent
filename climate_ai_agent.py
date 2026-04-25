
"""
climate_ai_agent.py

AI-style climate agent for OWID global monthly temperature anomalies.

Behavior:
- Downloads OWID monthly-temperature-anomalies.csv
- Filters for "World"
- Uses "day" as the date column
- Uses OWID's own anomaly (vs 1991-2020) for simplicity
- Checks if there is any new data since the last run (stored in agent_state.json)
- If new data exists:
    - Fits a linear trend vs fractional year
    - Forecasts next few years
    - Saves a plot, numeric summary, explantory text
    - Updates the stte file
- If no new data:
    - Prints a message and exits quickly

Hook:
- generate_explanation() is where you plug an LLM (ChatGPT, Gemini, etc.)
"""

import os
import json
from datetime import datetime 
