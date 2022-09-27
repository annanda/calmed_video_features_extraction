import pathlib
import os.path

import pandas as pd

main_folder = pathlib.Path(__file__).parent.absolute()
dataset_video_folder = os.path.join(main_folder, 'dataset', 'video')


def set_window_size_bigger():
    df = pd.read_csv('/Users/user/PycharmProjects/features_extraction/processed_csv/dev_1.csv', sep=r'\s*,\s*',
                     header=0, engine='python')

    base = 0.04
    df = df.assign(
        timestamp=df['timestamp'].map(lambda x: round(base * round(x / base), 2))
    )
    between = 0
    for index, row in df.iterrows():
        if row['timestamp'] == 0.0:
            print('It is zero')
            continue
        # timestamp = fix_window_size_timestamp(row['timestamp'])
        value = row['timestamp']
        if is_window_multiples(value):
            print(f'multiple of 0.4: {value}')
            print(f'number of values between: {between}')
            if between != 9:
                print('##################################################### \n ALERTTTTTT')
            between = 0
        else:
            print(f'NOT multiple of 0.4: {value}')
            between += 1


def is_window_multiples(number):
    number = round(number * 100)
    return (number % 40) == 0


# to find float numbers multiples of 0.2
# float_range = arange(0, 1, 0.01)
# multiples = absolute(float_range % 0.2) < 1e-13
# # now multiples is a boolean array
# print(float_range[multiples])
# set_window_size_bigger()
print(is_window_multiples(298.4))
