# -*- coding:utf-8 -*-
# Author: yuyongsheng
# Time: 18-7-18 上午9:00
# Description:将一批txt文件的每一段文本保存成独立的文件

import os
import sys

project_path = os.getcwd()
text_path = project_path+'/text'

# read each sentence
def text_split(file_path):
    output_name = os.path.basename(file_path).split('.')[0]
    global folder_path
    folder_path = text_path + '/' + output_name
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(file_path ,'r') as f_input:
        num = 1
        for sentence in f_input:
            save_file(sentence, output_name, num)
            num +=1


# save each sentence to file
def save_file(sentence, output_name, num):
    global folder_path
    # file name format
    with open(folder_path+'/'+output_name+'_'+str(num).zfill(3)+'.txt', 'w') as f_output:
        f_output.writelines(sentence)

if __name__ == '__main__':
    for root, dirs, files in os.walk(text_path):
        for file in files:
            text_split(root+'/'+file)