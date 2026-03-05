# Speed-Enroller-2

## Setup (Currently for MacOS ONLY)
1. run `setup.py`

2. go into `main.py` and set `FirefoxAppPath` to the path to the `Firefox.app` on your system.

3. configure the settings in `settings.py`

4. run `main.py`

## Usage

### settings.py
This is the settings file for the program


#### `testing = bool` 
This is used for changing whether you want to run the script in `testing` mode. 
Testing mode makes it so that it runs in a simpler mode and sets the `targetTime` to 1.5 minutes ahead.

#### `simpleMode = bool` 
extention to `testing` and make it so that nothing is set for `username` and `password` and sets `targetTime` to 1.5 minutes ahead. This mode wont make it past the OKTA login screen but is useful for testing whether your browser paths and settings are configured correctly.


#### `id = ""` 
Your username to login to ERNIE

#### `pw = ""` 
Your password to log into ERNIE

#### `targetTime = ""` 
This is the time you want to have the script login at. It is in the format `HH:MM`



`DEV_TABS = 2` This is how many tabs the program should open and be loging in on. It opens this many tabs beforehand and configures them so when it comes time, it goes through each and confirms the registration sending that many requests to the server.

`SHOPPING_CART_DELAY = 5` IDK what this does, David made this. I`d recommend not changing it.

`CLICKTEXT = ""` IDK what this does either, probably shouldnt mess with it either.
