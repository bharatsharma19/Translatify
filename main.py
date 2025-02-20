import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key from environment variable
API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(api_key=API_KEY)


def translate_text(text, source_lang="English", target_lang="French"):
    """Translates text using OpenAI's GPT-4 API."""
    prompt = f"""
    Please translate the following text from {source_lang} to {target_lang}. 
    This content is from NutriCheck and is intended for either customers or professionals. 
    The translation must be perfectly accurate, maintaining the original meaning and intent while ensuring clarity and precision. 
    The goal is to achieve maximum satisfaction (NPS 10/10).

    Text to translate:
    {text}

    Please provide only the translation, with no additional comments.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,  # Ensures accurate translations
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print("\n🌍 Translation Bot Running (Press Ctrl+C to Stop)\n")

    while True:
        try:
            text_to_translate = input(
                "Enter text to translate (or type 'exit' to quit): "
            ).strip()
            if text_to_translate.lower() == "exit":
                print("\n🚪 Exiting Translator... Goodbye!\n")
                break  # Stop the loop when 'exit' is entered

            translated_text = translate_text(text_to_translate)
            print("\n📝 Translated Text:\n", translated_text, "\n")

        except KeyboardInterrupt:
            print("\n\n🚪 Exiting Translator... Goodbye!\n")
            break  # Stop the loop if Ctrl+C is pressed
