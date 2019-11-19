import ffmpy3
import json
import os

path = '.\\AV20191119'         #这是AV号，以后换成要处理的文件夹吧 ---待扩展

for i in os.listdir(path):     #遍历AV下层目录，对每集视频进行处理

    layer1 = path+"\\"+i+"\\"                #第一层目录-------
    with open(layer1+"entry.json",'r',encoding='UTF-8') as f:
        data = json.load(f)                  #加载json文件
        title= data['title']                 #提取 视频标题
        page = data['page_data']['page']     #提取 视频序号
        part = data['page_data']['part']     #提取 视频名称

        # print(title+'  >  '+str(page)+' '+part)   #打印信息

        layer2= layer1+"64\\"                #第二层目录-------
        audio = layer2 + "audio.m4s"         #对应音频
        video = layer2 + "video.m4s"         #对应视频
        dir = ".\\"+title                    #储存目录          ---待扩展
        combine = dir +"\\"+part+".mp4"      #储存文件          ---待扩展

        if not os.path.exists(dir):          #确认目录存在，没有则创建
            os.makedirs(dir)
            # print('创建文件夹: ' + dir.split("\\",1)[1])

        if os.path.exists(combine):          #确认文件存在，若有则跳过
            continue

        ff = ffmpy3.FFmpeg(                  #FFmpeg合成音视频
            inputs={video : None,audio : None},
            outputs = {combine : None}
            )
        ff.run()




