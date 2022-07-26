import pathlib
import os.path

from decouple import config

main_folder = pathlib.Path(__file__).parent.parent.absolute()
dataset_video_folder = os.path.join(main_folder, 'dataset', 'video')
processed_video_csv_folder = os.path.join(main_folder, 'processed_csv', 'video')

MAIN_FOLDER = config('MAIN_FOLDER', default=main_folder)
DATASET_VIDEO_FOLDER = config('DATASET_VIDEO_FOLDER', default=dataset_video_folder)
PROCESSED_VIDEO_CSV_FOLDER = config('PROCESSED_VIDEO_CSV_FOLDER', default=processed_video_csv_folder)

# FEATURES VIDEO VALUES
FEATURE_TYPE_DICT = {
    'gaze': {'start': 'gaze_0_x', 'end': 'gaze_angle_y'},
    '2d_eye_landmark': {'start': 'eye_lmk_x_0', 'end': 'eye_lmk_y_55'},
    '3d_eye_landmark': {'start': 'eye_lmk_X_0', 'end': 'eye_lmk_Z_55'},
    'head_pose': {'start': 'pose_Tx', 'end': 'pose_Rz'},
    'face_2d_landmarks': {'start': 'x_0', 'end': 'y_67'},
    'face_3d_landmarks': {'start': 'X_0', 'end': 'Z_67'},
    'AU': {'start': 'AU01_r', 'end': 'AU45_c'}
}

FEATURES_VIDEO = ['gaze', '2d_eye_landmark', '3d_eye_landmark', 'head_pose', 'face_2d_landmarks', 'face_3d_landmarks',
                  'AU']
