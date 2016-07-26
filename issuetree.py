import os
import sys
def tree(pre,filepath):
#遍历filepath下所有文件，包括子目录
  files = os.listdir(filepath)
  for f in files:
    fullpath = os.path.join(filepath,f)
    if (f == files[-1]):
        print('{}{}{}{}'.format(pre, '└','── ', os.path.basename(fullpath)))
    else:
        print('{}{}{}{}'.format(pre, '├','── ', os.path.basename(fullpath)))
    if os.path.isdir(fullpath):
        if (fullpath == filepath + files[-1]):
            tree(pre + ' ' + '   ' ,fullpath)
        else:
            tree(pre + '│' + '   ' ,fullpath)

try:
        l = [1]
        l[0] = sys.argv[1]

except BaseException:
         l[0] = os.getcwd()

tree('',l[0])