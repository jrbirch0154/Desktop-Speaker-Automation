# Desktop Speaker Automation

Automatically turns on/off desktop speakers (and other smart devices) based on PC state using the SmartThings API and Windows Task Scheduler. This was built to solve a personal annoyance. My speakers draw phantom power and emit a quiet but audible buzz when left on, I automated them to follow my PC's startup/shutdown cycle as a quick fix.

## How It Works

The script communicates directly with a Kasa HS300 smart power strip over the local network using the `python-kasa` library. No cloud account or API token required. It targets three specific outlets by name and toggles them simultaneously using `asyncio.gather()`. I chose to do this simultaneously, as calling each one by one adds time to the script, and sometimes did not complete in time before my computer shut down.

Windows Task Scheduler triggers the script on four events:
- Startup → speakers on
- Log in → speakers on
- Lock → speakers off
- Shutdown → speakers off

## Requirements

- Python 3.x (Anaconda recommended)
- Kasa HS300 smart power strip
- Windows Task Scheduler

Install dependencies:
```
pip install python-kasa
```

## Setup

**1. Find your strip's local IP**

Run the following in your terminal to discover devices on your network. (python-kasa must already be installed):
```
kasa discover
```

Note the IP address of your HS300.

**2. Name your outlets**

In the Kasa app, name the outlets you want to control (e.g. LSpeaker, RSpeaker, Subwoofer). The script matches by name.

**3. Update the script**

Edit these two lines in `speaker.py` to match your setup:
```python
STRIP_IP = "your.strip.ip.here"
SPEAKER_NAMES = ["YourOutlet1", "YourOutlet2", "YourOutlet3"]
```

**4. Create bat files**

`speakers_on.bat`:
```bat
@echo off
call C:\Users\YOURUSERNAME\anaconda3\Scripts\activate.bat
python "C:\Users\YOURUSERNAME\Documents\YOURSAVEPATH\speaker.py" on
```

`speakers_off.bat`:
```bat
@echo off
call C:\Users\YOURUSERNAME\anaconda3\Scripts\activate.bat
python "C:\Users\YOURUSERNAME\Documents\YOURSAVEPATH\speaker.py" off
```

Update the paths to match your system.

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

Update `SPEAKER_NAMES` to include any additional outlet names from your HS300. They must match the outlet names exactly as set in the Kasa app.
