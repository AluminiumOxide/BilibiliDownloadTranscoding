## BilibiliDownloadTranscoding

Use python FFmpy transcoding bilibili Mobile terminal download file to MP4 
+ JJdown老是崩掉受不了了，直接使用FFmpeg批量转手机上的m4s文件到mp4
+ ~~需要jjmpy3库~~
+ 需要确保exe文件能调用到ffmpeg一起传了，下载地址
    [Download FFmpeg](https://ffmpeg.org/download.html) →[Builds - CODEX FFMPEG @ gyan.dev ](https://www.gyan.dev/ffmpeg/builds/)→[ffmpeg-release](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)
    直接到最后那个地址下载也行，然后解压压缩包得到ffmpeg.exe，不下载也行，反正这有

## 使用方法:

+ 把B站移动端缓存的视频复制到电脑上，脚本和AV号目录放在同一个目录下
+ 先输入：输入目录（默认download）
+ 再输入：输出目录（默认output）
+    不输入默认是当前目录

## 2023/04/07更新

克隆仓库后，直接使用`change_video.exe`即可，最好确保电脑安装了`ffmpeg`如果报错，就把`ffmpeg.exe`放在同名目录下

就是直接用`PE_video_change.py`拿`auto-py-to-exe`导出的，在命令行里提示应该能记得比较清楚

```
pyinstaller --noconfirm --onefile --console --add-data "./ffmpeg.exe;."  "./PE_video_change.py"
```

以后再慢慢改，反正能跑就行
