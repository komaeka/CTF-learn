import os
from time import sleep
import datetime

# 递归获取当前linux目录下所有文件名
def get_all_file(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

# 循环get_all_file(".")函数，如果下一次的返回值不同于上一次，就打印警告

if __name__ == "__main__":
    file_list_pre = get_all_file(".")
    now_time = datetime.datetime.now().strftime("%H:%M")
    warning = ""
    while True:
        file_list_change = get_all_file(".")
        if len(file_list_change) > len(file_list_pre):
            warning = now_time+'--'+"警告: 有新文件加入，新加入的文件为："+str(set(file_list_change).difference(set(file_list_pre)))
            print(warning)
        elif len(file_list_change) < len(file_list_pre):
            warning = now_time+'--'+"警告: 有文件被删除，被删除的文件为："+str(set(file_list_pre).difference(set(file_list_change)))
            print(warning)
        else:
            info = now_time+'--'+"目录中暂无变化"
            print(info)
        if warning != "":
            with open("warning.log", "a") as f:
                f.writelines(warning+'\n')
        sleep(3)
