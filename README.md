# Super mega comics mirror site thing

A mirror of the super comics website since its apparent death. This is something I made in literally an hour but it seems to work. It uses CGI Python so it's kinda slow but hey, it's something.

Comics are in `comics` subdir and are in the format `number.gif`.

`comic.py` is the page which loads the comics, and takes an `id` parameter which corresponds to the comic's filename, then loads it in an <img> element. `index.py` just loads the most recent comic.

`ui.py` loads the header and footer and takes care of the back/next buttons.

Tested with Python 2.7 on Apache on Linux.