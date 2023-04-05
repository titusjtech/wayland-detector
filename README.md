# Wayland Detector

This Python script provides information about the current session on Linux systems and prints the current display server - X11, Wayland, or tty (if there is no display server installed/running on the system).

## Requirements

- Linux system
- Python 3.x
- systemd (Linux distributions such as Alpine Linux, Devuan, Void Linux, Gobo Linux, and most of the distributions listed on [this article](https://itsfoss.com/systemd-free-distros/) will not work, but some of them have options to enable systemd.)

## Usage

To use this script, simply run it from the command line:

```python
python display_server.py
```

## Script Details

This script checks if the operating system is Linux. If not, it displays an error message and exits.

Next, the script uses the `os` module to execute `loginctl`, which provides information about the current session. It extracts the display server type from the session information and then prints it to the terminal.

If the loginctl command fails to execute, the script displays an error message and exits.

## Example Output

```python
$ python session_info.py
wayland
```

In this example output, Wayland is the type of the current display server.

## Troubleshooting

- Make sure you are running the script on a Linux system.
- Check if Python 3.x is installed.
- Ensure that systemd is installed on the system.
