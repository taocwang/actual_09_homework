#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
因为不确定需要拷贝的文件是什么格式，所以使用二进制读取文件并拷贝到目的文件。
为了解决拷贝大文件的时候机器内存不足，设定了每次读取文件的字节数，该字节数可以自己设置。
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
def CopyFile(SrcFile,DestFile,TmpSize):
    SF=open(SrcFile,'rb')
    DF=open(DestFile,'wb')
    try:
        while True:
            Tmp=SF.read(TmpSize)
            if not Tmp:
                break
            DF.write(Tmp)
    except Exception ,e:
        print 'Error:源文件:%s目的文件%s文件复制失败：'%(SrcFile,DestFile),e
    finally:
        SF.close()
        DF.close()
        
if __name__ == "__main__":
    CopyFile('www_access_20140823.log', 'test3.txt', 1024)