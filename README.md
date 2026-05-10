# Desktop Speaker Automation

Automatically turns on/off desktop speakers (and other smart devices) based on PC state using the SmartThings API and Windows Task Scheduler. This was built to solve a personal annoyance. My speakers draw phantom power and emit a quiet but audible buzz when left on, I automated them to follow my PC's startup/shutdown cycle as a quick fix.

## What It Does

- Turns on left speaker, right speaker, and subwoofer when the PC starts or unlocks
- Turns them off when the PC shuts down or locks
- All device IDs and credentials are stored securely in a `.env` file

## How It Works

The script hits the SmartThings REST API to send on/off commands to each speaker outlet on a Kasa HS300 smart power strip. It's triggered automatically by Windows Task Scheduler on startup, shutdown, lock, and unlock events.

## Requirements

- Python 3.x (Anaconda recommended)
- A Samsung SmartThings account
- A Kasa HS300 (or any SmartThings-compatible smart plug)
- Windows Task Scheduler

Install dependencies:
```
pip install requests python-dotenv
```

## Setup

**1. Get a SmartThings Personal Access Token**

- Go to [account.smartthings.com](https://account.smartthings.com)
- Personal Access Tokens → Generate New Token
- Give it Devices (read + execute) permissions
- Copy the token. It's only shown once

**2. Get your device IDs**

Uncomment the GET DEVICE NAMES block in the script and run it once. It will print all your SmartThings device IDs and labels. Copy the ones you need.

**3. Create a `.env` file**

Create a `.env` file in the same directory as the script:

```
token=your_smartthings_pat_here
wlc=your_device_id_here
sp=your_device_id_here
rsp=your_device_id_here
lsp=your_device_id_here
sub=your_device_id_here
mon=your_device_id_here
usb=your_device_id_here
```

**4. Create bat files**

`speakers_on.bat`:
```bat
@echo off
call C:\Users\YourName\anaconda3\Scripts\activate.bat
python "C:\path\to\speaker.py" on
```

`speakers_off.bat`:
```bat
@echo off
call C:\Users\YourName\anaconda3\Scripts\activate.bat
python "C:\path\to\speaker.py" off
```

**5. Set up Task Scheduler**

Create two tasks in Windows Task Scheduler:

| Task | Trigger1 | Trigger2 | Bat File |
|------|---------|----------|----------|
| Speakers On | At log on of any user | At workstation unlock of any user | speakers_on.bat |
| Speakers Off | System, User32, ID 1074 | At workstation lock of any user | speakers_off.bat |



## Usage

Can also be run manually from the command line:
```
python speaker.py on
python speaker.py off
```

## Adding More Devices

All SmartThings devices are stored in the `devices` dict and loaded from `.env`. To control additional outlets, add their IDs to `.env` and update the `devices` dict and `speakers` list in the script. Feel free to mix and match based on the smart devices you have!
