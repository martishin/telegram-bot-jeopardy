
# Telegram Jeopardy Bot

Telegram bot that uses a machine learning model to answer questions related to Jeopardy!  
The bot is built with the `python-telegram-bot` library and uses a `Doc2Vec` model that **will be trained** based on a Jeopardy dataset. Once trained, the model can provide answers to questions from the Jeopardy dataset.  
Interact with the live bot [here](t.me/martishin_jeopardy_bot)!

<img src="https://i.imgur.com/BsNjAG3.png" width="300" />

## Requirements
- Python 3.8 or above
- Telegram bot token (you can create one using [BotFather](https://core.telegram.org/bots#botfather))

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/martishin/telegram-bot-jeopardy.git
cd telegram-bot-jeopardy
```

### 2. Create the `.env` File
In the project root, create a `.env` file and add your bot token:
```bash
TELEGRAM_BOT_TOKEN=your-telegram-bot-token-here
```

### 3. Create a Virtual Environment and Install Dependencies
You can use the provided `Makefile` to automate the setup process.
```bash
make create-venv
```

### 4. Train the Model
You need to train the machine learning model (Doc2Vec) using the Jeopardy dataset:
```bash
make train-model
```

### 5. Run the Bot
After training the model, you can start the Telegram bot:
```bash
make run-bot
```

### 6. Run Tests
To ensure everything is working correctly, you can run the tests:
```bash
make test
```

## Usage
Once the bot is running, you can interact with it on Telegram. Start a conversation and ask questions related to Jeopardy. The bot will infer the most relevant question from its dataset and provide an answer.
