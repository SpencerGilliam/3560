#   Michael Cooper
#   document this when we come up with our style guide
#   for now cheaply but effectively documented

import Documenter as dc
import json

#figure out how json package works in python

#store file content in line array and insert comments using list.insert(index, obj)

fileContent = \
	["def Lorem ipsum dolor sit amet, consecteturdef adipiscing elit.",
	 "Integer luctus dictum leo defvitae gravida.",
	 "def Sed placerat turpis def eu odio fermentum maximus.",
	 "Sed eu facilisis def purus."]


dc.findFuncDec(fileContent, "def", 0)	#will return lines OF declaration, work BACKWARDS with these to avoid doing
										#extra unneeded math to get new line of each function after adding lines
