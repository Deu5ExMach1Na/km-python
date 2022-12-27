from kmcore import domain,crypto,json_handler,sigcode
import requests,json


class video:
  def __init__(self,uid,uname,vtime,vid,vimg,vlike,vurl,vtitle):
    self.uid=uid          #用户id
    self.uname=uname      #用户昵称
    self.vtime=vtime      #发布时间
    self.vid=vid          #视频id
    self.vimg=vimg        #封面
    self.vlike=vlike      #赞数
    self.vurl=vurl        #视频地址
    self.vtitle=vtitle    #视频标题
    

def get_all_videos(page,perpage,vlist):
  url=domain+'api/videos/listAll'
  raw=f'{{"perPage":{str(perpage)},"page":{str(page)}}}'
  headers={'Host': domain[8:-1],'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46'}
  args=f"data={str.upper(crypto.encrypt(raw))}&sig={sigcode.get_sigcode(str.upper(crypto.encrypt(raw)))}"
  r=requests.post(url=url,data=args,headers=headers)
  text=json_handler.handle(crypto.decrypt(r.text))
  js0n=json.loads(text)
  if js0n['code']!=0:
    raise Exception(js0n)
  for mv in js0n['data']['list']:
    if(mv['is_cat_ads'] is 0):
      v=video(mv['mu_id'],mv['mu_name'],mv['mv_created'],mv['mv_id'],mv['mv_img_url'],mv['mv_like'],mv['mv_play_url'],mv['mv_title'])
    # v.vurl=fix_mv_url(v.vid)  默认不修正下载链接
      vlist.append(v)


def get_hot_videos(page,perpage,vlist):
  url=domain+'api/videos/listHot'
  raw=f'{{"perPage":{str(perpage)},"page":{str(page)}}}'
  headers={'Host': domain[8:-1],'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46'}
  args=f"data={str.upper(crypto.encrypt(raw))}&sig={sigcode.get_sigcode(str.upper(crypto.encrypt(raw)))}"
  r=requests.post(url=url,data=args,headers=headers)
  text=json_handler.handle(crypto.decrypt(r.text))
  js0n=json.loads(text)
  if js0n['code']!=0:
    raise Exception(js0n)
  for mv in js0n['data']['list']:
    if(mv['is_cat_ads'] is 0):
      v=video(mv['mu_id'],mv['mu_name'],mv['mv_created'],mv['mv_id'],mv['mv_img_url'],mv['mv_like'],mv['mv_play_url'],mv['mv_title'])
    # v.vurl=fix_mv_url(v.vid)  默认不修正下载链接
      vlist.append(v)


def get_fav_videos(page,perpage,uid,vlist):
  url=domain+'api/community/videoCollectList'
  raw=f'{{"page":{page},"uId":"{uid}","perPage":{perpage}}}'
  headers={'Host': domain[8:-1],'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46'}
  args=f"data={str.upper(crypto.encrypt(raw))}&sig={sigcode.get_sigcode(str.upper(crypto.encrypt(raw)))}"
  r=requests.post(url=url,data=args,headers=headers)
  text=json_handler.handle(crypto.decrypt(r.text))
  js0n=json.loads(text)
  # print(js0n)
  if js0n['code']!=0:
    raise Exception(js0n)
  for item in js0n['data']:
    if item.get('video',0)==0:
      continue
    mv=item['video']
    v=video(mv['mu_id'],'None',mv['mv_created'],mv['mv_id'],mv['mv_img_url'],mv['mv_like'],mv['mv_play_url'],mv['mv_title'])
    # v.vurl=fix_mv_url(v.vid)  默认不修正下载链接
    vlist.append(v)


#需要调用/detail才能获取正确的播放地址

def fix_mv_url(mv_id):
  # print("st")
  url=domain+'api/videos/detail'
  raw=f'{{"uId":"114514","mvId":"{mv_id}","type":0}}'
  headers={'Host': domain[8:-1],'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46'}
  args=f"data={str.upper(crypto.encrypt(raw))}&sig={sigcode.get_sigcode(str.upper(crypto.encrypt(raw)))}"
  r=requests.post(url=url,data=args,headers=headers)
  text=json_handler.handle(crypto.decrypt(r.text))
  js0n=json.loads(text)
  if js0n['code']!=0:
    raise Exception(js0n)
  # print(js0n['data']['mv_play_url'])
  return js0n['data']['mv_play_url']