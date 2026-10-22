import logging
import sys
from pathlib import Path
from anyio import Path
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("summarizer.log", encoding="utf-8")
    ]
)
logger = logging.getLogger(__name__)

def read_and_preprocess(input_file):
    "Read and preprocess the input text file."
    logger.info("Processing input file: %s", input_file)

    path = Path(input_file)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    if not path.is_file():
        raise ValueError(f"Input path is not a file: {input_file}")

text = os.path
if not text.strip():
    raise ValueError("Input file is empty")
text = text.replace("\n","Input")
logger.info("Successfully read and preprocessed the input file.")


def summarize_text(text, length, model):
    logging.debug(f'summarize_text called with model={model}, length={length}')
    # Simulate summaries depending on length parameter
    if length == 'short':
        return 'AI summaries save developer integration overhead.'
    elif length == 'medium':
        return 'Enterprise AI applications use REST endpoints instead of bespoke ML pipelines, saving deployment overhead.'
    else:
        return 'Modern enterprise platforms leverage cloud LLM completions APIs. This minimizes time-to-market but requires orchestrations to manage API security and errors.'

def generate_summary(text):
    """
    Genedrate a summary of the input text using the AI model.
    """
    logger.info("Generating summary for the input text.")
    try:
        prompt = build_prompt(text)
        response = client.models.generate_content(
            mdel="gemini-3.6.-flash",
            contents=prompt,
        )
        return response.contents.text
    except Exception:
        logger.exception("Error occurred while generating summary")
        raise

def save_summary_to_file(summary,output_file):
    """
    Save the generated summary to an output file.
    """
    logger.info("Saving summary to output file: %s",output_file)
    try:
        path = Path(output_file)
        path.write_text(summary,encoding="utf-8")
        logger.info("Summary successfully saved to output file.")
    except Exception :
        logger.error("Error occurred while saving summary to file: %s")
        raise

