# Gemini ADK Travel Concierge  
**Hyper-Personalized, Health-Safe, Budget-Optimized Travel Planner**  
Built with Google Agent Development Kit (ADK) – Kaggle Agents Intensive Capstone Project 2025  

---
### Problem
Travel planning is **stressful, time-consuming, and often unsafe** for real people:
- 10–15 hours wasted per trip across 10+ websites  
- No tool understands **age**, **respiratory issues**, **low walking tolerance**, **gut problems**, **extreme cleanliness obsession**, **vegetarian + Italian food**, **mild weather**, **night-owl/early-bird rhythm**, or **family composition**  
- Result: budget overruns, inaccessible hotels, breathing problems in summer heat, exhausting tours  

### Solution: A True Digital Travel Butler
This project is a **multi-agent system built 100% with Google ADK** that turns a single message into a **complete, visual, personalized travel plan** in under 2 minutes.

**Features**  
- Understands **health constraints**, **cleanliness obsession (>9.5/10)**, **food allergies**, **mobility limits**, **sleep patterns**  
- Automatically picks **best dates** (e.g., mild October for respiratory health)  
- Searches **flights + hotels + activities** in parallel  
- **LoopAgent** re-plans up to 3× if over budget — never violates rules  
- **Google Places integration** to vet real hotels for cleanliness, breakfast, wheelchair access, and photos  
- Outputs a **beautiful Markdown catalog** with images, maps, day-by-day itinerary, and compliance report  

---

### Architecture (SequentialAgent Pipeline)

```mermaid
graph TD
    A[" USER INPUT:  e.g. \"Italy, 4 people, senior with respiratory issues,extreme cleanliness, vegetarian\""] 
    --> B["SequentialAgent Pipeline\n(Main Orchestrator)"]

    B --> C["1. Profile ExtractorLlmAgent → state['profile']"]
    C --> D["2. Strategist Suggest dates using health + weather"]
    D --> E["3. ParallelAgent Concurrent searches"]

    E --> F["Flight Agent Scale cost × travelers Direct flights for low mobility"]
    E --> G["Hotel Agent Places API vetting Cleanliness >9.5 + Breakfast + Photos"]
    E --> H["Activity Agent Golf-cart tours, vegetarian dining"]

    E --> I["4. LoopAgent Optimizer Max 3 iterations If total > budget → regenerate"]
    I --> J["5. Catalog Generator Markdown + Embedded Images + Compliance"]
    J --> K["Final Visual Itinerary"]

    style B fill:#e3f2fd,stroke:#1565c0,stroke-width:3px
    style E fill:#f3e5f5,stroke:#7b1fa2,stroke-width:3px
    style I fill:#fff3e0,stroke:#e65100,stroke-width:3px
