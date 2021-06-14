import sys
import cv2

print('Hello OpenCV', cv2.__version__)
img = cv2.imread('cat.bmp', cv2.IMREAD_COLOR) # cat.bmp파일 불러와서 img변수 저장하기
img2 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE) # 흑백사진 출력

if img is None: # 영상 파일 불러오기 실패하면 에러 메시지 출력하고 종료하기
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image', cv2.WINDOW_NORMAL) # normal = 크기조절
cv2.imshow('image', img)  # 'image'라는 이름의 새 창을 만들고 img영상 출력, 키보드 입력 대기
cv2.imshow('catzz.png',img2)
# cv2.waitKey(3000) # 키보드 입력대기하기
while True:
    # if cv2.waitKey() == ord('q'): # 특정키 사용하여 종료.
    if cv2.waitKey() == 27:
        break

cv2.destroyAllWindows() # 생성된 모든 창 닫기



