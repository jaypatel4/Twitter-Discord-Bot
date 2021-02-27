import discord
from discord.ext import commands
import tweepy
import time

try:
    from config import BOT_PREFIX,TOKEN,APP_ID,OWNER,CONSUMER_KEY,CONSUMER_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET, VERSION, CONTINUOUS
except IOError:
    sys.exit("Could not open configs")
except ModuleNotFoundError
    sys.exit("Config file not set")

#Set command prefix for the bot
bot = commands.Bot(command_prefix = '!')

#List of watched users on twitter
watchList = []

#Authenticate credentials to access Twitter API
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

#Start tweepy (this is used to stream the tweets)
try:
    api = tweepy.API(auth, wait_on_rate_limit =True)
except:
    print("Twitter authentication failed")


#Declare tweepy streamlistener, you can change this to change how the stream handles events such as errors, data streamed, etc
#For full documentation visit: https://docs.tweepy.org/en/latest/streaming_how_to.html#summary
class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        bot.say("Encountered error {status_code}")
        
        if status_code == 420:
            # Tweepy's configs allow for the stream to be restarted automatically with a cooldown
            if(CONTINUOUS = "True")
                time.sleep(5)
                return True
            return False

    #When tweepy returns data from the stream
    def on_data(self, data){
        printTweets(data)
    }
#Begin stream listener
StreamListener = StreamListener()
try: 
    Stream = tweepy.Stream(auth = api.auth, listener=StreamListener)
except:
    bot.say("Encountered error setting up tweet streamer")

#Filter the stream to only the users being watched by the discord server
def startStream(watchlist):

    myStream.filter(follow=watchList)

#Change the stream to search for specific items rather than followers
def searchStream(searchList):
    myStream.filter(track = searchList)

#Prints data returned by the stream
def printTweets(data):
    bot.say("Data retrieved from twitter:")
    for item in data:
        bot.say(item)

#Basic bot configuration
@bot.event
async def on_ready():
    print('Bot is ready')
    print('Running version {VERSION} of the TweetBot')


@bot.command(pass_context = True)
#Use watch command to add a user to the watch list
async def watch(ctx, *args):
    watchList.append(args)
    startStream(watchlist)
    bot.say("Added {args} to the watchlist")

#Use search to search current tweets (Twitter API will automatically set the default date searched)
async def search(ctx, *args):
    searchStream(args)
