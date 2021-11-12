import os
import time
from datetime import datetime
import shutil

root_dir = '/Users/juhopark/Downloads'

now = datetime.now().timestamp()

# 루트 폴더 하위 파일 추출
def print_files_in_dir(target_dir, prefix):
    file_list = os.listdir(target_dir)
    for file in file_list:
        path = os.path.join(target_dir + "/" + file)

        if os.path.isdir(path):  # 폴더라면 재귀처리
            print_files_in_dir(path, prefix + "     ")
        else:
            try:
                # 생성일
                create_time = os.stat(path).st_ctime
                diff_day_create = (now - create_time) / (24 * 60 * 60)

                # 수정일
                modify_time = os.stat(path).st_mtime
                diff_day_modify = (now - modify_time) / (24 * 60 * 60)

                # 생성일 or 수정일이 48시간 이상일 경우
                if diff_day_create > 48 or diff_day_modify > 48:
                    continue


                print("create: " + time.ctime(create_time), end=" ")
                print("modify: " + time.ctime(modify_time), end=" ")
                print("diff days: " + str(diff_day_create), end=' ')
                print(path)

                # 파일 복사
                destination = "/Users/juhopark/Desktop/result"
                file_name = path.split('/')[-1]
                shutil.copyfile(path, destination + "/" + file_name)

            except:
                print("Error!")
            # try:
            #     # 생성시간 기준
            #     create_time = time.gmtime(os.path.getctime(path))
            #
            #     year = str(create_time.tm_year)
            #     mon = str(create_time.tm_mon)
            #     day = str(create_time.tm_mday)
            #     hour = str(create_time.tm_hour + 9)  # UTC 기준 9시간이 느리므로
            #     min = str(create_time.tm_min)
            #
            #     date_to_create = datetime.strptime(year + mon + day + " " + hour + min, "%Y%m%d %H%M")
            #     date_diff = now - date_to_create
            #
            #     if date_diff.days > 3:
            #         continue
            #
            #     date_diff_hour = (date_diff.days * 24) + (date_diff.seconds / 3600)
            #
            #     if date_diff_hour <= 48:
            #         print(date_to_create, end='  ')
            #         print(date_diff.seconds / 3600, end='  ')
            #         print(path)
            #
            # except ValueError as e:
            #     print("Error: ", e, end=' ')
            #     print(path)


if __name__ == '__main__':
    print(now)
    print_files_in_dir(root_dir, "")
