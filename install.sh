#!/bin/sh
set -e

echo "1. Установка зависимостей"
uv sync
echo "Завершено установка основных зависимостей"

echo "2. Установка библиотек через openmim"
uv run mim install mmengine
uv run mim install "mmcv==2.1.0"
echo "Завершена установка библотек openmim"

echo "3. Установка mmsegmentation"
if [ -d "mmsegmentation" ]; then
  echo "Папка существует"
else
  git clone -b main https://github.com/open-mmlab/mmsegmentation.git
fi
cd mmsegmentation
uv run pip install -v -e .
echo "Установка завершена"

echo "4. Проверка установки mmsegmentation"
mkdir -p tmp

uv run mim download mmsegmentation --config pspnet_r50-d8_4xb2-40k_cityscapes-512x1024 --dest tmp/

uv run demo/image_demo.py \
  demo/demo.png \
  configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024.py pspnet_r50-d8_512x1024_40k_cityscapes_20200605_003338-2966598c.pth \
  tmp/pspnet_r50-d8_512x1024_40k_cityscapes_20200605_003338-2966598c.pth \
  --device cuda:0 \
  --out-file tmp/result.jpg

rm -rf tmp/

echo "Всё установлено"
