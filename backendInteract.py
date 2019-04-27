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
	content = [tmp.strip('\n\t') for tmp in content]
	return content

#print(getFileContent("languageKeywords.json"))

def addComment(file, comment, index):
	newContent = dc.comment(getFileContent(file), comment, index)
	f = open(file, 'w')
	newContent = "\n".join(newContent)
	if newContent != "machine broke error":
		f.write(newContent)

def getDefiners(lang):
	with open('languageKeywords.json', encoding='utf-8') as langInfo:
		data = json.loads(langInfo.read())

	definers = []

	for i in data[lang]:
		definers.append(("^" + i))
		print(i)
	return definers

def getClasses(definers):
	content = []
	for file in FILES:
		content = getFileContent(file)
		lines = []
		tmpDef = ["^class"]
		lines = dc.findFuncDec(content, tmpDef)

		linesDict = dict()
		for line in lines:
			print("Class Declared at line:", line)
			linesDict[line] = content[line]

		for key in linesDict:
			print(key, linesDict[key])

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

FILES.append("Test Code\doctumentorTest.py")
FILES.append("Test Code\doumentorTest2.py")
definers = getDefiners("Python")
if definers[0] != "def":
	definers = getClasses(definers)

content = []
for i in range(FILES.__len__()):
	content.append(getLines(FILES[i], definers))

comment = ["#test line 1 appear first", "#test line 2 appear second"]
#soon replace # in string with commentDef[LANG]
cont = []
for i in range(0, FILES.__len__()):
	cont.append(list(reversed(sorted(content[i].keys()))))
coms = []
i = 0
for f in FILES:
	for key in cont[i]:
		comment = input("comment for line " + str(content[i][key]) + " -> ")
		comment = "#" + comment
		coms.append(comment)
		addComment(f, coms, key)
		coms.clear()
	i += 1