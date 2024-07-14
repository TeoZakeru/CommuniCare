# **The Smart Assistive Communication System - CommuniCare**

## **Introduction**

The Smart Assistive Communication System - CommuniCare is a tool designed to improve the communication abilities of paralysis patients. Utilizing advanced AI and affordable technology, this system translates subtle finger or eye movements into coherent sentences. By providing a real-time, intuitive, and user-friendly interface, it significantly reduces isolation and frustration, enhancing the quality of life for individuals with conditions like quadriplegia, paraplegia, stroke, ALS, or severe cerebral palsy. This innovative solution ensures effective communication and better interaction with caregivers and loved ones and ensures that the voices of those who face difficulty in speaking are heard loud and clear.

## **Overview**

The CommuniCare employs a camera to detect finger or eye movements, translating them into coherent sentences via advanced AI algorithms. It features a user-friendly interface, customization options and timely reminders for medications and checkups. Designed with affordability in mind, it utilizes the cost-effective Raspberry Pi Zero 2 W, making it accessible to a wider range of patients. This system not only empowers paralysis patients by enhancing communication but also supports caregivers and healthcare providers in delivering more efficient and personalized care.

## **Operational Workflow Diagram**
![Workflow Diagram](assets/flowchart.png)
## **Model Training Video**

https://github.com/TeoZakeru/CommuniCare/assets/130887983/345544d2-329b-42b0-a027-b75c48721132


## **Tasks Completed Until Now**
### **Model Training**

- To ensure our system can accurately detect and classify various hand movements, we undertook a comprehensive data collection process. We gathered a diverse dataset of hand orientations and finger movements, specifically focusing on minimal movements that individuals with severe paralysis can perform.

### **Data Collection**

- The data collection process involved capturing numerous images and videos of different hand and finger positions. We included a variety of movements, such as:

   - Hand Lifting: Various degrees of hand elevation.
   - Finger Movements: Individual finger lifts, particularly focusing on minimal movements like lifting just the index finger.

### **Detection Capabilities**

- As a result of this rigorous training process, our AI model can accurately detect whether the hand is lifted or if just a specific finger, such as the index finger, is raised. The model is sensitive enough to detect minimal movements, ensuring that even the slightest gestures are recognized. This precision is particularly important for providing reliable control mechanisms for paralyzed patients.
## **Features Implemented Until Now**

### **Blink Detection**


https://github.com/TeoZakeru/CommuniCare/assets/130887983/20d78fef-2c9d-4a59-90b1-a86107867a54

- We implemented a sophisticated Blink Detection feature that enables our system to accurately detect when a user blinks and distinguish between voluntary and involuntary blinks. This advanced capability allows blinks to be utilized for a range of practical purposes.

- Voluntary blinks can be used to select items on a screen or to simulate mouse clicks, thereby providing an intuitive method for users to interact with their devices. This feature enhances the overall functionality of the system, making it possible for users to perform various tasks without needing to rely on traditional input methods.

### **Iris Controlled Cursor**


https://github.com/TeoZakeru/CommuniCare/assets/130887983/6edf22cf-0a52-4368-a11d-d6ea1196e5db


- We have developed an eye-controlled cursor system using Python's OpenCV library. This system tracks the movement of the iris and moves the mouse cursor accordingly, allowing users to control their computer with eye movements.

- This kind of control method provides users with an efficient way to navigate their computer, enhancing accessibility and ease of use for individuals with limited mobility.

### **Finger Controlled Keyboard**

https://github.com/TeoZakeru/CommuniCare/assets/130887983/3d18e297-3a9b-4e3b-982c-bcb0beda0538


- We have developed a specialized keyboard for typing, designed to cater to the needs of users with severe mobility limitations. The keyboard features three rows, each containing ten keys. Users can select a row by blinking their eyes, utilizing the blink detection system previously described. Once a row is selected, the user can type by using specific finger movements, detected by our previously trained AI models.

- This approach combines eye blinks and finger movements to provide an efficient and user-friendly typing experience. By leveraging the capabilities of our advanced AI models, we ensure that users can communicate effectively and with minimal effort, despite their physical limitations.


### **Finger Controlled Messaging**

- The Raspberry Pi Camera detects and tracks finger movement using Mediapipe, OpenCV and picamera2 Libraries. We utilise this tracking technology to detect a finger-tap movement and keep track of number of finger taps and send a specific pre-defined message to a care-taker or any saved cotact that corresponds to a specific number of taps.

#### **One-Tap Message**

https://github.com/TeoZakeru/CommuniCare/assets/130887983/8d2c987c-0217-4aaf-b94a-b458282d3797

- One Tap here corresponds to Food.

#### **Two-Tap Message**


https://github.com/TeoZakeru/CommuniCare/assets/130887983/05e14df8-3bc5-456a-b755-14167367f305

- Two Taps here correspond to Emergency

#### ***Three-Tap Message**


https://github.com/TeoZakeru/CommuniCare/assets/130887983/fe3fd8c7-926c-4ebb-92c5-b32d40232099

- Three Taps here correspond to TV.

# **Product Demo**

## ***Product Overview***



## ***Product Setup***

- This is the setup that we are using for our product. The Raspberry Pi Zero 2 W is coupled with the Camera Module and enclosed within a cardboard box with an opening for a power supply. This cardboard box can be attached to any holder. We have used a tripod stand here. The device can be configured to work with any bluetooth-enabled speaker if you want the sound to be heard out loud or to a wireless bluetooth headset if the voice is intended to be heard by only one person. We have used a speaker here.

- Our product can be used in 2 ways :
	- With a computer/display for usage
	- Without a computer/display for usage

- For both ways, we have to first access the Bluetooth settings and add the speaker/headset as the main audio output device. This can be done in 2 ways - through the Terminal or via VNC.

## ***Working 1 - ( requires a Computer)***

- In this method, we have a simple python code that streams the live footage from the camera module onto a website with a Flask backend, which can be received by a server/computer that can perform the required operations and exeute the required code on the received video footage.

- For this, we need a computer/display for configuration as well as usage as demonstrated in the below videos.

### Device Overview
 
- This document provides an overview of the various modules and command sets used in the device, along with information on the built-in tutorial interface.

#### Modules Overview

##### HandTrackingModule

- The HandTrackingModule is utilized for configuring and tracking finger movements.

##### HandTappingModule

- The HandTappingModule employs a machine learning model trained on custom datasets to identify the number of hand taps within a short time frame.

##### Configure Module

- The Configure module is responsible for setting up the eye movement detection parameters.

##### ParalysisMovement Module

- The ParalysisMovement module uses the threshold values provided by the Configure module to detect and predict the nature of eye movements.

##### Integration and Functionality

These modules are integrated into the main GUI to perform various tasks:

- *Hand Tap Commands:* Initiate various tasks through hand taps.
- *Eye-Controlled Mouse:* Control the mouse using eye movements.
- *Finger-Controlled Keyboard:* Operate the keyboard with limited finger motion.

#### Command Sets Overview

##### Primary Commands

- Primary commands necessitate the assistance of a caretaker. Examples include commands for FOOD, WATER, and EMERGENCY. The specific command invoked is determined by the number of hand taps. Once a primary command is activated, it runs on a loop through the speaker, and messages are sent repeatedly to the caretaker's mobile until the caretaker attends to the patient.

##### Secondary Commands

- Secondary commands enable the patient to navigate the digital world independently. These commands are controlled through eye movements, blinking, and limited finger lifting. They facilitate actions such as cursor control, keyboard typing, and other digital interactions.

#### Interface Tutorial

- The interface includes a built-in tutorial designed to instruct users on how to operate the device. This feature eliminates the need for a specialized person to configure everything, ensuring that users can independently set up and use the device efficiently.

### ***Code for Working1***

#### config.py

```
CHROME_DATA_PATH = "user-data-dir=C:\\Users\\jishu\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
```
#### Configure.py

