# Whirl Automation

**Last Updated**: May 2024

Whirl Main Controller

This is a manufacturing automation program for the handheld spreader Whirl. This automation line uses Denso robots ran by **WINCAPS** as well as **Cognex** cameras to run and work with **main.py** to run pallets through with error handling and product packaging.


This product can be seen for sale in full assembly as the [Scotts® Whirl™ Hand-Powered Spreader](https://www.scotts.com/en-us/products/spreaders/scotts-whirl-hand-powered-spreader).

In addition, it produces a similar product known as the [Ace Handheld Spreader For Fertilizer/Ice Melt/Seed 1500 sq ft](https://www.acehardware.com/departments/lawn-and-garden/lawn-care/seed-and-fertilizer-spreaders/7030137?store=17401&gad_source=1&gclid=EAIaIQobChMI9uaIoveDhgMVetjCBB11Rgm9EAQYAiABEgJ2IvD_BwE&gclsrc=aw.ds) and the [Sta-Green 8-lb Hand Powered Handheld Fertilizer Spreader](https://www.lowes.com/pd/Sta-Green-8-lb-Hand-Powered-Handheld-Fertilizer-Spreader/5013973811?cm_mmc=shp-_-c-_-prd-_-lwn-_-ggl-_-CRP_SHP_LIA_LWN_Online_C-D-_-5013973811-_-local-_-0-_-0&gad_source=1&gclid=EAIaIQobChMIt4yXqfeDhgMVAdHCBB1Puw2PEAQYASABEgJDbfD_BwE&gclsrc=aw.ds) .

## Part Assembly

#### Within the line there are 14 different molded components done in house by Scotts Temecula as of 2024. Those parts include:

1. Lower Housing
2. Ring Gear
3. Pinion
4. Cross Gear
5. Crank Handle 
6. Upper Housing
7. Crank Arm
8. Rotor 
9. Arm Support (_Scotts_ Whirl only)
10. Left Handle
11. Dial 
12. Trigger 
13. Hopper 
14. Right Handle 
15. Agitator

#### There are addiitonal items added to automation and product such as

- Grease on lower housing 
- Date Code to upper housing
- Final packaging box

## Denso Robot Layout

### Robot 5
  - Start of automation
  - Picks up incoming pallet completed part and places in box
  - Once box reaches limit of 6 robot pushes box to gravity roller
  - Picks up **lower housing** from conveyor to be slid against barcode label then places on pallet

### Robot 1
  - Picks up **ring gear** and places on lower housing  
  - Picks up **pinion** and places on lower housing 
  - Picks up **cross gear** and places on lower housing 
  - Picks up **crank handle** and places on pallet cavity.

### Robot 2
  - Picks up **upper housing** and places on top of gears and lower housing 
  - Picks up **rotor** and places on upper housing
  - Picks up **crank arm** and snaps on crank handle then inserted to right side

### Robot 3
  - Picks up **lower left handle** and places on grooved location elevated
  - Picks up **support arm** and places on handle
  - Picks up **trigger** and rotates orientation then places on handle
  - Picks up **dial** and places on handle

### Robot 4
  - Picks up **right handle** and places on rotator
  - Picks it back up places it on lower left handle and puts pressure on corners to snap in parts
  - Flips over the handle and places in back of upper housing 
  - Picks up **hopper** and places in slots on top of handle
  - Picks up **agitator** and places on mount the flips to pick up with vaccum and place inside hopper center

## Software Components

- PyCharm IDE
- Python 3.7
  - pyserial
  - requests
  - pymodbus
  - opencv-contrib-python
  - svglib
  - PyInstaller
  - candle-driver
- WINCAPS III (Denso Robot's)
- QT Designer (UI and Settings)

## Hardware Components

- I-7565-DNM DeviceNet-USB Converter
    https://www.icpdas-usa.com/i_7565_dnm.html
- SMC EX180-SDN2
- Cognex Vision System
- Cognex DM60 Barcode Reader
- Denso Robots (VS068A4-AVD and VS0682-AVD)
- 2~3 GYEMS Motors with CANable adapter.
    http://www.gyems.cn/product.html
    https://store.protofusion.org/product/canable/

## Settings up Environment

1. Install Drivers

    - CANable driver from [driver/canable-driver](driver/canable-driver)
    - I7565 DNM Driver from [driver/I7565 DNM](driver/I7565 DNM)

2. Update the firmware of the CANable adapter.

    CANables ship with *slcan* firmware, which uses the standard serial device and hence not fast enough for our purpose.

    Visit [this](https://canable.io/updater/) link and select **candlelight**, and update the firmware of your CANable Pro adapter.

3. Download & install Python3.9(x64)

    https://www.python.org/downloads/windows/

    (*NOTE*: Add python to PATH when you install it!)

4. Install packages

    ```shell script
       python -m pip install -U setuptools wheel pip
       python -m pip install -r requirements.txt
    ```

5. Configure the Denso Robot

    - Install WINCAPS III from [here](https://dpamrobotics.app.box.com/s/sg0gfx41grqzacj8uwlm3htwdtbkyc3s/file/581391953596)
    
        License Key: `WCDU-P2YW-LRUF-DB82`

    - Configure the controller by following [this](https://www.densorobotics.com/knowledge-base/orin2-robot-controller-setup-rc5-rc7-rc7m/) guide.

- Setup FTP server to save the result images from the Cognex Vision Systems

    Follow [this](https://www.windowscentral.com/how-set-and-manage-ftp-server-windows-10) instruction to configure the FTP server.
  
- Follow [this](https://techlibrary.hpe.com/docs/otlink-wo/How-to-Configure-a-Local-NTP-Server.html) guide to set up local NTP server.

- Configure the Cognex Vision systems to use the above FTP server and NTP server.

## Package the application

- Create an executable: 

    ```shell script
    cp utils\hook-fastprogress.py venv_win\Lib\site-packages\PyInstaller\hooks
    venv_win\Scripts\pyinstaller.exe main.spec
    cp -R venv_win\Lib\site-packages\PySide6\plugins\platforms dist\Whirl
    ```

