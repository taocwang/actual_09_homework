#/bin/env python
#encoding:utf-8
import os
import argparse

all_files=[]
def list_all_files(dir):
    for _col in os.listdir(dir):
        real_path=os.path.join(dir,_col)
        if os.path.isdir(real_path):
            list_all_files(real_path)
        else:
            all_files.append(real_path)
    return all_files

#为防止\t \n转义，路径请用r格式化

if __name__ == '__main__':
    _argparse=argparse.ArgumentParser()
    _argparse.add_argument('-p','--path',help="dir path")
    _args=_argparse.parse_args()
    print _args.path
    for i in list_all_files(r'C:\Users\Administrator\PycharmProjects\test_project\reboot\10'):
        print i