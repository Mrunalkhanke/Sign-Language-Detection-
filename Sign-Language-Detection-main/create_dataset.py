import os
import pickle
import numpy as np
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize the MediaPipe Hands model
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data'

data = []
labels = []

# Function to process an image and extract hand landmarks
def process_image(img_path, max_landmarks=21):
    x_ = []
    y_ = []

    # Read the image
    img = cv2.imread(img_path)
    
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the image to detect hand landmarks
    results = hands.process(img_rgb)

    # If hand landmarks are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                # Get the x, y coordinates of the landmark
                x = landmark.x
                y = landmark.y
                x_.append(x)
                y_.append(y)

        # Normalize the coordinates and add to the data_aux list
        min_x, min_y = min(x_), min(y_)
        normalized_landmarks = []
        for i in range(len(x_)):
            normalized_landmarks.append(x_[i] - min_x)
            normalized_landmarks.append(y_[i] - min_y)

        # Pad or truncate the landmarks to ensure a fixed length
        if len(normalized_landmarks) < 2 * max_landmarks:
            normalized_landmarks.extend([0] * (2 * max_landmarks - len(normalized_landmarks)))
        elif len(normalized_landmarks) > 2 * max_landmarks:
            normalized_landmarks = normalized_landmarks[:2 * max_landmarks]

        return normalized_landmarks

    else:
        # If hand landmarks are not detected, return None
        return None

# Loop through the directories and images to create the dataset
for dir_ in os.listdir(DATA_DIR):
    for img_name in os.listdir(os.path.join(DATA_DIR, dir_)):
        img_path = os.path.join(DATA_DIR, dir_, img_name)

        # Process the image and extract hand landmarks
        landmarks_data = process_image(img_path)

        # If hand landmarks are extracted, add to the dataset
        if landmarks_data:
            data.append(landmarks_data)
            labels.append(dir_)

# Convert the lists to numpy arrays
data = np.array(data)
labels = np.array(labels)

# Save the data and labels to a pickle file
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)
