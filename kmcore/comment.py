from kmcore import domain,crypto,json_handler,sigcode
import requests,json

class comment:
  def __init__(self,uid,uname,time,floor,text):
    self.uid=uid
    self.uname=uname
    self.time=time
    self.floor=floor
    self.text=text
    self.reply=list()
  def set_reply():
    pass

def get_all_comment(vid,page,clist):
  url=domain+'api/community/listComments'
  raw=f'{{"mvId":"{str(vid)}","page":{str(page)}}}'
  headers={'Host': domain[8:-1],'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46'}
  args=f"data={str.upper(crypto.encrypt(raw))}&sig={sigcode.get_sigcode(str.upper(crypto.encrypt(raw)))}"
  r=requests.post(url=url,data=args,headers=headers)
  text=json_handler.handle(crypto.decrypt(r.text))
  js0n=json.loads(text)
  if js0n['code']!=0:
    raise Exception(js0n)
  for cm in js0n['data']['list']:
    c=comment(cm['mu_id'],cm['mu_name'],cm['mc_created'],cm['mc_floor'],cm['mc_text'])
    clist.append(c)