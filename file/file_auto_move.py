#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys, re, shutil

printColor = '\033[0;32m'

def show_help():
    print('\033[1;33m')
    print('会不会用? 辣鸡')
    print('\033[1;32m')
    sys.exit(0)

def execute(args = []):
    try:
        file = args.pop(0)
        fromDir = args.pop(0)
        toDir = args.pop(0)

        # 验证参数
        if not os.path.isfile(file):
            error('no such file')
            return False
        if not os.path.isdir(fromDir):
            error('fromdir not exists: ' + fromDir)
            return False
        if not os.path.isdir(toDir):
            error('todir not exists: ' + toDir)
            return False

        # 读取文件并按行处理
        # 将来源文件直接覆盖到目标文件
        with open(file, 'r') as fr:
            content = fr.read()

        items = list(set(content.split('\n')))

        if (len(items) < 1):
            error('no such content in file.')

        info('starting...')

        for item in items:
            if (len(item) < 1):
                continue

            sourceFile = fromDir.rstrip('/') + '/' + item
            if (not os.path.isfile(sourceFile)):
                notice('can not locate file: ' + sourceFile)
                continue

            targetFile = toDir.rstrip('/') + '/' + item
            # 分隔出文件和文件夹的名称
            targetPathInfo = os.path.split(targetFile)

            targetDir = targetPathInfo[0]

            # 文件夹不存在时自动创建新文件夹: mkdir -p
            if (not os.path.isdir(targetDir)):
                os.makedirs(targetDir)

            info('moving: ' + sourceFile + ' >>> ' + targetFile)
            # 复制文件
            shutil.copy(sourceFile, targetDir);

    except Exception as e:
        print('\033[0;31mError!!!')
        print(Exception)
        print(e)
        print('\033[0m')
    finally:
        done()
        sys.exit(0)

def info(text = ''):
    print(printColor + text)

def done():
    print(printColor + 'Done.\033[0m')
    sys.exit(0)


def error(text = ''):
    print('\033[0;31m' + text + printColor)


def notice(text = ''):
    print('\033[0;33m' + text + printColor)


if __name__ == '__main__':
    args = sys.argv

    if '--help' in args or len(args) < 4:
        show_help()
    else:
        # 去除脚本文件名
        args.pop(0)
        execute(args)