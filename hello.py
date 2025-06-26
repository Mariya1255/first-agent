from dotenv import load_dotenv
load_dotenv()

from my_agents import Agent, Runner

#from openai import AsyncOpenAI
#import os

#gemini_api_key = os.getenv('GEMINI_API_KEY')

#client = AsyncOpenAI(
    #api_key=gemini_api_key,
    #base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#)


agent = Agent(
    name= 'Assistant',
    instructions= 'You are a helpful assistant.',
)

prompt = 'Hello, how are you ?'

runner = Runner.run_sync(agent, prompt)
print(runner.final_output)



#import asyncio
#from openai import AsyncOpenAI
#from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

#gemini_api_key = ""

#Reference: https://ai.google.dev/gemini-api/docs/openai
#client = AsyncOpenAI(
   # api_key=gemini_api_key,
   # base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
#)

#set_tracing_disabled(disabled=True)

#model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),

#async def main():
    # This agent will use the custom LLM provider
    #agent = Agent(
       # name="Assistant",
       # instructions="You are a smart and helpful assistant.",
      #  model=model,
    #)

    #result = await Runner.run(
       # agent,
      #  "Tell me about recursion in programming.",
    #)
    #print(result.final_output)


#if __name__ == "__main__":
    #asyncio.run(main())