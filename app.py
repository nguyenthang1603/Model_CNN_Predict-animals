

import os
import random
import shutil

# Đường dẫn tới thư mục chứa ảnh
data_dir = "D:/data/train"
# Số lượng ảnh bạn muốn lấy
num_images_to_select = 200

# Danh sách các tên tệp ảnh trong thư mục
image_names = os.listdir(data_dir)

# Lựa chọn ngẫu nhiên 100 tệp ảnh từ danh sách
selected_image_names = random.sample(image_names, num_images_to_select)

# Tạo một thư mục mới để lưu trữ các ảnh được chọn
selected_images_dir = "D:/data/val"
os.makedirs(selected_images_dir, exist_ok=True)

# Sao chép các tệp ảnh đã chọn vào thư mục mới
for image_name in selected_image_names:
    src = os.path.join(data_dir, image_name)
    dst = os.path.join(selected_images_dir, image_name)
    shutil.copyfile(src, dst)

print("Đã sao chép thành công", num_images_to_select, "ảnh vào thư mục mới.")

# Xóa các ảnh đã sao chép khỏi thư mục gốc
for image_name in selected_image_names:
    os.remove(os.path.join(data_dir, image_name))

print("Đã xóa các ảnh đã sao chép khỏi thư mục gốc.")