import os
import time

def l():
    a = input("ЗАПУСТИТЬ БОТА ВК? [Y/n] ")

    if a.lower() == "y":
        os.system("cd")
        os.system("cd storage/downloads/VkBot/")
        os.system("python bot.py")
    
    elif a.lower() == "n":
        print("Завершение работы...")
        time.sleep(5)
        os.system("clear")
        
    else:
        l()
        
l()

