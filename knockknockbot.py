import tweepy
import time
import random


def word_list(f):
    """Opens a file and creates a list of each word
    f : str, file name
        file should be formated with one word on each line
    """
    fin = open(f)
    words = []
    for line in fin:
        word = line.strip()
        words.append(word)
    return words


def rand_noun():
    """chooses one random noun
    """
    path = 'nounlist.txt'
    words = word_list(path)
    return random.choice(words)


def rand_word():
    """chooses one random word
    """
    path = 'commonwords.txt'
    words = word_list(path)
    return random.choice(words)


def joke():
    """creates a knock knock jokes with a random noun and word
    """
    word1 = rand_noun()
    word2 = rand_word()
    joke = " Knock, knock.\n Who\'s there? \n {something}. \n {something} who? \n {something} {punchline}!".format(something=word1, punchline=word2)
    return joke

def main():

    # this code will not function as I erased these entries that are connected to
    # my twitter account
    CONSUMER_KEY = "" #'your API key number here'
    CONSUMER_SECRET = "" #'your API secret key number here'
    ACCESS_KEY = '' #'your access token here'
    ACCESS_SECRET = '' #'your access token secret here'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)



    twitter_API = tweepy.API(auth)
    twitter_API.update_status(joke())


main()