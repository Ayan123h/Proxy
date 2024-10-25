import requests,termcolor,colorama,time,sys,random,os,platform,threading,datetime
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
def fresh():
	if platform.system() == "Windows": os.system('cls')
	else: os.system("clear")
colorama.init()
def Rndua():
    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
    user_agents = user_agent_rotator.get_user_agents()
    user_agent = user_agent_rotator.get_random_user_agent()
    return user_agent
def Proxy(RandomProxy,protocol):
	try:
	        proxy = RandomProxy.split(':')
	        if len(proxy) == 2:
	            return {
	                'http' : f'{protocol}://{proxy[0]}:{proxy[1]}',
	                'https' : f'{protocol}://{proxy[0]}:{proxy[1]}'
	            }
	        elif len(proxy) == 4:
	            return {
	                'http' : f'{protocol}://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}',
	                'https' : f'{protocol}://{proxy[2]}:{proxy[3]}@{proxy[0]}:{proxy[1]}'
	            }
	        else: Proxy(RandomProxy,protocol)
	except: Proxy(RandomProxy,protocol)
def ProxyCheck(likes,site='https://google.com'):
	re = requests.session()
	try:
		r = re.get(site,headers = {"User-agent":Rndua()},proxies = likes)
	except Exception as e:
		r = "404"
	if str(r).__contains__('<Response [200]>'): return "Live"
	else: return 'Dead'
def Banner(color):
			print(termcolor.colored('''
	 ╔═╦╦╦═╦╦╦╦╗╔══╦═╦═╦╗╔══╗
         ║╔╣╔╣║╠─╬╗║╚╗╔╣║║║║╚╬╗╚╣
         ╚╝╚╝╚═╩╩╝╚╝─╚╝╚═╩═╩═╩══╝
		
		''',color = color))
fresh()
Banner('red')
for i in "Channel: @Cyber_Steal\n":
	sys.stdout.write(i)
	time.sleep(0.03)
	sys.stdout.flush()
Combo = open(input(termcolor.colored('\nEnter Your ProxyList File Path - ',color = 'green'))).readlines()
Proxy_protocol = input(termcolor.colored('\nEnter Your Protocol [ HTTP/ SOCKS4 / SOCKS5 ] - ',color = 'green'))
def Banner_cols():
	fresh()
	for i in range(0,5):
		col,used = ["green","red","blue",'yellow',"cyan","white","magenta"],[]
		R_col = random.choice(col)
		if R_col in used:
			for i in range(0,2):
				fresh()
				Banner(random.choice(col))
				time.sleep(0.05)
		else:
			used.append(R_col)
			fresh()
			Banner(R_col)
			time.sleep(0.05)
Banner_cols()
fresh()
Banner('red')
sit = input(termcolor.colored('Would You Like To Change Target Site ? (Y/N) - ',color = 'yellow')).lower()
if sit == 'y':
	sites = 1
	site = input(termcolor.colored('\nEnter Your Site - ',color = 'green'))
	if 'https://' not in site: site = "https://"+site
else: sites = 0
Banner_cols()
fresh()
Banner('green')
date = datetime.datetime.now()
def Complete(line):
	line = line.replace('\n','')
	proxys = Proxy(line,Proxy_protocol)
	if sites == 1: chk = ProxyCheck(proxys,site)
	else: chk = ProxyCheck(proxys)
	if chk == 'Live':
		print(termcolor.colored(line,color = 'green'))
		w = open(f'Live_Proxy[{date}].txt','a').write(line+'\n')
	else:
		print(termcolor.colored(line,color = 'red'))
task = []
for lines in Combo:
	processor = threading.Thread(target=Complete,args = (lines,))
	processor.start()
	task.append(processor)
for runner in task:
	runner.join()