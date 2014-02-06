import extract_file
import os

from sys import argv

script, directory = argv

for file in os.listdir(directory):
	if file.endswith(".eml"):
		if not directory.endswith('/'):
			directory += '/'
		extract_file.main(directory + file)