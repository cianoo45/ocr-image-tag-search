# ocr-image-tag-search
Application to Tag and Search Images using Google OCR

## What does it do

This application passes images through Google's OCR API to grab text in the image, as well as perform label detection (Such as detecting cars, people etc) 
It then inserts these results into the images Exif metadata in the UserComment section, this allows the results to permenantly be stored within the image,
So it can be searched whenever and persists after the application is finished, and will persist if the image is moved or emailed etc

## Applications

In my mind this would be a great phone app, The ability to tag an entire gallery of photos and make them searchable would be extremely useful for finding memes, 
finding typed notes etc

## Installation
Set up google cloud vision api account

```shell
# clone repo
cd ocr-image-tag-search
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

## Usage

Tag a single image
```shell
python run.py -m tag -f images/test.jpg
```

Tag all images in the images/ folder
```shell
python run.py -m tag -f 
```

Search for an image containing a word
```shell
python run.py -m search -s searchword
```
