# PyClip

PyClip wraps the `xclip` command-line program to provide an easy python 
interface to the X11 clipboard. To install the library, download the code
and run `sudo python setup.py install`. You can then use the library like so

	import clipboard

	# copy some text to the clipboard
	clipboard.copy('blah blah blah')

	# get the text currently held in the clipboard
	text = clipboard.paste()

	# helpful wrapper that passes pasted text through the csv module
	# useful for dealing with data copied from spreadsheets
	data = clipboard.paste_table()