```
import cv2
import mediapipe as mp
import numpy as np
import time

class Configure():
    
    def __init__(self):
        
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        self.eye_closed = [float('inf'), float('-inf')]
        self.eye_open = [float('inf'), float('-inf')]
        self.left = float('-inf')
        self.right = float('inf')
        self.up =  float('-inf')
        self.down = float('inf')
        
        self.iterations = 0
        self.face_mesh = self.mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, 
                                                    refine_landmarks=True, min_detection_confidence=0.5,
                                                    min_tracking_confidence=0.5)
        
        self.eye_open_config = True
        self.eye_closed_config = False
        self.left_config = False
        self.right_config = False
        self.up_config = False
        self.down_config = False
        
    def get_landmarks(self, image):
        
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(imageRGB)
        
        self.imageheight, self.imagewidth, self.imagechannels = image.shape
        
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
        else:
            landmarks = []
            
        return results, landmarks
    
    def configure_eye_open(self, landmarkA, landmarkB):
        self.iterations += 1  # Increment iterations
        
        landmarkA = np.array([int(landmarkA.x * self.imagewidth), int(landmarkA.y * self.imageheight)])
        landmarkB = np.array([int(landmarkB.x * self.imagewidth), int(landmarkB.y * self.imageheight)])
        
        distance = int(np.linalg.norm(landmarkA - landmarkB))
        
        if distance < self.eye_open[0]:
            self.eye_open[0] = distance
        elif distance > self.eye_open[1]:
            self.eye_open[1] = distance
        
        if self.iterations >= 100:
            self.iterations = 0
            self.eye_open_config = False
            self.eye_closed_config = True
            return True
        return False
    
    def configure_eye_closed(self, landmarkA, landmarkB):
        self.iterations += 1  # Increment iterations
        
        landmarkA = np.array([int(landmarkA.x * self.imagewidth), int(landmarkA.y * self.imageheight)])
        landmarkB = np.array([int(landmarkB.x * self.imagewidth), int(landmarkB.y * self.imageheight)])
        
        distance = int(np.linalg.norm(landmarkA - landmarkB))
        
        if distance < self.eye_closed[0]:
            self.eye_closed[0] = distance
        elif distance > self.eye_closed[1] and distance < self.eye_open[0]:
            self.eye_closed[1] = distance
        
        if self.iterations >= 100:
            self.iterations = 0
            self.eye_closed_config = False
            self.left_config = True
            return True
        return False
    
    def configure_eye_left(self, landmarkA):
        self.iterations += 1  # Increment iterations
        
        landmarkA = np.array([int(landmarkA.x * self.imagewidth), int(landmarkA.y * self.imageheight)])
        
        if self.iterations > 70:
            if landmarkA[0] > self.left:
                self.left = landmarkA[0]
            
        if self.iterations >= 100:
            self.iterations = 0
            self.left_config = False
            self.right_config = True
            return True
        return False
    
    def configure_eye_right(self, landmarkA):
        self.iterations += 1  # Increment iterations
        
        landmarkA = np.array([int(landmarkA.x * self.imagewidth), int(landmarkA.y * self.imageheight)])
        
        if self.iterations > 70:
            if landmarkA[0] < self.right:
                self.right = landmarkA[0]
            
        if self.iterations >= 100:
            self.iterations = 0
            self.right_config = False
            self.up_config = True
            return True
        return False
    
    def configure_eye_up(self, landmarkA):
        self.iterations += 1  # Increment iterations
        
        landmarkA = np.array([int(landmarkA.x * self.imagewidth), int(landmarkA.y * self.imageheight)])
        
        if self.iterations > 70:
            if landmarkA[1] > self.up:
                self.up = landmarkA[1]
            
        if self.iterations >= 100:
            self.iterations = 0
            self.up_config = False
            self.down_config = True
            return True
        return False
    
    def configure_eye_down(self, landmarkA):
        self.iterations += 1  # Increment iterations
        
        landmarkA = np.array([int(landmarkA.x * self.imagewidth), int(landmarkA.y * self.imageheight)])
        
        if self.iterations > 70:
            if landmarkA[1] < self.down:
                self.down = landmarkA[1]
            
        if self.iterations >= 100:
            self.iterations = 0
            self.down_config = False
            return True
        return False

        
        

def main():
    cap = cv2.VideoCapture(0)
    config = Configure()
    pTime = 0
    
    while True:
        success, img = cap.read()
        if not success:
            print("Failed to read frame from camera. Exiting...")
            break
        
        img = cv2.resize(img, (1000, 1000))
        img = cv2.flip(img, 1)
        
        results, landmarks = config.get_landmarks(img)
        if landmarks:
            
            if config.eye_open_config:
                cv2.putText(img, "Please Keep Your Eyes Open", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                done = config.configure_eye_open(landmarks[160], landmarks[144])
                if done:
                    continue
                
            elif config.eye_closed_config: 
                cv2.putText(img, "Please Close Your Eyes", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                done = config.configure_eye_closed(landmarks[160], landmarks[144])
                if done:
                    continue
            
            elif config.left_config:
                cv2.putText(img, "Please Follow The Dot", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                cv2.circle(img, (20, int(config.imageheight / 2)), 20, (0, 0, 255), -1)

                done = config.configure_eye_left(landmarks[469])
                if done:
                    continue
            
            elif config.right_config:
                cv2.putText(img, "Please Follow The Dot", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                cv2.circle(img, (int(config.imagewidth - 20), int(config.imageheight / 2)), 20, (0, 0, 255), -1)
                done = config.configure_eye_right(landmarks[469])
                if done:
                    continue
                
            elif config.up_config:
                cv2.putText(img, "Please Follow The Dot", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                cv2.circle(img, (int(config.imagewidth / 2), 20), 20, (0, 0, 255), -1)
                done = config.configure_eye_up(landmarks[469])
                if done:
                    continue
                
            elif config.down_config:
                cv2.putText(img, "Please Follow The Dot", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                cv2.circle(img, (int(config.imagewidth / 2), int(config.imageheight - 20)), 20, (0, 0, 255), -1)
                done = config.configure_eye_down(landmarks[469])
                if done:
                    continue
            
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        cv2.putText(img, f'FPS: {int(fps)}', (20, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)
        pTime = cTime
        
        cv2.imshow("ANNOTATED IMAGE", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    print(config.eye_closed)
    print(config.eye_open)
    print(config.left)
    print(config.right)
    print(config.up)
    print(config.down)
    
    
    

if __name__ == "__main__":
    main()
```

#### EuroFIlter.py

```
import math

class OneEuroFilter:
    def __init__(self, mincutoff=1.0, beta=0.0, dcutoff=1.0):
        self.min_cutoff = mincutoff
        self.beta = beta
        self.d_cutoff = dcutoff
        self.x_prev = None
        self.dx_prev = None
        self.t_prev = None

    def alpha(self, cutoff, dt):
        tau = 1.0 / (2.0 * math.pi * cutoff)
        return 1.0 / (1.0 + tau / dt)

    def apply_filter(self, x, t):
        if self.t_prev is None:
            self.x_prev = x
            self.dx_prev = 0
            self.t_prev = t
            return x
        
        dt = t - self.t_prev
        dx = (x - self.x_prev) / dt if dt > 0 else 0.0
        dx_hat = self.dx_prev + self.alpha(self.d_cutoff, dt) * (dx - self.dx_prev)
        cutoff = self.min_cutoff + self.beta * abs(dx_hat)
        x_hat = self.x_prev + self.alpha(cutoff, dt) * (x - self.x_prev)
        
        self.x_prev = x_hat
        self.dx_prev = dx_hat
        self.t_prev = t
        
        return x_hat
```

#### GUI.py

