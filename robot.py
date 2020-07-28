import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
import json
webhook = 'webhook地址'
timestamp = str(round(time.time() * 1000))
secret = '密钥'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
baseUrl = webhook+'&timestamp='+timestamp+"&sign="+sign

HEADERS = {
    "Content-Type": "application/json ;charset=utf-8 "
}
message=input("你要发送的消息：")
stringBody ={
    "msgtype": "text",
    "text": {"content": message},
    "at": {
        "atMobiles": ["1825718XXXX"],
            "isAtAll": False

     }
}
MessageBody = json.dumps(stringBody)
result = requests.post(url=baseUrl, data=MessageBody, headers=HEADERS)
print(result.text)
