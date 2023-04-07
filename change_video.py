import ffmpy3
import json
import os


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
    save_name = title + '_' + str(page) + '_' + part + '.mp4'
    # 检查问题标题
    char_list = ['*', '|', ':', '?', '/', '<', '>', '"', '\\']
    news_title = title
    for code in char_list:
        if code in save_name:
            print('change')
            save_name = save_name.replace(code, "_")  # 防止标题出问题统一改一下
    if print_info:
        print(c1, c2, c3, title, page, part)
        print(audio,video,save_name)
    return [audio,video,save_name]


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
    print('Please ensure ffmpeg input in your computer !important')
    print('open path correspond to PE bili video store path: \Android\data\tv.danmaku.bili\download\, make sure copyed to the computer')
    print('e.g. if now: ------------------')
    print('  download')
    print('  |- 111111111')
    print('  |- 233333333')
    print('     |- c_123456789')
    print('        |- 64')
    print('        |- danmaku.xml')
    print('        |- entry.json')
    print('  |- ...')
    print('  change_format.exe')
    print('  ...')
    print("please input 'download', equal with default")
    dir_open = input("input openpath: ")  # 定制打开路径，不定义的话为当前路径
    print("open path is the path to save changed videos ,default 'output'")
    dir_save = input("input savepath: ")  # 定制存储路径，不定义的话为当前路径
    print('running...')
    if dir_open == '':
        dir_open = './download'
    if dir_save == '':
        dir_save = './output'
    if not os.path.exists(dir_save):  # 确认目录存在，没有则创建
        os.makedirs(dir_save)

    dir_list_1 = next_dir_list([dir_open])
    dir_list_2 = next_dir_list(dir_list_1)
    for index,dir_video in enumerate(dir_list_2):
        [path_audio,path_video,save_name] = deal_video(dir_video)

        path_save = os.path.join(dir_save, save_name)
        if not check_exist(path_video,path_audio):
            print('ignore video error {}'.format(dir_video))
            continue
        ff = ffmpy3.FFmpeg(  # FFmpeg合成音视频
            inputs={path_video: None, path_audio: None},
            outputs={path_save: None},
            global_options='-hide_banner -loglevel error'
        )
        ff.run()
        print('{} video change success, save to {}'.format(index, path_save))

    print('finish')
    os.system('pause')