```
import tkinter as tk
import threading
import logging
import time
import os
from PIL import Image, ImageTk
import cv2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyttsx3
from pynput.mouse import Button, Controller

# Custom modules
import Configure as cf
import HandTrackingModule as htm
import HandTappingModule as httm
import ParalysisMovements as pm
from config import CHROME_DATA_PATH
from Keyboard import KeyBoard
import json

logging.basicConfig(level=logging.INFO)

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.transition_id = None
        self.rotation_id = None

        self.title("CommuniCare")
        self.geometry("1440x1080")

        self.welcome_frame = tk.Frame(self)
        self.welcome_frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.welcome_frame, text="Welcome to CommuniCare", font=("Helvetica", 30))
        self.label.pack(pady=200)
                
        self.eye_configure = cf.Configure()
        self.hand_tracker = htm.HandDetector()
        self.hand_tap_detector = httm.HandTappingModule()
        
        self.MOUSE_MOTION = False
        self.KEYBOARD = False
        self.EXPLAIN_TUTORIAL = True
        self.BUTTON_CLICK = True
        self.SEND_PRIMARY_MESSAGE = False
        self.USE_SECONDARY_FUNCTIONS = False
        
        self.mouse = Controller()
        self.driver = None
        self.thread = None
        
        self.video_capture = cv2.VideoCapture(0)
        
        self.after(1000, self.welcome_message)
        
    def welcome_message(self):
        self.text_to_speech("Welcome to CommuniCare. We will begin with the configuration. We will start configuring your eyes first. Please follow the instructions written on the screen.")
        self.after(2000, self.show_configure)
        
    def explain_tutorial(self):
        self.text_to_speech("Communicare assists you in communicating effectively with your caregivers and navigating the digital world.\
                            There are two types of commands: Primary and Secondary. Primary Commands: These require the assistance of a\
                            caregiver. Examples include requesting food, water, or emergency help. These commands are detected through\
                            tapping, with the number of taps indicating which command is executed. A message is then sent to the\
                            caregiver's number. Secondary Commands: These commands assist you in navigating your phone or laptop using\
                            limited movements. Detailed instructions for these commands will be provided when you start using the services.")
        self.EXPLAIN_TUTORIAL = False
            
        self.transition_id = self.after(3000, self.show_option2)
    
    def button_click(self):
        self.text_to_speech("The button when it is blue is active. Blink once when the button is active to select it.")

        
    def text_to_speech(self, text):
        engine = pyttsx3.init()
        
        engine.setProperty('rate', value=150)
        engine.setProperty('volume', value=1)
        
        engine.say(text)
        
        engine.runAndWait()
                
    def show_menu(self):
        
        self.BUTTON_CLICK = True
        self.after(1000, self.text_to_speech, "The button when it is blue is active. Blink once when the button is active to select it.")
        
        self.clear_frames()
        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.menu_frame, text="Do you want a Tutorial?", font=("Helvetica", 20))
        self.label.pack(pady=50)

        self.btn_option1 = tk.Button(self.menu_frame, text="Yes", font=("Helvetica", 20), command=self.show_option1)
        self.btn_option1.pack(pady=20)

        self.btn_option2 = tk.Button(self.menu_frame, text="No", font=("Helvetica", 20), command=self.show_option2)
        self.btn_option2.pack(pady=20)

        self.rotate_buttons([self.btn_option1, self.btn_option2])
        
        self.process_frame_for_blinks([self.btn_option1, self.btn_option2])

    def show_option1(self):
        
        self.BUTTON_CLICK = False
        
        self.clear_frames()
        self.option1_frame = tk.Frame(self)
        self.option1_frame.pack(fill="both", expand=True)

        
        img = Image.open("C:\\Users\\jishu\\OneDrive\\Desktop\\PythonCodes\\TutorialIMG.png")
        img_tk = ImageTk.PhotoImage(img)
        label = tk.Label(self.option1_frame, image=img_tk)
        label.image = img_tk  # Keep a reference to prevent garbage collection
        label.pack()

        self.btn_back = tk.Button(self.option1_frame, text="Back to Menu", font=("Helvetica", 15), command=lambda: self.go_back(self.option1_frame, self.show_menu))
        self.btn_back.pack(pady=20)
        self.btn_back.config(bg='lightblue')

        if self.EXPLAIN_TUTORIAL:
            self.after(1000, self.explain_tutorial)

    def show_option2(self):
        
        self.SEND_PRIMARY_MESSAGE = False
        self.BUTTON_CLICK = False
        
        self.clear_frames()
        self.option2_frame = tk.Frame(self)
        self.option2_frame.pack(fill="both", expand=True)
    
        self.label = tk.Label(self.option2_frame, text="Menu", font=("Helvetica", 20))
        self.label.pack(pady=50)
    
        self.btn_option2_1 = tk.Button(self.option2_frame, text="Food", font=("Helvetica", 20), command=self.show_food_menu)
        self.btn_option2_1.pack(pady=20)
    
        self.btn_option2_2 = tk.Button(self.option2_frame, text="Emergency", font=("Helvetica", 20), command=self.show_emergency_menu)
        self.btn_option2_2.pack(pady=20)
    
        self.btn_option2_3 = tk.Button(self.option2_frame, text="Water", font=("Helvetica", 20), command=self.show_water_menu)
        self.btn_option2_3.pack(pady=20)
    
        self.btn_option2_4 = tk.Button(self.option2_frame, text="Apps", font=("Helvetica", 20), command=self.show_apps_menu)
        self.btn_option2_4.pack(pady=20)
    
        self.btn_back = tk.Button(self.option2_frame, text="Back to Menu", font=("Helvetica", 15), command=self.show_menu)
        self.btn_back.pack(pady=20)
        self.btn_back.config(bg='lightblue')
    
        # Start frame processing for hand tap detection
        self.after(1000, self.process_frame_for_taps)

    def process_frame_for_taps(self):
        success, image = self.video_capture.read()
        if not success:
            print("Failed to read frame from camera. Exiting...")
            self.update_configure_label("Configuration Failed")
            return
    
        image = cv2.resize(image, (1000, 1000))
        image = cv2.flip(image, 1)
    
        if self.hand_tap_detector.make_prediction(image):
            tapCount = self.hand_tap_detector.detectTap(self.hand_tap_detector.make_prediction(image))
    
        if tapCount == 1:
            self.show_food_menu()
            return
        elif tapCount == 2:
            self.show_emergency_menu()
            return
        elif tapCount == 3:
            self.show_water_menu()
            return
        elif tapCount == 4:
            self.show_apps_menu()
            return
    
        self.after(10, self.process_frame_for_taps)
    
    def process_frame_for_blinks(self, buttons):
        
        success, image = self.video_capture.read()
        if not success:
            print("Failed to read frame from camera. Exiting...")
            self.update_configure_label("Configuration Failed")
            return
    
        image = cv2.resize(image, (1000, 1000))
        image = cv2.flip(image, 1)
        
        results, landmarks = self.eye_movements.get_landmarks(image)
        
        if landmarks:
            
            if self.eye_movements.did_Blink(landmarkA=landmarks[160], landmarkB=landmarks[144]):
                
                for i, button in enumerate(buttons):
                    if button.cget("state") == "normal":
                        button.invoke()
                        
        
        
        if self.BUTTON_CLICK:
            self.after(1, self.process_frame_for_blinks, buttons)
            
    def speak_primary_message(self, text):
        if self.SEND_PRIMARY_MESSAGE:
            self.text_to_speech(text)
            self.after(2000, self.speak_primary_message, text)
        
    
    def send_whatsapp_headlessmessage(self, phone_number, message):
        
        self.speak_primary_message(message)
        
        def run_whatsapp():
            try:
                os.system("taskkill /im chrome.exe /f")
                options = webdriver.ChromeOptions()
                options.add_argument(CHROME_DATA_PATH)
                options.add_argument("--headless=new")
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')

                s = Service(executable_path="chromedriver-win64\chromedriver.exe")
                driver = webdriver.Chrome(service=s, options=options)
                driver.get("https://web.whatsapp.com/")
                time.sleep(15)

                search_icon = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div/div[2]/button")
                search_icon.click()
                time.sleep(2)

                search_new_chat = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[1]/div/div[2]/div[2]/div/div[1]/p")
                search_new_chat.send_keys(phone_number)
                time.sleep(2)
               
                first_name = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div[3]/div[1]/div/div/div[1]")
                first_name.click()
                time.sleep(2)

                msg_send_key = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
                msg_send_key.send_keys(message)
                time.sleep(2)

                send_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")
                send_button.click()
                time.sleep(2)

                logging.info("Message sent successfully!")
            except Exception as e:
                logging.error(f"Error sending WhatsApp message: {e}")
        
        thread = threading.Thread(target=run_whatsapp)
        thread.start()
        # thread.join()
            
        # if self.SEND_PRIMARY_MESSAGE:
        #     self.after(1000, self.send_whatsapp_headlessmessage, phone_number, message)


    def show_food_menu(self):
        self.SEND_PRIMARY_MESSAGE = True
        self.clear_frames()
        self.food_frame = tk.Frame(self)
        self.food_frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.food_frame, text="Food Menu", font=("Helvetica", 20))
        self.label.pack(pady=50)

        self.btn_back = tk.Button(self.food_frame, text="Back to Menu", font=("Helvetica", 15), command=self.show_option2)
        self.btn_back.pack(pady=20)
        self.btn_back.config(bg='lightblue')
        
        self.after(3000, self.send_whatsapp_headlessmessage, "916291798504", "I want something to eat\n")

    def show_emergency_menu(self):
        self.SEND_PRIMARY_MESSAGE = True
        self.clear_frames()
        self.emergency_frame = tk.Frame(self)
        self.emergency_frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.emergency_frame, text="Emergency Menu", font=("Helvetica", 20))
        self.label.pack(pady=50)

        self.btn_back = tk.Button(self.emergency_frame, text="Back to Menu", font=("Helvetica", 15), command=self.show_option2)
        self.btn_back.pack(pady=20)
        self.btn_back.config(bg='lightblue')
        
        self.after(3000, self.send_whatsapp_headlessmessage, "916291798504", "I need help\n")

    def show_water_menu(self):
        self.SEND_PRIMARY_MESSAGE = True
        self.clear_frames()
        self.water_frame = tk.Frame(self)
        self.water_frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.water_frame, text="Water Menu", font=("Helvetica", 20))
        self.label.pack(pady=50)

        self.btn_back = tk.Button(self.water_frame, text="Back to Menu", font=("Helvetica", 15), command=self.show_option2)
        self.btn_back.pack(pady=20)
        self.btn_back.config(bg='lightblue')
        
        self.after(3000, self.send_whatsapp_headlessmessage, "916291798504", "I need some water\n")

    def show_apps_menu(self):
        
        self.USE_SECONDARY_FUNCTIONS = False
        self.BUTTON_CLICK = True
        
        self.clear_frames()
        self.apps_frame = tk.Frame(self)
        self.apps_frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.apps_frame, text="Apps Menu", font=("Helvetica", 20))
        self.label.pack(pady=50)

        self.btn_option2_4_1 = tk.Button(self.apps_frame, text="Youtube", font=("Helvetica", 20), command=self.show_youtube)
        self.btn_option2_4_1.pack(pady=20)

        self.btn_option2_4_2 = tk.Button(self.apps_frame, text="Whatsapp", font=("Helvetica", 20), command=self.show_whatsapp)
        self.btn_option2_4_2.pack(pady=20)

        self.btn_option2_4_3 = tk.Button(self.apps_frame, text="Netflix", font=("Helvetica", 20), command=self.show_netflix)
        self.btn_option2_4_3.pack(pady=20)

        self.btn_back = tk.Button(self.apps_frame, text="Back to Menu", font=("Helvetica", 15), command=self.show_option2)
        self.btn_back.pack(pady=20)
        
        self.after(10, self.text_to_speech, "You can control the cursor using your eyes. Look where you want to move\
                   the cursor and blink once to select it. Keep in mind that you must lift your index finger in order to\
                       move the cursor.")


        self.rotate_buttons([self.btn_option2_4_1, self.btn_option2_4_2, self.btn_option2_4_3, self.btn_back])
        
        self.process_frame_for_blinks([self.btn_option2_4_1, self.btn_option2_4_2, self.btn_option2_4_3, self.btn_back])

    def show_youtube(self):
        
        self.text_to_speech("Opening Youtube")
        self.USE_SECONDARY_FUNCTIONS = True
        self.BUTTON_CLICK = False
        
        self.clear_frames()
        self.youtube_frame = tk.Frame(self)
        self.youtube_frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.youtube_frame, text="Youtube", font=("Helvetica", 20))
        self.label.pack(pady=50)

        self.btn_back = tk.Button(self.youtube_frame, text="Back to Apps Menu", font=("Helvetica", 15), command=self.show_apps_menu)
        self.btn_back.pack(pady=20)
        self.btn_back.config(bg='lightblue')
        
        def open_youtube():
            os.system("taskkill /im chrome.exe /f")
            options = Options()
            options.add_argument(CHROME_DATA_PATH)
            options.add_experimental_option("detach", True)

            s = Service(executable_path="chromedriver-win64/chromedriver.exe")
            self.driver = webdriver.Chrome(service=s, options=options)
            self.driver.get("https://www.youtube.com/")
            time.sleep(15)
            
        
        thread = threading.Thread(target=open_youtube)
        thread.start()
        
        self.after(20000, self.use_youtube)
    
    def use_youtube(self):
        
        success, image = self.video_capture.read()
        if not success:
            print("Failed to read frame from camera. Exiting...")
            self.update_configure_label("Cannot Open WhatsApp")
            return
    
        image = cv2.resize(image, (1000, 1000))
        image = cv2.flip(image, 1)
        
        finger_list = self.hand_tracker.get_finger_lmllist(image)
        if len(finger_list) != 0:
            if self.hand_tracker.isIndex(finger_list[1]):
                self.MOUSE_MOTION = True
                print("Index")
            else:
                self.MOUSE_MOTION = False
        
        results, landmarks = self.eye_movements.get_landmarks(image)
        
        if self.MOUSE_MOTION:
            if landmarks:
                if self.eye_movements.eye_left(landmarks[469]):
                    self.mouse.move(-5, 0)
                if self.eye_movements.eye_right(landmarks[469]):
                    self.mouse.move(5, 0)
                if self.eye_movements.eye_up(landmarks[469]):
                    self.mouse.move(0, -5)
                if self.eye_movements.eye_down(landmarks[469]):
                    self.mouse.move(0, 5)
        
        if self.eye_movements.did_Blink(landmarkA=landmarks[160], landmarkB=landmarks[144]):
            self.mouse.click(Button.left, 1)
    
        
        if self.USE_SECONDARY_FUNCTIONS:
            self.after(1, self.use_youtube)

    def show_whatsapp(self):
        
        self.text_to_speech("Opening Whatsapp")
        self.USE_SECONDARY_FUNCTIONS = True
        self.BUTTON_CLICK = False
        
        self.clear_frames()
        self.whatsapp_frame = tk.Frame(self)
        self.whatsapp_frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.whatsapp_frame, text="Whatsapp", font=("Helvetica", 20))
        self.label.pack(pady=50)

        self.btn_back = tk.Button(self.whatsapp_frame, text="Back to Apps Menu", font=("Helvetica", 15), command=self.show_apps_menu)
        self.btn_back.pack(pady=20)
        self.btn_back.config(bg='lightblue')
        
        def open_whatsapp():
            os.system("taskkill /im chrome.exe /f")
            options = Options()
            options.add_argument(CHROME_DATA_PATH)
            options.add_experimental_option("detach", True)

            s = Service(executable_path="chromedriver-win64/chromedriver.exe")
            self.driver = webdriver.Chrome(service=s, options=options)
            self.driver.get("https://web.whatsapp.com/")
            time.sleep(15)
            
            script = """
            document.addEventListener('click', function(event) {
                var clickedElement = event.target;
                var elementInfo = {
                    tag: clickedElement.tagName,
                    id: clickedElement.id,
                    class: clickedElement.className,
                    text: clickedElement.innerText,
                    html: clickedElement.outerHTML
                    };
                window.localStorage.setItem('clickedElementInfo', JSON.stringify(elementInfo));
                }, true);
            """
            
            self.driver.execute_script(script)
        
        thread = threading.Thread(target=open_whatsapp)
        thread.start()
        
        self.after(20000, self.use_whatsapp, self.driver)
        
    
    def use_whatsapp(self, driver):
        
        success, image = self.video_capture.read()
        if not success:
            print("Failed to read frame from camera. Exiting...")
            self.update_configure_label("Cannot Open WhatsApp")
            return
    
        image = cv2.resize(image, (1000, 1000))
        image = cv2.flip(image, 1)
        
        finger_list = self.hand_tracker.get_finger_lmllist(image)
        if len(finger_list) != 0:
            if self.hand_tracker.isIndex(finger_list[1]):
                self.MOUSE_MOTION = True
                print("Index")
            else:
                self.MOUSE_MOTION = False
        
        results, landmarks = self.eye_movements.get_landmarks(image)
        
        if self.MOUSE_MOTION:
            if landmarks:
                if self.eye_movements.eye_left(landmarks[469]):
                    self.mouse.move(-5, 0)
                if self.eye_movements.eye_right(landmarks[469]):
                    self.mouse.move(5, 0)
                if self.eye_movements.eye_up(landmarks[469]):
                    self.mouse.move(0, -5)
                if self.eye_movements.eye_down(landmarks[469]):
                    self.mouse.move(0, 5)
        
        if self.eye_movements.did_Blink(landmarkA=landmarks[160], landmarkB=landmarks[144]):
            self.mouse.click(Button.left, 1)
        
        # clicked_element_info = driver.execute_script("return window.localStorage.getItem('clickedElementInfo');")

        # if clicked_element_info:
        #     element_info = json.loads(clicked_element_info)
            
        #     if "selectable-text copyable-text x15bjb6t x1n2onr6" in element_info["class"]:
        #         if not self.KEYBOARD:
        #             print("Clicked on the specified element!")
        #             keyboard = KeyBoard()
        #             typed_text = keyboard.get_typed_text()  
        #             print("Typed text:", typed_text)
        #             if typed_text != "":
                        
        #                 if "search input class name" in element_info["class"]:
        #                     msgSendKey = driver.find_element(By.CLASS_NAME, "search input class name")
        #                 else:
        #                     msgSendKey = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
     
        #                     msgSendKey.send_keys(typed_text)
        #                     msgSendKey.send_keys(Keys.RETURN)
        #                     print("Typed and sent the message")
        #                     time.sleep(5)
        
        #             self.KEYBOARD = True
            
        #     else:
        #         self.KEYBOARD = False
     
        # # Clear the localStorage entry after processing
        # driver.execute_script("window.localStorage.removeItem('clickedElementInfo');")
     
        # # Short sleep to prevent high CPU usage
        # time.sleep(0.1)
        
        if self.USE_SECONDARY_FUNCTIONS:
            self.after(1, self.use_whatsapp, self.driver)

    def show_netflix(self):
        
        self.USE_SECONDARY_FUNCTIONS = True
        self.BUTTON_CLICK = False
        
        self.clear_frames()
        self.netflix_frame = tk.Frame(self)
        self.netflix_frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.netflix_frame, text="Netflix", font=("Helvetica", 20))
        self.label.pack(pady=50)

        self.btn_back = tk.Button(self.netflix_frame, text="Back to Apps Menu", font=("Helvetica", 15), command=self.show_apps_menu)
        self.btn_back.pack(pady=20)
        self.btn_back.config(bg='lightblue')

    def show_configure(self):
        self.clear_frames()

        self.configure_frame = tk.Frame(self)
        self.configure_frame.pack(fill="both", expand=True)

        self.label = tk.Label(self.configure_frame, text="We will begin configuring", font=("Helvetica", 20))
        self.label.pack(pady=10)
        
        self.video_label = tk.Label(self.configure_frame)
        self.video_label.pack(padx=100, pady=10)
        
        self.eye_process_frame()

    def eye_process_frame(self):
        
        success, image = self.video_capture.read()
        if not success:
            print("Failed to read frame from camera. Exiting...")
            self.update_configure_label("Configuration Failed")
            return
        
        image = cv2.resize(image, (1000, 1000))
        image = cv2.flip(image, 1)

        self.results, self.landmarks = self.eye_configure.get_landmarks(image)

        if self.landmarks:
            if self.eye_configure.eye_open_config:
                cv2.putText(image, "Please Keep Your Eyes Open", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                done = self.eye_configure.configure_eye_open(self.landmarks[160], self.landmarks[144])
                if done:
                    self.after(2000, self.eye_process_frame)
                    return

            elif self.eye_configure.eye_closed_config: 
                cv2.putText(image, "Please Close Your Eyes", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                done = self.eye_configure.configure_eye_closed(self.landmarks[160], self.landmarks[144])
                if done:
                    self.after(2000, self.eye_process_frame)
                    return

            elif self.eye_configure.left_config:
                cv2.putText(image, "Please Follow The Dot", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                cv2.circle(image, (20, int(self.eye_configure.imageheight / 2)), 20, (0, 0, 255), -1)
                done = self.eye_configure.configure_eye_left(self.landmarks[468])
                if done:
                    self.after(20, self.eye_process_frame)
                    return

            elif self.eye_configure.right_config:
                cv2.putText(image, "Please Follow The Dot", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                cv2.circle(image, (int(self.eye_configure.imagewidth - 20), int(self.eye_configure.imageheight / 2)), 20, (0, 0, 255), -1)
                done = self.eye_configure.configure_eye_right(self.landmarks[468])
                if done:
                    self.after(20, self.eye_process_frame)
                    return

            elif self.eye_configure.up_config:
                cv2.putText(image, "Please Follow The Dot", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                cv2.circle(image, (int(self.eye_configure.imagewidth / 2), 20), 20, (0, 0, 255), -1)
                done = self.eye_configure.configure_eye_up(self.landmarks[468])
                if done:
                    self.after(20, self.eye_process_frame)
                    return

            elif self.eye_configure.down_config:
                cv2.putText(image, "Please Follow The Dot", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                cv2.circle(image, (int(self.eye_configure.imagewidth / 2), int(self.eye_configure.imageheight - 20)), 20, (0, 0, 255), -1)
                done = self.eye_configure.configure_eye_down(self.landmarks[468])
                if done:
                    self.after(20, self.eye_process_frame)
                    return

            else:
                self.eye_movements = pm.ParalysisMovements(eye_closed= self.eye_configure.eye_closed, 
                                                           eye_open= self.eye_configure.eye_open,
                                                           eye_left_threshold= self.eye_configure.left,
                                                           eye_right_threshold= self.eye_configure.right,
                                                           eye_up_threshold= self.eye_configure.up,
                                                           eye_down_threshold= self.eye_configure.down)
                print(self.eye_configure.eye_closed, self.eye_configure.eye_open)
                self.label.config(text="Configuring Hands")
                self.after(1000, self.text_to_speech("Now we will be configuring your hands. Please keep the hands on the table so that they are visible."))
                self.after(2000, self.hand_process_frame)
                return

        # Convert the image to RGB and then to PIL format for Tkinter
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        # Update the label with the new image
        self.video_label.config(image=image)
        self.video_label.image = image

        # Continue processing the next frame
        self.after(10, self.eye_process_frame)
    
    def hand_process_frame(self):
        success, image = self.video_capture.read()
        if not success:
            print("Failed to read frame from camera. Exiting...")
            self.update_configure_label("Configuration Failed")
            return
        
        image = cv2.resize(image, (1000, 1000))
        image = cv2.flip(image, 1)
        
        self.lml_list = self.hand_tracker.get_finger_lmllist(image)
        
        if len(self.lml_list) != 0:
            image = self.hand_tracker.drawHands(image, self.lml_list)
            if not self.hand_tracker.leftHand_config:
                image = self.hand_tracker.left_hand_configure(self.lml_list, image)
            else:
                self.update_configure_label("Configuration Done")
                
                self.after(2000, self.show_menu)
                return
            
        # Convert the image to RGB and then to PIL format for Tkinter
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)
    
        # Update the label with the new image
        self.video_label.config(image=image)
        self.video_label.image = image
    
        # Continue processing the next frame
        self.after(10, self.hand_process_frame)
        

    def update_configure_label(self, new_text):
        for widget in self.configure_frame.winfo_children():
            widget.destroy()
        self.label = tk.Label(self.configure_frame, text=new_text, font=("Helvetica", 30))
        self.label.pack(pady=200)

    def go_back(self, current_frame, back_function):
        if self.transition_id is not None:
            self.after_cancel(self.transition_id)
            self.transition_id = None
        if self.rotation_id is not None:
            self.after_cancel(self.rotation_id)
            self.rotation_id = None
        current_frame.destroy()
        back_function()

    def clear_frames(self):
        for widget in self.winfo_children():
            widget.destroy()

    def rotate_buttons(self, buttons):
        if hasattr(self, 'current_button'):
            current_index = self.current_button
        else:
            current_index = -1

        next_index = (current_index + 1) % len(buttons)
        self.current_button = next_index

        for i, btn in enumerate(buttons):
            if i == next_index:
                btn.config(bg="lightblue", state="normal")
            else:
                btn.config(bg='white', state="disabled")

        self.rotation_id = self.after(2000, lambda: self.rotate_buttons(buttons))

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
```

