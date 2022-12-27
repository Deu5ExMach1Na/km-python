#爬取广场3000赞以上的视频

import kmcore
from downloader import downloader

videos=list()
pagef=12500  #从多少页开始
paget=20000  #结束

for i in range(pagef,paget):
  kmcore.video.get_all_videos(i,20,videos)
  for v in videos:
    if int(v.vlike)<3000:  #爱心数小于3000则跳过
      continue
    v.vurl=kmcore.video.fix_mv_url(v.vid)
    print(f"Starting Download:{v.vtitle}.")
    print(f"Likes:{v.vlike},url:{v.vurl}")
    try:
      downloader(v.vurl,8,v.vtitle+'.mp4').main()
    except Exception :
      i=i-1
      print(f"Failed. ID:{v.vid}.")
  videos.clear()