# Phase3
Here, we present the python code that has to do with NLP tasks related to biomedical text.
## Task 1: Causality Inference
* Given a corpus of texts, that consists of abstracts and titles from papers and has to do with chemical compounds that are related to food and cosmetics industry, determine if the compound has a positive or negative relation to several adverse effects(cancer, neurotoxicity etc).
  * asdf
  * dfkj
  * asdkjfhaksjdf

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
  * Finally, install the program “wget” using Conda to download any files using CLI:
    `conda install wget`
    
  ###  Python Requirements
* nltk==3.5
* pandas==1.1.3
* numpy==1.18.5
* python_Levenshtein==0.12.0
* torch==1.7.0
* transformers==3.5.1
* tqdm==4.53.0
* scikit_learn==0.24.0

## Usage
* To execute the training process, (e.g. for task1) navigate to the phase3 folder and run: `python  scr/train.py`