#### HandTappingModule.py

```
import cv2
from ultralytics import YOLO
import supervision as sv
import time

class HandTappingModule():
    
    def __init__(self):  
        self.model = YOLO("best.pt")
        self.start_time = 0
        self.tapCount = 0
        self.handLiftedFlag = False
        
    
    def make_prediction(self, image): 
        className = "No Detection"
        results = self.model.predict(source=image, conf=0.5)[0]
        detections = sv.Detections.from_ultralytics(results)
        
        for _, _, _, classID, _, _ in detections:
            className =self. model.model.names[classID]
            
        return className
    
        
    def detectHandLifted(self, classId):
        if classId == "HandLifted":
            return True
        else:
            return False
        
    def detectHandFlat(self, classId):
        if classId == "FlatHand":
            return True
        else:
            return False
        
    def detectTap(self, classId):
        
        temp_tapCount = None
        
        if self.start_time == 0:
           self.start_time = time.time()
           
        cTime = time.time()
        elapsed_time = cTime - self.start_time
        
        if elapsed_time >= 10:
           self.start_time = 0
           temp_tapCount = self.tapCount
           self.tapCount = 0
           return temp_tapCount
           
        if self.detectHandLifted(classId):
           self.handLiftedFlag = True
        
        if self.handLiftedFlag:
            if self.detectHandFlat(classId):
                self.tapCount += 1;
                self.handLiftedFlag = False
        
        return temp_tapCount
    
    
        
def main():
    
    cap = cv2.VideoCapture(0)
    
    
    hand_tap_tracker = HandTappingModule()
    
    box_annotator = sv.BoxAnnotator(thickness = 2,
                                    text_thickness = 3,
                                    text_scale = 1)
    
    finaltapCount = 0
    
    while True:
        
        className = "NoDetection"
        success, frame = cap.read()
        
        
        results = hand_tap_tracker.model.predict(source=frame, conf=0.5)[0]
        
        # Convert the YOLOv8 results into supervision detections
        detections = sv.Detections.from_ultralytics(results)
        
        # print(detections)
        labels = [
            f"{hand_tap_tracker.model.model.names[classid]} {confidence:0.2f}"
            for _, _, confidence, classid, _, _ # Unpacking detections
            in detections
            ]
        
        
        frame = box_annotator.annotate(frame, detections, labels)
        
        for _, _, _, classID, _, _ in detections:
            className = hand_tap_tracker.model.model.names[classID]
            
            
        tapCount = hand_tap_tracker.detectTap(className)
        
        if tapCount != None:
            finaltapCount = tapCount
        
        # print(frame.shape)
        # frame.shape = (480, 640)
        
        cv2.putText(frame, f"TapCount: {finaltapCount}", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
        cv2.imshow("yolov8", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    
    
    
if __name__ == "__main__":
    main()
```

