
import cv2
from pathlib import Path

# 데이터 로드
data_path = 'C:/Users/user/Desktop/seaweed_data/captured_images'
file = 'image_141.jpg'
path = str(Path(data_path, file))
img = cv2.imread(path)  # 이미지 로드
# print(img.shape)

# 이미지 자르기
w_interval, h_interval = 4, 6
x_interval, y_interval = img.shape[0] // w_interval, img.shape[1] // h_interval
x, y = x_interval, y_interval  
w, h = x * w_interval,  y * h_interval
cropped_img = img[y:(y + h), x:(x + w)]

# 결과 보기
cv2.imshow('origin', img)
# cv2.imshow('crop img', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()





# 이미지 저장