import os
import random

import requests
import nltk

import numpy as np

from bark import SAMPLE_RATE
from bark.generation import (
    generate_text_semantic,
    preload_models,
)

from bark.api import semantic_to_waveform
from scipy.io.wavfile import write as write_wav

# download and load all models
preload_models()


langs = [
#	"eng",
	"spa",
#	"ita",
#	"fre",
#	"ger"
	]

texts = [
	"occupational_therapy",
	"boring",
	"concrete",
	"fasting",
#	"patents",
	]

#speakers = ['p225', 'p226', 'p227', 'p228', 'p229', 'p230', 'p231', 'p232', 'p233', 'p234', 'p236', 'p237', 'p238', 'p239', 'p240', 'p241', 'p243', 'p244', 'p245', 'p246', 'p247', 'p248', 'p249', 'p250', 'p251', 'p252', 'p253', 'p254', 'p255', 'p256', 'p257', 'p258', 'p259', 'p260', 'p261', 'p262', 'p263', 'p264', 'p265', 'p266', 'p267', 'p268', 'p269', 'p270', 'p271', 'p272', 'p273', 'p274', 'p275', 'p276', 'p277', 'p278', 'p279', 'p280', 'p281', 'p282', 'p283', 'p284', 'p285', 'p286', 'p287', 'p288', 'p292', 'p293', 'p294', 'p295', 'p297', 'p298', 'p299', 'p300', 'p301', 'p302', 'p303', 'p304', 'p305', 'p306', 'p307', 'p308', 'p310', 'p311', 'p312', 'p313', 'p314', 'p316', 'p317', 'p318', 'p323', 'p326', 'p329', 'p330', 'p333', 'p334', 'p335', 'p336', 'p339', 'p340', 'p341', 'p343', 'p345', 'p347', 'p351', 'p360', 'p361', 'p362', 'p363', 'p364', 'p374', 'p376']

#speakers = ['p225', 'p226', 'p227', 'p228', 'p229', 'p230', 'p231', 'p232', 'p233', 'p234']

speakers = ["es_speaker_0", "es_speaker_1", "es_speaker_3", "es_speaker_4", "es_speaker_5", "es_speaker_6", "es_speaker_7", "es_speaker_8", "es_speaker_9"]

for lang in langs:

	for textname in texts:

		for speaker in speakers:
			
			print("Generating", lang, textname, speaker)

			script = open(f"./{lang}/{textname}/text.txt").read().replace("\n", " ").strip()
			
			pieces = []
			
			sentences = nltk.sent_tokenize(script)
			
			for sentence in sentences:
				
				semantic_tokens = generate_text_semantic(
					sentence,
					history_prompt=f"v2/{speaker}",
					temp=0.6,
					min_eos_p=0.05,  # this controls how likely the generation is to end
				)

				audio_array = semantic_to_waveform(semantic_tokens, history_prompt=f"v2/{speaker}")
				
				pieces += [audio_array, np.zeros(int((random.random()*2) * SAMPLE_RATE))]
				
			
			audio_array = np.concatenate(pieces)


			write_wav(f'./{lang}/{textname}/audio-{speaker}.wav', SAMPLE_RATE, audio_array)
			

			os.system(f"ffmpeg -i './{lang}/{textname}/audio-{speaker}.wav' -acodec pcm_s16le -ac 1 -ar 16000 './{lang}/{textname}/audio-{speaker}.16k.wav'")
			
			os.system(f"rm './{lang}/{textname}/audio-{speaker}.wav'")


