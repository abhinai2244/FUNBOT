# Fun Telegram Bot

A fun Telegram bot that can interact with users by sharing jokes, fun facts, and allowing users to play Rock-Paper-Scissors. It also includes a basic spam detection feature to ensure smooth interactions within the chat.

## Features:
- **Joke**: Get a random joke.
- **Fun Fact**: Get a random fun fact.
- **Rock-Paper-Scissors**: Play the classic game with the bot.
- **Spam Detection**: Automatically detects and bans users who send too many messages within a short time.
- **Commands**: `/start`, `/joke`, `/funfact`, `/rps <choice>`, and `/help`.

## Installation

1. **Clone the Repository**
   Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-folder>
Install Dependencies You need Python 3.7 or higher installed on your system. Install the required libraries using pip.

bash
Copy code
pip install python-telegram-bot --upgrade
pip install "python-telegram-bot[job-queue]"
Set Up Your Bot on Telegram

Create a new bot using BotFather on Telegram.
Copy the bot token provided by BotFather.
Configure Your Bot Open the test.py file and replace the bot token with your own:

python
Copy code
application = Application.builder().token('<YOUR_BOT_TOKEN>').build()
Replace <YOUR_BOT_TOKEN> with the token you received from BotFather.

Run the Bot Run the bot using the following command:

bash
Copy code
python3 test.py
The bot will now be up and running. It will start receiving commands and interacting with users.

Usage
Once the bot is up and running, you can interact with it through the following commands:

/start: Start the bot and get a list of available commands.
/joke: Get a random joke.
/funfact: Get a random fun fact.
/rps <choice>: Play Rock-Paper-Scissors with the bot. (Replace <choice> with rock, paper, or scissors)
/help: Show the available commands and how to use them.
Example Commands:
Start the bot:

plaintext
Copy code
/start
This will welcome the user and show the available commands.

Get a random joke:

plaintext
Copy code
/joke
The bot will reply with a random joke.

Get a random fun fact:

plaintext
Copy code
/funfact
The bot will reply with a random fun fact.

Play Rock-Paper-Scissors:

plaintext
Copy code
/rps rock
/rps paper
/rps scissors
The bot will play Rock-Paper-Scissors with you and show the result.

Get help:

plaintext
Copy code
/help
This command will list all available commands and their usage.

Spam Detection
The bot includes a spam detection feature. If a user sends more than 5 messages within a 5-second window, they will be banned from the chat. This feature helps to prevent spamming and ensures a smoother experience for all users.

Contributing
Feel free to fork this repository and submit pull requests for new features or bug fixes. Contributions are welcome!

License
This bot is open-source and free to use. It is licensed under the MIT License.

Contact
If you have any questions or issues, please contact the bot owner:

Telegram Username: @clutch008
kotlin
Copy code

### Instructions for New Users:
- This `README.md` will guide them through setting up the bot, using it, and understanding the key features like jokes, fun facts, and the Rock-Paper-Scissors game.
- It also covers the spam detection mechanism, which automatically bans users who spam the chat.

Feel free to customize the repository URL and any other details specific to your project!
