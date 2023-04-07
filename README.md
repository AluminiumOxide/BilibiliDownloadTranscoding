## BilibiliDownloadTranscoding

Use python FFmpy transcoding bilibili Mobile terminal download file to MP4 
+ JJdown老是崩掉受不了了，直接使用FFmpeg批量转手机上的m4s文件到mp4
+ 需要jjmpy3库

## 使用方法:

+ 把B站移动端缓存的视频复制到电脑上，脚本和AV号目录放在同一个目录下
+ 首先输入输入目录
+ 再输入保存目录
+    不输入默认是当前目录

## 2023/04/07更新

克隆仓库后，直接使用`change_video.exe`即可

就是直接用`change_video.py`拿pyinstaller导出的，在命令行里提示应该能记得比较清楚

```
pyinstaller -F -i image.ico change_video.py
```

`-i image.ico`就是个封面，可忽略
