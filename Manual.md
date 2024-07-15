# Steps for Initial Setup

## Step 1: Download and Install Raspberry Pi Imager
1. Download Raspberry Pi Imager from the official Raspberry Pi website.
2. Install the Raspberry Pi Imager on your computer.

## Step 2: Flash the OS to the MicroSD Card
1. Insert the MicroSD card into the card reader connected to your computer.
2. Open Raspberry Pi Imager.
3. Click on "Choose Device" and select "Raspberry Pi Zero 2 W" 
4. Click on "Choose OS" and select "Raspberry Pi OS (64-bit)"
5. Click on "Choose Storage" and select your MicroSD card.
6. On your keyboard, press Ctrl+Shift+X and the OS Customisation Menu appears.
7. Check all the tickboxes aligned to the left and set the hostname, username, password of your choice.
8. Enter the Credentials of a Wireless Network of 2.4 GHz Band only and select your country.
9. Go to Services Tab and check the tickbox and click on the first radio button and click on the SAVE Button at the bottom of the screen.
10. Click on "Next" and then on "Yes" and wait for the flashing process to finish.

## Step 3: Initial Boot and SSH Setup
1. Once the flashing process is complete, insert the MicroSD card into the Raspberry Pi Zero 2 W.
2. Connect the Raspberry Pi to a power supply.
3. Give it a couple of minutes to boot and connect to your Wi-Fi network.
4. Find the IP address of your Raspberry Pi.

## Step 4: Connect via SSH
1. Open a terminal (Linux/Mac) or Command Prompt (Windows).
2. Use the ssh command to connect to your Raspberry Pi:
```
ssh <username>@<IP_ADDRESS>
```
- Replace <IP_ADDRESS> with the actual IP address and <username> with the actual username of your Raspberry Pi.
3. Enter the password you set during the configuration.

## Step 5: Enable VNC
1. Enable the VNC server:
 ```
sudo raspi-config
```
3. Navigate to Interfacing Options -> VNC -> Yes to enable VNC and similarly enable One-Wire.

## Step 6: Connect via VNC
1. Download and install VNC Viewer on your computer from the RealVNC website.
2. Open VNC Viewer and enter the IP address of your Raspberry Pi.
3. Connect and log in with the username pi and the password you set.

# Steps to change the swap space **(IMPORTANT)**

## 1. Open a Terminal
- You can access your Raspberry Pi via SSH.

## 2. Edit the Swap File Configuration
1. Open the dphys-swapfile configuration file:
   ```
   sudo nano /etc/dphys-swapfile
   ```
## 3. Change the Swap Size
1. Locate the line:
```CONF_SWAPSIZE=100```
2. Replace with the below line
```CONF_SWAPSIZE=1024```

## 4. Save and Exit
1. Press Ctrl + X to exit.
2. Press Y to confirm saving the changes.
3. Press Enter to save the file.

## 5. Restart the System
1. Restart the system to apply the changes:
 ```
 sudo reboot
 ```
## 6. Verify the Swap Space
1. Check the current swap space to confirm the change:
 ```
 free -h
 ```

# Device Configuration Steps for using Method -  1

## Step 1: Update the package list:
```
sudo apt update
sudo apt full-upgrade
```
## Step 2: Installing the required Libraries:
```
sudo apt-get install python3-opencv Flask libcamera-apps libcamera-dev picamera2
```

## Step 3: Running the code:
```
python3 stream.py
```

# Device Configuration Steps for using Method -  2

## Step 1: Update the package list:
```
sudo apt update
sudo apt full-upgrade
```
## Step 2: Installing the required Libraries on device:
```
sudo apt-get install python3-opencv Flask libcamera-apps libcamera-dev picamera2
```
## Step 3: Installing libraries on Virtual Environment
1. Create a Virtual Environment
   ```
   python3 -m venv <name> --system-site-packages
   ```
2. Access the Virtual Environment
   ```
   source <name>/bin/activate
   ```
3. Install the required libraries
   ```
   pip install mediapipe pyttsx4 numpy
   ```
## Step 4: Running the code:
1. While in the Virtual Environment, run the below code
 ```
 python3 rasp.py
 ```
