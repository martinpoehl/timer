# Windows Alert Reminder

This Python script displays a Windows alert every 20 minutes to remind the user to relax their eyes for 20 seconds. It utilizes the `pymsgbox` library to show the alert.

## Prerequisites

- Python 3.x installed
- `pymsgbox` library installed. If not installed, you can install it using the following command:

```bash
pip install pymsgbox
```

## Usage

1. Open a text editor and create a new Python file.
2. Copy and paste the provided code into the file.
3. Save the file with a `.py` extension (e.g., `windows_alert_reminder.py`).
4. Open a terminal or command prompt.
5. Navigate to the directory where the Python file is saved.
6. Run the script using the following command:

```bash
python windows_alert_reminder.py
```

7. The script will display a Windows alert every 20 minutes with the message "Augen für 20 Sekunden entspannen" and the title "Alert".
8. To stop the script, press `Ctrl + C` in the terminal or command prompt.

## Customization

- To change the alert message or title, modify the corresponding values in the `display_alert()` function.
- To adjust the time interval between alerts, modify the argument of `time.sleep()`. The current setting is 1200 seconds (20 minutes).

## Notes

- This script is designed specifically for Windows systems as it uses the `pymsgbox` library, which is Windows-specific. It may not work on other operating systems.
- The script runs in an infinite loop until it is manually stopped. To stop the script, press `Ctrl + C` in the terminal or command prompt.

---

Feel free to customize the documentation further based on your specific requirements or preferences.