#### HandTrackingModule.py

```
import cv2
import mediapipe as mp
import numpy as np
import EuroFIlter as ef
import time

class HandDetector():
    def __init__(self, mode = False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5): # The parameters are the basic parameters that are required for the hands
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)        
        self.mpDraw = mp.solutions.drawing_utils 
        
        self.handLifted = float('-inf')
        self.leftIndex = float('-inf')
        self.leftThumb = float('-inf')
        self.leftMiddle = float('-inf')
        self.leftRing = float('-inf')
        self.leftPinky = float('-inf')
        
        self.leftThumb_config = True
        self.leftIndex_config = False
        self.leftMiddle_config = False
        self.leftRing_config = False
        self.leftPinky_config = False
        self.leftHand_config = False
        self.isHands_stable = False
        
        self.iterations = 0
        
        self.stability_buffer_size = 30  # Number of frames to check for stability
        self.stability_threshold = 100  # Threshold for the variance to consider the hand stable
        self.stability_buffer = {i: [] for i in range(5)}  # Buffer to store positions for each finger
        
        self.eurofilter_x = ef.OneEuroFilter()
        self.eurofilter_y = ef.OneEuroFilter()

    # Detection Part
    def findHands(self, img, draw = True): 
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks: 
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS) 
        
        return img

                   

    # Method to Find the List of Positions Values for the Landmarks

    def findPosition(self, img, handNo = 0, draw = True): 

        lml_List = []
        self.imageheight, self.imagewidth, self.imagechannels = img.shape

        if self.results.multi_hand_landmarks:

            my_hand = self.results.multi_hand_landmarks[handNo] 


            for id, ln in enumerate(my_hand.landmark): 

                h, w, c = img.shape
                cx, cy = int(ln.x * w), int(ln.y * h) 
                lml_List.append([id, cx, cy])

        return lml_List
    
    # Function to get finger landmarks
    def get_finger_lmllist(self, img, handNo = 0, draw = True):
        
        lml_list = []
        
        self.imageheight, self.imagewidth, self.imagechannels = img.shape
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:

            my_hand = self.results.multi_hand_landmarks[handNo]
            
            for id, ln in enumerate(my_hand.landmark):
                
                if id == 4 or id == 8 or id == 12 or id ==16 or id == 20:
                    lml_list.append(ln)
        
        return lml_list
    
    # Function To draw the Tip of fingers
    def drawHands(self, img, lml_list):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # imgRGB = img
        
        for i in range(len(lml_list)):
            cv2.circle(imgRGB, (int(lml_list[i].x * self.imagewidth), int(lml_list[i].y * self.imageheight)), radius=10, color=(0, 0, 255), thickness=-1)
        
        return imgRGB
        
    def is_hand_stable(self):
         for finger, buffer in self.stability_buffer.items():
             if len(buffer) < self.stability_buffer_size:
                 return False
             variance = np.var(buffer, axis=0)
             if variance[0] > self.stability_threshold or variance[1] > self.stability_threshold:
                 return False
         self.isHands_stable = True
         return True
 
    def update_stability_buffer(self, lml_list):
         for i, landmark in enumerate(lml_list):
             if len(self.stability_buffer[i]) >= self.stability_buffer_size:
                 self.stability_buffer[i].pop(0)
             self.stability_buffer[i].append([int(landmark.x * self.imagewidth), int(landmark.y * self.imageheight)])
 
    def left_hand_configure(self, lml_list, img):
        
        # Setting the Hand Correctly
         self.update_stability_buffer(lml_list)
         
         if not self.isHands_stable:
             if not self.is_hand_stable():
                 cv2.putText(img, "Please keep your hand steady", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
                 return img
         
         # Assuming lml_list = [Thumb, Index, Middle, Ring, Pinky]
        
        # Initializing the filter
         
         # Configuring Thumb
         if self.leftThumb_config:
             self.iterations += 1  # Increment iterations
             landmark = np.array([int(lml_list[0].x * self.imagewidth), int(lml_list[0].y * self.imageheight)])
             cv2.putText(img, "Please Lift Your Thumb", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
             
             cTime = time.time()
             landmark[0] = self.eurofilter_x.apply_filter(landmark[0], cTime)
             landmark[1] = self.eurofilter_y.apply_filter(landmark[1], cTime)
             
             if self.iterations > 70:
                 if landmark[1] > self.leftThumb:
                     self.leftThumb = landmark[1]
                 
             if self.iterations >= 100:
                 self.iterations = 0
                 self.leftThumb_config = False
                 self.leftIndex_config = True
                 self.eurofilter_x = ef.OneEuroFilter()
                 self.eurofilter_y = ef.OneEuroFilter()
                 return img
             return img
         
         # Configuring Index
         if self.leftIndex_config:
             self.iterations += 1  # Increment iterations
             landmark = np.array([int(lml_list[1].x * self.imagewidth), int(lml_list[1].y * self.imageheight)])
             cv2.putText(img, "Please Lift Your Index Finger", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
             
             cTime = time.time()
             landmark[0] = self.eurofilter_x.apply_filter(landmark[0], cTime)
             landmark[1] = self.eurofilter_y.apply_filter(landmark[1], cTime)
             
             if self.iterations > 70:
                 if landmark[1] > self.leftIndex:
                     self.leftIndex = landmark[1]
                 
             if self.iterations >= 100:
                 self.iterations = 0
                 self.leftIndex_config = False
                 self.leftMiddle_config = True
                 self.eurofilter_x = ef.OneEuroFilter()
                 self.eurofilter_y = ef.OneEuroFilter()
                 return img
             return img
         
         # Configuring Middle
         if self.leftMiddle_config:
             self.iterations += 1  # Increment iterations
             landmark = np.array([int(lml_list[2].x * self.imagewidth), int(lml_list[2].y * self.imageheight)])
             cv2.putText(img, "Please Lift Your Middle Finger", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
             
             cTime = time.time()
             landmark[0] = self.eurofilter_x.apply_filter(landmark[0], cTime)
             landmark[1] = self.eurofilter_y.apply_filter(landmark[1], cTime)
             
             if self.iterations > 70:
                 if landmark[1] > self.leftMiddle:
                     self.leftMiddle = landmark[1]
                 
             if self.iterations >= 100:
                 self.iterations = 0
                 self.leftMiddle_config = False
                 self.leftRing_config = True
                 self.eurofilter_x = ef.OneEuroFilter()
                 self.eurofilter_y = ef.OneEuroFilter()
                 return img
             return img
         
         # Configuring Ring
         if self.leftRing_config:
             self.iterations += 1  # Increment iterations
             landmark = np.array([int(lml_list[3].x * self.imagewidth), int(lml_list[3].y * self.imageheight)])
             cv2.putText(img, "Please Lift Your Ring Finger", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
             
             cTime = time.time()
             landmark[0] = self.eurofilter_x.apply_filter(landmark[0], cTime)
             landmark[1] = self.eurofilter_y.apply_filter(landmark[1], cTime)
             
             if self.iterations > 70:
                 if landmark[1] > self.leftRing:
                     self.leftRing = landmark[1]
                 
             if self.iterations >= 100:
                 self.iterations = 0
                 self.leftRing_config = False
                 self.leftPinky_config = True
                 self.eurofilter_x = ef.OneEuroFilter()
                 self.eurofilter_y = ef.OneEuroFilter()
                 return img
             return img
         
         # Configuring Pinky
         if self.leftPinky_config:
             self.iterations += 1  # Increment iterations
             landmark = np.array([int(lml_list[4].x * self.imagewidth), int(lml_list[4].y * self.imageheight)])
             cv2.putText(img, "Please Lift Your Pinky Finger", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
             
             cTime = time.time()
             landmark[0] = self.eurofilter_x.apply_filter(landmark[0], cTime)
             landmark[1] = self.eurofilter_y.apply_filter(landmark[1], cTime)
             
             if self.iterations > 70:
                 if landmark[1] > self.leftPinky:
                     self.leftPinky = landmark[1]
                 
             if self.iterations >= 100:
                 self.iterations = 0
                 self.leftPinky_config = False
                 self.leftHand_config = True
                 self.eurofilter_x = ef.OneEuroFilter()
                 self.eurofilter_y = ef.OneEuroFilter()
                 return img
             return img
    
    
    def isIndex(self, landmarkA):
        
        landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y < self.leftIndex:
            return True
        else:
            return False 
        
    def isThumb(self, landmarkA):
        
        landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y < self.leftThumb:
            return True
        else:
            return False 
        
    def isMiddle(self, landmarkA):
        
        landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y < self.leftMiddle:
            return True
        else:
            return False 
        
    def isRing(self, landmarkA):
        
        landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y < self.leftRing:
            return True
        else:
            return False 
    
    def isPinky(self, landmarkA):
        
        landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y < self.leftPinky:
            return True
        else:
            return False
        
def main():
    
    cap = cv2.VideoCapture(0)
    hand_motion_detector = HandDetector()
    
    index_taps = 0
    start_timer = 0
    index_flag = 0
    final_no_of_taps = 0
    
    while True:
        
        success, img = cap.read()
        finger_list = hand_motion_detector.get_finger_lmllist(img)
        if len(finger_list) != 0:
            img = hand_motion_detector.drawHands(img, finger_list)
            if not hand_motion_detector.leftHand_config:
                img = hand_motion_detector.left_hand_configure(finger_list, img)
        
        
        # if hand_motion_detector.leftHand_config == True:
        #     break
        
        cv2.imshow("IMAGE", img)
        cv2.waitKey(1)
        
    
    while True:
        
        success, img = cap.read()
        finger_list = hand_motion_detector.get_finger_lmllist(img)
        
        
        cv2.putText(img, f"Index_taps = {index_taps}", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
        cv2.putText(img, f"Final_Index_taps = {final_no_of_taps}", (20, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

        if hand_motion_detector.isIndex(finger_list[1]):
            index_flag = 1
            if start_timer == 0:
                start_timer = time.time()
            
        else:
            if index_flag == 1:
                index_taps += 1
                index_flag = 0
        
        cTime = time.time()
        elapsed_time = cTime - start_timer
        if elapsed_time > 10:
            start_timer = 0
            if index_taps != 0:
                final_no_of_taps = index_taps
            index_taps = 0
    
            
                
        
        cv2.imshow("ANNOTATED IMAGE", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
        
if __name__ == "__main__":
    main()    
```

