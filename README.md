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
    A[User Input<br>e.g., "Rome, 4 people, senior with respiratory issues,<br>extreme cleanliness, vegetarian"] 
    --> B[SequentialAgent Pipeline<br>(Main Orchestrator)]
    
    B --> C[1. Profile Extractor<br>LlmAgent → state['profile']]
    C --> D[2. Strategist<br>Suggest dates using {profile.health/weather}]
    D --> E[3. ParallelAgent<br>Concurrent searches]
    
    E --> F[Flight Agent<br>Scale cost × travelers<br>Direct flights for low mobility]
    E --> G[Hotel Agent<br>Places API vetting<br>Cleanliness >9.5 + Breakfast + Photos]
    E --> H[Activity Agent<br>Golf-cart tours, vegetarian dining]
    
    E --> I[4. LoopAgent Optimizer<br>Max 3 iterations<br>If total > budget → regenerate]
    I --> J[5. Catalog Generator<br>Markdown + Embedded Images + Compliance]
    J --> K[Final Visual Itinerary]
    
    style B fill:#e3f2fd,stroke:#1565c0
    style E fill:#f3e5f5,stroke:#7b1fa2
    style I fill:#fff3e0,stroke:#e65100
