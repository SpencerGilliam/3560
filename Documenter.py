#   Michael Cooper
#   document this when we come up with our style guide
#   for now cheaply but effectively documented

import re

#langdef: function def for language; ind: line to search from
def findFuncDec(fileContent, langDefs):
	#loop this, return all match lines; let back/front interaction do quick maths to get line before.

	arrInds = []	#empty list

	for langDef in langDefs:
		curLine = 0
		for line in fileContent:
			ind = re.search(langDef, line)
			if ind is not None:
				arrInds.append(curLine)
			curLine += 1


	return arrInds

def comment(filecontent, comment, index):	#comment will be array of lines to comment
	comment.reverse()			#reverse comment to place comment in proper order
	for line in comment:
		filecontent.insert(index, line)
	return filecontent		#return new version of filecontent