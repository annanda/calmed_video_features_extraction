import pathlib
import os.path

import pandas as pd

main_folder = pathlib.Path(__file__).parent.absolute()
dataset_video_folder = os.path.join(main_folder, 'dataset', 'video')
feature_type_dict = {
    'gaze': {'start': 'gaze_0_x', 'end': 'gaze_1_z'}
}


def extract_gaze(extrated_csv):
    prefix = extrated_csv.split('/')[-1]
    df_raw = pd.read_csv(extrated_csv, sep=r'\s*,\s*',
                         header=0, engine='python')
    df_initial = df_raw[['frame', 'timestamp']]
    gaze_df = df_raw.loc[:, 'gaze_0_x':'gaze_1_z']
    final = pd.concat([df_initial, gaze_df], axis=1)
    final.to_csv(f'{dataset_video_folder}/gaze/{prefix}', index=False)


def extract_features(extrated_csv, feature_type):
    prefix = extrated_csv.split('/')[-1]
    df_raw = pd.read_csv(extrated_csv, sep=r'\s*,\s*',
                         header=0, engine='python')
    df_initial = df_raw[['frame', 'timestamp']]
    column_to_extract_start = feature_type_dict[feature_type]['start']
    column_to_extract_end = feature_type_dict[feature_type]['end']
    gaze_df = df_raw.loc[:, column_to_extract_start:column_to_extract_end]
    final = pd.concat([df_initial, gaze_df], axis=1)
    final.to_csv(f'{dataset_video_folder}/gaze/{prefix}', index=False)


def extract_3d_eye_landmark():
    pass


if __name__ == '__main__':
    dataset_path = 'processed_csv/train_3.csv'
    # extract_gaze(dataset_path)
    # extract_features(dataset_path, 'gaze_0_x', 'gaze_1_z')
    feature_type = 'gaze'
    extract_features(dataset_path, feature_type)
