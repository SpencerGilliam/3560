#   Michael Cooper
#   document this when we come up with our style guide
#   for now cheaply but effectively documented

import Documenter as dc
import json

#figure out how json package works in python

#store file content in line array and insert comments using list.insert(index, obj)

#LANGUAGE will be set by the frontend
LANGUAGE = "Python"		#default Python

FILES = []

def setLang(lang):
    global LANGUAGE
    LANGUAGE = lang

def setFiles(files):
    for f in files:
        FILES.append(f)

def getFileContent(file):
	content = ""
	with open(file) as f:
		content = f.readlines()
	content = [tmp.strip('\n') for tmp in content]
	return content

#print(getFileContent("languageKeywords.json"))

def addComment(file, comment, index):
    dc.comment(getFileContent(file), comment, index)

def getDefiners():
	with open('languageKeywords.json', encoding='utf-8') as langInfo:
		data = json.loads(langInfo.read())

	definers = []

	for i in data[LANGUAGE]:
		definers.append(("^" + i))
	return definers

	# to find all function declarations just look for function keywords at beginning of line following names and then parenthesis MAYBE
def getLines(file, definers):
	fileContent = getFileContent(file)
	lines = dc.findFuncDec(fileContent, definers)	#will return lines OF declaration, work BACKWARDS with these to avoid doing

	linesDict = dict()
	for line in lines:
		print("Function Declared at line:", line)
		linesDict[line] = fileContent[line]

	for key in linesDict:
		print(key, linesDict[key])
	return linesDict   #returns dictionary of lines indexed by number so GUI can

def getCustomDataTypes(files, definers):
	pass	#for each file in files, open, read, look for class/struct declarations. return new definers list

getLines("languageKeywords.json", "\"")