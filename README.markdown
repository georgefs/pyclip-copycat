# PyClip

PyClip wraps the `xclip` command-line program on Linux and the `pbcopy` and 
`pbpaste` programs on Mac OS X to provide an easy python interface to the 
system clipboard. To install the library, download the code and run 
`sudo python setup.py install`. You can then use the library like so

	import clipboard

	# copy some text to the clipboard
	clipboard.copy('blah blah blah')

	# get the text currently held in the clipboard
	text = clipboard.paste()

	# helpful wrapper that passes pasted text through the csv module
	# useful for dealing with data copied from spreadsheets
	data = clipboard.paste_table()

Note: I don't actually have a Mac to test things on, so if you are using Mac
OS X and you find that the code is not working, please patch it and send a 
pull request.

PyClip is release under an MIT license, reproduced in LICENSE.
