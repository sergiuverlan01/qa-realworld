from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text

messages = []

# Primul schimb
add_user_message(messages, "defineste mecanica cuantica intr-o propozitie de 10 cuvinte")
first_answer = chat(messages)
print(f"Primul raspuns:\n{first_answer}\n")

# Salvezi primul raspuns real in conversatie
add_assistant_message(messages, first_answer)

# Al doilea schimb - Claude stie contextul
add_user_message(messages, "mai adauga o propozitie de 5 cuvinte legata de acelasi subiect")
second_answer = chat(messages)
print(f"Al doilea raspuns:\n{second_answer}")