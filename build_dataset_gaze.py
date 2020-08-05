import pathlib
import os.path
import glob

import pandas as pd

main_folder = pathlib.Path(__file__).parent.absolute()
dataset_video_folder = os.path.join(main_folder, 'dataset', 'video')
feature_type_dict = {
    'gaze': {'start': 'gaze_0_x', 'end': 'gaze_1_z'},
    '2d_eye_landmark': {'start': 'eye_lmk_x_0', 'end': 'eye_lmk_y_55'},
    '3d_eye_landmark': {'start': 'eye_lmk_X_0', 'end': 'eye_lmk_Z_55'},
}


def extract_features(extrated_csv, feature_type):
    prefix = extrated_csv.split('/')[-1]
    df_raw = pd.read_csv(extrated_csv, sep=r'\s*,\s*',
                         header=0, engine='python')
    df_initial = df_raw[['frame', 'timestamp']]
    column_to_extract_start = feature_type_dict[feature_type]['start']
    column_to_extract_end = feature_type_dict[feature_type]['end']
    gaze_df = df_raw.loc[:, column_to_extract_start:column_to_extract_end]
    final = pd.concat([df_initial, gaze_df], axis=1)
    final.to_csv(f'{dataset_video_folder}/{feature_type}/{prefix}', index=False)


def extract_features_all_files(feature_type):
    # files = []
    files = glob.glob(f'{main_folder}/processed_csv/*.csv')
    for file in files:
        extract_features(file, feature_type)


if __name__ == '__main__':
    feature_type = '2d_eye_landmark'
    extract_features_all_files(feature_type)
