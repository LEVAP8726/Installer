import os
cl = "clear"
os.system(cl)
os.system("pkg update -y && pkg upgrade -y")
os.system("termux-setup-storage")
os.system("pip install vk_api")
os.sistem("mv storage/downloads/VkBot/* .")
os.system("rm installer.sh")
os.system("rm installer.py")
os.system(cl)
os.system("python bot.py")
