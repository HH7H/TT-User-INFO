
# a simple TIKTOK User INFO BY: HH7H -> GitHub

import requests # type "pip3 install requests" if not downloaded
import json
import os

#---------------------------API----------------------------#
def Signer(TT_URL,UserAgent): # a Signer Function
    REQ_data = {
        'url': TT_URL, #TIKTOK URL
        'userAgent': UserAgent, #YOU Can chanage userAgent
        'Token': 'main-HH7H@X-Bogus', #API_TOKEN
        'method': 'GET' #TIKTOK INFO use GET method
    }
    response = requests.post(url='https://x-bogus.onrender.com/api/x-bogus/',data=REQ_data).json()
    return response['new_url']
#---------------------------API----------------------------#

username = 'tiktok' # username of user

TT_URL = f'https://www.tiktok.com/api/user/detail/?abTestVersion=%5Bobject%20Object%5D&aid=1988&appType=m&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F16.2%20Safari%2F605.1.15&channel=tiktok_web&cookie_enabled=true&device_id=7205333789277455877&device_platform=web_pc&focus_state=true&from_page=user&history_len=5&is_fullscreen=false&is_page_visible=true&language=en&os=mac&priority_region=IQ&referer=https%3A%2F%2Fwww.tiktok.com%2F&region=IQ&root_referer=https%3A%2F%2Fwww.tiktok.com%2F&screen_height=900&screen_width=1440&secUid=&tz_name=Asia%2FBaghdad&uniqueId={username}&user=%5Bobject%20Object%5D&&webcast_language=en' # TIKTOK URL

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15' # The userAgent most be the same on request

TT_URL = Signer(TT_URL=TT_URL,UserAgent=userAgent) # Sign TT_URL

command = f"curl '{TT_URL}' -H 'User-Agent: {userAgent}' -H 'X-Requested-With: XMLHttpRequest'" # Request Headers

response = os.popen(command).read() # use curl command because requests module get an empty

INFO = json.loads(response) # transform response as json data

print(INFO) # INFO :)
