import os
from skimage import io,transform,color
import numpy as np

path_name='F:\\dataset\\cocodatasets2014\\lastv5val2014'
#path_name :表示你需 要批量改的文件夹
i=0

def convert_gray2rgb(f, **args):
    gray = io.imread(f)
    rgb = color.gray2rgb(gray)
    return rgb

str=path_name + '/*.jpg'
coll = io.ImageCollection(str, load_func=convert_gray2rgb)#批处理
for i in range(len(coll)):
    io.imsave(r'F:\\dataset\\cocodatasets2014\\rgblastv5val2014\\'+np.str(i)+'.jpg', coll[i])#保存至路径

