def headers():
	print 'Content-Type: text/html'
	print

def show_header():
	print '''
	<!doctype html>
	<html>
		<head>
			<meta charset="utf-8">
			<title>super mega comics mirror!</title>
			<style>
				body{
					width: 940px;
					font-family: arial, sans-serif;
					margin: 0 auto;
				}

				.subtext{
					font-style: italic;
				}

				.ct{
					text-align: center;
				}
			</style>
		</head>
		<body>
			<h1>joe's super mega comics mirror!! not the official site!!</h1>
			<p class="subtext">At the moment, the Super Mega Comics website is down. This site has some of the comics on it, and it will only be
			up until the main site is up.</p>
			<hr>
	'''

def show_comic(id, max):
	html = ''

	id = int(id)
	max = int(max)

	prev = id - 1
	next = id + 1

	if id > 1:
		html += '<a href="comic.py?id=' + str(prev) + '">Previous comic</a> |'

	html += ' <a href="random_comic.py">Random comic</a> '

	if id < max:
		html += '| <a href="comic.py?id=' + str(next) + '">Next comic</a>'

	html += '<hr>'
	html += '<h2 class="ct">#' + str(id) + '</h2>'
	html += '<img src="comics/' + str(id) + '.gif">'

	print html

def show_footer():
	print '''
		</body>
	</html>
	'''