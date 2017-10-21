import io
import os
import json


# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

#visionClient = vision.Client()



# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
path = ('grocery_list3.jpg')

# Loads the image into memory

groceryData = []

def detect_text(path):
 
    client = vision.ImageAnnotatorClient()

    # [START migration_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #Comment this out print('Texts:')
    
    for text in texts:
        word = text.description
        # Comment this out print('\n"{}"'.format(word))
        groceryData.append(word)
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        # Comment this out print('bounds: {}'.format(','.join(vertices)))
    # [END migration_text_detection]
# [END def_detect_text]

#Calls the detect_text function
detect_text(path)

#Cleans up Grocery List
groceryDataModified = groceryData[1:]
groceryDataObject = {"groceryList" : groceryDataModified}

#Creates a JSON File of the Grocery List
groceryDataJSON = json.dumps(groceryDataObject)
print(groceryDataJSON)

