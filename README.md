# ✈️ The Hyper-Personalized Travel Concierge Agent

**Submission Track:** Concierge Agents
**Project Goal:** To create a strategic travel planner that prioritizes user health, comfort, and personal preferences over generalized booking algorithms, producing a visually appealing, comprehensive final catalog.

-----

## ۱. The Pitch: Problem, Solution, and Value

### 🧐 Problem Statement

Traditional travel planning is fundamentally inefficient and impersonal. Existing booking systems fail to incorporate **complex, non-monetary constraints** such as the traveler's **respiratory condition, mobility level, strict cleanliness standards, and party size ($N$)**. This results in sub-optimal, stressful, and potentially unsafe itineraries, particularly for specialized travelers (e.g., seniors or individuals with chronic conditions).

### 💡 Solution Pitch

We introduce the **Personal Travel Planner Agent**, a sophisticated **multi-agent system** that functions as a Strategic, Health-Aware Travel Consultant. The system's core innovation is its ability to:

1.  **Strategically Optimize:** Use the **Strategist Agent** to determine the single best time window for travel by cross-referencing health constraints, climate data, and budget.
2.  **Actively Optimize Cost:** Employ the **Optimization Loop Agent** to dynamically adjust the travel plan until the total cost for $N$ travelers meets the budget cap without violating critical health constraints.
3.  **Deliver a Premium Output:** Utilize the **Catalog Generator Agent** to produce a final, magazine-quality visual itinerary.

### ✨ Value Proposition

The agent shifts planning from hours of manual, risk-prone research to minutes of personalized strategy. It provides a unique blend of:

  * **Safety & Wellness:** Proactive avoidance of environmental or logistical hazards (e.g., high heat for respiratory patients, or low-rated clean hotels).
  * **Financial Efficiency:** The **Optimization Loop Agent** guarantees the best possible value and budget compliance for the entire group ($N$).
  * **Premium Experience:** Delivers a professional, visually rich travel catalog, enhancing user experience.

-----

## ۲. Technical Implementation

### 🤖 Agent Architecture

The system is orchestrated by the **Planner Agent** following a three-phase workflow, managing **8 distinct agents** (Sequential, Parallel, and Loop).

1.  **Strategy Phase (Sequential):**

      * **Planner Agent:** Parses the user's detailed profile (including **Party Size ($N$)**) and health needs, converting them into strict **Filtering Rules** (e.g., `Hotel_Cleanliness_Score > 90%`).
      * **Strategist Agent:** Uses rules and tools (Google Search) to recommend the **optimal date range** for travel, prioritizing health and avoiding peak season.

2.  **Execution Phase (Parallel):** All investigation agents receive the filtering rules and the party size ($N$).

      * **FlightSearchAgent:** Finds flights for $N$ people within the budget.
      * **Hotel Vetting Agent:** Finds $N$-capacity rooms/units and performs **Data Triangulation** (using search tools) to verify cleanliness, breakfast options, and accessibility features against the rigid rules.
      * **ActivitySearchAgent:** Finds $N$-capacity activities that match interests while respecting mobility limits.

3.  **Optimization, Finalization & Output:**

      * **Optimization Loop Agent (Loop Agent):** **If** the total cost exceeds the budget cap for $N$ travelers, this agent enters a loop, iteratively suggests compromises (e.g., cheaper dates/flights) until a compliant solution is found.
      * **Summarizer Agent:** Compiles results, ensuring final compliance with all health rules.
      * **Catalog Generator Agent:** Uses the compiled data and mock `Image_Retrieval_Tool` to produce the final visual itinerary output.

### 🔑 Key Concepts Applied

| Concept | Application |
| :--- | :--- |
| **Multi-agent System** | Utilized an advanced flow featuring **Sequential, Parallel, and Loop Agents** to distribute complex tasks across the planning, execution, and monitoring phases. |
| **Tools (Built-in & Custom)** | Integrated **Google Search** (Built-in) for strategic data retrieval and custom tools (`Image_Retrieval_Tool`, `Catalog_Formatting_Tool`). |
| **Loop Agents** | The **Optimization Loop Agent** actively iterates and modifies the solution (plan) until all constraints (budget and health) are met, demonstrating sophisticated problem-solving. |
| **Sessions & Memory** | **Long Term Memory** is used by the Planner Agent to store and recall the user's detailed health profile and preferences for subsequent trips, ensuring continued personalization. |
| **Bonus: Effective Use of Gemini** | Gemini powers the **Strategist Agent** for advanced reasoning (synthesizing budget, health, and climate data) and the **Catalog Generator Agent** for high-quality content preparation. |

-----

## ۳. Project Files

| File | Description |
| :--- | :--- |
| **`travel_agent.py`** | The main orchestration script containing the **Planner Agent** and the sequential/parallel workflow logic. |
| **`tools.py`** | Contains the definitions for all custom mock tools (e.g., `Image_Retrieval_Tool`, `PriceTracker_Tool`) used by the investigator agents. |
| **`requirements.txt`** | Lists required Python libraries, including ADK-Python. |

## ۴. Instructions for Setup and Run

### Prerequisites

  * Python 3.9+
  * The Agent Development Kit (ADK-Python)

### Installation

1.  Clone the repository:
    ```bash
    git clone [Your GitHub URL]
    cd AI-Travel-Concierge-Capstone
    ```
2.  Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration (Security Notice 🚨)

Set your Google Gemini API Key as an environment variable before running the agent. **Do not hardcode keys in the source files.**

```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

### Execution Example

The system is initiated with a comprehensive natural language query that includes all personal constraints and the group size ($N$):

```bash
python travel_agent.py "Plan a 10-day trip to Rome for 4 people. Our budget is $8,000 total. The party includes a senior with a respiratory issue and a need for extremely high cleanliness. We love historical sites but need low-impact walking tours."
```
