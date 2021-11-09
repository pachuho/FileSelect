import os
import time
from datetime import datetime

root_dir = '/Users/juhopark/Desktop'
now = datetime.now()


# 루트 폴더 하위 파일 추출
def print_files_in_dir(target_dir, prefix):
    file_list = os.listdir(target_dir)
    for file in file_list:
        path = os.path.join(target_dir + "/" + file)
        if os.path.isdir(path):  # 폴더라면 재귀처리
            print_files_in_dir(path, prefix + "     ")
        else:
            try:
                create_time = time.ctime(os.path.getctime(path))
                modify_time = time.ctime(os.path.getmtime(path))
                print("%s  |  %s" % (create_time, modify_time), end='  |  ')
                print(path)
            except:
                print("Error!")
                pass


def print_current_time():
    print(now)


if __name__ == '__main__':
    print_current_time()
    print("===========생성날짜=======================수정날짜==========================파일경로===============")
    print_files_in_dir(root_dir, "")
