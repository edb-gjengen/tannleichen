#!/usr/bin/evn python
#coding: utf-8
import MySQLdb
import json
import time
import ConfigParser
import locale
import logging
from datetime import datetime
from dateutil import tz

__version__ = "1.3"

_con = None
_cfg = None

def loadCfg(configname):
    global _cfg
    _cfg = ConfigParser.RawConfigParser()
    _cfg.read(configname)

def connect():
    global _con
    try:
        _con = MySQLdb.connect(host=_cfg.get('DB', 'host'), user=_cfg.get('DB', 'username'),
                               db=_cfg.get('DB', 'dbname'), passwd=_cfg.get('DB', 'password'), connect_timeout=5)
    except MySQLdb.OperationalError:
        logging.error('Could not connect to database')

def disconnect():
    if _con.open:
        _con.close()
    else:
        logging.warn('Tried do disconnect from closed database connection')

def addConfession(text, tweet=None):
    connect()
    cur = _con.cursor()
    res = 0L
    try:
        if tweet:
            created_at = _twitterUTCToLocal(json.loads(tweet)['created_at'])
            tweet_id_str = str(json.loads(tweet)['id'])
            sql = u'INSERT INTO confession (text, created_at, tweet_id_str) VALUES (%s, %s, %s)'
            res = cur.execute(sql, (text, created_at, tweet_id_str))
            insertid = cur.lastrowid
        else:
            sql = u'INSERT INTO confession (text) VALUES (%s)'
            res = cur.execute(sql, (text,))
            insertid = cur.lastrowid
    except MySQLdb.Error as e:
        logging.error(e)
        pass

    if not res:
        logging.warn('Result was empty')
    else:
        logging.debug('Inserted new confession with id: %s', insertid)
    
    cur.close()
    disconnect()
    return res

def _twitterUTCToUTC(twittertime):
    twitterutc = u'%a %b %d %H:%M:%S +0000 %Y'
    utc = u'%Y-%m-%d %H:%M:%S'

    #curloc = locale.getlocale()
    #locale.setlocale(locale.LC_ALL, ('en_US', 'UTF8'))
    newtime = time.strftime(utc, time.strptime(twittertime, twitterutc))
    #locale.setlocale(locale.LC_ALL, curloc)

    return newtime

def _twitterUTCToLocal(twittertime):
    twitterutcformat = u'%a %b %d %H:%M:%S +0000 %Y'
    datetimeformat = u'%Y-%m-%d %H:%M:%S'

    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    utc = datetime.strptime(twittertime, twitterutcformat).replace(tzinfo=from_zone)
    #utc = utc.replace(tzinfo=from_zone)

    localtime = utc.astimezone(to_zone)

    return localtime.strftime('%Y-%m-%d %H:%M:%S')
