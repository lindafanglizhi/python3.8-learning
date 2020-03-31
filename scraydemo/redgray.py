import os
import cv2

# 彩色变灰色
def RgbToGray(Rfile,Wfile):
    '''
    :param Rfile: 要处理的图像文件夹名
    :param Wfile: 处理后要写入的文件夹名
    '''
    for filename in os.listdir(Rfile):  #遍历文件夹中所有图像
        print(filename)
        file_read = os.path.join(Rfile, filename) #依次读取图像的路径
        img = cv2.imread(file_read) #读取图像
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #将图像灰度化
        file_write = os.path.join(Wfile, filename) #要写入的文件路径
        cv2.imwrite(file_write,gray_img) #处理后的图像写入相应文件夹

# 需要变化的地方就是存入图片的地址和入变化后的图片地址。
RgbToGray('/Users/lindafang/PycharmProjects/scraydemo/images','/Users/lindafang/PycharmProjects/scraydemo/gray_images')


