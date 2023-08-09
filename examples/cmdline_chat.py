# Very simple command line chat client
import os
import openai
import connectlm as cm


openai.api_key = os.environ["OPENAI_API_KEY"]

print("To exit the chat, type 'exit'\n")

query = cm.ChatQuery()
while (prompt := input("you : ")) != "exit":
    message = query.send(prompt)
    print(f"\n{message['role']} : {message['content']}\n")
