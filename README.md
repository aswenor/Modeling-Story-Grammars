# Modeling Story Grammars

This repository contains the data and prompts used for learning a novel approach for literary analysis through story grammar labeling. This data and its corresponding prompts were passed to gpt to teach the model through few-shot learning. The literary data in this repository is modified from both the [Tesserae Project](https://tesserae.caset.buffalo.edu/) and the [Perseus Digital Library](https://www.perseus.tufts.edu/hopper/). 

This repository also contains the small amount of software needed to process the labeled results produced from an LLM using our data and prompts. The files process the resulting data through simple enumeration of the used labels and through processing the subsequences of varying length that appear across the labeled text. 
