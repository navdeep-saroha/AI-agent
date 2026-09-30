# AI Agent with OpenRouter

A Python application that interfaces with Large Language Models (LLMs) via the OpenRouter API gateway using the official OpenAI Python SDK.

## Features

- **OpenRouter Gateway:** Connects to OpenRouter's API endpoint, enabling access to various models including free routing options (`openrouter/free`).
- **OpenAI SDK Compatibility:** Leverages standard OpenAI client patterns by configuring a custom `base_url`.
- **Environment Configuration:** Secure credential handling using `python-dotenv` to keep API secrets out of source control.

## Prerequisites

- [Python](https://www.python.org/) 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended package manager) or `pip`
- An [OpenRouter](https://openrouter.ai/) account and API key

## Setup

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd your-project-directory
   ```

2. **Install dependencies**:
   Using `uv`:
   ```bash
   uv sync
   ```
   Or using standard `pip`:
   ```bash
   pip install openai python-dotenv
   ```

3. **Configure Environment Variables**:
   Create a `.env` file in the root directory:
   ```bash
   touch .env
   ```
   Add your OpenRouter API key:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

   > **Note:** Ensure `.env` is listed in your `.gitignore` to prevent committing secrets to version control.

## Usage

Run the program with `uv`:

```bash
uv run main.py
```

Or directly with Python:

```bash
python main.py
```

The script will query the `openrouter/free` model and display the generated response in the console.

## Project Structure

```
├── .env                # Local environment secrets (ignored by git)
├── .gitignore          # Git exclusion rules
├── pyproject.toml      # Project configuration and dependencies
├── main.py             # Application entrypoint
└── README.md           # Documentation
```
