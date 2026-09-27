import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)



SYSTEM_PROMPT = """you need to be an hackathon assistance, and you need not to answer for unrelevant question apart from hackathon

"""

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

print("🚀 Hackathon Assistant AI")
print("Your AI teammate for hackathons")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower().strip() in ["exit", "quit"]:
        print("\nChefMate: Happy cooking! 👨‍🍳")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    try:

        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            temperature=1,
            max_completion_tokens=2048,
            top_p=1,
            reasoning_effort="medium",
            stream=True,
            stop=None
        )

        print("\nHackathon Assistant: ", end="")

        assistant_response = ""

        for chunk in completion:
            text = chunk.choices[0].delta.content or ""
            print(text, end="", flush=True)
            assistant_response += text

        print("\n")

        # Save response so Hackathon Assistant remembers the conversation
        messages.append({
            "role": "assistant",
            "content": assistant_response
        })

    except Exception as e:
        print("\nError:", e)