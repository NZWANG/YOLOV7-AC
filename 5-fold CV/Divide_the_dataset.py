# *_*coding: utf-8 *_*

import os
import random
import shutil
import time


def copyFile(fileDir, origion_path1, class_name):
    name = class_name
    path = origion_path1
    image_list = os.listdir(fileDir)  # 获取图片的原始路径
    image_number = len(image_list)
    train_number = int(image_number * train_rate)

    train_sample1 = random.sample(image_list, train_number)
    test_sample1 = list(set(image_list) - set(train_sample1))

    train_sample2 = random.sample(test_sample1, train_number)
    test_sample2 = list(set(test_sample1) - set(train_sample2))

    train_sample3 = random.sample(test_sample2, train_number)
    test_sample3 = list(set(test_sample2) - set(train_sample3))

    train_sample4 = random.sample(test_sample3, train_number)
    test_sample4 = list(set(test_sample3) - set(train_sample4))

    test_sample5 = list(set(image_list) - set(train_sample1) - set(train_sample2) - set(train_sample3) - set(train_sample4))

    sample = [train_sample1, train_sample2,train_sample3,train_sample4,test_sample5]

    # 复制图像到目标文件夹
    for k in range(len(save_dir)):
        if os.path.isdir(save_dir[k]) and os.path.isdir(save_dir1[k]):
            for name in sample[k]:
                name1 = name.split(".")[0] + '.xml'
                shutil.copy(os.path.join(fileDir, name), os.path.join(save_dir[k], name))
                shutil.copy(os.path.join(path, name1), os.path.join(save_dir1[k], name1))
        else:
            os.makedirs(save_dir[k])
            os.makedirs(save_dir1[k])
            for name in sample[k]:
                name1 = name.split(".")[0] + '.xml'
                shutil.copy(os.path.join(fileDir, name), os.path.join(save_dir[k], name))
                shutil.copy(os.path.join(path, name1), os.path.join(save_dir1[k], name1))


if __name__ == '__main__':
    time_start = time.time()

    # 原始数据集路径
    origion_path = r'.\2021URPC\image/'
    origion_path1 = r'.\2021URPC\annotations/'

    # 保存路径
    save_train1_dir = r'.\2021URPC/train1/images/'
    save_train2_dir = r'.\2021URPC/train2/images/'
    save_train3_dir = r'.\2021URPC/train3/images/'
    save_train4_dir = r'.\2021URPC/train4/images/'
    save_train5_dir = r'.\2021URPC/train5/images/'

    save_train_dir1 = r'.\2021URPC/train1/annotations/'
    save_train_dir2 = r'.\2021URPC/train2/annotations/'
    save_train_dir3 = r'.\2021URPC/train3/annotations/'
    save_train_dir4 = r'.\2021URPC/train4/annotations/'
    save_train_dir5 = r'.\2021URPC/train5/annotations/'
    save_dir = [save_train1_dir, save_train2_dir,save_train3_dir,save_train4_dir,save_train5_dir]
    save_dir1 = [save_train_dir1, save_train_dir2,save_train_dir3,save_train_dir4,save_train_dir5,]

    # 训练集比例
    train_rate = 0.2

    # 数据集类别及数量
    file_list = os.listdir(origion_path)
    num_classes = len(file_list)
    for i in range(num_classes):
        class_name = file_list[i]
    copyFile(origion_path, origion_path1, class_name)
    print('划分完毕!')
    time_end = time.time()
    print('---------------')
    print('训练集和测试集划分共耗时%s!' % (time_end - time_start))
