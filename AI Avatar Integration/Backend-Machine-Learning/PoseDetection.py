import cv2
from openpose import openpose as op

def detectPosture(imagePath):
    params = {
        "model_folder": "openpose/models/",
        "face": False,
        "hand": False
    }

    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    # Read image
    image = cv2.imread(imagePath)
    datum = op.Datum()
    datum.cvInputData = image
    opWrapper.emplaceAndPop([datum])

    return datum.poseKeypoints
