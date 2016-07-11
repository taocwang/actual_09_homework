#!/bin/env python
#coding:utf-8
import sys,os,argparse

if __name__ == '__main__':
    _argparse=argparse.ArgumentParser()
    _argparse.add_argument('-H','--host',help="host name or IP",default='localhost')
    _argparse.add_argument('-p','--port',help="rs port",type=int)
    _argparse.add_argument('-C','--cmds',nargs='+',type=str,help="要执行的命令，多个命令之间用,分割",default=[])
    _args=_argparse.parse_args()

    print _args.host
    print _args.port
    print _args.cmds

    print len(sys.argv)
    print len(_args.cmds)

    if len(_args.cmds) == 0:
        _argparse.print_help()