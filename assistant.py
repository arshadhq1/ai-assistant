import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq

API_KEY = os.environ.get("GROQ_API_KEY")

client = Groq(api_key=API_KEY)

system_prompt = "You are a brutally honest mentor for a student who just finished class 12. You give direct, practical advice about technology, AI, careers, and learning. No fluff, no motivation quotes. Just truth. Always respond in 3-5 lines maximum. No bullet points. Be direct."

conversation_history = []

print("AI Assistant ready. Type quit to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Bye!")
        break

    conversation_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": system_prompt}] + conversation_history
    )

    reply = response.choices[0].message.content

    conversation_history.append({"role": "assistant", "content": reply})

    print(f"AI: {reply}\n")