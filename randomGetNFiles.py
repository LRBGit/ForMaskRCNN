import random
import os
import shutil

def random_copyfile(srcPath,dstPath,numfiles):
    name_list=list(os.path.join(srcPath,name) for name in os.listdir(srcPath))
    random_name_list=list(random.sample(name_list,numfiles))
    if not os.path.exists(dstPath):
        os.mkdir(dstPath)
    for oldname in random_name_list:
        shutil.copyfile(oldname,oldname.replace(srcPath, dstPath))

srcPath='F:\\dataset\\cocodatasets2014\\train2014'         
dstPath='F:\\dataset\\cocodatasets2014\\4000train2014'
random_copyfile(srcPath,dstPath,4000)

