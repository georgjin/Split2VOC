import os
import shutil
import random

data_dir = "F:\南信大行人摩特车数据归档"
images_dir = os.path.join(data_dir, "images")
labels_dir = os.path.join(data_dir, "label")
images = os.listdir(images_dir)
labels = os.listdir(labels_dir)

my_list = [image[:-4] for image in images]

num_train = int(len(images) * 0.8)
num_valid = int(len(images) * 0.1)
num_test = len(images) - num_train - num_valid

if not os.path.exists("VOC2007"):
    os.mkdir("VOC2007")
if not os.path.exists("VOC2007/test"):
    os.mkdir("VOC2007/test")
if not os.path.exists("VOC2007/train"):
    os.mkdir("VOC2007/train")
if not os.path.exists("VOC2007/valid"):
    os.mkdir("VOC2007/valid")
if not os.path.exists("VOC2007/test/images"):
    os.mkdir("VOC2007/test/images")
if not os.path.exists("VOC2007/test/labels"):
    os.mkdir("VOC2007/test/labels")
if not os.path.exists("VOC2007/train/images"):
    os.mkdir("VOC2007/train/images")
if not os.path.exists("VOC2007/train/labels"):
    os.mkdir("VOC2007/train/labels")
if not os.path.exists("VOC2007/valid/images"):
    os.mkdir("VOC2007/valid/images")
if not os.path.exists("VOC2007/valid/labels"):
    os.mkdir("VOC2007/valid/labels")

random.shuffle(my_list)
train_lists = my_list[:num_train]
valid_lists = my_list[num_train:num_train + num_valid]
test_lists = my_list[num_train + num_valid:]

def write_image(src_dir, dst_dir, lists):
    for list in lists:
        src_file = os.path.join(src_dir, list + ".jpg")
        if not os.path.exists(src_file):
            src_file = os.path.join(src_dir, list + ".png")
        dst_file = os.path.join(dst_dir, list + ".jpg")
        if not os.path.exists(dst_file):
            dst_file = os.path.join(dst_dir, list + ".png")
        shutil.copy2(src_file, dst_file)


def write_txt(src_dir, dst_dir, lists):
    for list in lists:
        src_file = os.path.join(src_dir, list + ".txt")
        dst_file = os.path.join(dst_dir, list + ".txt")
        shutil.copy2(src_file, dst_file)

def write_image_list_to_file():
    write_image("images", "VOC2007/train/images", train_lists)
    write_image("images", "VOC2007/valid/images", valid_lists)
    write_image("images", "VOC2007/test/images", test_lists)


def write_label_list_to_file():
    write_txt("label", "VOC2007/train/labels", train_lists)
    write_txt("label", "VOC2007/valid/labels", valid_lists)
    write_txt("label", "VOC2007/test/labels", test_lists)


write_image_list_to_file()
write_label_list_to_file()
print("train: %d, valid: %d, test: %d" % (num_train, num_valid, num_test))
print("Done!")
