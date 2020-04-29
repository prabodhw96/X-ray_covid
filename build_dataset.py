import pandas as pd
import shutil
import urllib.request
import os
from imutils import paths
import random

df = pd.read_csv("metadata.csv")

img_url = "https://raw.githubusercontent.com/ieee8023/covid-chestxray-dataset/master/images/"
imgpath = []
for i, row in df.iterrows():
    if row["finding"]!="COVID-19" or row["view"]!="PA":
        continue
    imgpath.append(row["filename"])
    
for i in imgpath:
    urllib.request.urlretrieve(img_url+str(i), "dataset/covid/"+str(i))
    
path, dirs, files = next(os.walk("dataset/covid"))
covid_file_count = len(files)
print(covid_file_count)

basePath = os.path.sep.join(["chest_xray", "train", "NORMAL"])
imagePaths = list(paths.list_images("chest_xray"))

random.seed(42)
random.shuffle(imagePaths)
imagePaths = imagePaths[:covid_file_count]

for (i, imagePath) in enumerate(imagePaths):
    filename = imagePath.split(os.path.sep)[-1]
    outputPath = os.path.sep.join(["dataset/normal", filename])
    shutil.copy2(imagePath, outputPath)
    
path, dirs, files = next(os.walk("dataset/normal"))
normal_file_count = len(files)
print(covid_file_count == normal_file_count)