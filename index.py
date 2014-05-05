#!/usr/local/bin/python

import ui
import comic_helper

ui.headers()
ui.show_header()

ui.show_comic(comic_helper.get_latest_comic(), comic_helper.get_latest_comic())

ui.show_footer()