# Speaker try 2
# Sun May 10 22:15:41 2026
# Jacob Birch

# %% Initializing

import asyncio
# from kasa import Device -> would be the better alternative for more modern strips
from kasa.iot import IotStrip
import sys

STRIP_IP = "192.168.0.7"
SPEAKER_NAMES = ["LSpeaker", "RSpeaker", "Subwoofer"]


async def toggle(child, state: bool):
    if state:
        await child.turn_on()
    else:
        await child.turn_off()


async def control_speakers(state: bool):
    strip = IotStrip(STRIP_IP)
    await strip.update()
    speakers = [c for c in strip.children if c.alias in SPEAKER_NAMES]
    await asyncio.gather(*[toggle(c, state) for c in speakers])


if __name__ == "__main__":
    if sys.argv[1] == "on":
        asyncio.run(control_speakers(True))

    elif sys.argv[1] == "off":
        asyncio.run(control_speakers(False))

    else:
        print(f"Invalid input: {sys.argv[1]}.")
