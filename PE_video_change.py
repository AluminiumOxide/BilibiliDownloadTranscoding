# import ffmpy3
import json
import os
import subprocess


def next_dir_list(dir_pro_list,print_info=False):
    """

    :param dir_pro_list: 传入列表，每个元素储存着一个路径
    :return:
    """
    dir_list = []
    for dir_pro in dir_pro_list:
        for dir_now in os.listdir(dir_pro):
            dir_mix = os.path.join(dir_pro,dir_now)
            dir_list.append(dir_mix)
            if print_info:
                print(dir_mix)
    return dir_list


def deal_video(proto_path,print_info=False):
    json_path = os.path.join(proto_path, 'entry.json')
    with open(json_path, 'r', encoding='UTF-8') as f:
        data = json.load(f)  # 加载json文件
        if print_info:
            print(json.dumps(data, indent=4, sort_keys=True,ensure_ascii=False))
        title = data['title']  # 提取 视频标题
        owner_name = data['owner_name']
        page = data['page_data']['page']  # 提取 视频序号
        part = ''  # 提取 切片子名称
        if 'part' in data['page_data']:  # 有的不存在
            part = data['page_data']['part']
        if part == title:
            part = ''
        c1 = data['prefered_video_quality']  # 这三个内容一样，主要不想往下面走了
        c2 = data['type_tag']
        c3 = data['video_quality']

    audio = os.path.join(proto_path, str(c3), "audio.m4s")
    video = os.path.join(proto_path, str(c3), "video.m4s")
    save_name = title + '-' + str(page) + '-' + part + '.mp4'
    # 检查问题标题
    char_list = ['*', '|', ':', '?', '/', '<', '>', '"', '\\','&',' ']
    news_title = title
    for code in char_list:
        if code in save_name:
            save_name = save_name.replace(code, "_")  # 防止标题出问题统一改一下
            print('change save_name to:{}'.format(save_name))
    for code in char_list:
        if code in owner_name:
            owner_name = owner_name.replace(code, "_")  # 防止标题出问题统一改一下
            print('change owner_name to:{}'.format(owner_name))

    if print_info:
        print(c1, c2, c3, title, page, part)
        print(audio,video,save_name)
    return [audio,video,save_name,owner_name]


def check_exist(path_video,path_audio):
    pass_video = False
    pass_audio = False
    if os.path.exists(path_video):
        pass_video = True
    if os.path.exists(path_audio):
        pass_audio = True
    if pass_video and pass_audio:
        return True
    return False


if __name__ == '__main__':
    # dir_open = "./download"  # 定制打开路径，不定义的话为当前路径
    # dir_save = "./output"  # 定制打开路径，不定义的话为当前路径
    print('尽管和ffmpeg一起打包了,但是还是建议电脑已安装ffmpeg,并可直接通过cmd调用')
    print('复制PE的视频缓存: \Android\data\tv.danmaku.bili\download\ (包括download\目录)到exe文件相同的路径下')
    print('e.g. ------------------')
    print(' download')
    print('  |- 111111111')
    print('  |- 233333333')
    print('     |- c_123456789')
    print('        |- 64')
    print('        |- danmaku.xml')
    print('        |- entry.json')
    print('  |- ...')
    print(' change_format.exe')
    print('-----------------------')
    print("设置输入目录,默认:'./download'")
    dir_open = input("输入目录: ")  # 定制打开路径，不定义的话为当前路径
    print("设置输出目录,默认:'./output'")
    dir_save = input("输出目录: ")  # 定制存储路径，不定义的话为当前路径
    print('开始转码(‾v‾)...')
    if dir_open == '':
        dir_open = './download'
    if dir_save == '':
        dir_save = './output'
    if not os.path.exists(dir_save):  # 确认目录存在，没有则创建
        os.makedirs(dir_save)

    dir_list_1 = next_dir_list([dir_open])
    dir_list_2 = next_dir_list(dir_list_1)

    ## 设计ffmpeg的路径
    dir_now = os.path.dirname(os.path.abspath(__file__))  # 获取当前目录
    dir_ffmpeg = os.path.join(dir_now, 'ffmpeg.exe')

    for index,dir_video in enumerate(dir_list_2):
        [path_audio,path_video,save_name,save_owner] = deal_video(dir_video)

        path_save = os.path.join(dir_save,save_owner, save_name)
        if not os.path.exists(os.path.join(dir_save, save_owner)):  # 确认目录存在，没有则创建
            os.makedirs(os.path.join(dir_save, save_owner))
        if not check_exist(path_video,path_audio):
            print('ignore video error {}'.format(dir_video))
            with open('有问题的索引.txt', 'a', encoding='utf-8') as f:
                f.write(os.path.basename(os.path.dirname(dir_video)) + "\n")
            continue


        command = dir_ffmpeg + ' -i ' + path_video + ' -i ' + path_audio + ' -codec copy ' + path_save + ' -hide_banner -loglevel quiet'
        subprocess.run(command)
        # os.system(command)
        print('{} video {} change success, save to {}'.format(index,os.path.basename(os.path.dirname(dir_video)), path_save))

    print('转码结束')
    os.system('pause')
