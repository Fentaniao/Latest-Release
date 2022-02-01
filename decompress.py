# gz： 即gzip。通常仅仅能压缩一个文件。与tar结合起来就能够实现先打包，再压缩。
# tar： linux系统下的打包工具。仅仅打包。不压缩
# tgz：即tar.gz。先用tar打包，然后再用gz压缩得到的文件
# zip： 不同于gzip。尽管使用相似的算法，能够打包压缩多个文件。只是分别压缩文件。压缩率低于tar。
# rar：打包压缩文件。最初用于DOS，基于window操作系统。

import gzip
import os
import tarfile
import zipfile

import rarfile


# gz
# 因为gz一般仅仅压缩一个文件，全部常与其它打包工具一起工作。比方能够先用tar打包为XXX.tar,然后在压缩为XXX.tar.gz
# 解压gz，事实上就是读出当中的单一文件
def un_gz(file_name):
    """ungz zip file"""
    f_name = file_name.replace('.gz', '')
    # 获取文件的名称，去掉
    g_file = gzip.GzipFile(file_name)
    # 创建gzip对象
    open(f_name, 'w+').write(g_file.read())
    # gzip对象用read()打开后，写入open()建立的文件里。
    g_file.close()
    # 关闭gzip对象


# tar
# XXX.tar.gz解压后得到XXX.tar，还要进一步解压出来。
# 注：tgz与tar.gz是同样的格式，老版本号DOS扩展名最多三个字符，故用tgz表示。
# 因为这里有多个文件，我们先读取全部文件名称。然后解压。例如以下：
# 注：tgz文件与tar文件同样的解压方法。
def un_tar(file_name):
    # untar zip file"""
    tar = tarfile.open(file_name)
    names = tar.getnames()
    # 因为解压后是很多文件，预先建立同名目录
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for name in names:
        tar.extract(name, file_name + "_files/")
    tar.close()


# zip
# 与tar类似，先读取多个文件名称，然后解压。例如以下：

def un_zip(file_path,file_name, way):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_path+'/'+file_name)
    if way == 'auto':
        compress_to = file_path
    else:
        if os.path.isdir(file_name + '_files'):
            pass
        else:
            os.mkdir(file_name + '_files')
        compress_to = file_name + '_files/'
    for names in zip_file.namelist():
        zip_file.extract(names, compress_to)
    zip_file.close()


# rar
# 由于rar通常为window下使用，须要额外的Python包rarfile。
# 可用地址： http://sourceforge.net/projects/rarfile.berlios/files/rarfile-2.4.tar.gz/download
# 解压到Python安装文件夹的/Scripts/文件夹下，在当前窗体打开命令行,
# 输入Python setup.py install
# 安装完毕。
def un_rar(file_name):
    """unrar zip file"""
    rar = rarfile.RarFile(file_name)
    if os.path.isdir(file_name + '_files'):
        pass
    else:
        os.mkdir(file_name + '_files')
    os.chdir(file_name + '_files')
    rar.extractall()
    rar.close()

# inputname = 'test/Liquid/v0.3.4/Liquid.zip'
# un_zip(inputname)
# un_gz(inputname)
# un_rar(inputname)
# un_tar(inputname)
