# Very simple command line chat client
import connectlm as cm


cm.init(["openai"])

print("To exit the chat, type 'exit'\n")

query = cm.QueryChat()
while (prompt := input("you : ")) != "exit":
    response = query.send(prompt)
    print(response["content"])
