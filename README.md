# BibHelioTech

[![DOI](https://zenodo.org/badge/515186537.svg)](https://zenodo.org/badge/latestdoi/515186537)
[![License](https://img.shields.io/github/license/ADablanc/BibHelioTech.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)
[![GitHub release](https://img.shields.io/github/release/ADablanc/BibHelioTech.svg)](https://github.com/ADablanc/BibHelioTech/releases/tag/v2.0.0)
[![GitHub issues](https://img.shields.io/github/issues/ADablanc/BibHelioTech)](https://github.com/ADablanc/BibHelioTech/issues)

## BibHelioTech project description

## Installation guide
STEP 1: install all dependency<br />
&nbsp;&nbsp;&nbsp;On your shell, run: pip install -r requirements.txt<br />
&nbsp;&nbsp;&nbsp;Don't forget to install SUTime Java dependencies, more details on: https://pypi.org/project/sutime/ <br />
&nbsp;&nbsp;&nbsp;Put the "english.sutime.txt" under sutime install directory, jars/stanford-corenlp-4.0.0-models.jar/edu/stanford/nlp/models/sutime/

STEP 2: tesseract 5 installation (Ubuntu exemple)<br />
&nbsp;&nbsp;&nbsp;sudo apt update<br />
&nbsp;&nbsp;&nbsp;sudo add-apt-repository ppa:alex-p/tesseract-ocr-devel<br />
&nbsp;&nbsp;&nbsp;sudo apt install -y tesseract-ocr<br />
&nbsp;&nbsp;&nbsp;sudo apt update<br />
&nbsp;&nbsp;&nbsp;tesseract --version

STEP 3: GROBID installation<br />
&nbsp;&nbsp;&nbsp;install GROBID under ../<br />
&nbsp;&nbsp;&nbsp;Follow install instruction on: https://grobid.readthedocs.io/en/latest/Install-Grobid/ <br />
&nbsp;&nbsp;&nbsp;Make sure you have JVM 8 used by default !

STEP 4: GROBID python client installation<br />
&nbsp;&nbsp;&nbsp;install GROBID python client under ../<br />
&nbsp;&nbsp;&nbsp;Follow install instruction on: https://github.com/kermitt2/grobid_client_python <br />

## User guide
Put pdf files under BibHelio_Tech/DATA/Papers<br />
You just have to run "MAIN.py".

## License
If you use BibHelio_Tech, you agree to use it following this license.

## Authors