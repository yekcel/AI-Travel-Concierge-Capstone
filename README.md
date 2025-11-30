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

graph TD
    A[User Input: Prefs + Constraints<br>e.g., Age 65, Respiratory, Cleanliness Obsession] --> B[SequentialAgent Pipeline<br>(Core Orchestrator)]
    B --> C[Step 1: Profile Extractor<br>(LlmAgent: Parse JSON, Store in State)]
    C --> D[Step 2: Strategist<br>(Suggest Dates via {profile.state})]
    D --> E[Step 3: ParallelAgent<br>(Concurrent: Flight + Hotel + Activity)]
    E --> F[Flight Agent<br>(Tool: Budget Calc x Travelers)]
    E --> G[Hotel Vetter<br>(Tool: Google Places API<br>Check Cleanliness >9.5, Amenities)]
    E --> H[Activity Planner<br>(Match Interests/Food/Health)]
    E --> I[Step 4: LoopAgent Optimizer<br>(Max 3 Iter: If Total > Budget, Regenerate Plan)]
    I --> J[Step 5: Catalog Generator<br>(Markdown + Images/Maps from State)]
    J --> K[Final Itinerary<br>Visual Catalog Output]
    style B fill:#e1f5fe
    style I fill:#fff3e0
    style E fill:#f3e5f5
