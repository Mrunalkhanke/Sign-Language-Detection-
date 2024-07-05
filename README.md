 # VANI 
![Screenshot 2024-06-06 114837](https://github.com/Mrunalkhanke/Sign-Language-Detection-/assets/136327297/00526f79-18d0-42df-b4bb-7c0c301d2f2f)

# Problem Statement 
The problem statement involves developing a machine learning model to recognize sign language using Python and OpenCV. The model will process video or image inputs to detect and interpret hand gestures representing different signs. This will facilitate communication for individuals with hearing impairments by translating sign language into text or speech.

# Proposed Solution 
This project aims to develop a robust sign language recognition system using Python and OpenCV, leveraging a Convolutional Neural Network (CNN) with the Pre-Trained SSD MobileNet V2 architecture. 
The system is designed to recognize signs with 70-80% accuracy in various environments, facilitating communication for the deaf community and aiding learners in practicing sign language.

You can view [Demo video](https://drive.google.com/file/d/1FGzaVH7WWBe-hBcguFbSeC0x8rzJFwiV/view?usp=drive_link)
# Screenshots :
![Group 9 (1)](https://github.com/Mrunalkhanke/Sign-Language-Detection-/assets/136327297/4163b208-269e-4ca3-8712-45ce65398c77)

# Project Goals

### 1. Develop a sign language recognition model:
Utilize Python and OpenCV for image and video processing.
Implement a CNN model using the pre-trained SSD MobileNet V2 architecture.
### 2. Achieve high accuracy:
Target recognition accuracy of 70-80% for various sign language gestures.
### 3. Support diverse environments:
Ensure the model works effectively in different lighting and background conditions.
### 4.Facilitate communication:
Help the deaf community by translating sign language into text or speech.
Aid learners in practicing and improving their sign language skills.

# Methodology

### 1. Data Collection:
Gather a diverse dataset of sign language gestures, ensuring variability in background, lighting, and hand positions.
### 2.Data Preprocessing:
Perform data augmentation techniques such as rotation, scaling, and flipping to increase the robustness of the model.
Normalize the images for consistent input to the neural network.
### 3. Model Architecture:
Use the SSD MobileNet V2 architecture for object detection and feature extraction.
Fine-tune the pre-trained model on the collected dataset to adapt it to sign language recognition.
### 4. Training and Evaluation:
Split the dataset into training, validation, and test sets (e.g., 70% training, 15% validation, 15% testing).
Train the model using appropriate loss functions and optimizers.
Evaluate the model's performance on the test set, aiming for 70-80% accuracy.
### 5. Deployment:
Develop a user-friendly interface for real-time sign language recognition.
Optimize the system for deployment on various devices (e.g., PCs, smartphones).

# Process Flow : 
![work flow](https://github.com/Mrunalkhanke/Sign-Language-Detection-/assets/136327297/cd49602a-10b6-4f57-ab1a-b02c583211cc)


#  Key Features
### 1. Real-Time Recognition:  
Capture and recognize sign language gestures in real-time using a webcam.
### 2. High Accuracy:
Utilizes a pre-trained SSD MobileNet V2 model fine-tuned for sign language recognition.
### 3. User-Friendly Interface: 
Provides an intuitive interface for capturing live video input and displaying recognized gestures.
### 4. Accessibility: 
Includes features like adjustable font sizes, high contrast modes, and audio feedback options.

# Tech Stack 
1.  Python: The primary programming language for implementing machine learning algorithms and computer vision techniques.
2.  OpenCV: Used for capturing video input from the camera and processing the video frames.
3. TensorFlow/Keras: Utilized for building and training the convolutional neural network (CNN) model for gesture recognition.
4. CNN: The core of the system, responsible for extracting features from the video frames and classifying them into sign language gestures.
5. Real-time Processing: Techniques such as frame differencing and motion detection will be used for real-time processing of sign language gestures.
6. Graphical User Interface (GUI): A GUI will be developed to provide a user-friendly interface for interacting with the system, displaying the recognized gestures and their corresponding meanings.

# How quick can this technology be implemented?
This technology can be implemented within a few weeks, depending on the availability of a suitable dataset and the specific requirements of the deployment environment.

# What is the impact of this solution?
This solution enhances communication accessibility for the deaf community and provides an effective tool for learning and practicing sign language, fostering inclusivity and improving social integration. Furthermore, it can be integrated into various applications, making it easily accessible and usable in different contexts.

**Accuracy:** The model achieved an overall accuracy of approximately 75% on the test set, with individual gesture recognition rates ranging between 70% and 80%.

**Latency:** The average processing time per frame is approximately 0.2 seconds, making the system suitable for real-time applications.

**Robustness:** The model performed well across different environmental conditions, demonstrating consistent accuracy in various lighting and background settings.

# Is the solution scalable?
Yes, the solution is scalable, as it can be expanded to recognize more sign language gestures, trained on larger and more diverse datasets, and integrated into various applications and platforms, ensuring broad accessibility and adaptability.

# Future Scope
1. **Dataset Expansion**: Enhance the model's accuracy and versatility by including a wider variety of sign language gestures and variations.
2. **Model Improvement**: Experiment with advanced neural network architectures and fine-tuning techniques to improve recognition accuracy and efficiency.
3. **User Feedback Integration**: Incorporate real-time user feedback to refine the system and address practical challenges in diverse environments.
4. **Cross-Platform Deployment**: Develop mobile and web applications to increase accessibility and usability across different devices and operating systems.
5. **Real-Time Translation**: Implement real-time text or speech translation to facilitate seamless communication between sign language users and non-users.
  
# Steps To Run The Project : 
 **step 1 : Clone the repository:**
 git clone https://https://github.com/Mrunalkhanke/Sign-Language-Detection-

 **Step 2: Navigate to the project directory:**
 cd sign-language-recognition

**Step 3 : Run the inference script:**
python inference_classifier.py

**Step 4 :Run the training script:** 
python train_classifier.py









