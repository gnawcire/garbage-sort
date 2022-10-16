import os, io
from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'VisionAPI\teak-instrument-365600-fb80cfabc45d.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('Images/image0.jpg')





def getLabelList():
    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    #prints labels
    labelList = []
    for label in labels:
        labelList.append(label.description)
    print(labelList)
    
    whatToDo = 'Throw This Item In The Trash'
    recycleItems = ['Metal', 'Bottle', 'Glass', 'Can', 'Aluminium', 'Cups', 'Paper', 'Cardboard', 'Water', 'Plastic', 'Carton', 'Newspaper', 'Folder', 'Fluid', 'Wood', 'Electronics', 'Phone', 'Television', 'Font', 'Battery']
    for x in labelList:
        if x == 'Food':
            whatToDo = 'Compost This Item'
        for y in recycleItems:
            if x == y:
                whatToDo = 'Recycle This Item'
    print(whatToDo)
    return whatToDo



