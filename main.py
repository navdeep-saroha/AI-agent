import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("API key not found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ],
)

def main():
    usage_token = response.usage.prompt_tokens
    complete_token = response.usage.completion_tokens

    if not usage_token or not complete_token:
        raise RuntimeError("API Key Failed")

    print(f"Prompt tokens: {usage_token}")
    print(f"Response tokens: {complete_token}")
    print("Response:")
    print(response.choices[0].message.content)



if __name__ == "__main__":
    main()
