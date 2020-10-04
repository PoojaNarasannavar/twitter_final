import tweepy
import os # operating system library

def create_api():
  consumer_key = os.getenv('P369EuIsKXTG7ZlWy3UOEhrnl')
  consumer_secret = os.getenv('9MZIeK1o381sdc1Ka47sVCYMdpMIwzSy2ziDJyvOMmszgWDyqc')
  access_token = os.getenv('1062764490498818048-dHAjbCiFIOliDgiIpp32Ng1e6N5mnr')
  access_token_secret = os.getenv('aALIZ29FUWeDboJmptdPVjuEKvRTGLthCdfcy5bjAruOZ')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
  api.verify_credentials()
  print('API Created')
  return api
  
# Complete code
import time

def follower_count(user):
  emoji_numbers =  {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                      4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

  uf_split = [int(i) for i in str(user.followers_count)]# Used to seperate 

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()]) 
  return emoji_followers

api = create_api()

while True:
    user = api.get_user('PavanSogalad')
    api.update_profile(name=f'pavan|{follower_count(user)} Followers')
    print(f'Updating Twitter Name : pavan|{follower_count(user)} Followers')
    print('Waiting to refresh')
    time.sleep(60)
            
  
                                                                                         
                
