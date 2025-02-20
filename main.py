import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API key and translation prompt from environment variables
API_KEY = os.getenv("OPENAI_API_KEY")
TRANSLATION_PROMPT = os.getenv("TRANSLATION_PROMPT")

# Initialize OpenAI client
client = openai.OpenAI(api_key=API_KEY)


def translate_text(text, source_lang="English", target_lang="French"):
    """Translates text using OpenAI's GPT-4 API."""
    prompt = TRANSLATION_PROMPT.format(
        source_lang=source_lang, target_lang=target_lang, text=text
    )

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
