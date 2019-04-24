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

#call like bi.setLang
def setLang(lang):
    global LANGUAGE
    LANGUAGE = lang

#call like bi.setFiles(fileList)
def setFiles(files):
    for f in files:
        FILES.append(f)

#do NOT call this one
def getFileContent(file):
	content = ""
	with open(file) as f:
		content = f.readlines()
	content = [tmp.strip('\n') for tmp in content]
	return content

#print(getFileContent("languageKeywords.json"))

#call this in child window when user accepts their comment input like addComment(curFile, commentList, index)
						#get index arg from dict that is returned by getLines
def addComment(file, comment, index):
	newContent = dc.comment(getFileContent(file), comment, index)
	f = open(file, 'w')
	newContent = "\n".join(newContent)
	if newContent != "machine broke error":
		f.write(newContent)

#do NOT call this one
def getDefiners(lang):
	with open('languageKeywords.json', encoding='utf-8') as langInfo:
		data = json.loads(langInfo.read())

	definers = []

	for i in data[lang]:
		definers.append(("(^|\t| )" + i))
		print(i)
	return definers

#do NOT call this one
def getClasses(definers):
	content = []
	for file in FILES:
		content = getFileContent(file)
		lines = []
		lines = dc.findFuncDec(content, definers)

		linesDict = dict()
		for line in lines:
			print("Class Declared at line:", line)
			linesDict[line] = content[line]

		for key in linesDict:
			print(key, linesDict[key])

	return definers

#call from GUI in child window process while asking to comment
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
