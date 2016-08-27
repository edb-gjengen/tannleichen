#!/usr/bin/env python
#coding: utf-8
import sys
import twitter
import logging
import tldb
import re

"""
THE NINJA IS STRONG WITH THIS ONE
TODO: FIX EVERYTHING
"""

__version__ = "0.1"

_api = None
initialized = False

def init():
    global _api

# TWITTER IS FUCKED. paalbra 2016-06-08
#    cfg = ConfigParser.RawConfigParser()
#    cfg.read("tweetorator.cfg")
#    consumer_key = cfg.get("twitter", "consumer_key")
#    consumer_secret = cfg.get("twitter", "consumer_secret")
#    access_token_key = cfg.get("twitter", "access_token_key")
#    access_token_secret = cfg.get("twitter", "access_token_secret")
#    _api = twitter.Api(consumer_key = consumer_key,
#                      consumer_secret = consumer_secret,
#                      access_token_key = access_token_key,
#                      access_token_secret = access_token_secret)
#
#    logging.debug("VerifyCredentials: %s" % _api.VerifyCredentials())

    tldb.loadCfg('tldb.cfg')

def post_confession(text):
    global _api

    # Return if text only contains whitespace
    if re.search(r'\S', text) is None:
        logging.info("Confession only containing whitespace. Abort")
        return

    if not initialized:
        init()

## UNFUCK START
    logging.info("Adding unfucked confession")
    try:
        tldb.addConfession(text)
    except:
        logging.error("%s, 0, text was >>%s<<" % (sys.exc_info()[0], text))
        pass
## UNFUCK END

# THIS IS FUCKED BEFAUSE TWITTER IS FUCKED. paalbra 2016-06-08
#    if len(text) > 140:
#        logging.info("Adding confession longer than 140")
#        try:
#            tldb.addConfession(text)
#        except:
#            logging.error("%s, 1, text was >>%s<<" % (sys.exc_info()[0], text))
#            pass
#    else:
#        logging.info("Adding confession shorter than 140")
#        try:
#            status = _api.PostUpdate(text)
#            tldb.addConfession(text, status.AsJsonString())
#        except:
#            logging.error("%s, 2, text was >>%s<<" % (sys.exc_info()[0], text))
#            pass
