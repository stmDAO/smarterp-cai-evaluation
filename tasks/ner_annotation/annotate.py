import spacy

import os
import random
import json


langs = [
	"eng",
	"spa",
	"ita",
	"fre",
	"ger"
	]
	
models = {
	"eng": "en_core_web_trf",
	"spa": "es_core_news_lg",
	"ita": "it_core_news_lg",
	"fre": "fr_core_news_lg",
	"ger": "de_core_news_lg"
	}

texts = [
	"occupational_therapy",
	"boring",
	"concrete",
	"fasting",
	"patents",
	]

for lang in langs:

	for textname in texts:

	
		print("Annotating", lang, textname)

		script = [ f"{x.strip()}." for x in open(f"./{lang}/{textname}/text.txt").read().replace("\n", " ").strip().split(".") ][:-1]
		

		pipe = spacy.load(models[lang])

		result = []

		for line in script:
			
			tokens = {}

			words = line.split(" ")
			
			doc = pipe(line)
			
			#print(words[2:])
			
				
			for token in doc.ents:
				
				#line = line.replace(str(token.text), "["+token.text+"; "+token.label_+"]")
					
				#print("Found NE: ", token.text, token.label_)
				
				tokens[token.text] =  token.label_
				

			#print(line)
			#print(tokens)
			
			result.append({"text": line, "tokens": [tokens]})
			
			
		output = json.dumps(result, indent=4)
		
		annotated_file = open(f'./{lang}/{textname}/text-annotated.json', "w+")
		
		annotated_file.write(output)
		
		annotated_file.close()
