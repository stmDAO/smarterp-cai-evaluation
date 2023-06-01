# smarterp-cai-evaluation

This repository contains materials and code used to evaluate the SmarTerp CAI system and some of the results obtained in the process.

This evaluation is ongoing; take any results cautiously as they are still provisional, and more tests and revisions are needed. 


## Task description
### Language selection
The evaluation is currently being performed for the following languages:
English
Spanish
Italian
French
German
Not all characteristics are ready to be evaluated in all languages at this point in time; this benchmark will be updated as they become ready.

### Topic selection
We started evaluating the system, mimicking the typical workflow we can expect from real users. The initial situation is that the interpreter has the information related to the session topic, maybe participants in the session and probably materials about the contents that can be discussed.

We choose the following topics trying to cover diverse situations where interpreters can benefit from the system's assistance:
Boring
Concrete
Fasting
Occupational therapy
Patents


### Glossary generation
With these topics defined, we gathered documentation about them and created glossaries for each in all the evaluated languages. In total, we documented, generated and finetuned a total of 23 session glossaries. 

This part of the benchmarking process was made "by hand" using the SmarTerp Prep tools, as human expertise was crucial for establishing glossaries and documentation as a gold standard.

### Discourse generation
To evaluate the system, we also needed a speech for each of the topics mentioned, and we needed this in all the languages we wished to consider. 

One possibility was to write the speeches ourselves, but doing it that way could bias the evaluation as we had already created the glossaries and searched for the documentation.

We decided to use generative ML models to create the speeches. In particular, we used ChatGPT to generate the text documents referenced in the posterior tasks. The ChatGPT prompt was fed with fragments of the documents, and also we asked to create content using some of the terms we included in the glossaries. 

We also asked to include numbers, dates and other Named Entities in the speeches generated, as we're trying to evaluate not only terms in the generated glossaries but also other elements.

### Audio synthesis
With the speeches generated, we tried different text-to-speech implementations to generate the voice utterances the system consumes when a session is being evaluated.

We tried to use models from the Coqui TTS framework, but there was only good support for English models; for other languages, the generation was too monotone, lacking multiple speakers or voice variations.

Then we found out about the Bark model, which is a mix between existing TTS models and generative (GPT like) models. We decided that this generation tool was better to try to benchmark the system, as we can cover a lot of different accents, prosodies and even ambient noises. 

We generated 20 audio samples for each session on each language, for a total of about 60h of audio. We tried to make each audio piece as heterogeneous as possible, mixing different speakers at the sentence level.

### Evaluation execution


## Dataset
### Materials
### Key aspects

## Experimental setup
### Environment
### Tools

## Evaluation


## Comparison

## Final notes
