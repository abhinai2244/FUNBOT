import logging
from telegram import Update, ChatMember
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from collections import defaultdict
import random
import time

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the bot owner ID
OWNER_ID = 5756495153  # Replace with your actual Telegram user ID

# Dictionary to keep track of messages from users
user_message_count = defaultdict(int)
user_last_message_time = defaultdict(lambda: 0)

# Maximum number of messages allowed in the time frame (5 seconds)
SPAM_THRESHOLD = 5
SPAM_TIME_FRAME = 5  # in seconds

# Start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Welcome to the Fun Bot! 🎉\n"
        "Here are some commands you can use:\n"
        "/joke - Get a random joke\n"
        "/funfact - Get a fun fact\n"
        "/rps <rock/paper/scissors> - Play Rock-Paper-Scissors\n"
        "/help - Show this message\n"
        "owner:Abhinai"
    )

# Command to tell a joke
async def joke(update: Update, context: CallbackContext) -> None:
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them."
    ]
    await update.message.reply_text(random.choice(jokes))

# Command to tell a fun fact
async def funfact(update: Update, context: CallbackContext) -> None:
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible.",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries are not.",
        "A group of flamingos is called a 'flamboyance'."
    ]
    await update.message.reply_text(random.choice(facts))

# Command to play Rock-Paper-Scissors
async def rps(update: Update, context: CallbackContext) -> None:
    user_choice = context.args[0].lower() if context.args else ""
    choices = ["rock", "paper", "scissors"]
    bot_choice = random.choice(choices)

    if user_choice not in choices:
        await update.message.reply_text("Please choose rock, paper, or scissors. Usage: /rps <choice>")
        return

    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and bot_choice == "scissors") or \
         (user_choice == "scissors" and bot_choice == "paper") or \
         (user_choice == "paper" and bot_choice == "rock"):
        result = "You win!"
    else:
        result = "You lose!"

    await update.message.reply_text(
        f"You chose: {user_choice}\n"
        f"I chose: {bot_choice}\n"
        f"{result}"
    )

# Help command
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Here are some commands you can use:\n"
        "/joke - Get a random joke\n"
        "/funfact - Get a fun fact\n"
        "/rps <rock/paper/scissors> - Play Rock-Paper-Scissors\n"
        "/help - Show this message"
    )

# Spam detection function
async def detect_spam(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_message_count[user_id] += 1
    user_last_message_time[user_id] = time.time()

    # Check for spam
    if user_message_count[user_id] > SPAM_THRESHOLD:
        chat = update.effective_chat
        if chat.get_member(user_id).status in [ChatMember.ADMINISTRATOR, ChatMember.CREATOR]:
            return  # Don't ban admins

        await update.message.reply_text(f"{update.message.from_user.first_name}, you are spamming! You have been banned.")
        await context.bot.ban_chat_member(chat.id, user_id)  # Banning user
        reset_user(user_id)

    # Reset counts after time frame
    current_time = time.time()
    for user in list(user_message_count.keys()):
        if current_time - user_last_message_time[user] > SPAM_TIME_FRAME:
            reset_user(user)

# Reset user message counts
def reset_user(user_id):
    user_message_count[user_id] = 0
    user_last_message_time[user_id] = 0

# Send command usage details to the owner after bot starts
async def send_command_usage(context: CallbackContext) -> None:
    command_usage = (
        "Bot Command Usage:\n"
        "/joke - Get a random joke\n"
        "/funfact - Get a fun fact\n"
        "/rps <rock/paper/scissors> - Play Rock-Paper-Scissors\n"
        "/help - Show this message\n"
    )
    await context.bot.send_message(chat_id=OWNER_ID, text="Bot has started!\n" + command_usage)

# Main function to run the bot
def main() -> None:
    # Use Application instead of Updater in v20+
    application = Application.builder().token("7484528577:AAHHsvodUPBQIrgEGaf8P5XUiVc0MA8PH5E").build()  # Replace with your token

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("joke", joke))
    application.add_handler(CommandHandler("funfact", funfact))
    application.add_handler(CommandHandler("rps", rps))
    application.add_handler(CommandHandler("help", help_command))

    # Register Message handler for spam detection in groups
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, detect_spam))

    # Send command usage details to the owner
    application.job_queue.run_once(send_command_usage, when=0)

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
