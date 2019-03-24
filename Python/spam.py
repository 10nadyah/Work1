from pynput.keyboard import Key, Controller
import time
count = 0

ustring = input("Enter What You Want To Spam:")
xValue = int(input("How many times would you like to spam:"))
cooldown = int(input("Cooldown:"))

keyboard = Controller()
while xValue > count:
    keyboard.type(ustring)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    count += 1
    time.sleep(cooldown)

print()
print()
print()
print("Finished!")
time.sleep(8)