#### Keyboard.py

```
from tkinter import *

class KeyBoard:
    def __init__(self):
            self.root = Tk()
            self.root.title("Keyboard GUI")
            
            # Creating the input text
            self.text_var = StringVar()
            self.e = Entry(self.root, textvariable=self.text_var, width=50, font=('Helvetica', 16))
            self.e.grid(row=0, column=0, columnspan=11)
            self.cursorValue = 0  # Keeps track of the cursor position
            
            # Defining the buttons
            buttons = [
                ('Q', 1, 0), ('W', 1, 1), ('E', 1, 2), ('R', 1, 3), ('T', 1, 4), ('Y', 1, 5), ('U', 1, 6), ('I', 1, 7), ('O', 1, 8), ('P', 1, 9),
                ('A', 2, 0), ('S', 2, 1), ('D', 2, 2), ('F', 2, 3), ('G', 2, 4), ('H', 2, 5), ('J', 2, 6), ('K', 2, 7), ('L', 2, 8), ('Enter', 2, 9),
                ('Z', 3, 0), ('X', 3, 1), ('C', 3, 2), ('V', 3, 3), ('Space', 3, 4), ('B', 3, 6), ('N', 3, 7), ('M', 3, 8), (',', 3, 9), ('.', 3, 10)
            ]
            
            self.buttons = {}
            for (text, row, col) in buttons:
                self.buttons[text] = Button(self.root, text=text, padx=20, pady=20, command=lambda t=text: self.buttonClick(t), font=('Helvetica', 16))
                self.buttons[text].grid(row=row, column=col, sticky="ew" if text == "Space" else "")

            # Main Loop
            self.root.mainloop()
        
    def buttonClick(self, character):
        if character == "Enter":
            self.root.destroy()  # Close the GUI
        elif character == "Space":
            self.e.insert(self.cursorValue, " ")
            self.cursorValue += 1
        else:
            self.e.insert(self.cursorValue, character)
            self.cursorValue += 1
    
    def get_typed_text(self):
        return self.text_var.get()

    # Function to disable the buttons
    def disableRow1(self):
        for char in 'QWERTYUIOP':
            self.buttons[char].config(state=DISABLED, fg="black", bg="white")
        
    def disableRow2(self):
        for char in 'ASDFGHJKL':
            self.buttons[char].config(state=DISABLED, fg="black", bg="white")
        self.buttons["Enter"].config(state=DISABLED, fg="black", bg="white")
    
    def disableRow3(self):
        for char in 'ZXCVBNM,. ':
            self.buttons[char].config(state=DISABLED, fg="black", bg="white")
        self.buttons["Space"].config(state=DISABLED, fg="black", bg="white")
        
    # Function to Enable all the Rows
    def enableRow1(self):
        for char in 'QWERTYUIOP':
            self.buttons[char].config(state=NORMAL, fg="white", bg="black")
        
    def enableRow2(self):
        for char in 'ASDFGHJKL':
            self.buttons[char].config(state=NORMAL, fg="white", bg="black")
        self.buttons["Enter"].config(state=NORMAL, fg="white", bg="black")
    
    def enableRow3(self):
        for char in 'ZXCVBNM,. ':
            self.buttons[char].config(state=NORMAL, fg="white", bg="black")
        self.buttons["Space"].config(state=NORMAL, fg="white", bg="black")
    
    def start_timer(self):
        self.enableRow1()
        self.disableRow2()
        self.disableRow3()
        
        self.root.after(3000, self.switch_to_row2)  # Switch to Row 2 after 3 seconds
    
    def switch_to_row2(self):
        self.disableRow1()
        self.enableRow2()
        self.disableRow3()
        
        self.root.after(3000, self.switch_to_row3)  # Switch to Row 3 after 3 seconds
    
    def switch_to_row3(self):
        self.disableRow1()
        self.disableRow2()
        self.enableRow3()
        
        self.root.after(3000, self.start_timer)  # Switch back to Row 1 after 3 seconds
        
    def simulate_button_click(self, character):
        self.buttonClick(character)

# # Example usage
# k = KeyBoard()
# print(k.get_typed_text())
```

