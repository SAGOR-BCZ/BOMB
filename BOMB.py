import os, sys
os.system('git pull')
try:
    __import__("bomb.enc").main()
except Exception as e:
    exit(str(e))
