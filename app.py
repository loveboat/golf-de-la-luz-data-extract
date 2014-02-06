import fileinput
from sys import argv

script, filename = argv

# some vars to hold everything in place
processing = False
key = ''
files = []
data = {}


#for line in fileinput.input("example.txt"):
for line in fileinput.input(filename):

	text = line.strip(' \r\n') # strip space & new line chars
	
	if 'validate_name:' in text:
		processing = True 

	if not processing:
		continue

	# add break when we get to "Visitor tracking information:"
	if "Visitor tracking information:" in text:
		#print "BAIL!!"
		break

	#print text

	# pick out each key and cache data against it (until the next key)
	if text.endswith(':'):
		key = text
		data[key] = ''
	else: # key != '':
		data[key] += text

#print data
files.append(data)

for item in files:
	print "%s,%s,%s,%s,%s" % (item['validate_name:'],
							item['tel:'],
							item['validate_email:'],
							item['how_hear:'],
							item['other_detail:'])
