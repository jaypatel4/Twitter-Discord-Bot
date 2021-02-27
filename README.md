# Discord-Tweet Bot

Discord-Tweet is a twitter discord bot that allows users to monitor and search twitter from Discord.
## Installation

Clone this repository using the command

```bash
git clone https://github.com/jaypatel4/Twitter-Discord-Bot
```

## Usage
Fill in the token and access information in config.py
```python

# Discord configurations and access tokens
BOT_PREFIX = ("BOT_PREFIX_HERE")
TOKEN = "DISCORD_TOKEN_HERE"
APP_ID = "APPLICATION_ID"
OWNER = []
VERSION = "1.0.0"

# Twitter access tokens
CONSUMER_KEY = "TWITTER_CONSUMER_KEY"
CONSUMER_SECRET_KEY = "TWITTER_CONSUMER_SECRET_KEY"
ACCESS_TOKEN = "ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "ACCESS_TOKEN_SECRET"

#Twitter streaming preferences
#True = continue tweepy if bot encounters an error for a specific user, False = stop stream on error
COUNTINUOUS = "TRUE"
```
Once done, simply run the bot using the command:
```bash
python bot.py
``` 

## License
[MIT](https://choosealicense.com/licenses/mit/)
