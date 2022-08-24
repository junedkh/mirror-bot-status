# Mirror bot status

## This repo is spacialy made for offical [MLTB](https://github.com/anasty17/mirror-leech-telegram-bot)

**_I am not good at editing README file_**

## Config env file

```bash
cp sample.env .env
```

## Required Field

- `BOT_TOKEN`: You guys know how to get it

## Optional Fields

- `STATUS_UPDATE_INTERVAL`: Message update intervel time
- `TIME_ZONE`: Timezone google it
- `HEADER_MSG`: A message for header side (you can use html)
- `FOOTER_MSG`: A message for footer side (you can use html)
- `CONFIG_JSON_URL`: To download the config.json it will orverwrite the existing one
- `CONFIG_ENV_URL`: To download the .env it will orverwrite the existing one

## Config.json [Json](https://www.w3schools.com/whatis/whatis_json.asp)

```bash
cp config-sample.json config.json
```

```json
{
  "bots": {
    "bot1": {
      "base_url_of_bot": "http://0.0.0.0",
      "host": "Heroku/Whatever",
      "bot_uname": "@botfather"
    },
    "bot2": {
      "base_url_of_bot": "http://0.0.0.0",
      "host": "Vps",
      "bot_uname": "@botfather"
    }
  },
  "channels": {
    "chat1": {
      "chat_id": "-100987654321",
      "message_id": "54321"
    },
    "chat2": {
      "chat_id": "-100123456789",
      "message_id": "12345"
    }
  }
}
```

### Required Fields bots

(**You can add upto 18 bots this will work slowly**)

- `bot1` : it could be anything but it should unique name ex: `bot1`, `bot2`
- `base_url_of_bot` : Read it from [here](https://github.com/anasty17/mirror-leech-telegram-bot#qbittorrent-1)
- `host`: it could be anything
- `bot_uname`: Bot username it will show on top of status

## You can add multiple bots in json

### Required Fields channels

- `chat1`: same as `bot1`
- `chat_id`: Channel id or you can try add channel username
- `message_id`: Message id which message you want update `https://t.me/JMDKH_Team/153` this `153` is message id

## If You Want Show This Status Message in Group

```bash
bash sendMsg.sh -100123456789 123456:abcdefg
```

This Script will send a message in group from the bot then you can get message id from it

## Add few require imports [Here](https://github.com/anasty17/mirror-leech-telegram-bot/blob/master/web/wserver.py#L2)

```python
from time import sleep, time
from psutil import boot_time, disk_usage, net_io_counters
from subprocess import check_output
from os import path as ospath
```

## Add This Code Above This [Line](https://github.com/anasty17/mirror-leech-telegram-bot/blob/master/web/wserver.py#L775)

```python
botStartTime = time()
if ospath.exists('.git'):
    commit_date = check_output(["git log -1 --date=format:'%y/%m/%d %H:%M' --pretty=format:'%cd'"], shell=True).decode()
else:
    commit_date = 'No UPSTREAM_REPO'

@app.route('/status', methods=['GET'])
def status():
    bot_uptime = time() - botStartTime
    uptime = time() - boot_time()
    sent = net_io_counters().bytes_sent
    recv = net_io_counters().bytes_recv
    return {
        'commit_date': commit_date,
        'uptime': uptime,
        'on_time': bot_uptime,
        'free_disk': disk_usage('.').free,
        'total_disk': disk_usage('.').total,
        'network': {
            'sent': sent,
            'recv': recv,
        },
    }
```

<p align="center"><a href="https://heroku.com/deploy?template=https://github.com/junedkh/mirror-bot-status"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a></p>

## Waiting for pr
