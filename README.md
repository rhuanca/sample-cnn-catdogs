## Goal
test implementation of cnn described in https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html

## Downloading and preparing data
1. install kaggle command line tools https://github.com/Kaggle/kaggle-api
2. save your kaggle api key to: ~/.kaggle/kaggle.json
3. to download and organize data set:
```
$ kaggle competitions download -c dogs-vs-cats
$ ./prepare_data.sh
```

## Train
```
$ python3 classifier_from_little_data_script_1.py
```
weights will be saved at first_try.h5

while the process is running you will see something like this:
![training console output](training.png "training console output")

## Test
to test just call test_model.py

i.e.:
```
$ python3 test_model.py test1/4.jpg
```

you will see an output similar like this one
![test console output](test.png "test console output")
