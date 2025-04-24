#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7580026996:AAGA6SYg9Zl6NMSnwbYxSAtKMTtEfCTSXz0")
    API_ID = int(os.environ.get("API_ID", "22528446"))
    API_HASH = os.environ.get("API_HASH", "0d81bf18019c5f3839037d0ae737c358")
    AUTH_USERS = os.environ.get("AUTH_USERS", "633111330")
