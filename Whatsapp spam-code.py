import pyautogui as pt
import time

limit=input("Enter the Limit")
msg=input("Enter Your Message")
c=1

time.sleep(4)
for i in range(int(limit)):
    pt.typewrite(msg+" "+str(c))
    pt.press('Enter')
    c+=241223
