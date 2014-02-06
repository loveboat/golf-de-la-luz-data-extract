import fileinput

processing = False
key = ''
data = {}

#for line in fileinput.input("example.txt"):
for line in fileinput.input("noname.eml"):

	text = line.strip(' \r\n') # strip space & new line chars
	
	if 'validate_name:' in text:
		processing = True 

	if not processing:
		continue

	# add break when we get to "Visitor tracking information:"
	if "Visitor tracking information:" in text:
		print "BAIL!!"
		break

	print text

	if text.endswith(':'):
		key = text # == "validate_name:":
		
		#print "key", key

		data[key] = ''
	else: # key != '':
		print "what?", text
		data[key] += text




print data

