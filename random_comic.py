#!/usr/local/bin/python

import comic_helper
import random

lc = int(comic_helper.get_latest_comic())
cid = 'comic.py?id=' + str(random.randrange(1, lc))

print 'Location: ' + cid
print