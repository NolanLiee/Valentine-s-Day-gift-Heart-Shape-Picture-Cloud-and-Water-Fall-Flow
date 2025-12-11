import os
import subprocess

# 源文件夹路径
source_folder = '/Users/nolanliee/Documents/gift/images/origin'
# 目标文件夹路径
target_folder = '/Users/nolanliee/Documents/gift/images/full1'

# 创建目标文件夹
os.makedirs(target_folder, exist_ok=True)

# 获取源文件夹中的所有图片文件
image_files = [f for f in os.listdir(source_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# 批量处理图片
for i, filename in enumerate(image_files, start=1):
    source_path = os.path.join(source_folder, filename)
    target_path = os.path.join(target_folder, f'{i:03d}.jpg')
    
    # 使用 ImageMagick 缩放图片
    subprocess.run(['magick', source_path, target_path])

print(f'处理完成，共处理了 {len(image_files)} 张图片。')