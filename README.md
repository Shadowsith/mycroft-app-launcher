## App Launcher Skill
Execute and stop Linux desktop programs

## Description 
The App Launcher Skill allows to open and close linux desktop applications
with simple open/close commands. It is very similiar to [Desktop
Launcher](https://github.com/MycroftAI/skill-desktop-launcher) from Mycroft but 
ony uses subprocesses to open/close programs. It also gives you a message if a
application is not found on the device.

## Examples 
* "App open firefox"
* "Program open firefox"
* "App launch thunderbird"
* "App close firefox"
* "App exit thunderbird"
* "Program close chromium"

## Installation
Clone this repository into /opt/mycroft/skills and restart the mycroft service

## Tested on
* Arch (Manjaro Linux)

## TODO
* Check if a process with app launches before killing
* User can allow/deny if a app can be opened twice

## Issues
* Dolphin filemanager does not open

## Credits 
Philip Mayer

## License
MIT
