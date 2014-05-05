import os
import os.path

cpath = 'comics'

def get_latest_comic():
	comics = os.listdir(os.path.abspath(cpath))
	ilist = []
	for c in comics:
		ilist.append(int(c.split('.')[0]))
	ilist.sort()
	return str(ilist[len(ilist) - 1])