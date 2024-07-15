# Steps for initial Setup

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

## Step 4:Connect via SSH
1. Open a terminal (Linux/Mac) or Command Prompt (Windows).
2. Use the ssh command to connect to your Raspberry Pi:
``` ssh <username>@<IP_ADDRESS> ```
- Replace <IP_ADDRESS> with the actual IP address and <username> with the actual username of your Raspberry Pi.
3. Enter the password you set during the configuration.
