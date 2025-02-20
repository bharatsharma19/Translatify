# GPT-4 Translator Bot
A Python-based translation tool powered by OpenAI's GPT-4 API. This script allows users to translate text from one language to another with high accuracy.

## 🚀 Features
- Uses **GPT-4** for high-quality translations
- Supports **customizable translation prompts** via `.env`
- **Command-line interface** for easy text input and output
- **Secure API key handling** with environment variables

## 📺 Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/bharatsharma19/Translatify.git
   cd Translatify/
   ```

2. **Set up a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** based on `.env.example`
   ```bash
   cp .env.example .env
   ```

5. **Edit `.env` and add your OpenAI API key**
   ```ini
   OPENAI_API_KEY=your_api_key_here
   ```

## 🎮 Usage
Run the script and enter text to translate:
```bash
python main.py
```

Example interaction:
```
🌍 Translation Bot Running (Press Ctrl+C to Stop)

Enter text to translate (or type 'exit' to quit): Hello, how are you?
📝 Translated Text:
 Bonjour, comment ça va?
```

## ⚙️ Configuration
You can customize the translation prompt and model settings in the `.env` file:

```ini
# Default languages
DEFAULT_SOURCE_LANGUAGE=English
DEFAULT_TARGET_LANGUAGE=French

# OpenAI model selection\OPENAI_MODEL=gpt-4

# Temperature setting (0 = accurate, 1 = creative)
OPENAI_TEMPERATURE=0.0
```

## 🤝 Contributing
Feel free to fork this repo, submit issues, or suggest improvements!

## 📜 License
This project is licensed under the **MIT License**.
