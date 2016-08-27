#!/usr/bin/env python
#coding: utf-8
import urwid
from time import sleep

palette = [
    ('streak', '', '', '', '#ffa', '#60a'),
    ('inside', '', '', '', 'g38', '#808'),
    ('outside', '', '', '', 'g27', '#a06'),
    ('bg', '', '', '', '#ffa', '#606'),
	('err', '', '', '', '#000', '#f00'),
	('suc', '', '', '', '#000', '#0f0')	]

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

class ConfessionBox(urwid.Filler):
    def keypress(self, size, key):
        if key == 'f12': 
            statusbar.base_widget.set_text([('err', u"db"),('suc', u"tw")])
        if key != 'enter':
            return super(ConfessionBox, self).keypress(size, key)
        text = self.original_widget.get_edit_text()
        self.original_widget = urwid.Edit(text +"\n")

placeholder = urwid.SolidFill()
loop = urwid.MainLoop(placeholder, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)

outside = urwid.AttrMap(urwid.Divider(), 'outside')
inside = urwid.AttrMap(urwid.Divider(), 'inside')
text = urwid.AttrMap(urwid.Text(u"\nHello World\n", align='center'), 'streak')
pile = urwid.Pile([])
for item in [outside, inside, text, inside, outside]:
    pile.contents.append((item, pile.options()))

edit = urwid.Edit(u"What?:\n")
bf = ConfessionBox(edit, valign='top')

statusbar = urwid.AttrMap(urwid.Text(u"Status bar"), 'bg')

frame = urwid.Frame(bf, pile, statusbar)

loop.widget = frame
loop.run()
