import datetime
import Modes
import settings as s
import os
import glob
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
import securepassword

def main():
    print("===================Speed Enroller v2=====================")
    if s.testing:
        s.simpleMode = True if input("Simple Mode? (y/n): ") == 'y' else False
        s.id = ""
        s.pw = ""
        s.targetTime = datetime.datetime.now() + datetime.timedelta(minutes=1.5)
        s.CLICKTEXT = "Continue"
    else:
        if (s.id and s.pw and s.targetTime) == "" and s.testing == False:
            s.id = input("ERAU login ID: ")
            s.pw = securepassword.getpass("ERAU login PW: ")
            now = datetime.datetime.now()
            goal = datetime.datetime.strptime(input("Target Time (HH:MM): "), "%H:%M")
            s.targetTime = datetime.datetime(now.year, now.month, now.day, goal.hour, goal.minute, 0)
            s.CLICKTEXT = "Continue"
        else:
            now = datetime.datetime.now()
            goal = datetime.datetime.strptime(s.targetTime, "%H:%M")
            s.targetTime = datetime.datetime(now.year, now.month, now.day, goal.hour, goal.minute, 0)
            s.CLICKTEXT = "Continue"
    print("=========================================================")
    print(f"Target Time: {s.targetTime}")

    print("Starting web driver...")
    
    FirefoxAppPath = "/Applications/Firefox.app"
    
    options = Options()
    home = os.path.expanduser("~")
    profiles_path = os.path.join(home, "Library/Application Support/Firefox/Profiles/")
    options.binary_location = os.path.join(FirefoxAppPath, "Contents/MacOS/firefox")
    
    try:
        found_profiles = glob.glob(os.path.join(profiles_path, "*.default-release"))
        if found_profiles:
            profile_path = found_profiles[0]
            print(f"Automatically detected profile: {os.path.basename(profile_path)}")
            options.add_argument("-profile")
            options.add_argument(profile_path)
        else:
            print("No default-release profile found. Using a fresh session.")
    except Exception as e:
        print(f"Could not autodiscover profile: {e}")

    try:
        service = FirefoxService(executable_path=os.path.join("geckodriver"))
        driver = webdriver.Firefox(options=options, service=service)
        print("Web driver started with your profile.")
    except Exception as e:
        print(f"Web driver failed: {e}")
        return

    if (Modes.DevMode(driver) < 0):
        if input("Process failed, retry (y/n)? ") == 'y':
            main()

if __name__ == '__main__':
    main()