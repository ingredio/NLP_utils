# Phase3
Here, we present the python code that has to do with NLP tasks related to biomedical text.
## Task 1: Causality Inference
* Given a corpus of texts, that consists of abstracts and titles from papers and has to do with chemical compounds that are related to food and cosmetics industry, determine if the compound has a positive or negative relation to several adverse effects(cancer, neurotoxicity etc).
 
## Task 2: Named Entity Recognition
* Given a corpus of texts, that consists of abstracts and titles and are related to food and cosmetics extract names of compounds that are not listed in our in-house dataset.

## Installation
### Conda environment
` curl -sL \
  "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh" > \
  "Miniconda3.sh" `
  * Restart your Terminal. Now your prompt should list which environment is active (in this case “base”, i.e. the default).
  * Update Conda using the command:
    `conda update conda`
  * After installation, delete the installer:
    `rm Miniconda3.sh`
  * Install the program “wget” using Conda to download any files using CLI:
    `conda install wget`
  *  Create a conda environment named Phase3 and install python v3.6.9
    `conda create -n Phase3 python=3.6.9`
  * Activate conda environment
    `conda activate Phase3`
  * Clone github repo:  
    `git clone https://github.com/ingredio/Phase3`  
    `cd Phase3`
  * Install dependencies:
    `pip3 install -r requirements.txt`

###  Python Requirements
* nltk==3.5
* pandas==1.1.3
* numpy==1.18.5
* python_Levenshtein==0.12.0
* torch==1.7.0
* transformers==3.5.1
* tqdm==4.53.0
* scikit_learn==0.24.0
## Datasets    

Phase3
├── causality_inference
│   ├── dataset
│   ├── input
│   │   └── bert_base_uncased
│   │       ├── config.json
│   │       ├── pytorch_model.bin
│   │       └── vocab.txt
│   └── src
│       ├── config.py
│       ├── dataset.py
│       ├── engine.py
│       ├── model.py
│       ├── predict.py
│       └── train.py
├── entity_extraction
│   ├── datasets
│   └── src
│       ├── config.py
│       ├── dataset.py
│       ├── find_compounds.py
│       ├── model.py
│       ├── predict.py
│       └── train.py
├── README.md
└── requirements.txt

8 directories, 17 files

Dataset must ha
## Usage
* To execute the training process, (e.g. for task1) navigate to the phase3 folder and run: `python  scr/train.py`