#### ParalysisMovements.py

```
import cv2
import mediapipe as mp
import numpy as np
import time

def calc_distance(landmarkA, landmarkB, image):
    
    imageheight, imagewidth, imagechannels = image.shape
    
    landmarkA = np.array([int(landmarkA.x * imagewidth), int(landmarkA.y * imageheight)])
    landmarkB = np.array([int(landmarkB.x * imagewidth), int(landmarkB.y * imageheight)])
    
    distance = int(np.linalg.norm(landmarkA - landmarkB))
    
    return distance

class ParalysisMovements():
    
    def __init__(self, eye_closed, eye_open, eye_left_threshold, eye_right_threshold, eye_up_threshold, eye_down_threshold):
        
        self.eye_closed = eye_closed
        self.eye_open = eye_open
        self.eye_down_threshold = eye_down_threshold
        self.eye_up_threshold = eye_up_threshold
        self.eye_left_threshold = eye_left_threshold
        self.eye_right_threshold = eye_right_threshold
        
        self.mp_drawing = mp.solutions.download_utils
        self.mp_face_mesh = mp.solutions.face_mesh
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        self.face_mesh = self.mp_face_mesh.FaceMesh(static_image_mode = True, max_num_faces = 1, 
                                                    refine_landmarks = True, min_detection_confidence = 0.5,
                                                    min_tracking_confidence = 0.5)
        
        self.blink_timer = 0
        self.closed_flag = False
        
    
    def get_landmarks(self, image):
        
        
        
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        results = self.face_mesh.process(imageRGB)
        
        self.imageheight, self.imagewidth, self.imagechannels = image.shape
        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
        else:
            landmarks = []
            
        return results, landmarks
    
    def did_close_eyes(self, landmarkA, landmarkB):
         
         landmarkA = np.array([int(landmarkA.x * self.imagewidth), int(landmarkA.y * self.imageheight)])
         landmarkB = np.array([int(landmarkB.x * self.imagewidth), int(landmarkB.y * self.imageheight)])
         
         distance = int(np.linalg.norm(landmarkA - landmarkB))
         
         if distance < self.eye_open[0]:
             if self.blink_timer == 0:
                 self.blink_timer = time.time()
                 
             else:
                 current_time = time.time()
                 elapsed_time = current_time - self.blink_timer
                 
                 if elapsed_time >= 1:
                     self.closed_flag = True
                     return True
                 else:
                     self.closed_flag = False
                     return False
         # else:
             # self.blink_timer = 0  # Reset blink timer if eyes are not closed
         return False
     
        
    def did_open_eyes(self, landmarkA, landmarkB):
        
        landmarkA = np.array([int(landmarkA.x * self.imagewidth), int(landmarkA.y * self.imageheight)])
        landmarkB = np.array([int(landmarkB.x * self.imagewidth), int(landmarkB.y * self.imageheight)])
        
        distance = int(np.linalg.norm(landmarkA - landmarkB))
        
        if distance > self.eye_closed[1]:
            return True
        
        return False
     
    def did_Blink(self, landmarkA, landmarkB):
         
        if not self.closed_flag:
            self.did_close_eyes(landmarkA, landmarkB)
        if self.closed_flag:
            x = self.did_open_eyes(landmarkA, landmarkB)
            if x == True:
                self.closed_flag = False
                self.blink_timer = 0
                return True
            
        return False
    
    def eye_left(self, landmarkA):
        
        landmarkA.x = int(landmarkA.x * self.imagewidth)
        if landmarkA.x < self.eye_left_threshold:
            return True
        else:
            return False
        
    def eye_right(self, landmarkA):
        
        # landmarkA.x = int(landmarkA.x * self.imagewidth)
        if landmarkA.x > self.eye_right_threshold:
            return True
        else:
            return False
    
    def eye_up(self, landmarkA):
        
        landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y < self.eye_up_threshold:
            return True
        else:
            return False  
        
    def eye_down(self, landmarkA):
        
        # landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y > self.eye_down_threshold:
            return True
        else:
            return False 
    
    

def main():
    
    cap = cv2.VideoCapture(0)
    
    pm = ParalysisMovements([6, 7], [8, 10], 388, 413, 478, 509)
    
    pTime = 0
    
    blinkCount = 0
    
    
    while True:
        
        
        success, img = cap.read()
        
        if not success:
            print("Failed to read frame from camera. Exiting...")
            break
        
        cv2.putText(img, f'BlinkCount: {int(blinkCount)}', (1, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
        
        results, landmarks = pm.get_landmarks(img)
        
        
        if landmarks:
            
            distance = calc_distance(landmarks[160], landmarks[144], img)
            cv2.putText(img, f'EyeDistance: {int(distance)}', (1, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
            
            
            if pm.did_Blink(landmarks[160], landmarks[144]):
                blinkCount += 1
            
                
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            
            cv2.putText(img, f'FPS: {int(fps)}', (1, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)
            pTime = cTime
            
            
            
            cv2.imshow("ANNOTATED IMAGE", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        

        
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
    
```
## ***Working 2 - ( doesn't require a computer for usage but requires a computer for configuration)***

- In this method, we have a python code that runs on the Raspberry Pi Zero 2 W that first configures the code to track the movement of a hand and detect taps.

- We need a computer to visualize the configuration.

- Configuration Step:

	- First, keep your hand steady.
	- Then, lift your Thumb.
	- Then, lift your Index Finger.
	- Then, lift your Middle Finger.
	- Then, lift your Ring Finger.
	- Then, lift your Pinky Finger
	- Now, Configuration Step is completed. You can disconnect the computer and your device is ready to communicate.
	
- Communication Step:

	- The message sent from the device to the speaker/headset depends on the number of taps of hand
	
		- One tap doesn't mean anything as sometimes the patient may tap accidently.

		- Two taps convey the message "Food"

		- Three taps convey the message "Emergency"

		- Four taps convey the message "Water"

		- Five taps convey the message "Turn Off the Light"

		- Six taps convey the message "Help"
		
	- The message can also be accessed on any device connected to the same Wi-Fi network as the Raspberry Pi Zero 2 W by accessing the following link: http://<raspberry_pi_ip_address>:5000 , where the raspberry_pi_ip_address refers to the IP Address of the Raspberry Pi Zero 2 W.
	
### ***Code for Working2***

#### rasp.py

