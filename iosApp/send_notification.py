import json
import jwt
import time
import sys
import codecs
from hyper import HTTPConnection

ALGORITHM = 'ES256'
APNS_KEY_ID = 'NGV4VHPBAX'
TEAM_ID = '9L9TN8HWYW'
BUNDLE_ID = 'com.iragsdale.KotlinConf'

APNS_AUTH_KEY = sys.argv[1]

f = open(APNS_AUTH_KEY)
secret = f.read()

token = jwt.encode(
    {
        'iss': TEAM_ID,
        'iat': time.time()
    },
    secret,
    algorithm= ALGORITHM,
    headers={
        'alg': ALGORITHM,
        'kid': APNS_KEY_ID,
    }
)

device_token = sys.argv[2]
REGISTRATION_ID = codecs.encode(codecs.decode(device_token.encode(), 'base64'), 'hex').decode()

path = '/3/device/{0}'.format(REGISTRATION_ID)

request_headers = {
    'apns-expiration': '0',
    'apns-priority': '10',
    'apns-topic': BUNDLE_ID,
    'authorization': 'bearer {0}'.format(token.decode('ascii'))
}
payload_data = { 
    'aps': { 'badge': int(sys.argv[3]), 'alert' : sys.argv[4] }
}
payload = json.dumps(payload_data).encode('utf-8')

conn = HTTPConnection('api.development.push.apple.com:443')

conn.request(
    'POST', 
    path, 
    payload, 
    headers=request_headers
)

resp = conn.get_response()
print(resp.status)
print(resp.read())
