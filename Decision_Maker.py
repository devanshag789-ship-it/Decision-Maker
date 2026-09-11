import random
import time

question = input("Ask your question: ")

print("Thinking...")
time.sleep(2)

responses = {
    "yes": ["Yes", "Absolutely", "Without doubt"],
    "no": ["No", "Definitely not"],
    "maybe": ["Ask again later", "Unclear right now", "Try again soon"]
}

# pick a random category, then a random response from it
category = random.choice(list(responses.keys()))
decision = random.choice(responses[category])

print("AI Decision:", decision)
