import twitter

auth = twitter.OAuth(consumer_key="YCblw4wgWjV1T0K7tQir6TrFR",
consumer_secret="VbanfHUJQMPvrZXnWz0e5zEzVyWy84f0sDnb2zTCNuGWaYh3vB",
token="153933346-KVIgBgiTgzeu9PKnKM0eYropsLowBpEPQyy6W53e",
token_secret="f80mPqqN8F21y9shM6mg2Cv5M0l0hCfb5rGNlobUvKgWe"
)

t = twitter.Twitter(auth = auth)

status="おっぱい"
t.statuses.update(status = status)

