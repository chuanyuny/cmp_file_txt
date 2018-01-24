#!/usr/bin/python
#-*- coding:utf-8 -*-
'''

该py文件主要用于对比两个文件夹内txt文档内容是否相同。
运行完该py文件后，在result文件夹下会有html文件展示结果。
目录结构为：
result   #最后所有的对比结果即html文件都在result文件夹中
|
table_data_new--1.txt
|             --2.txt
|             --3.txt
table_data_old--1.txt
|             --2.txt
|             --3.txt
compare_txt.py

'''
import difflib
import time
import os

def read_txt(path):
	fo=open(path,'r',encoding="utf-8")
	content=fo.readlines()
	return content

def aa(filename,tablename):
	path='./result/'+tablename+'.%f.html'%time.time()
	diffmkfile = open(path,'w',encoding="utf-8")
	# diffmkfile = open('./result/.%f.html' % time.time(),'w',encoding="utf-8")
	diffmkfile.write("<meta charset='utf-8'>")
	diffmkfile.write(filename)
	diffmkfile.close()
	time.sleep(0.5)

def file_name(file_dir):  #file_dir为文件目录
	filename=[]
	for root,dirs,files in os.walk(file_dir):
		filename=files  #输出当前目录下所有非目录的文件名
	return filename   #list


if __name__=="__main__":	
	all_txt=file_name("./table_data_old/")   #以一个文件夹中所有txt为基准，来对比另一个文件夹txt
	for each in all_txt:
		try:
			txt1=read_txt("./table_data_old/"+each.strip())
			txt2=read_txt("./table_data_new/"+each.strip())
		except:
			print("其中一个文件夹没有%s"%each.strip())
		else:
			d=difflib.HtmlDiff()
			aa(d.make_file(txt1,txt2),each.strip('.txt\n'))
			print("%s对比成功！"%each.strip())
		
