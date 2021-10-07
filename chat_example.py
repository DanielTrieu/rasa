import rasa.core.agent as rasaAgent
import asyncio

model_path ='test/models/20211006-090042.tar.gz'
endpoints = None
agent = rasaAgent.create_agent(model_path,endpoints)

async def rasabot(message):
    
    responses = await agent.handle_text(message)
    for response in responses:
        for response_type, value in response.items():
            if response_type == "text":
               reply=value
    return reply           

print("Your bot is ready to talk!")
while True:
    message = input()
    reply_message = asyncio.run(rasabot(message))
    print(reply_message)
