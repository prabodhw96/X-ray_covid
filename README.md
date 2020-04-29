# Detecting COVID-19 in X-ray images with Deep Learning
## Overview
This is the code for detecting COVID-19 in X-ray images with Keras, Tensorflow, and Deep Learning.

Since COVID-19 attacks the epithelial cells that line our respiratory tract, we can use X-rays to analyze the health of a patient's lungs.

# Data
**COVID-19 X-Ray Images Metadata:** https://raw.githubusercontent.com/ieee8023/covid-chestxray-dataset/master/metadata.csv

**Chest X-Ray Images:** https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia

## Steps
1. Create the following directories: ``dataset/covid`` and ``dataset/normal``
2. Run ``build_dataset.py`` to create the required dataset.

## Dependencies
* Numpy
* Matplotlib
* OpenCV
* Keras
* Urllib

## Result
**Accuracy:** 93-95%<br>
**Sensitivity:** 100%<br>
**Specificity:** 90.91%<br>
(given the limited dataset)
