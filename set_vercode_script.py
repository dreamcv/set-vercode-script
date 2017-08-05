# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw
import pygame
from numpy.random import randint
import numpy as np


def merge_img(image_list, opt="horizontal"):
# opt= vertical ,horizontal 选择水平显示拼接的图像，或者垂直拼接
    image_num = len(image_list)
    image_size = image_list[0].size
    height = image_size[1]
    width = image_size[0]

    if opt == 'vertical':
        new_img = Image.new('RGB', (width, image_num * height), 255)
    else:
        new_img = Image.new('RGB', (image_num * width, height), 255)

    count = x = y = 0
    for img in image_list:
        new_img.paste(img, (x, y))
        count += 1
        if opt == 'horizontal':
            x += width
        else:
            y += height
    return new_img


def set_sigle_word_img(i):
    pygame.init()
    font = pygame.font.SysFont('Microsoft YaHei', 64)
    # 渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色,; 后面一个选项是背景颜色
    col1 = tuple([randint(0,255) for i in range(3)])
    # col2 = tuple([randint(0,255) for i in range(3)])
    # 字符集合
    az = [chr(x + 97) for x in range(26)]
    az.extend([chr(x + 48) for x in range(10)])
    az.extend([chr(x + 65) for x in range(26)])
    # 产生单字图片
    gaim_word = randint(0, len(az))
    text = u"" + str(az[gaim_word])
    ftext = font.render(text, True, col1, None)
    file = "./temp_img/temp.jpg"
    pygame.image.save(ftext, file)
    # 旋转
    angle = randint(-20, 30)
    im2 = Image.open(file).rotate(angle)
    im2.save("./temp_img/demo" + str(i) + ".png")
    return az[gaim_word]


def set_rand_point(x_len, y_len):
    x = [randint(0, x_len) for i in range(2)]
    y = [randint(0, y_len) for i in range(2)]
    return (x[0], y[0]), (x[1], y[1])


def main():
    temp_file = "./temp_img/temp4.png"
    num = 4
    # 4个数的验证码; 建立四个验证
    ans = [set_sigle_word_img(i+1) for i in range(4)]
    imgs = ["./temp_img/demo"+str(i+1)+".png" for i in range(num)]
    img_list = [Image.open(imgs[i]) for i in range(num)]
    img = merge_img(img_list)

    img.save(temp_file)
    """
    # 加上点噪声；
    from skimage import data, io
    img = data.load(temp_file)
    rows, cols, dims = img.shape

    for i in range(4000):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        color = np.random.randint(0, 255)
        img[x, y, :] = color

    io.imshow(img)
    """
    # 打开图像
    img = Image.open(temp_file)
    img_d = ImageDraw.Draw(img)
    # 获取 图片的 x轴，y轴 像素

    x_len, y_len = img.size
    for x in range(30):
        col1 = tuple([randint(0, 255) for i in range(3)])
        # 两个随机点之间划线
        img_d.line(xy=set_rand_point(x_len, y_len), fill=col1, width=1)

    # 保存图片
    img.save("./result_img/" + "".join(ans) + '.png')
    return

if __name__ == "__main__":
    import time
    start_time = time.time()
    import os
    for _dir in ["./result_img", "./temp_img", ]:
        try:
            os.mkdir(_dir)
        except:
            pass
    n = 200
    [main() for i in range(n)]
    __import__('shutil').rmtree(_dir)
    run_time = time.time() - start_time
    print("生成 " + str(n) + " 个验证码需要 " + str(run_time) + "s 的时间")
