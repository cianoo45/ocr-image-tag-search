
import piexif
# Imports the Google Cloud client library
from PIL import Image
from google.cloud import vision
import pickle
import glob

def search_for_image(searchword):
    fileList = glob.glob("tagged-images/*")
    searchword = searchword.lower()
    resultList =[]

    for image in fileList:
        tags = read_image(image)
        words = tags['words']
        labels = tags['labels']
        results = words + labels

        for word in results:
            if word.lower() == searchword:
                resultList.append(image)
    resultList = list(set(resultList))
    print("List of images containing the word {0} :".format(searchword),resultList)


def read_image(path):
    img = Image.open(path)
    raw = img.getexif()[piexif.ExifIFD.UserComment]
    tags = pickle.loads(raw)
    return tags


def tag_image(paths):
    for path in paths:
        filename = path.split("\\")
        if len(filename) ==1:
            filename = path.split("/")
        filename = filename[-1]
        img = Image.open(path)
        exif_dict = piexif.load(path)

        ocrWords = detect_text(path)
        data = pickle.dumps(ocrWords)
        exif_dict['Exif'][piexif.ExifIFD.UserComment] = data
        exif_dat = piexif.dump(exif_dict)
        print("Tagged Image: {0}...Saving".format(filename))
        img.save('tagged-images/{0}'.format(filename), exif=exif_dat)


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    labelList=[]
    for label in labels:
        labelList.append(label.description)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    textList=[]
    for text in texts[1:]:
        textList.append(text.description)
    exifDict = {"words":textList,"labels":labelList}

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return exifDict



