import csv
import json

##### Update these paths: #####
coffee_fpath_in = '../data/coffee-tweets.json'
coffee_csv_fpath_out = '../data/coffee-tweets-data.csv'

def load_multiline_json(json_fpath):
    
    with open(json_fpath) as file_in:
        dicts_out = [json.loads(x) for x in file_in.readlines()]

    return dicts_out


def get_tweet_info(tweet, return_col_names=False, keywords_in_tweet=None):
    
    colnames = ['tweet_id', 'user_id', 'follower_count', 'acct_verified',
    'favorite_count', 'retweet_count', 'hashtag_count', 'user_mention_count']

    top_data = {'tweet_id': 'id',  'favorite_count': 'favorite_count',
        'retweet_count': 'retweet_count'}

    user_data = {'user_id': 'id', 'follower_count': 'followers_count',
        'acct_verified': 'verified'}

    entity_data = {'hashtag_count': 'hashtags', 'user_mention_count':
        'user_mentions'}

    tweet_data = []
    for col in colnames:
        if col in top_data:
            elem = tweet[top_data[col]]
        elif col in user_data:
            # use int to convert boolean to 1/0.
            elem = int(tweet['user'][user_data[col]])
        elif col in entity_data:
            elem = len(tweet['entities'][entity_data[col]])
        else:
            raise Exception(f'Cant find {col}')
        tweet_data.append(elem)

        if keywords_in_tweet:
            tweet_data.extend(tweet_text2keywords_count(tweet['text'],
                                                        keywords_in_tweet))

    if return_col_names:
        if keywords_in_tweet:
        # include the keywords as column names with _count appended to name
            colnames.extend([x + '_count' for x in keywords_in_tweet])
        return [colnames, tweet_data]
    else:
        return tweet_data

def tweet_text2keywords_count(tweet, keywords):

    counts = []
    for word in keywords:
        if word != word.lower():
            raise ValueError(f'Expecting keywords to be lowercase, got: {word}')
        counts.append(tweet.lower().count(word))
    return counts


def tweet_info2csv(tweets, csv_fpath, include_header=True, keywords_in_tweet=None):
   
    with open(csv_fpath, 'w') as file_out:
        writer = csv.writer(file_out)
        already_printed_header = False
        for tweet in tweets:
            if include_header and not already_printed_header:
                writer.writerows(get_tweet_info(tweet, return_col_names=True,
                                        keywords_in_tweet=keywords_in_tweet))
                already_printed_header = True
            else:
                writer.writerow(get_tweet_info(tweet, return_col_names=False,
                                        keywords_in_tweet=keywords_in_tweet))


if __name__ == '__main__':
    coffee_dicts = load_multiline_json(coffee_fpath_in)

    coffee_kwds = ['coffee', 'espresso', 'cappuccino', 'latte', 'mocha']
    tweet_info2csv(coffee_dicts, coffee_csv_fpath_out, include_header=True,
                   keywords_in_tweet=coffee_kwds)