from pynput.mouse import Listener
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
import comtypes
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

# Setup volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, comtypes.CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Volume step size
STEP = 0.05  # 5%

def on_click(x, y, button, pressed):
    if pressed:
        logger.info(f"Mouse button clicked: {button}")
        if str(button) == 'Button.x1':  # Side button 1 (usually the back button)
            current = volume.GetMasterVolumeLevelScalar()
            new_volume = max(current - STEP, 0.0)
            volume.SetMasterVolumeLevelScalar(new_volume, None)
            logger.info(f"Volume Up: {round(new_volume * 100)}% (was {round(current * 100)}%)")
            return True  # Keep listener running
        elif str(button) == 'Button.x2':  # Side button 2 (usually the forward button)
            current = volume.GetMasterVolumeLevelScalar()
            new_volume = min(current + STEP, 1.0)
            volume.SetMasterVolumeLevelScalar(new_volume, None)
            logger.info(f"Volume Down: {round(new_volume * 100)}% (was {round(current * 100)}%)")
            return True  # Keep listener running
        else:
            logger.debug(f"Ignoring non-volume button: {button}")
    return True  # Allow default behavior for other buttons

# Start listening
with Listener(on_click=on_click) as listener:
    listener.join()