#   Michael Cooper
#   document this when we come up with our style guide
#   for now cheaply but effectively documented

import re

#langdef: function def for language; ind: line to search from
def findFuncDec(fileContent, langDef, lineInd):
	#loop this, return all match lines; let back/front interaction do quick maths to get line before.
	ind = re.search(langDef, fileContent[0])
	if ind != None:
		print(ind.span())
	else:
		print("No match")