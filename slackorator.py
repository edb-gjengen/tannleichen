#!/usr/bin/env python
#coding: utf-8
import ConfigParser
import json
import logging
import re
import requests
import sys

"""
hello this is documentation
"""

__version__ = "0.1"

template = {
    'channel': '#tannlegen',
    'username': 'Tannlegen',
    'icon_emoji': ':beers:'
}

configname = "slackorator.cfg"
cfg = ConfigParser.RawConfigParser()
cfg.read(configname)

headers = {'content-type': 'application/json'}
hook = cfg.get("stuff", "hook")

def post_confession(text):
    # Return if text only contains whitespace
    if re.search(r'\S', text) is None:
        logging.info("Confession only containing whitespace. Abort")
        return

    logging.info("Attempting to post confession to slack")
    try:
        r = requests.post(hook,
                          data=json.dumps(dict({'text': text}, **template)),
                          headers=headers)
        r.raise_for_status()
    except Exception, e:
        logging.error("Failed to post confession to slack")
        logging.exception(e)
        pass
