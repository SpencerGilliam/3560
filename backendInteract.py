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
	LANGUAGE = lang

def setFiles(files):
	for f in files:
		FILES.append(f)

fileContent = \
	["def Lorem ipsum dolor sit amet, consecteturdef adipiscing elit.",
	 "Integer luctus dictum leo defvitae gravida.",
	 "int main",
	 "main int",
	 "def Sed placerat turpis def eu odio fermentum maximus.",
	 "Sed eu facilisis def purus."]



with open('languageKeywords.json', encoding='utf-8') as langInfo:
	data = json.loads(langInfo.read())



definers = []

for i in data[LANGUAGE]:
	definers.append(("^" + i))
	# to find all function declarations just look for function keywords at beginning of line following names and then parenthesis MAYBE

lines = dc.findFuncDec(fileContent, definers)	#will return lines OF declaration, work BACKWARDS with these to avoid doing
											#extra unneeded math to get new line of each function after adding lines
for line in lines:
	print("Function Declared at line:", line)