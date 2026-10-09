from dotenv import load_dotenv
from crewai import LLM, Agent,Task,Crew
import os

load_dotenv()

#api_key = os.getenv("OPENAI_API_KEY")
#model = os.getenv("OPENAI_MODEL_NAME")

print("MODEL:", os.getenv("OPENAI_MODEL_NAME"))
print("API KEY FOUND:", bool(os.getenv("OPENAI_API_KEY")))


llm = LLM(
    model=os.getenv("OPENAI_MODEL_NAME"),
    api_key=os.getenv("OPENAI_API_KEY")
)

print("MODEL:", os.getenv("OPENAI_MODEL_NAME"))
print("API KEY FOUND:", bool(os.getenv("OPENAI_API_KEY")))

city = input("Enter the city you want to travel to?: ")

planner = Agent(role="Travel Planner",
                 goal="Create a travel plan for {city}", 
                 backstory="You are a experienced travel planner who creates travel plans for users based on their preferences and interests.",
                 llm = llm,
                 verbose=True
                )
task = Task(description=f"Create a travel plan for the user who wants to travel to {city}." ,
             expected_output="suggests 3 places to visit there . For Example Amber Fort - hilltop fort with mirrored halls, go early",
             agent=planner
            )
crew = Crew(agents=[planner], tasks=[task])
print(crew.kickoff(inputs={"city": city}))