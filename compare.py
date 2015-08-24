import os, re, collections

class compare(object):
	'''
	Compares two folders of language files
	from the babylab and reports missing
	translations
	'''
	
	dirs = []
	files = collections.OrderedDict()
	entries = collections.OrderedDict()

	def __init__(self):
		'''
		checks which folders exists
		lists the files in those folders
		lists the items in those files
		initiates a compare script
		'''
		self.checkDirs()
		self.checkFiles()
		self.checkMissingFiles()
		self.readFiles()
		self.checkMissingEntries()
		
	def checkDirs(self):
		'''
		Lists the subdirectories of the
		current working directory
		'''
		for d in os.listdir('.'):
			if os.path.isdir(d):
				self.dirs += [d]

	def checkFiles(self):
		'''
		Lists the files in the subdirectories
		'''
		for d in self.dirs:
			self.files[d] = []
			for f in os.listdir(d):
				self.files[d] += [f]

	def checkMissingFiles(self):
		'''
		Prints a list of files
		that is in one directory,
		but not the other.
		'''
		for d1 in self.files.keys():
			for d2 in self.files.keys():
				for f in self.files[d1]:
					if not f in self.files[d2]:
						print "File %s exists in %s but not in %s" %(f, d1, d2)
		print
		print

	def readFiles(self):
		'''
		Reads all the entries in all the files and saves
		them in a dictionary of dictionaries
		'''
		for d in self.dirs:
			self.entries[d] = dict()
			for f in self.files[d]:
				self.entries[d][f] = dict()			
				stream = open(d + '/' + f)
				text = stream.read()
				stream.close()
				text = [re.split(r"\s=\s*|\s*=\s", l) for l in re.split('("|\');\s*\n', text)]
				for l in text:
					if len(l) == 2:
						self.entries[d][f][l[0]] = l[1]
					#else: print "\n%s\n%s\n%s\n%d" %(d, f, l, len(l)) #debug
	
	def checkMissingEntries(self):
		'''
		prints a list of entries that exist in one file but not in the other,
		split per file.
		'''
		for d in self.entries.keys():
			print "====Directory:", d.upper(), "====\n"
			for f in self.entries[d].keys():
				print "=== file:", f.upper(), "==="
				for d1 in self.entries.keys():		
					if not f in self.entries[d1]:
						print "File %s is in %s but not in %s" %(f, d, d1)
					else:		
						for entry in self.entries[d][f].keys():
							if not entry in self.entries[d1][f]:
								print "Entry %s with value %s is not in %s" %(entry, self.entries[d][f][entry], d1)
				print "\n"
			print "\n\n\n ======================================\n\n\n"
				
					
		
		
compare()


