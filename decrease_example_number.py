import pathlib
import os.path
import glob

import pandas as pd
from numpy import arange, absolute
from math import modf, fabs

main_folder = pathlib.Path(__file__).parent.absolute()
dataset_video_folder = os.path.join(main_folder, 'dataset', 'video')


def set_window_size_bigger():
    df = pd.read_csv('/Users/user/PycharmProjects/features_extraction/processed_csv/dev_1.csv')
    for index, row in df.iterrows():
        if row['timestamp'] // 2:
            pass


# to find float numbers multiples of 0.2
float_range = arange(0, 1, 0.01)
multiples = absolute(float_range % 0.2) < 1e-13
# now multiples is a boolean array
print(float_range[multiples])
