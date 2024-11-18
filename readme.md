[TOC]

惠尔顿上网认证系统客户端

- 根据需求自行修改 `main.py` 中的 `host`, `user`, `passwd`

```shell
$ git clone https://github.com/yewq/wholeton-client.git
$ cd wholeton-client
$ sudo python3 -m venv /opt/wholeton-client
$ sudo /opt/wholeton-client/bin/python -m pip install websocket-client
$ sudo cp main.py /opt/wholeton-client/
$ sudo cp wholeton-client.service /etc/systemd/system/wholeton-client.service
$ sudo systemctl daemon-reload
$ sudo systemctl enable wholeton-client.service
$ sudo systemctl start wholeton-client.service
```
