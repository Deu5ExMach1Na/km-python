### 获取视频列表
---
```python
import kmcore.video

page=1  #页数
perpage=19  #只能是19,暂时没用

videos=list()

kmcore.video.get_hot_videos(page,perpage,videos)  #热门
kmcore.video.get_all_videos(page,perpage,videos)  #广场
```





