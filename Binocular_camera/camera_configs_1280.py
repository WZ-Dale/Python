# filename: camera_configs.py
# 该标定数据混乱了，不清楚为旧摄像头还是新的摄像头
import cv2
import numpy as np
"""
left_camera_matrix = np.array([[434.50360, 0., 319.86253],
                               [0., 435.43845, 221.37277],
                               [0., 0., 1.]])
left_distortion = np.array([[-0.35674, 0.13182, -0.00131, -0.00154, 0.00000]])



right_camera_matrix = np.array([[432.60165, 0., 322.87233],
                                [0., 433.79590, 235.53182],
                                [0., 0., 1.]])
right_distortion = np.array([[-0.32937, 0.09618, 0.00072, 0.00249, 0.00000]])
om = np.array([ 0.01523, 0.03511, 0.00793]) # 旋转关系向量
R = cv2.Rodrigues(om)[0]  # 使用Rodrigues变换将om变换为R
T = np.array([-120.82831, -0.02854, -7.31451])# 平移关系向量
size = (640, 480)# 图像尺寸
"""
left_camera_matrix = np.array([[814.31696, 0, 646.45384],
                               [0, 810.65784, 380.99421],
                               [0., 0., 1.]])
left_distortion = np.array([[0.02019, -0.04002, 0.00278, -0.00194, 0.00000]])

right_camera_matrix = np.array([[815.09944, 0., 671.51656],
                                [0, 811.24656, 417.50857],
                                [0., 0., 1.]])
right_distortion = np.array([[0.01359, -0.03503, 0.00291, -0.00247, 0.00000]])
# 旋转关系向量
om = np.array([0.00623, -0.00101, -0.00334])
# 使用Rodrigues变换将om变换为R
R = cv2.Rodrigues(om)[0]
# 平移关系向量
T = np.array([-120.36083, 0.53067, 0.43056])
# 图像尺寸
size = (1280, 720)



# 进行立体更正
R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)
# 计算更正map
left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)