#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

# https://python-gtk-3-tutorial.readthedocs.io/en/latest/clipboard.html?highlight=clipboard
clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
# urgggg https://gitlab.gnome.org/GNOME/gtk/issues/364
clipboard.set_with_data

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
