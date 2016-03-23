# neurofinder-datasets

This README describes the datasets for the [neurofinder](http://neurofinder.codeneuro.org) analysis benchmarking challenge. You probably received this document when downloading a dataset.

Training datasets are provided with ground truth labeled regions for identified neurons, and testing datasets are provided without ground truth. Each downloadable dataset includes metadata (as `.json`), images (as `.tiff`), and coordinates of identified neurons, also known as ROIs (as `.json`). Datasets are around 1 GB zipped and a few GBs unzipped. Visit the [neurofinder](https://github.com/codeneuro/neurofinder) repository for current download links for all datasets.

Along with the data itself, each download includes example loading scripts in `python`, `MATLAB`, and `javascript`, the source code of which are in this [reposistory](https://github.com/codeneuro/neurofinder-datasets). 

To contribute example loading scripts for other languages, just submit a pull request! If there are problems with the loading scripts, submit an issue on GitHub.
