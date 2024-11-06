import os
import shutil
import random

def split_images_into_four(source_dir):
    # 원본 디렉토리에서 파일 목록을 가져옵니다.
    images = [f for f in os.listdir(source_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))]
    
    # 이미지를 랜덤하게 섞습니다.
    random.shuffle(images)

    # 4개의 디렉토리 생성 (존재하지 않으면 생성)
    output_dirs = [os.path.join(source_dir, f"folder_{i+1}") for i in range(4)]
    for dir_path in output_dirs:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # 이미지를 4개의 디렉토리로 분배
    for i, image in enumerate(images):
        dest_dir = output_dirs[i % 4]  # 이미지 순서에 따라 디렉토리 분배
        src_path = os.path.join(source_dir, image)
        dest_path = os.path.join(dest_dir, image)
        
        # 파일을 목적지로 이동
        shutil.move(src_path, dest_path)
        print(f"Moved {image} to {dest_dir}")

# 예시로 사용할 디렉토리 경로 (사용자가 수정 필요)
source_directory = './img_capture_1'
split_images_into_four(source_directory)
