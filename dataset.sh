#!/bin/sh

set -e

echo 1. Скачивание датасета
wget https://code.s3.yandex.net/deep-learning/train_dataset_for_students.zip?etag=89d65db2fda8773993898ad054fe6732 -O train_dataset_for_students.zip

echo 2. Распаковка датасета
unzip train_dataset_for_students.zip

rm train_dataset_for_students.zip

mkdir mmsegmentation/data
mv train_dataset_for_students mmsegmentation/data
