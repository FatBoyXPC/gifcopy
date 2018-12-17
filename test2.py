#!/usr/bin/env python2

# This is a mess and in Python 2 because the Python 3 gtk bindings don't
# support setting multiple selection targets. See
# https://gitlab.gnome.org/GNOME/gtk/issues/364 for more info.
# COPIED AND MODIFIED FROM
# https://github.com/makepost/acme-commander/blob/master/bin/clipboard.py

import gtk
import sys

targets = [("text/html",0,0), ("image/png",0,0)]

def get_func(clipboard, selection_data, info, data):
  if selection_data.get_target() == "text/html":
    text_html = '<meta http-equiv="content-type" content="text/html; charset=utf-8"><img src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Rotating_earth_(large).gif" alt="https://upload.wikimedia.org/wikipedia/commons/2/2c/Rotating_earth_(large).gif" class="transparent shrinkToFit" width="396" height="396">'
    selection_data.set(selection_data.get_target(), 8, text_html)
  else:
    img_png = open('/home/jeremy/tmp/gifcopy/image_png', 'rb').read()
    selection_data.set(selection_data.get_target(), 8, img_png)
    #<<< selection_data.set(selection_data.get_target(), 8, uris)

def clear_func(clipboard, data):
  gtk.main_quit()

clipboard = gtk.clipboard_get()
clipboard.set_with_data(targets, get_func, clear_func)
gtk.main()
