import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("API key not found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
#Get and parse user prompt
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type = str, help = "Add your query")
args = parser.parse_args()
content = args.user_prompt

#Generate Response
response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": content,
        }
    ],
)



def main():
    usage = response.usage
    if usage is None:
        raise RuntimeError("API Key Failed")    

    usage_token = usage.prompt_tokens
    complete_token = usage.completion_tokens



    print(f"Prompt tokens: {usage_token}")
    print(f"Response tokens: {complete_token}")
    print("Response:")
    print(response.choices[0].message.content)



if __name__ == "__main__":
    main()
