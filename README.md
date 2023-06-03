# smarterp-cai-evaluation

This repository contains materials and code used to evaluate the SmarTerp-CAI tool and some of the results obtained in the process.

This evaluation is ongoing; *take any results cautiously as they are still provisional*, and more tests and revisions are needed. 


## Task description
### Language selection

The evaluation is currently being performed for the following languages:
- English
- Spanish
- Italian
- French
- German

Not all features are ready to be evaluated in all languages at this point in time; this evaluation will be updated as they become ready.

### Topic selection
We started evaluating the system, mimicking the typical workflow we can expect from conference interpreters. In the first place, the interpreter has to gather information related to the session topic, possibly the agenda with the names of the participants in the session and several documents about the contents that will be discussed in the interpreting session.

We chose the following topics trying to cover diverse situations where interpreters can benefit from the tool's assistance:
- Boring (Tunnel Boring Machines)
- Concrete
- Fasting (Therapeutical fasting)
- Occupational therapy
- Patents

### Glossary generation
Once the topics defined, we searched the Internet for documentation and created glossaries for each of them in all the evaluated languages. In total, we documented, generated and reviewed a total of 23 session glossaries (Patents has only been evaluated in ENG, FRA and DEU, the three official working languages of the European Patents Office. 

This part of the evaluation process was made by a professional interpreter using the SmarTerp-prep tool, as human expertise was crucial for establishing glossaries and documentation as a gold standard.

### Speech generation
To evaluate the system, we also needed a speech for each of our topics in all the evaluation languages. 

As writing the speeches ourselves could have biased the evaluation (we had already created the glossaries and searched for the documentation), we decided to use generative ML models to create the speeches. In particular, we used ChatGPT to generate the text documents referenced in the subsequent tasks. The ChatGPT prompt was fed with fragments of the documents, and also we asked to create content using some of the terms we included in the glossaries. 

We also asked to include numbers, dates and other Named Entities in the speeches generated, as we are trying to evaluate not only terms in the generated glossaries but also Named Entities.

### Audio synthesis
For the generated speeches, we tried different text-to-speech implementations to generate the voice utterances the system consumes when a session is being evaluated.

We tried to use models from the Coqui TTS framework, but there was only good support for English models; for other languages, the generation was too monotone, lacking multiple speakers or voice variations.

Then we found out about the Bark model, which is a mix between existing TTS models and generative (GPT like) models. We decided that this generation tool was better to try to evaluate the system, as we can cover a lot of different accents, prosodies and even ambient noise. 

We generated 20 audio samples for each session on each language, for a total of about 60 hours of audio. We tried to make each audio fragment as heterogeneous as possible, mixing different speakers at the sentence level.

### Evaluation execution
Our system generates a language model with the documentation provided by the interpreter with the objective of tailoring an ASR component to the particular corpus of an interpreting session. This task was performed for each of the 23 glossaries created.

In our system, each session is handled by a worker that runs the ASR system in tandem with some NLP components that search for matches of terms included in the glossary, and named entities (including numeric entities). For the performing of the evaluation, there workers were launched as needed and kept up and running the necessary time.

With the current code that orchestrates the audio submission and result gathering, the benchmark execution is performed sequentially. This limitation is a bottleneck that limits the size of the corpora for the benchmark, and parallelization is an ongoing task. The system consumes audio in real-time, so the evaluation of corpora of ~60 hours of audio takes the same amount of time.

## Experimental setup
### Environment
For the server side, the regular SmarTerp-CAI infrastructure was used. A specially crafted tool for sending audio was developed for the client side, as the technician console that sends audio streams is powered by WebRTC technology running in the browser.

### Software used
- Spacy for NER annotation
- Coqui TTS for regular speech synthesis
- Bark generative model for audio synthesis
- ChatGPT for text generation

## Evaluation

# Delay evaluation

# Terms evaluation
The typical approach to measuring the precision of an Automatic Speech Recognition system (and also for the opposite task, Text-to-Speech) is to calculate the WER (word error rate) metric. This metric is similar to the Levenshtein distance but takes words into account, not characters or phonemes.

Although the WER metric is an excellent way to measure a ASR component, our system works as a whole, and the ASR component is just the first step in a longer process. On the other hand, the WER metric treats all the words on an equal footing, and in our system not all the words have the same relevance. 

Our system tries to provide assistance with a subset of the words that the ASR component needs to be able to recognise, but the fact that other words that are not important for the interpreter are not recognised is not relevant. 

The critical question here is not what the general WER result is, but which words are the ones that need to be accurately recognised, taking into account that we can define the words that are probably going to be useful for interpreters. 

With that in mind, we modelled the evaluation as a simple binary classification: glossary terms and other words. The following metrics were then calculated: 
- Precision
- Recall
- F1 score


# Named entities evaluation
[TODO]

# Numbers evaluation
[TODO]

## Comparison
[pending]

## Final notes
[pending]
