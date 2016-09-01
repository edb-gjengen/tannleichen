#!/usr/bin/env python
#coding: utf-8
import sys
import urwid
import random
import tweetorator
import slackorator
import os
import logging
from time import sleep

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', filename='tannlegen.log', level=logging.DEBUG)

__version__ = "0.2"

asciiheader = """   ___           ___           ___           ___           ___       ___           ___           ___           ___     \n  /\  \         /\  \         /\__\         /\__\         /\__\     /\  \         /\  \         /\  \         /\__\    \n  \:\  \       /::\  \       /::|  |       /::|  |       /:/  /    /::\  \       /::\  \       /::\  \       /::|  |   \n   \:\  \     /:/\:\  \     /:|:|  |      /:|:|  |      /:/  /    /:/\:\  \     /:/\:\  \     /:/\:\  \     /:|:|  |   \n   /::\  \   /::\~\:\  \   /:/|:|  |__   /:/|:|  |__   /:/  /    /::\~\:\  \   /:/  \:\  \   /::\~\:\  \   /:/|:|  |__ \n  /:/\:\__\ /:/\:\ \:\__\ /:/ |:| /\__\ /:/ |:| /\__\ /:/__/    /:/\:\ \:\__\ /:/__/_\:\__\ /:/\:\ \:\__\ /:/ |:| /\__\\\n /:/  \/__/ \/__\:\/:/  / \/__|:|/:/  / \/__|:|/:/  / \:\  \    \:\~\:\ \/__/ \:\  /\ \/__/ \:\~\:\ \/__/ \/__|:|/:/  /\n/:/  /           \::/  /      |:/:/  /      |:/:/  /   \:\  \    \:\ \:\__\    \:\ \:\__\    \:\ \:\__\       |:/:/  / \n\/__/            /:/  /       |::/  /       |::/  /     \:\  \    \:\ \/__/     \:\/:/  /     \:\ \/__/       |::/  /  \n                /:/  /        /:/  /        /:/  /       \:\__\    \:\__\        \::/  /       \:\__\         /:/  /   \n                \/__/         \/__/         \/__/         \/__/     \/__/         \/__/         \/__/         \/__/    \n                                                                                              Landets frieste tannlegestol"""

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
               u"How's it going?"]
    if not prompt:
        prompt = random.choice(prompts)
    prompt = prompt + ":\n"
    return urwid.Edit(prompt)

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

class ConfessionBox(urwid.Filler):
    def keypress(self, size, key):
        """
        if key == 'f12': 
            statusbar.base_widget.set_text([('err', u"test err"),('suc', u"test suc")])
        """
        if key != 'enter':
            return super(ConfessionBox, self).keypress(size, key)
        text = self.original_widget.get_edit_text()
        tweetorator.post_confession(text)
        #slackorator.post_confession(text)
        self.original_widget = get_edit_box()

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