```
from picamera2 import Picamera2, Preview
import cv2
import mediapipe as mp
import numpy as np
import EuroFIlter as ef
import time
from flask import Flask, jsonify
from threading import Thread
from flask import Flask, jsonify, render_template_string
import pyttsx4

def text_to_speech(text):
    if text == 'Nothing':
        return
    # Initialize the TTS engine
    engine = pyttsx4.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed (words per minute)
    engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

class HandDetector():
    def __init__(self, mode=False, maxHands=1, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)        
        self.mpDraw = mp.solutions.drawing_utils 
        
        self.handLifted = float('-inf')
        self.leftIndex = float('-inf')
        self.leftThumb = float('-inf')
        self.leftMiddle = float('-inf')
        self.leftRing = float('-inf')
        self.leftPinky = float('-inf')
        
        self.leftThumb_config = True
        self.leftIndex_config = False
        self.leftMiddle_config = False
        self.leftRing_config = False
        self.leftPinky_config = False
        self.leftHand_config = False
        self.isHands_stable = False
        
        self.iterations = 0
        
        self.stability_buffer_size = 30
        self.stability_threshold = 100
        self.stability_buffer = {i: [] for i in range(5)}
        
        self.eurofilter_x = ef.OneEuroFilter()
        self.eurofilter_y = ef.OneEuroFilter()

    def findHands(self, img, draw=True): 
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks: 
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS) 
        
        return img

    def findPosition(self, img, handNo=0, draw=True): 
        lml_List = []
        self.imageheight, self.imagewidth, self.imagechannels = img.shape

        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[handNo] 
            for id, ln in enumerate(my_hand.landmark): 
                h, w, c = img.shape
                cx, cy = int(ln.x * w), int(ln.y * h) 
                lml_List.append([id, cx, cy])

        return lml_List
    
    def get_finger_lmllist(self, img, handNo=0, draw=True):
        lml_list = []
        self.imageheight, self.imagewidth, self.imagechannels = img.shape
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[handNo]
            for id, ln in enumerate(my_hand.landmark):
                if id == 4 or id == 8 or id == 12 or id == 16 or id == 20:
                    lml_list.append(ln)
        
        return lml_list
    
    def drawHands(self, img, lml_list):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        for i in range(len(lml_list)):
            cv2.circle(imgRGB, (int(lml_list[i].x * self.imagewidth), int(lml_list[i].y * self.imageheight)), radius=15, color=(0, 0, 255))
        return imgRGB
        
    def is_hand_stable(self):
        for finger, buffer in self.stability_buffer.items():
            if len(buffer) < self.stability_buffer_size:
                return False
            variance = np.var(buffer, axis=0)
            if variance[0] > self.stability_threshold or variance[1] > self.stability_threshold:
                return False
        self.isHands_stable = True
        return True

    def update_stability_buffer(self, lml_list):
        for i, landmark in enumerate(lml_list):
            if len(self.stability_buffer[i]) >= self.stability_buffer_size:
                self.stability_buffer[i].pop(0)
            self.stability_buffer[i].append([int(landmark.x * self.imagewidth), int(landmark.y * self.imageheight)])

    def left_hand_configure(self, lml_list, img):
        self.update_stability_buffer(lml_list)
        
        if not self.isHands_stable:
            if not self.is_hand_stable():
                cv2.putText(img, "Please keep your hand steady", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
                #text_to_speech('Please keep your hand steady')
                return img
        
        # Assuming lml_list = [Thumb, Index, Middle, Ring, Pinky]

        # Configuring Thumb
        if self.leftThumb_config:
            self.iterations += 1
            landmark = np.array([int(lml_list[0].x * self.imagewidth), int(lml_list[0].y * self.imageheight)])
            #text_to_speech('Please Lift Your Thumb')
            cv2.putText(img, "Please Lift Your Thumb", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
            
            cTime = time.time()
            landmark[0] = self.eurofilter_x.apply_filter(landmark[0], cTime)
            landmark[1] = self.eurofilter_y.apply_filter(landmark[1], cTime)
            
            if self.iterations > 70:
                if landmark[1] > self.leftThumb:
                    self.leftThumb = landmark[1]
                
            if self.iterations >= 100:
                self.iterations = 0
                self.leftThumb_config = False
                self.leftIndex_config = True
                self.eurofilter_x = ef.OneEuroFilter()
                self.eurofilter_y = ef.OneEuroFilter()
                return img
            return img
        
        # Configuring Index
        if self.leftIndex_config:
            self.iterations += 1
            landmark = np.array([int(lml_list[1].x * self.imagewidth), int(lml_list[1].y * self.imageheight)])
            #text_to_speech('Please Lift Your Index Finger')
            cv2.putText(img, "Please Lift Your Index Finger", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
            
            cTime = time.time()
            landmark[0] = self.eurofilter_x.apply_filter(landmark[0], cTime)
            landmark[1] = self.eurofilter_y.apply_filter(landmark[1], cTime)
            
            if self.iterations > 70:
                if landmark[1] > self.leftIndex:
                    self.leftIndex = landmark[1]
                
            if self.iterations >= 100:
                self.iterations = 0
                self.leftIndex_config = False
                self.leftMiddle_config = True
                self.eurofilter_x = ef.OneEuroFilter()
                self.eurofilter_y = ef.OneEuroFilter()
                return img
            return img
        
        # Configuring Middle
        if self.leftMiddle_config:
            self.iterations += 1
            landmark = np.array([int(lml_list[2].x * self.imagewidth), int(lml_list[2].y * self.imageheight)])
            #text_to_speech('Please Lift Your Middle Finger')
            cv2.putText(img, "Please Lift Your Middle Finger", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
            
            cTime = time.time()
            landmark[0] = self.eurofilter_x.apply_filter(landmark[0], cTime)
            landmark[1] = self.eurofilter_y.apply_filter(landmark[1], cTime)
            
            if self.iterations > 70:
                if landmark[1] > self.leftMiddle:
                    self.leftMiddle = landmark[1]
                
            if self.iterations >= 100:
                self.iterations = 0
                self.leftMiddle_config = False
                self.leftRing_config = True
                self.eurofilter_x = ef.OneEuroFilter()
                self.eurofilter_y = ef.OneEuroFilter()
                return img
            return img
        
        # Configuring Ring
        if self.leftRing_config:
            self.iterations += 1
            landmark = np.array([int(lml_list[3].x * self.imagewidth), int(lml_list[3].y * self.imageheight)])
            #text_to_speech('Please Lift Your Ring Finger')
            cv2.putText(img, "Please Lift Your Ring Finger", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
            
            cTime = time.time()
            landmark[0] = self.eurofilter_x.apply_filter(landmark[0], cTime)
            landmark[1] = self.eurofilter_y.apply_filter(landmark[1], cTime)
            
            if self.iterations > 70:
                if landmark[1] > self.leftRing:
                    self.leftRing = landmark[1]
                
            if self.iterations >= 100:
                self.iterations = 0
                self.leftRing_config = False
                self.leftPinky_config = True
                self.eurofilter_x = ef.OneEuroFilter()
                self.eurofilter_y = ef.OneEuroFilter()
                return img
            return img
        
        # Configuring Pinky
        if self.leftPinky_config:
            self.iterations += 1
            landmark = np.array([int(lml_list[4].x * self.imagewidth), int(lml_list[4].y * self.imageheight)])
           # text_to_speech('Please Lift Your Pinky Finger')
            cv2.putText(img, "Please Lift Your Pinky Finger", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
            
            cTime = time.time()
            landmark[0] = self.eurofilter_x.apply_filter(landmark[0], cTime)
            landmark[1] = self.eurofilter_y.apply_filter(landmark[1], cTime)
            
            if self.iterations > 70:
                if landmark[1] > self.leftPinky:
                    self.leftPinky = landmark[1]
                
            if self.iterations >= 100:
                self.iterations = 0
                self.leftPinky_config = False
                self.leftHand_config = True
                self.eurofilter_x = ef.OneEuroFilter()
                self.eurofilter_y = ef.OneEuroFilter()
                return img
            return img

    def isIndex(self, landmarkA):
        landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y < self.leftIndex:
            return True
        else:
            return False 
        
    def isThumb(self, landmarkA):
        landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y < self.leftThumb:
            return True
        else:
            return False 
        
    def isMiddle(self, landmarkA):
        landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y < self.leftMiddle:
            return True
        else:
            return False 
        
    def isRing(self, landmarkA):
        landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y < self.leftRing:
            return True
        else:
            return False 
    
    def isPinky(self, landmarkA):
        landmarkA.y = int(landmarkA.y * self.imageheight)
        if landmarkA.y < self.leftPinky:
            return True
        else:
            return False

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    global final_no_of_taps, command
    return jsonify(taps=final_no_of_taps, command=command)

@app.route('/', methods=['GET'])
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hand Gesture Data</title>
        <script type="text/javascript">
            function fetchData() {
                fetch('/data')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('command').innerText = data.command;
                });
            }
            setInterval(fetchData, 5000);
            window.onload = fetchData;
        </script>
    </head>
    <body>
        <h1>Hand Gesture Data</h1>

        <p style="font-size: 40px">Command: <span id="command" style="font-size: 40px;">Loading...</span></p>
    </body>
    </html>
    ''')

def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
def main():
    global final_no_of_taps, command

    # Initialize picamera2
    picam2 = Picamera2()
    picam2.start_preview(Preview.NULL)
    picam2.configure(picam2.create_preview_configuration(main={'size':(480,320)}))
    picam2.start()

    hand_motion_detector = HandDetector()

    index_taps = 0
    start_timer = 0
    index_flag = 0
    final_no_of_taps = 0
    command = ""

    # Command-taps mapping
    command_taps_mapping = {0 : 'Nothing', 1: "Food", 2: "Emergency", 3: "Water", 4: 'Turn off Light', 5: 'Help', 6: 'Play Music'}

    # Start Flask app in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.start()

    try:
        while True:
            # Capture image using picamera2
            img = picam2.capture_array()

            finger_list = hand_motion_detector.get_finger_lmllist(img)
            img = hand_motion_detector.left_hand_configure(finger_list, img)

            if hand_motion_detector.leftHand_config:
                break
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow("IMAGE", img)
            cv2.waitKey(1)

        while True:
            # Capture image using picamera2
            img = picam2.capture_array()
            finger_list = hand_motion_detector.get_finger_lmllist(img)

            cv2.putText(img, f"Index_taps = {index_taps}", (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

            if len(finger_list) >= 5:
                if (hand_motion_detector.isIndex(finger_list[1]) or 
                    hand_motion_detector.isMiddle(finger_list[2]) or 
                    hand_motion_detector.isRing(finger_list[3]) or 
                    hand_motion_detector.isPinky(finger_list[4])):
                    index_flag = 1
                    if start_timer == 0:
                        start_timer = time.time()
                else:
                    if index_flag == 1:
                        index_taps += 1
                        index_flag = 0

            cTime = time.time()
            elapsed_time = cTime - start_timer
            if elapsed_time > 8:
                start_timer = 0
                if index_taps != 0:
                    final_no_of_taps = index_taps - 1
                    command = command_taps_mapping.get(final_no_of_taps, "Unknown Command")
                    text_to_speech(command)
                index_taps = 0
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow("ANNOTATED IMAGE", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        picam2.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```

#### EuroFIlter.py

```import math

class OneEuroFilter:
    def __init__(self, mincutoff=1.0, beta=0.0, dcutoff=1.0):
        self.min_cutoff = mincutoff
        self.beta = beta
        self.d_cutoff = dcutoff
        self.x_prev = None
        self.dx_prev = None
        self.t_prev = None

    def alpha(self, cutoff, dt):
        tau = 1.0 / (2.0 * math.pi * cutoff)
        return 1.0 / (1.0 + tau / dt)

    def apply_filter(self, x, t):
        if self.t_prev is None:
            self.x_prev = x
            self.dx_prev = 0
            self.t_prev = t
            return x
        
        dt = t - self.t_prev
        dx = (x - self.x_prev) / dt if dt > 0 else 0.0
        dx_hat = self.dx_prev + self.alpha(self.d_cutoff, dt) * (dx - self.dx_prev)
        cutoff = self.min_cutoff + self.beta * abs(dx_hat)
        x_hat = self.x_prev + self.alpha(cutoff, dt) * (x - self.x_prev)
        
        self.x_prev = x_hat
        self.dx_prev = dx_hat
        self.t_prev = t
        
        return x_hat
```
