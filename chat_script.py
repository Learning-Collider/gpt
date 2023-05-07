import os
import openai

# Read openai api key from secure file
with open('gpt_apikey.txt') as api_key:
    openai.api_key = api_key.readline()

# Example method to store previous responses
memory = []

while True:
    inp = input("User: ")
    if (inp=='exit'):
        break
    memory.append(inp)
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Take on the role of a tour guide."},
        # Join previously stored responses into the "assistant" role to give ChatGPT api "memory"
        {"role": "assistant", "content": ''.join(memory)},
        {"role": "user", "content": inp},
    ]
    )

    memory.append(completion.choices[0].message.content)

    print('\n'+completion.choices[0].message.content+'\n')

print("Thanks for consulting me, Learning Collider's trustworthy GPT Assistant. Have a good day ahead!")