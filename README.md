# TT-User-INFO

First Version by: HH7H

# example
```py

# a simple TIKTOK User INFO BY: HH7H -> GitHub

import requests # type pip3 install requests if not downloaded
import json
import os

def Signer(TT_URL,UserAgent): # a Signer Function
    REQ_data = {
        'url': TT_URL, #TIKTOK URL
        'userAgent': UserAgent, #YOU Can chanage userAgent
        'Token': 'main-HH7H@X-Bogus', #API_TOKEN
        'method': 'GET' #TIKTOK INFO use GET method
    }
    response = requests.post(url='https://x-bogus.onrender.com/api/x-bogus/',data=REQ_data).json()
    return response['new_url']


username = 'tiktok' # username of user

TT_REQ_URL = f'https://www.tiktok.com/api/user/detail/?abTestVersion=%5Bobject%20Object%5D&aid=1988&appType=m&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_6%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F15.3%20Safari%2F605.1.15&channel=tiktok_web&cookie_enabled=true&device_id=7199589529188419078&device_platform=web_pc&focus_state=true&from_page=user&history_len=2&is_fullscreen=false&is_page_visible=true&language=en&os=mac&priority_region=&referer=&region=IQ&screen_height=1194&screen_width=834&secUid=&tz_name=Asia%2FBaghdad&uniqueId={username}&webcast_language=en&msToken=9i4_vwtv-LUm9N2RwFWNJgLV44wOLjFcbhHwotGK1ceWXuTAkR-8q3cr8EVIa-GSOV3hqTjC2k_1IwKEe_z-Qj19P66yA2_5Q825xAe6CiQqd6AcFftIqVQ5BAlybzY6QPoC2wslwg==' # TIKTOK URL

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15' # The userAgent most be the same on request

TT_REQ_URL = Signer(TT_URL=TT_REQ_URL,UserAgent=userAgent) # Sign a TT_REQ_URL
print(TT_REQ_URL)
# a Simple solution because requests lib get empty response
command = f"curl '{TT_REQ_URL}' -H 'User-Agent: {userAgent}'"

response = os.popen(command).read() # make a requests with curl command

INFO = json.loads(response) # decode with json

print(INFO) # INFO :)
```
# result

```json
{
  "userInfo" : {
    "stats" : {
      "heart" : 285700000,
      "followerCount" : 67700000,
      "diggCount" : 0,
      "videoCount" : 578,
      "heartCount" : 285700000,
      "followingCount" : 572
    },
    "user" : {
      "avatarLarger" : "https:\/\/p16-sign-va.tiktokcdn.com\/tos-maliva-avt-0068\/1971e99be0d67160f34f39fb1d66a0e5~c5_1080x1080.jpeg?x-expires=1676847600&x-signature=ZHkl%2FNBuTI9DE4K5RMdz0830I8w%3D",
      "followingVisibility" : 1,
      "secret" : false,
      "relation" : 0,
      "duetSetting" : 0,
      "nickname" : "TikTok",
      "avatarThumb" : "https:\/\/p16-sign-va.tiktokcdn.com\/tos-maliva-avt-0068\/1971e99be0d67160f34f39fb1d66a0e5~c5_100x100.jpeg?x-expires=1676847600&x-signature=%2B2Cz63r1qSNfKW4LHdU7MhEglks%3D",
      "bioLink" : {
        "link" : "linktr.ee\/tiktok",
        "risk" : 0
      },
      "privateAccount" : false,
      "signature" : "the 🕰️ app",
      "secUid" : "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
      "avatarMedium" : "https:\/\/p16-sign-va.tiktokcdn.com\/tos-maliva-avt-0068\/1971e99be0d67160f34f39fb1d66a0e5~c5_720x720.jpeg?x-expires=1676847600&x-signature=S9DjoLgmMRBxScxDPe7IxSjPris%3D",
      "isEmbedBanned" : false,
      "profileEmbedPermission" : 1,
      "stitchSetting" : 0,
      "ftc" : false,
      "commerceUserInfo" : {
        "categoryButton" : false,
        "downLoadLink" : {
          "android" : "",
          "ios" : ""
        },
        "category" : "Media & Entertainment",
        "commerceUser" : true
      },
      "id" : "107955",
      "isADVirtual" : false,
      "openFavorite" : false,
      "profileTab" : {
        "showPlayListTab" : true,
        "showQuestionTab" : true
      },
      "verified" : true,
      "commentSetting" : 0,
      "uniqueId" : "tiktok",
      "ttSeller" : false
    }
  },
  "statusCode" : 0,
  "log_pb" : {
    "impr_id" : "20230217234902631E44DF37B2998AB222"
  },
  "status_code" : 0,
  "extra" : {
    "logid" : "20230217234902631E44DF37B2998AB222",
    "fatal_item_ids" : [

    ],
    "now" : 1676677743000
  },
  "shareMeta" : {
    "desc" : "@tiktok 67.0m Followers, 572 Following, 285.0m Likes - Watch awesome short videos created by TikTok",
    "title" : "TikTok on TikTok"
  }
}
```



