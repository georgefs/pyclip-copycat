# PyClip fork from https://github.com/zhemao/pyclip

PyClip wraps the `xclip` command-line program on Linux and the `pbcopy` and 
`pbpaste` programs on Mac OS X and the `clip` and `paste` on Windows to provide an easy python interface to the 
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

Note: If you are using this on Linux, make sure you have the xclip 
program installed.

PyClip is release under an MIT license, reproduced in LICENSE.
