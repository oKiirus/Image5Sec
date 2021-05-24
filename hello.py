import cv2
import dropbox
import time
import random

startTime = time.time()

def TakeSnapshot():
    number = random.randint(1 , 100)

    video = cv2.VideoCapture(0)
    result = True

    while(result):
       
        ret, frame = video.read()
        imageName = 'img' + str(number) + '.png'
        cv2.imwrite(imageName, frame)
        result = False
        startTime = time.time()

    return imageName

    video.release()
    cv2.destroyAllWindows()

    print('Done')

def uploadFile(imageName):
    token = 'YlqvTTo4h10AAAAAAAAAATm7_cr6Sjqa0GCjZwXeoiL4QxsfJwru-Ji8MJmnUydE'
    file_from = imageName
    file_to = '/testFolder/' + imageName
    dbx = dropbox.Dropbox(token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print('Image Uploaded')

def Name():
    while(True):
        if ((time.time() - startTime) >= 5):
            name = TakeSnapshot()

            uploadFile(name) 

Name()
            
        


    

    