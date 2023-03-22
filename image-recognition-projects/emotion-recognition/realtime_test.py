import cv2
import numpy as np
from keras.models import model_from_json, load_model
# from keras.preprocessing import image

emotion_dict = {0: "angry", 1: "disgust", 2: "fear", 3: "happy", 4: "neutral", 5: "sad", 6: "surprised"}

emotion_model = load_model("./emotions_model/best_model_2.h5", compile=False)
print("Loaded model")

# camera:
source = cv2.VideoCapture(0)

# external file - mp4:
# source = cv2.VideoCapture("/Users/Gabi/PycharmProjects/pythonProject/Emotion_detection_with_CNN/production ID_4588478.mp4")

while True:
    ret, frame = source.read()
    if not ret:
        break
    face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    num_faces = face_detector.detectMultiScale(grayFrame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in num_faces:
        cv2.rectangle(frame, (x, y-50), (x+w, y+h+10), (120, 0, 255), 3) #3=pogrubienie
        roi_gray_frame = grayFrame[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
        cropped_img = cropped_img / 255.0
        # predict emotions:
        emotion_prediction = emotion_model.predict(cropped_img)
        maxindex = int(np.argmax(emotion_prediction, axis=1))
        cv2.putText(frame, emotion_dict[maxindex], (x+5, y-60),  cv2.FONT_HERSHEY_COMPLEX, 2, (50, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Emotion Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

source.release()
cv2.destroyAllWindows()