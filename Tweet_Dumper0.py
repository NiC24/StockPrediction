import pandas as pd  # to store tweets into csv
import tweepy

# Twitter API credentials

#Twitter API credentials
consumer_key = "IXX57HfN1zC7Yi9fdi25vqkep"
consumer_secret = "zY56zi2JAbDSpT6TttEC9PfIAFhwuvvGjEtGiotXLz5IsFNenf"
access_key = "2838198962-U3ju9AS1SQz72UFbSm2TSrJWIXlQEolDAgjqzUK"
access_secret = "VrXTSbWWSsKHIpzGleNi4Qhk4laPlDz0q2IVuMvS9TQbw"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


def get_all_tweets(screen_name):
    alltweets = []
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    while len(new_tweets) > 0:
        print
        "getting tweets before %s" % (oldest)
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
        alltweets.extend(new_tweets)
        oldest = alltweets[-1].id - 1
        print("...%s tweets downloaded so far" % (len(alltweets)))

    data = [
        [obj.text.encode("utf8")] for obj in alltweets]
    dataframe = pd.DataFrame(data, columns=['tweet'])
    dataframe.to_csv("AB/%s_tweets.txt" % (screen_name), index=False)


if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets("AxisBank")
