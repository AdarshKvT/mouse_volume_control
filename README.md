# Mouse Volume Control

Tired of your mouse side buttons doing nothing useful?
A Python script that allows you to control your Windows system volume using mouse side buttons (forward/back buttons). This makes it easy to adjust volume without reaching for keyboard controls or opening the volume mixer.

## Features

- Control system volume using mouse side buttons
- Forward button (X2) increases volume
- Back button (X1) decreases volume
- Volume changes in 5% increments
- Logging of volume changes with timestamps
- Runs in the background
- Python script for volume control
- media control using mouse

## Requirements

- Python 3.6 or higher
- Windows OS (as it uses Windows Core Audio API)
- Mouse with side buttons (forward/back buttons)

## Dependencies

The script requires the following Python packages:

```
pynput>=1.7.6
pycaw>=20181226
```

## Installation

1. Clone this repository or download the script
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the Script

Simply run the script using Python:

```
python mouse_volume_control.py
```

### Running at Startup

To make the script run automatically at Windows startup:

1. Create a shortcut to the script:

   - Right-click on `mouse_volume_control.py`
   - Select "Create shortcut"

2. Move the shortcut to the Windows Startup folder:
   - Press `Win + R`
   - Type `shell:startup`
   - Press Enter
   - Move the created shortcut to this folder

Alternatively, you can use Task Scheduler:

1. Open Task Scheduler
2. Create a new task
3. Set it to run at logon
4. Add a new action:
   - Program/script: `pythonw.exe`
   - Arguments: `path_to_script\mouse_volume_control.py`
   - Start in: `path_to_script_directory`

Note: Use `pythonw.exe` instead of `python.exe` to run the script without a console window.

## Controls

- **Back Mouse Button (X1)**: Decrease volume by 5%
- **Forward Mouse Button (X2)**: Increase volume by 5%

## Logging

The script logs all volume changes with timestamps in the following format:

```
HH:MM:SS - INFO - Volume Up/Down: XX% (was YY%)
```

## Developer

Developed by: Adarsh Kavtiyal
Contact: adarshkavtiyal@outlook.com

## License

This project is open source and available under the MIT License.
