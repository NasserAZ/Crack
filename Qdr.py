import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Qdr import Fire
    Fire()
elif bit == '32bit':
    from Qdr32 import Fire
    Fire()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS TOOL')
    os.system('exit')
