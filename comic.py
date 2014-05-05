#!/usr/local/bin/python

import ui
import comic_helper
import cgi

form = cgi.FieldStorage()

ui.headers()
ui.show_header()

if "id" not in form:
	print '<h2>Oops! You need to put a comic ID in...</h2>'
else:
	cid = form["id"].value
	ui.show_comic(cid, comic_helper.get_latest_comic())

ui.show_footer()