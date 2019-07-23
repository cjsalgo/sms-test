from globe.connect import sms

sms = sms.Sms("21580790", "UrSIj8JlBwhNhVAVuW5TpZ5kz6Zw93G6uAHVew_1aEU")
sms.setReceiverAddress("+639994521937")
sms.setMessage("Successfully Sent Test SMS Finally!")
sms.sendMessage()
print(sms.getResponse())

#SCRATCH CODES:

#oauth = oauth.Oauth("pLE5Sxo5zLh5rTGp5Bi5g6hq6L95SKBj", "3553fc8b8ebd155c558d881796b208757316b325717093db93ed5581072074cf")

#POST -f 'https://developer.globelabs.com.ph/oauth/access_token?app_id=pLE5Sxo5zLh5rTGp5Bi5g6hq6L95SKBj&app_secret=3553fc8b8ebd155c558d881796b208757316b325717093db93ed5581072074cf&code=kIbXEK6tBoqbqCqE4okSeBzGgfjb7j9sqpB9etEdLMbfL5jzghnbkz9HBkzndH6KRBkuzGeXpHAXgrXFKoqKqu5nzMEhGzpKBsoRek9sGjoLBCynnpXfxAa8RfA7ixrya7gTa6zfaznbxfzKoe9CM4eXas6EpnRsaqzXrheRqdXubLgbXF5renkHL7Re5uM4zKbHopkz8HdqjG7h8kLM7fkjBgBt9d7EgsjRzx8fAd4peSnXq7oCnzE8xtkBBK5I'

# from globe.connect import sms
#
# sms = sms.Sms("21585562", "zgNXZAglm0wZJGgOJMHEexW-L1-QVGy1zkaPmeu33MM")
# sms.setReceiverAddress("+639185228256")
# sms.setMessage("Successfully Sent Test SMS Finally!")
# sms.sendMessage()
# print(sms.getResponse())

#POST -f 'https://developer.globelabs.com.ph/oauth/access_token?app_id=X6dgtakX4XH9dTMLkKiXAeH4E6eztdgB&app_secret=5539cfd4b1f9d31b29c5e900a444c535c4142896d1b596ee1c333f405691c2a1&code=nSokbRxCnMEyRhBj8e5CeAzqnUdL6jgho56rMS7A86ntqpM8ehXzX9pCz7jynf6gRA7uEpkKbFnKR7kSbRrB6UKGzxosd9K49FpdR9RszgMMasrAKEaHe4yBqf4RcLrEqBeiyzefLnKGnHXaMGksj4RA5sk5KeXFRzzrEsLArMLU7MRnkS9jk7rFAkRp6uaejABfKyXXRCgrMM7haL8rytjE6BqS896zAhd4z94UXx8LoCBEEMXh8bb9bCxAX5MS'

# from globe.connect import oauth
#
# oauth = oauth.Oauth("pLE5Sxo5zLh5rTGp5Bi5g6hq6L95SKBj", "3553fc8b8ebd155c558d881796b208757316b325717093db93ed5581072074cf")
#
# # get redirect url
# print oauth.getRedirectUrl()
#
# # get access token
# print oauth.getAccessToken("nSokbRxCnMEyRhBj8e5CeAzqnUdL6jgho56rMS7A86ntqpM8ehXzX9pCz7jynf6gRA7uEpkKbFnKR7kSbRrB6UKGzxosd9K49FpdR9RszgMMasrAKEaHe4yBqf4RcLrEqBeiyzefLnKGnHXaMGksj4RA5sk5KeXFRzzrEsLArMLU7MRnkS9jk7rFAkRp6uaejABfKyXXRCgrMM7haL8rytjE6BqS896zAhd4z94UXx8LoCBEEMXh8bb9bCxAX5MS")
