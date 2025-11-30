import os
from dotenv import load_dotenv
from google.adk.agents import LlmAgent, SequentialAgent, ParallelAgent, LoopAgent, AgentTool
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
from pydantic import BaseModel, Field
from typing import List, Dict
from tools import budget_tool, places_tool, Profile, HotelVetting

load_dotenv()
import google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class Plan(BaseModel):
    dates: str = Field(..., description="Optimal dates e.g., '15-25 October 2026'")
    flights: Dict = Field(..., description="Flight details, scaled by travelers")
    hotel: HotelVetting = Field(..., description="Vetted hotel with photos")
    activities: List[Dict] = Field(..., description="Personalized low-impact activities")
    total_cost: float = Field(..., description="Optimized total")

session_service = InMemorySessionService()

# Step 1: Profile Extractor (Detailed personalization)
profile_agent = LlmAgent(
    model="gemini-2.5-pro",  # Fallback: "gemini-2.0-flash"
    name="profile_extractor",
    description="Extracts detailed profile: ages, health (respiratory/gut/mobility), cleanliness, interests (history/nature/shopping), food, weather/sleep.",
    instruction="Parse input into Profile JSON. Factor illnesses, obsessions (e.g., cleanliness >9.5), niches (vegetarian food, night-owl activities). Store in state['profile'].",
    output_schema=Profile,
    output_key="profile"  # Auto-saves to shared state
)

# Step 2: Strategist (Dates based on profile state)
strategist_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="strategist",
    description="Suggests dates matching weather/sleep/health (e.g., mild for respiratory, off-peak for budget).",
    instruction="From {profile} in state, suggest 10-day 2026 window. Avoid heat >30C, crowds; prefer mild for {profile.weather_pref}. For night owls, evening activities. Output JSON 'dates'. Use budget_tool for impact.",
    tools=[budget_tool],
    output_key="dates"
)

# Parallel Sub-Agents for Step 3
flight_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="flight_agent",
    description="Estimates flights: Scale by {profile.travelers}, direct for low mobility, check delays/baggage.",
    instruction="For {profile.destination} in {dates}, {profile.travelers} people. Adjust for health (e.g., short layovers for respiratory). Use budget_tool. Output JSON 'flights' with cost_usd.",
    tools=[budget_tool],
    output_key="flights"
)

hotel_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="hotel_agent",
    description="Vets hotels: Query Places for {profile.destination}, check cleanliness >9.5, amenities (breakfast, accessible), scale cost by travelers/duration.",
    instruction="Query for luxury hotels matching {profile.comfort_requirements} (e.g., extreme cleanliness). Use places_tool. Reject if score <9.5 or no breakfast. Include photos. Output HotelVetting JSON.",
    tools=[places_tool],
    output_key="hotel"
)

activity_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="activity_agent",
    description="Plans activities: Low-impact (golf-cart for mobility), match {profile.interests/food_preferences}, night-owl friendly.",
    instruction="Suggest 3-5 options for {profile.interests} (e.g., historical tours, vegetarian dining). Filter for health (low walking, gut-safe food). Scale cost by travelers. Use budget_tool. Output list JSON.",
    tools=[budget_tool],
    output_key="activities"
)

parallel_search = ParallelAgent(
    name="parallel_search",
    sub_agents=[flight_agent, hotel_agent, activity_agent],
    description="Concurrent searches: Flights + Hotels + Activities, sharing state."
)

# Step 4: Loop Optimizer (Iterate plans if over budget)
optimizer_agent = LoopAgent(
    name="optimizer",
    sub_agent=parallel_search,  # Re-runs parallel for new plans
    max_iterations=3,
    description="Loop: Generate plan, check total vs {profile.budget_usd}. If over, regenerate (shift dates, cheaper options) without violating health/cleanliness.",
    instruction="Calc total = flights.cost + hotel.cost + sum(activities.cost). If > budget, adjust (e.g., off-peak dates) and re-run parallel_search. Use budget_tool. Stop if under or max iter. Output Plan JSON.",
    tools=[budget_tool],
    output_key="optimized_plan"
)

# Step 5: Catalog Generator (Visual output with state compaction)
catalog_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="catalog_generator",
    description="Compiles Markdown catalog: Day-by-day, costs, compliance, embed hotel/activity photos/maps from state.",
    instruction="From {optimized_plan}, generate Markdown: Title, dates, budget breakdown, itinerary. Embed images (e.g., ![Hotel]({hotel.photos[0]})). Compliance: All rules met (health-safe, clean >9.5). Compact prior state.",
    output_key="itinerary"
)

# Main Sequential Pipeline (Core: Chains all steps with shared state)
travel_pipeline = SequentialAgent(
    name="travel_concierge_pipeline",
    sub_agents=[
        profile_agent,      # 1. Extract
        strategist_agent,   # 2. Dates
        parallel_search,    # 3. Parallel searches
        optimizer_agent,    # 4. Loop optimize
        catalog_agent       # 5. Catalog
    ],
    description="Sequential pipeline for personalized travel: Profile → Dates → Search → Optimize → Catalog. Shared state enables pipelining."
)

# Router (Deploys pipeline as root)
root_agent = LlmAgent(
    model="gemini-2.5-pro",
    name="router",
    description="Initial router: Delegates to travel_pipeline.",
    instruction="Route all travel queries to travel_pipeline. Log events.",
    tools=[AgentTool(target_agent=travel_pipeline)]
)

# Runner
runner = Runner(agent=root_agent, session_service=session_service, app_name="travel_concierge")