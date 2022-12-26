### 获取视频列表
---
```python
import kmcore.video

page=1  #页数
perpage=19  #视屏个数

videos=list()

kmcore.video.get_hot_videos(page,perpage,videos)  #热门
kmcore.video.get_all_videos(page,perpage,videos)  #广场

uId=19260817  #用户Id

kmcore.video.get_fav_videos(page,perpage,uId,videos)  #获取该用户收藏夹内容

for mv in videos:
    print(mv.vtitle,mv.vurl)
```





### 获取评论区内容

---

```python
import kmcore.comment

mvid=114514  #视频id
page=1  #页数

comments=list()

kmcore.comment.get_all_comments(mvid,page,comments)

for comment in comments
    print(comment.vname)

```

