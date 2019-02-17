## Goal
Test implementation of cnn described in https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html

## Downloading and organizing data
1. install kaggle command line tools https://github.com/Kaggle/kaggle-api
2. save your kaggle api key to: ~/.kaggle/kaggle.json
3. to download and organize data set:
```
$ kaggle competitions download -c dogs-vs-cats
$ mv *.zip data
$ unzip data/train.zip data

kaggle datasets download jessicali9530/stanford-dogs-dataset
```
4. to organize data execute
```
$ mkdir data
$ unzip stanford-dogs-dataset.zip -d data
$ chmod 644 data/images.tar
$ tar -xvf data/images.tar

```

##