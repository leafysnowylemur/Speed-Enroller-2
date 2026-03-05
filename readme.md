# Setup (Currently for MacOS ONLY)
run '''setup.py'''

go into '''main.py''' and set '''FirefoxAppPath''' at the beginning of the file to the path to the '''Firefox.app''' on your system.

configure the settings in '''settings.py'''

run '''main.py'''

## Usage
'''testing = False''' This is used for changing whether you want to run the script in '''testing''' mode. 
Testing mode makes it so that it runs in a simpler mode and sets the '''targetTime''' to 1.5 minutes ahead.

'''simpleMode = ""''' This is an extention to '''testing''' and make it so that nothing is set for the '''username''' and '''password''' and sets the '''targetTime''' to 1.5 minutes ahead. This mode wont make it past the OKTA login screen but is useful for testing wheither your browser paths and settings are configured correctly.


'''id = ''''' This is your username to login to ERNIE
'''pw = ''''' This is your password to log into ERNIE
'''targetTime = ''''' This is the time you want to have the script login at. It is in the format '''HH:MM'''


'''DEV_TABS = 2''' This is how many tabs the program should open and be loging in on. It opens this many tabs beforehand and configures them so when it comes time, it goes through each and confirms the registration sending that many requests to the server.

'''SHOPPING_CART_DELAY = 5''' IDK what this does, David made this. I'd recommend not changing it.

'''CLICKTEXT = ""''' IDK what this does either, probably shouldnt mess with it either.