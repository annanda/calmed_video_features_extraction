import pathlib
import os.path

from decouple import config

main_folder = pathlib.Path(__file__).parent.parent.absolute()
dataset_video_folder = os.path.join(main_folder, 'dataset', 'video')
processed_video_csv_folder = os.path.join(main_folder, 'processed_csv', 'video')

MAIN_FOLDER = config('MAIN_FOLDER', default=main_folder)
DATASET_VIDEO_FOLDER = config('DATASET_VIDEO_FOLDER', default=dataset_video_folder)
PROCESSED_VIDEO_CSV_FOLDER = config('PROCESSED_VIDEO_CSV_FOLDER', default=processed_video_csv_folder)
