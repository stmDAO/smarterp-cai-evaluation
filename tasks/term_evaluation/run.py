import os
import asyncio
import websockets
import uuid
import json
import sys
import base64
import random
import wave
import time
import pyaudio
import prettytable
from colorama import Fore, Back, Style


def exception_handler(x, exception):
	
	print(exception)


async def evaluate_glossary(wss, audio_file, results_file):
		
	
		
	print("Connecting to:", wss)
		
	async with websockets.connect(wss, ping_interval=None) as websocket:
		
		print("Performing evaluation")
		
		wavefile = wave.open(audio_file, 'r')
		
		'''p = pyaudio.PyAudio()
		
		stream = p.open(format = p.get_format_from_width(wavefile.getsampwidth()),  
						channels = wavefile.getnchannels(),  
						rate = wavefile.getframerate(),  frames_per_buffer=int(wavefile.getframerate()*0.4),
						output = True)  
		'''
				
		frames = wavefile.readframes(int(wavefile.getframerate()*0.2))
				
		t0 = time.time()
		
		results = []
				
		while len(frames) != 0:
		
			data = base64.encodebytes(frames)
			
			#print(len(data))
			
			msg = {"audio": data.decode("utf-8"), "info": []}
			
			#stream.write(frames)
			
			try:
						
				await asyncio.wait_for(websocket.send(json.dumps(msg)), timeout=0.1)
				
			except:
				
				pass
			
			#print("[",time.time()-t0,"] Chunk sent")
			
			try:
				
				resp = json.loads(await asyncio.wait_for(websocket.recv(), timeout=0.001))
				
				results.append({"time": time.time()-t0, "data": resp})
				
				print("Got", resp)
				
			except Exception as e:
								
				pass
				
			frames = wavefile.readframes(int(wavefile.getframerate()*0.2))
			
			await asyncio.sleep(0.2)

		results_file = open(results_file, "w+")
		
		results_file.write(json.dumps(results))
		
		results_file.close()



loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)




base_folder = "../.."



langs = [
#	"eng",
#	"spa",
#	"ita",
#	"fre",
	"ger"
	]

texts = {
	"eng": [
		"boring", 
		"concrete", 
		"fasting", 
		"occupational_therapy", 
		"patents"
	],
	"spa": [
		"boring", 
		"concrete", 
		"fasting",
		"occupational_therapy",
#		"patents"
	],
	"ita": [
		"boring", 
		"concrete",
		"fasting",
		"occupational_therapy",
#		"patents"
	],
	"fre": [
		"boring", 
		"concrete", 
		"fasting",
		"occupational_therapy",
		"patents"
	],
	"ger": [
#		"boring", 
#		"concrete", 
#		"fasting",
		"occupational_therapy",
		"patents"
	]
	}


for lang in langs:

	for text in texts[lang]:

		files = list(os.scandir(f"{base_folder}/{lang}/{text}/"))

		for filename in files:
			
			if filename.name.endswith(".wav") and "speaker" in filename.name:
				
				print("Evaluating language", lang, "text", text, "audio", filename.name)

				wss = f"wss://smarterp-cai.kunveno.digital/ws/benchmark/{lang}/{text}"
				
				audio_file = filename.path
				
				results_file = f"{audio_file}.eval.json"
				
				asyncio.run(evaluate_glossary(wss=wss, audio_file=audio_file, results_file=results_file))



