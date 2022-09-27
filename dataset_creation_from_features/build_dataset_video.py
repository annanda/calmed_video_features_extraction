import os.path

import pandas as pd

from dataset_creation_from_features.conf import DATASET_VIDEO_FOLDER, PROCESSED_VIDEO_CSV_FOLDER, FEATURE_TYPE_DICT, \
    FEATURES_VIDEO


def extract_features(session, feature_type):
    input_folder = os.path.join(PROCESSED_VIDEO_CSV_FOLDER, session)
    all_session_files = os.listdir(input_folder)
    output_folder = os.path.join(DATASET_VIDEO_FOLDER, feature_type, session)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in all_session_files:
        name = file.replace('.csv', '')
        file_path = os.path.join(input_folder, file)
        df_raw = pd.read_csv(file_path, sep=r'\s*,\s*',
                             header=0, engine='python')
        df_initial = pd.DataFrame()
        df_timestamp = df_raw[['timestamp']]
        base = 0.04
        df_initial = df_initial.assign(
            frametime=df_timestamp['timestamp'].map(lambda x: round(base * round(x / base), 2))
        )
        df_initial['frametime'] = name + '___' + df_initial['frametime'].astype(str)
        column_to_extract_start = FEATURE_TYPE_DICT[feature_type]['start']
        column_to_extract_end = FEATURE_TYPE_DICT[feature_type]['end']
        gaze_df = df_raw.loc[:, column_to_extract_start:column_to_extract_end]
        final = pd.concat([df_initial, gaze_df], axis=1)
        final.to_csv(os.path.join(output_folder, f'{name}.csv'), index=False)


def extract_all_features_from_session(session):
    for feature in FEATURES_VIDEO:
        extract_features(session, feature)


if __name__ == '__main__':
    session_number = 'session_04_01'
    # To extract all video features from a session use the function below
    extract_all_features_from_session(session_number)

    # To extract one specific feature from a session use the function below
    # extract_features(session_number, feature)
