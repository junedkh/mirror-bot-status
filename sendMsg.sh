#!/bin/bash
if [ "$1" == "-h" ]; then
    echo "Usage: $(basename $0) <group_id> <bot_token>"
    exit 0
fi

if [ -z "$1" ]; then
    echo "No group_id provided"
    exit 0
fi

if [ -z "$2" ]; then
    echo "No bot_token provided"
    exit 0
fi

curl -s --data "text=Hi This Message from mirror bot status <a href='https://github.com/junedkh/mirror_bot-status'>Repo</a>" \
    --data "chat_id=$1" --data "disable_web_page_preview=true" --data "parse_mode=html" \
    'https://api.telegram.org/bot'$2'/sendMessage' >/dev/null
