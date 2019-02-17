#!/bin/bash
mkdir data
mkdir data/validation
unzip train.zip -d data


mkdir data/train/cats
mkdir data/validation/cats
mv data/train/cat.* data/train/cats 
for counter in {1000..1400}; do
    mv data/train/cats/cat.$counter.jpg data/validation/cats
done

mkdir data/train/dogs
mkdir data/validation/dogs
mv data/train/dog.* data/train/dogs 
for counter in {1350..1390}; do
    mv data/train/dogs/dog.$counter.jpg data/validation/dogs
done