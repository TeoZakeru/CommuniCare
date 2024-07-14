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


