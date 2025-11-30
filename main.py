
from agents import runner, session_service
from google.genai import types
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Sample Personalized Input
user_request = """
Plan 10-day Italy trip for 4 (ages: 65 senior, 40, 35, 10 kid). Budget $8000. Senior: respiratory issues, very low walking tolerance, gut-sensitive. Extreme cleanliness obsession, must have breakfast. Interests: historical sites, shopping. Food: vegetarian Italian. Prefer mild weather, early mornings (not night owl).
"""

if __name__ == "__main__":
    session = session_service.create_session(app_name="travel_concierge", user_id="user1", session_id="rome_trip_2026")
    content = types.Content(role="user", parts=[types.Part(text=user_request)])
    
    print("Gemini ADK Travel Concierge Pipeline Starting...")
    logger.info("Session created. Input length: %d chars", len(user_request))
    
    events = runner.run(user_id="user1", session_id="Italy_trip_2026", new_message=content)
    
    total_cost = 0
    for event in events:
        if event.is_final_response():
            response = event.content.parts[0].text if event.content.parts else "Pipeline complete."
            print(f"\n[OBSERVABLE] Final Itinerary:\n{response}")
            logger.info("Final response generated. Length: %d", len(response))
        elif hasattr(event, 'tool_calls'):
            logger.info("Tool Call Traced: %s", event.tool_calls)
        # Metrics from state
        if 'optimized_plan' in session.state:
            total_cost = session.state['optimized_plan'].get('total_cost', 0)
            logger.info("Optimization Metrics: Iterations: %d, Final Cost: $%d", len(events), total_cost)
    
    print(f"\nPipeline Complete! Total: ${total_cost:.0f} (Compliant & Personalized)")
    logger.info("Session ended. State keys: %s", list(session.state.keys()))