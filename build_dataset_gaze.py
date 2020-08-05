import pandas as pd


def extract_gaze(extrated_csv):
    df_raw = pd.read_csv(extrated_csv, sep=r'\s*,\s*',
                         header=0, engine='python')
    df_initial = df_raw[['frame', 'timestamp']]
    gaze_df = df_raw.loc[:, 'gaze_0_x':'gaze_1_z']
    final = pd.concat([df_initial, gaze_df], axis=1)
    # final.to_csv()
    return final


def extract_2d_eye_landmark():
    pass


def extract_3d_eye_landmark():
    pass


if __name__ == '__main__':
    dataset_path = 'processed_csv/train_1.csv'
    extract_gaze(dataset_path)
