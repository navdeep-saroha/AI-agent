import os
import sys
import argparse

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

import prompts
from functions.call_function import available_functions, call_function

MAX_ITERS = 20


def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if not api_key:
        raise RuntimeError("API key not found")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    # Get and parse user prompt
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="Add your query")
    parser.add_argument("--verbose", action="store_true", help="increase output verbosity")
    args = parser.parse_args()

    messages: list[ChatCompletionMessageParam] = [
        {"role": "system", "content": prompts.system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")

    for _ in range(MAX_ITERS):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            temperature=0,
            tools=available_functions,
        )

        usage = response.usage
        if usage is None:
            raise RuntimeError("API response had no usage data")

        if args.verbose:
            print(f"Prompt tokens: {usage.prompt_tokens}")
            print(f"Response tokens: {usage.completion_tokens}")

        message = response.choices[0].message
        messages.append(message)  # assistant turn goes first

        if not message.tool_calls:
            print("Final response:")
            print(message.content)
            return

        for tool_call in message.tool_calls:
            if tool_call.type == "function":
                result_message = call_function(tool_call, verbose=args.verbose)

                if not result_message.get("content"):
                    raise RuntimeError(
                        f"Function {tool_call.function.name} returned no content"
                    )

                if args.verbose:
                    print(f"-> {result_message['content']}")

                messages.append(result_message)

    print(f"Error: agent did not finish within {MAX_ITERS} iterations.")
    sys.exit(1)


if __name__ == "__main__":
    main()