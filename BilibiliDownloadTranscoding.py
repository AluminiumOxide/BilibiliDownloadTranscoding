'''
BilibiliDownloadTranscoding beta 1.2
2019/11/20
AluminiumOxide
'''

import ffmpy3
import json
import os
diyopen = input("input openpath: ")    #定制打开路径，不定义的话为当前路径
diysave = input("input savepath: ")    #定制存储路径，不定义的话为当前路径
if diyopen == '':
    diyopen = '.'
if diysave == '':
    diysave = '.'

for dirlist in os.listdir(diyopen):    #遍历当前目录里面所有文件
    if os.path.isdir(dirlist):         #如果是文件夹，试着处理它
        print(dirlist)
        path =diyopen +'\\'+dirlist

        for i in os.listdir(path):     #遍历文件夹下层目录，对每集视频进行处理

            layer1 = path+"\\"+i+"\\"                #第一层目录-------
            if not os.path.exists(layer1+"entry.json"):
                break                                #假如没有entry.json则认为不是B站缓存，去下一个文件夹
            with open(layer1+"entry.json",'r',encoding='UTF-8') as f:
                data = json.load(f)                  #加载json文件
                title= data['title']                 #提取 视频标题
                page = data['page_data']['page']     #提取 视频序号
                part = data['page_data']['part']     #提取 视频名称

                char_list = ['*', '|', ':', '?', '/', '<', '>', '"', '\\']
                news_title = title
                for code in char_list:
                    if code in title:
                        news_title = title.replace(code, "_")  #防止标题出问题统一改一下

                print(news_title+'  >  '+str(page)+' '+part)   #打印信息

                layer2= layer1+"64\\"                #第二层目录-------
                audio = layer2 + "audio.m4s"         #对应音频
                video = layer2 + "video.m4s"         #对应视频
                dir = diysave+"\\"+news_title        #储存目录          ---待扩展
                combine = dir +"\\"+part+".mp4"      #储存文件          ---待扩展

                if not os.path.exists(dir):          #确认目录存在，没有则创建
                    print(dir)

                    os.makedirs(dir)
                    # print('创建文件夹: ' + dir.split("\\",1)[1])

                if os.path.exists(combine):          #确认文件存在，若有则跳过
                    continue

                ff = ffmpy3.FFmpeg(                  #FFmpeg合成音视频
                    inputs={video : None,audio : None},
                    outputs = {combine : None}
                    )
                ff.run()

