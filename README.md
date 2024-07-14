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
