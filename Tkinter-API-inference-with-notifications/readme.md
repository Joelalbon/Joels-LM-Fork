# Tkinter-API-inference-with-notifications

A simple GUI application developed using `tkinter` that allows users to send input to an API and subsequently display the API's response as a system notification.

## Features

- **Overlay Window**: A minimalistic GUI that remains on top of other windows for easy access.
- **User Input**: A textbox to type and submit queries to the API by pressing 'Return'.
- **Notifications**: Uses the `plyer` library to display API responses as system notifications, partitioned if they exceed a certain length.
- **API Communication**: Sends requests to `http://localhost:{PORT}/v1/chat/completions` and handles potential request exceptions.
- **Topmost Window**: The GUI always remains on top of other windows.
- **Exit Mechanism**: Pressing 'Escape' prompts a confirmation messagebox to exit.

## Installation & Setup

1. Ensure you have `tkinter`, `requests`, and `plyer` libraries installed.
2. Set the desired `PORT` value in the script.
3. Run the script `box.py` to initialize the GUI.

## Usage

1. Type a query into the textbox.
2. Press 'Return' to submit.
3. View the API's response as a system notification.

Note: Move the GUI by clicking and dragging anywhere on its window. To exit, press the 'Escape' key.

## Limitations

- There is no scrollback currently for entered messages
- Reponses will be split into ~240ish char chunks
- calling the overrideredirect(True) method in Tkinter removes the window's title bar and border, making it undecorated. This also removes the application from the taskbar. Unfortunately, Tkinter's native capabilities don't provide a straightforward way to keep an entry on the taskbar while using overrideredirect(True) so close it by pressing ESCAPE as noted in Features above

## Cross-Platform Considerations for Notifications
While `plyer` does support notifications on multiple platforms (Windows, macOS, Linux, Android, iOS), the behavior and appearance of notifications can vary depending on the platform and its specific configurations. For instance, on some Linux distributions, you might need to have certain notification daemons (like notify-osd or notification-daemon) installed for notifications to work.

## Errors
In the event the port is blocked, or the API is not running for some reason you will at least recieve a notification warning you

    HTTPConnection object at 0x000001C3503D9110>:
    Failed to establish a new connection: [WinError 10061]
    No connection could be made because the target
    machine actively refused it

