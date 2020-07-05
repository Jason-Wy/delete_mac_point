
import os


# 清理文件函数
def clear(path):
    print('正在扫描：' + path)
    # 获取目录中的所有文件和文件夹名字
    dir_list = os.listdir(path)
    # print(dir_list)
    # 遍历循环每个目录
    for i in dir_list:
        # 拼接绝对路径
        abspath = os.path.join(os.path.abspath(path), i)

        # 判断是否是文件
        if os.path.isfile(abspath):
            # print(abspath)
            # 判断文件是否是 ._ 开头的文件
            if i.startswith("._"):
                # 删除文件
                # 这是彻底删除 回收站不会存在
                # 这是彻底删除 回收站不会存在
                # 这是彻底删除 回收站不会存在
                os.remove(abspath)
                print('清理文件 : ' + abspath)

        else:
            # 不是文件就继续递归
            clear(abspath)
            pass


if __name__ == '__main__':
    # 设置日志文件的配置

    print("'开始清理...'")

    # 设置要清理的路径
    path = r"/Volumes/工作/SVN/doupingXCX"
    # path = r"../../../../../工作/SVN/"
    clear(path)
    print('操作完毕')
