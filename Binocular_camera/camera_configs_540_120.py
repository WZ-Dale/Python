# filename: camera_configs.py
# 540*120 的标定数据
# 标定部分为原图像540*120部分
import cv2
import numpy as np

left_camera_matrix = np.array([[396.65003 , 0., 264.57723],
                               [0.,  396.75805,  121.73296 ],
                               [0., 0., 1.]])
left_distortion = np.array([[ 0.00620   ,-0.04065 ,  -0.00313 ,  -0.00617,  0.00000 ]])



right_camera_matrix = np.array([[396.14729, 0., 280.92218],
                                [0., 396.12665, 123.36467],
                                [0., 0., 1.]])
right_distortion = np.array([[ -0.00267 ,  -0.03955   ,-0.00399  , -0.00466 , 0.00000 ]])

om = np.array([0.00610 ,  -0.00993 , -0.00508  ]) # ��ת��ϵ����
R = cv2.Rodrigues(om)[0]  # ʹ��Rodrigues�任��om�任ΪR
T = np.array([-120.89797 ,  0.48501 , -1.13408]) # ƽ�ƹ�ϵ����

size = (540, 120) # ͼ��ߴ�

# �����������
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# �������map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)