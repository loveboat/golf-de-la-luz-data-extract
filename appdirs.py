import app
import os

from sys import argv

script, directory = argv

for file in os.listdir(directory):
	if file.endswith(".eml"):
		app.main(file)