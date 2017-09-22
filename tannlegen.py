#!/usr/bin/env python
#coding: utf-8
import sys
import urwid
import random
import tweetorator
import slackorator
import os
import logging
import datetime
from time import sleep
from alphabet import *
from asciigriser import gris

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', filename='tannlegen.log', level=logging.DEBUG)

__version__ = "0.21" #Dan-Mikkel slang inn flere prompts.

header = "tannlegen"#Max 10 bokstaver!
slogan = "Norges frieste tannlegestol"

#Random bullshittery som kanskje dukker opp

n = random.randint(0,100)
if (n == 55):
    header = "sos"
    slogan = "Jeg er fanget i Tannlegestolen! Kontakt Stryret!"
if (n == 69):
    header = "Sexy"
    slogan = "Virru værra med meg hjem inatt?"
if (n == 0):
    slogan = "videreutvikles av Dan-Mikkel"
if (n == 1):
	header = "tt"
	slogan = "Tappetårnet er sexy!"
if (n == 2):
	header = "Storebror"
	slogan = "Politihøyskolen ser deg, ikke tiss utenfor!"


#Ting som MÅ dukke opp avhengig av tid

d = datetime.datetime.today();
if ((d.day == 23 or d.day == 25) and d.month == 2):
    header = "stiffi"
    slogan = "15 år med RESPEKT og MORO!"

c = map(lambda x: ord(x)-ord('a'),header.lower())
s = ""
for i in range(rows):
    for j in c:
            s+= alphabet[j][i]
    s+= "\n"

s+="\n                                                                      "
s+=slogan

asciiheader = s

#Legacy code

palette = [
    ('header', 'white', 'dark red'),
    ('inside', '', 'dark green'),
    ('outside', '', 'dark green'),
    ('statusbar', 'white', 'dark red'),
    ('err', 'black', 'dark red'),
    ('suc', 'black', 'dark green')]

def get_edit_box(prompt=None):
    prompts = [u"What's happening?",
               u"How are you feeling?",
               u"What's going on?",
               u"How are you doing?",
               u"How's it going?",
               u"Skriv navnet ditt her og vi melder deg inn i SOS Rasisme",
		u"Er du innover eller utover?",
		u"Why are you not dancing on the table?",
		u"GÅ DIN VEI!!!",
		u"What song makes you dance on the table?",
		u"Who are you in love with?",
		u"Remember to use condoms! Anyway, what's up?"]
    if not prompt:
        prompt = random.choice(prompts)
    prompt = prompt + ":\n"
    return urwid.Edit(prompt)

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

class ConfessionBox(urwid.Filler):
    def keypress(self, size, key):
        #"""
        if key == 'f12':
            statusbar.base_widget.set_text([('err', u"test err "),('suc', u"test suc")])
        #"""
        if key != 'enter':
            return super(ConfessionBox, self).keypress(size, key)
        text = self.original_widget.get_edit_text()
        tweetorator.post_confession(text)
        slackorator.post_confession(text)
        self.original_widget = get_edit_box()
	#TODO: Must find way to make header refresh. This is the best candidate to have such code!
	#statusbar.base_widget.set_text([('err', u"Something got refreshed!"),('suc', u"test suc") ])

outside = urwid.AttrMap(urwid.Divider(), 'outside')
inside = urwid.AttrMap(urwid.Divider(), 'inside')
text = urwid.AttrMap(urwid.Text(asciiheader, align='center'), 'header')
pile = urwid.Pile([])
for item in [outside, inside, text, inside, outside]:
    pile.contents.append((item, pile.options()))

edit = get_edit_box()
bf = ConfessionBox(edit, valign='top')

statusbar = urwid.AttrMap(urwid.Text(u"Status bar of epic failure"), 'statusbar')

frame = urwid.Frame(bf, pile, statusbar)

loop = urwid.MainLoop(frame, palette, unhandled_input=exit_on_q)
loop.widget = frame
try:
    loop.run()
except:
    logging.error("GREPTHISLINE: Random error in loop:%s" %sys.exc_info()[0])
