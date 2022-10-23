from cv2 import imshow
import numpy as np
import cv2
import sys


# img_size1 = (240, 320)
# img_size2 = (240, 320, 3)

# img1 = np.empty(img_size1, dtype=np.uint8)
# img2 = np.zeros(img_size2, dtype=np.uint8)
# img3 = np.ones(img_size2, dtype=np.uint8)
# img4 = np.full(img_size2, )




# img1 = cv2.imread('HappyFish.jpg')

# img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱
# img3 = img1[40:120, 30:150].copy()

# img2.fill(0)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.waitKey()
# cv2.destroyAllWindows()

#################################################################################


# 마스크 영상을 이용한 영상 합성
# src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
# mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
# dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

# if src is None or mask is None or dst is None:
#     print('Image load failed!')
#     sys.exit()

# cv2.copyTo(src, mask, dst)
# # dst[mask > 0] = src[mask > 0]

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.imshow('mask', mask)
# cv2.waitKey()
# cv2.destroyAllWindows()

#######################################################################

# logo = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)

# cv2.imshow('logo', logo)
# cv2.waitKey()
# cv2.destroyAllWindows()



#########################################################################

# 알파 채널을 마스크 영상으로 이용
# src = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)
# logo = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)  # cv2.IMREAD_UNCHANGED 
#                                                                   #         ㄴ> channel 4개 (앞에 3개 컬러, 마지막은 마스크 처럼 사용가능)

# if src is None or logo is None:
#     print('Image load failed!')
#     sys.exit()

# mask = logo[:, :, 3]    # mask는 알파 채널로 만든 마스크 영상
# logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
# h, w = mask.shape[:2]
# crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출

# cv2.imshow('crop', crop)
# cv2.copyTo(logo, mask, crop)
# # #crop[mask > 0] = logo[mask > 0]

# cv2.imshow('src', src)
# cv2.imshow('logo', logo)
# cv2.imshow('mask', mask)
# cv2.waitKey()
# cv2.destroyAllWindows()

##############################################################################################
############################## OpenCV 그리기 함수 #############################################
##############################################################################################





##############################################################################################
############################## openCV 카메라 출력 #############################################
##############################################################################################

# import sys
# import cv2

# cap = cv2.VideoCapture(0)
# # cap.open(0)

# if not cap.isOpened():
#     print('camera open failed!')
#     sys.exit()

# w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(w, h)

# while True:
#     ret, frame = cap.read()
    
#     if not ret:
#         break
    
#     edge = cv2.Canny(frame, 50, 150)
    
#     cv2.imshow('frame', frame)
#     cv2.imshow('edge', edge)
#     if cv2.waitKey(20) == 27: # ESC
#         break

# cap.release()
# cv2.destroyAllWindows()



##############################################################################################
################################# mouse callback #############################################
##############################################################################################

# import sys
# import numpy as np
# import cv2

# def on_mouse(event, x, y, flags, param):
    
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(f'EVENT_LBUTTONDONW: {x}, {y}')
#     elif event == cv2.EVENT_LBUTTONUP:
#         print(f'EVENT_LBUTTONDONW: {x}, {y}')
        
    
# img = np.ones((480, 640, 3), dtype=np.uint8) * 255



# cv2.namedWindow('image')
# cv2.setMouseCallback('image', on_mouse, img)
# cv2.imshow('image', img)
# cv2.waitKey()
# cv2.destroyAllWindows()


# ---------------------------------------------------------------
# oldx = oldy = -1

# def on_mouse(event, x, y, flags, param):
#     global oldx, oldy

#     if event == cv2.EVENT_LBUTTONDOWN:
#         oldx, oldy = x, y
#         print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

#     elif event == cv2.EVENT_LBUTTONUP:
#         print('EVENT_LBUTTONUP: %d, %d' % (x, y))

#     elif event == cv2.EVENT_MOUSEMOVE:
#         if flags & cv2.EVENT_FLAG_LBUTTON:
#             cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
#             cv2.imshow('image', img)
#             oldx, oldy = x, y


# img = np.ones((480, 640, 3), dtype=np.uint8) * 255

# cv2.namedWindow('image')
# cv2.setMouseCallback('image', on_mouse, img)

# cv2.imshow('image', img)
# cv2.waitKey()

# cv2.destroyAllWindows()


##############################################################################################
################################# mouse callback #############################################
##############################################################################################

# import numpy as np
# import cv2

# def on_level_changed(pos):
#     global img

#     level = pos * 16
#     level = np.clip(level, 0, 255)
    
#     img[:, :] = level
#     cv2.imshow('image', img)
    

# img = np.zeros((480, 640), np.uint8)

# # cv2.namedWindow('image')
# # cv2.createTrackbar('level', 'image', 0, 16, on_level_changed)
# cv2.imshow('image', img)
# cv2.createTrackbar('level', 'image', 0, 16, on_level_changed)
# cv2.waitKey()
# cv2.destroyAllWindows()



##############################################################################################
################################# 연산 시간 측정 방법 #########################################
##############################################################################################

# 컴퓨터 비전은 대용량 데이터를 다루고, 일련의 과정을 통해 최종 결과를 얻으므로 
# 매 단계에서 연산 시간을 측정하여 관리할 필요가 있음
#   ㄴ cv2.TickMeter() -> tm
#       tm:         cv2.TickMeter 객체
#       tm.start(): 시간 측정 시작
#       tm.stop() : 시간 측정 끝
#       tm.reset(): 시간 측정 초기화
#       tm.getTimeSec()  : 측정 시간을 초 단위로 반환
#       tm.getTimeMilli(): 측정 시간을 초 단위로 반환
#       tm.getTimeMicro(): 측정 시간을 초 단위로 반환


# import cv2
# import sys

# import numpy as np

# img = cv2.imread('hongkong.jpg')

# if img is None:
#     print('Image load failed!')
#     sys.exit()

# # tm = cv2.TickMeter()

# for i in range(10):
#     tm = cv2.TickMeter()
#     tm.start()

#     edge = cv2.Canny(img, 50, 150)

#     tm.stop()
#     ms = tm.getTimeMilli()

#     print(f'Elapsed time: {ms}ms.')



##############################################################################################
################################## 동영상 전환 이펙트 #########################################
##############################################################################################


