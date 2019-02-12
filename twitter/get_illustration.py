from requests_oauthlib import OAuth1Session
import json
import os
import re
import urllib
import setting

twitter = OAuth1Session(
    setting.CONSUMER_KEY,
    setting.CONSUMER_SECRET,
    setting.ACCESS_TOKEN,
    setting.ACCESS_TOKEN_SECRET
)
mkdir_name = 'kyoko_illustration'

def dir_check():
    if not os.path.isdir(mkdir_name):
        os.mkdir(mkdir_name)
    check_count = 0
    while True:
        if not os.path.isdir(mkdir_name + "/dir" + str(check_count)):
            os.mkdir(mkdir_name + "/dir" + str(check_count))
            dir_name = "/dir" + str(check_count)
            return dir_name
        check_count += 1
        　
def get_target_word(word): #searchTweetsのAPI参照　https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    params = {
        "q":word,
        "count":100
    }
    req = twitter.get(url, params = params)
    timeline = json.loads(req.text)
    return timeline

def get_illustration (timeline, dir_name):
    global image
    global image_number
    image_number = 0
    check_image = []
    for tweet in timeline['statuses']:
        try:
            media_list = tweet['extended_entities']['media']
            for media in media_list:
                image = media['media_url']
                if image in check_image:
                    continue
                with open(mkdir_name + dir_name +"/kyoko_image_"+str(image_number) +"_"+os.path.basename(image), 'wb') as f:
                    img = urllib.request.urlopen(image).read()
                    f.write(img)
                check_image.append(image)
                image_number += 1
            print("get tweet media")
        except KeyError:
            print("KeyError:画像を含んでいないツイートです")
        except:
            print("error")


if __name__ == '__main__':
    dir_name = dir_check()
    all_list = []
    # 検索対象の単語を設定
    # ORで条件を付けれる
    # 例:ward = "佐久間まゆ+OR+ままゆ"
    # ならば、ツイートに「佐久間まゆ」、もしくは「ままゆ」と含まれる物を取得
    word = "五十嵐響子"
    timeline = get_target_word(word)
    get_illustration(timeline, dir_name)