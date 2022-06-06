############################# The imports
from curses import wrapper
import curses
from notifypy import Notify
import time
from stopwatch import Stopwatch
import requests
############################# Cool logo
def timeSleepLogo():
    time.sleep(0.035)

print("────────────────────────────────────────────────────────────────────────────────────────────────────────────")
timeSleepLogo()
print("─██████──██████─██████████████─██████████████─██████──██████─██████████████─██████████████─██████──████████─")
timeSleepLogo()
print("─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░██─")
timeSleepLogo()
print("─██░░██──██░░██─██░░██████░░██─██░░██████████─██░░██──██░░██─██░░██████████─██░░██████████─██░░██──██░░████─")
timeSleepLogo()
print("─██░░██──██░░██─██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██─────────██░░██─────────██░░██──██░░██───")
timeSleepLogo()
print("─██░░██──██░░██─██░░██████░░██─██░░██─────────██░░██████░░██─██░░██████████─██░░██─────────██░░██████░░██───")
timeSleepLogo()
print("─██░░██──██░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██───")
timeSleepLogo()
print("─██░░██──██░░██─██░░██████████─██░░██─────────██░░██████░░██─██░░██████████─██░░██─────────██░░██████░░██───")
timeSleepLogo()
print("─██░░██──██░░██─██░░██─────────██░░██─────────██░░██──██░░██─██░░██─────────██░░██─────────██░░██──██░░██───")
timeSleepLogo()
print("─██░░██████░░██─██░░██─────────██░░██████████─██░░██──██░░██─██░░██████████─██░░██████████─██░░██──██░░████─")
timeSleepLogo()
print("─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░██─")
timeSleepLogo()
print("─██████████████─██████─────────██████████████─██████──██████─██████████████─██████████████─██████──████████─")
timeSleepLogo()
print("────────────────────────────────────────────────────────────────────────────────────────────────────────────")

############################# Create stopwatch object and get url from user
stopwatch = Stopwatch()

print("Enter url (Must include http):")
url = input('> ')
############################# Create notification object
notification = Notify()
appName = "UpCheck"
appIcon = "icon.png"

def notify(title, message):
    notification.application_name = appName
    notification.icon = appIcon
    notification.title = title
    notification.message = message
    notification.send()
############################# start stopwatch

stopwatch.start()
############################# Main and colors
def main(stdscr):
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

############################# Main stuff
    def mainScr():

        stdscr.addstr(0, 0, "UpCheck", curses.color_pair(2) | curses.A_BOLD)

        stdscr.addstr(4, 1, "Status")

        stdscr.addstr(3, 1, "Url")
        stdscr.addstr(3, 30, url)

        stdscr.addstr(6, 1, "Total Run Time")
        stdscr.addstr(6, 30, str(stopwatch.elapsed).split(".")[0] + " seconds")

        stdscr.refresh()
############################# Change status
    updateSpeed = 1.5
    def changeStatusAndOtherStuff(status, updateSpeed, statusColor):
        stdscr.clear()
        mainScr()
        stdscr.addstr(0, 79, f"Update speed: {str(updateSpeed)} seconds", curses.color_pair(3) | curses.A_BOLD)
        stdscr.addstr(4, 30, status, curses.color_pair(statusColor))
        stdscr.refresh()
    changeStatusAndOtherStuff("Checking...", 0, 3)
############################# Main run stuff (and the ping checker)
    def ping():
        request_response = requests.head(url)
        status_code = request_response.status_code
        website_is_up = status_code == 200
        if website_is_up:

            changeStatusAndOtherStuff("Online", 1.75, 1)
            while website_is_up != False:
                mainScr()
                request_response = requests.head(url)
                status_code = request_response.status_code
                website_is_up = status_code == 200
                time.sleep(1.75)

        else:
            
            changeStatusAndOtherStuff("Offline (Reconnecting)", 1, 4)
            notify(url, "Server is down!")

            while website_is_up == False:

                mainScr()
                request_response = requests.head(url)
                status_code = request_response.status_code
                website_is_up = status_code == 200
                time.sleep(1)

            changeStatusAndOtherStuff("Online", 1.75, 1)
            notify(url, "Server is back up!")
        
############################# Update stuff
    

    def update():
        
        while True:
            stdscr.clear()
            mainScr()
            ping()
    update()
############################# Starts it (i think?)
wrapper(main)