import os
from transformers import pipeline
from google import genai
import json 
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(
    api_key=os.getenv("genai_api_key")
)
# Load AI summarisation model
summarizer = pipeline("summarization")


def read_file(path):
    "Read and preprocess a text file."
    with open(path, "r", encoding="utf-8") as file:
        text = file.read().strip()

    if not text:
        return None
    return text

def summarize(text):
    prompt = f"""Summarise the following text and return ONLY valid JSON.
Required fields:
- title_topic
- summary
- keywords
- word_count
Text:{text}"""

    response = client.models.generate_content(
    model="gemini-3.6-flash",     
    contents=summarizer
)


def process_file(path):
    text = read_file(path)

    if text is None:
        return {
            "file": os.path.basename(path),
            "summary": None,
            "status": "empty"
        }

    return {
        "file": os.path.basename(path),
        "summary": "summary",
        "status": "success"
    }

def count_words(text):
    """Return the number of words in the original cleaned text."""
    return len(text.split()) 

# Prompt Construction
def build_prompt(text):
    """
    Construct the prompt sent to the AI model.
    """

    return f"""
You are an expert text summarisation system.

Analyse the following text and return ONLY a valid JSON object.

The JSON object MUST contain exactly these fields:"""

{{
    "title/topic": "A short title describing the main topic",
    "summary": "A concise summary in 2-3 lines",
    "keywords": ["keyword1", "keyword2", "keyword3"],
    "word_count": {count_words(text)}
}} 

def summarise_text(client, text):
    """Send text to the AI model and return structured JSON."""

    prompt = build_prompt(text)

    response = client.responses.create(
        MODEL=="gemini-3.6-flash",
        input=prompt
    )

    result = response.output_text.strip()

    # Convert the model's response into a Python dictionary.
    try:
        data = json.loads(result)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"The AI model did not return valid JSON.\n"
            f"Model output:\n{result}"
        ) from error

    # Validate the required fields.
    required_fields = {
        "title/topic",
        "summary",
        "keywords",
        "word_count"
    }

    missing_fields = required_fields - data.keys()

    if missing_fields:
        raise ValueError(
            f"Missing fields in AI response: {missing_fields}"
        )

    return data




def main():
 
 if  __name__ == "__main__":
    main()







