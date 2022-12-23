import os, sys
os.system('git pull')
try:
    __import__("BOMB").main()
except Exception as e:
    exit(str(e))
