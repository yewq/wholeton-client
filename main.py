#!/bin/python3

import urllib
from urllib import request
from http import cookies
import websocket
from datetime import datetime

host = '172.16.254.3'
user = 'test'
passwd = '123456@pku'
update_secs = 43200

uri_data = urllib.parse.urlencode({'id': '', \
                                   'url': '', \
                                   'user': '', \
                                   'mac': ''})
body_data = urllib.parse.urlencode({'param[UserName]': user, \
                                    'param[UserPswd]': passwd, \
                                    'uri': uri_data, \
                                    'force': 0})
cookie = cookies.SimpleCookie()

def main():
    try:
        while True:
            resp = request.urlopen('http://' + host + '/user-login-auth?' + uri_data, \
                                    data = body_data.encode('ascii'))
            cookie.load(resp.info()['Set-Cookie'])
            print(f"Login response: {resp.read()}")

            ws = websocket.WebSocket()
            ws.connect('ws://' + host + '/go-ws/user-auth', \
                        cookie = 'fms_session=' + cookie.get('fms_session').value, \
                        origin = 'http://' + host)
            dt_start = datetime.now()
            while ws:
                ws_data = ws.recv()
                dt_now = datetime.now()
                print(f"{dt_now} {ws_data}")
                if (dt_now - dt_start).seconds >= update_secs:
                    ws.close()
                    ws = None
    except KeyboardInterrupt:
        exit(1)

if __name__ == '__main__':
    main()
