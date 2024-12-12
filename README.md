# Cryptography Bot

## Overview
The Cryptography Bot is a Telegram bot designed to provide cryptographic services, including text encryption and hashing, directly within a chat interface. Users can encrypt text using AES encryption or generate hashes using SHA-1 or MD5 algorithms. Additionally, the bot includes administrative features for managing supported algorithms.

## Features
1. **Encryption**
   - Encrypt text using AES encryption.
   - Generate and provide the encryption key for decryption.
   
2. **Hashing**
   - Generate cryptographic hashes using:
     - SHA-1
     - MD5
   
3. **Admin Panel**
   - Accessible to the admin user.
   - View and manage supported algorithms.

4. **Interactive Commands**
   - User-friendly command-based interface for seamless interaction.

## Setup Instructions

### 1. Prerequisites
- Python 3.10 or higher installed.
- Install the required libraries:
  ```bash
  pip install cryptography python-telegram-bot
A Telegram bot token obtained from BotFather.
2. Environment Configuration
Replace YOUR_BOT_TOKEN_HERE in the code with your bot token.
Replace ADMIN_ID with your Telegram user ID (used for administrative commands).
3. Running the Bot
Save the bot code in a Python file (e.g., bot.py).
Run the bot using:
bash
Copy code
python bot.py
Commands
User Commands
/start
Displays a welcome message and the main menu of features.

/help
Provides guidance on how to use the bot and its features.

/encrypt
Initiates text encryption using AES.

/hash
Guides the user to select a hashing algorithm (SHA-1 or MD5).

Admin Commands
/admin
Accessible only to the admin.
Displays the current active algorithms and allows management of these algorithms.
How to Use
1. Start the Bot
Use the /start command to begin interacting with the bot.
2. Encrypt Text
Send /encrypt to initiate the encryption process.
Enter the text you want to encrypt.
The bot will respond with the encrypted text and a key. Keep the key safe for decryption.
3. Generate a Hash
Send /hash to choose a hashing algorithm.
Enter 1 for SHA-1 or 2 for MD5.
Provide the text to hash, and the bot will return the hash value.
4. Access Admin Panel
If you are the admin, send /admin to manage algorithms.
View active algorithms and update the list as needed.
Example Interactions
1. Encryption Example
User: /encrypt
Bot: Please send the text you want to encrypt.
User: Hello World
Bot:
plaintext
Copy code
🔒 Encrypted Text: gAAAAABk...
🔑 Keep this key safe: V3JUaWZt...
2. Hashing Example
User: /hash
Bot: Choose a hashing algorithm: 1. SHA-1 2. MD5
User: 1
Bot: Please send the text you want to hash using SHA-1.
User: Hello World
Bot: SHA-1 Hash: 2ef7bde6...
3. Admin Example
User (Admin): /admin
Bot:
plaintext
Copy code
Admin Menu:
You can manage algorithms here.

Current active algorithms:
- AES Encryption/Decryption
- SHA-1 Hashing
- MD5 Hashing

You can add or remove algorithms by typing them.
Notes
Security: Ensure that the encryption key provided during the encryption process is stored securely, as it is required for decryption.
Admin Access: Only the admin ID specified in the code can access administrative commands.
Error Handling: If the bot encounters unexpected input, it will gracefully handle it by resetting the user's mode.
Contact
For issues or feature requests, please contact the bot developer. 
## contact telegram : @clutch008







