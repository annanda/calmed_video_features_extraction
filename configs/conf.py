import pathlib
import os.path

from decouple import config

SESSION_PARTS = {
    'session_01_01': ['session_01_01_01', 'session_01_01_02', 'session_01_01_03', 'session_01_01_04',
                      'session_01_01_05', 'session_01_01_06', 'session_01_01_07'],
    'session_02_01': ['session_02_01_01', 'session_02_01_02', 'session_02_01_03', 'session_02_01_04',
                      'session_02_01_05', 'session_02_01_06'],
    'session_02_02': ['session_02_02_01', 'session_02_02_02', 'session_02_02_03', 'session_02_02_04',
                      'session_02_02_05', 'session_02_02_06'],
    'session_03_01': ['session_03_01_01', 'session_03_01_02', 'session_03_01_03', 'session_03_01_04',
                      'session_03_01_05', 'session_03_01_06', 'session_03_01_07'],
    'session_03_02': ['session_03_02_01', 'session_03_02_02', 'session_03_02_03', 'session_03_02_04',
                      'session_03_02_05', 'session_03_02_06'],
    'session_04_01': ['session_04_01_01', 'session_04_01_02', 'session_04_01_03', 'session_04_01_04',
                      'session_04_01_05'],
    'session_04_02': ['session_04_02_01', 'session_04_02_02', 'session_04_02_03', 'session_04_02_04',
                      'session_04_02_05'],
}

main_folder = pathlib.Path(__file__).parent.parent.absolute()
dataset_video_folder = os.path.join(main_folder, 'dataset', 'video')
dataset_audio_folder = os.path.join(main_folder, 'dataset', 'audio')
processed_video_csv_folder = os.path.join(main_folder, 'processed_csv', 'video')
open_smile_dataset_folder = os.path.join(main_folder, 'open_smile_all_output')

MAIN_FOLDER = config('MAIN_FOLDER', default=main_folder)
DATASET_VIDEO_FOLDER = config('DATASET_VIDEO_FOLDER', default=dataset_video_folder)
DATASET_AUDIO_FOLDER = config('DATASET_AUDIO_FOLDER', default=dataset_audio_folder)
PROCESSED_VIDEO_CSV_FOLDER = config('PROCESSED_VIDEO_CSV_FOLDER', default=processed_video_csv_folder)
OPEN_SMILE_DATASET_FOLDER = config('OPEN_SMILE_DATASET_FOLDER', default=open_smile_dataset_folder)

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

# FEATURES AUDIO VALUES
AUDIO_PARAMETER_FEATURES_GROUPS = {
    'pitch': {
        'intervals': [('F0semitoneFrom27.5Hz_sma3nz_amean', 'F0semitoneFrom27.5Hz_sma3nz_stddevFallingSlope')],
        'llds': ['F0semitoneFrom27.5Hz_sma3nz']
    },
    'jitter': {
        'intervals': [('jitterLocal_sma3nz_amean', 'jitterLocal_sma3nz_stddevNorm')],
        'llds': ['jitterLocal_sma3nz']
    },
    'formant_1-3_frequency': {
        'intervals': [
            ('F1frequency_sma3nz_amean', 'F1frequency_sma3nz_stddevNorm'),
            ('F2frequency_sma3nz_amean', 'F2frequency_sma3nz_stddevNorm'),
            ('F3frequency_sma3nz_amean', 'F3frequency_sma3nz_stddevNorm')],
        'llds': ['F1frequency_sma3nz', 'F2frequency_sma3nz', 'F3frequency_sma3nz']

    },
    'formant_1-3_bandwidth': {
        'intervals': [
            ('F1bandwidth_sma3nz_amean', 'F1bandwidth_sma3nz_stddevNorm'),
            ('F2bandwidth_sma3nz_amean', 'F2bandwidth_sma3nz_stddevNorm'),
            ('F3bandwidth_sma3nz_amean', 'F3bandwidth_sma3nz_stddevNorm')],
        'llds': ['F1bandwidth_sma3nz', 'F2bandwidth_sma3nz', 'F3bandwidth_sma3nz']
    },
    'shimmer': {
        'intervals': [('shimmerLocaldB_sma3nz_amean', 'shimmerLocaldB_sma3nz_stddevNorm')],
        'llds': ['shimmerLocaldB_sma3nz']
    },
    'loudness': {
        'intervals': [('loudness_sma3_amean', 'loudness_sma3_stddevFallingSlope'),
                      ('loudnessPeaksPerSec', 'loudnessPeaksPerSec')],
        'llds': ['Loudness_sma3']
    },
    'harmonics-to-noise_ratio': {
        'intervals': [('HNRdBACF_sma3nz_amean', 'HNRdBACF_sma3nz_stddevNorm')],
        'llds': ['HNRdBACF_sma3nz']
    },
    'alpha_ratio': {
        'intervals': [('alphaRatioV_sma3nz_amean', 'alphaRatioV_sma3nz_stddevNorm'),
                      ('alphaRatioUV_sma3nz_amean', 'alphaRatioUV_sma3nz_amean')],
        'llds': ['alphaRatio_sma3']
    },
    'hammarberg_index': {
        'intervals': [('hammarbergIndexV_sma3nz_amean', 'hammarbergIndexV_sma3nz_stddevNorm'),
                      ('hammarbergIndexUV_sma3nz_amean', 'hammarbergIndexUV_sma3nz_amean')],
        'llds': ['hammarbergIndex_sma3']
    },
    'spectral_slope': {
        'intervals': [('slopeV0-500_sma3nz_amean', 'slopeV500-1500_sma3nz_stddevNorm'),
                      ('slopeUV0-500_sma3nz_amean', 'slopeUV500-1500_sma3nz_amean')],
        'llds': ['slope0-500_sma3', 'slope500-1500_sma3']
    },
    'formant_1-3_relative_energy': {
        'intervals': [('F1amplitudeLogRelF0_sma3nz_amean', 'F1amplitudeLogRelF0_sma3nz_stddevNorm'),
                      ('F2amplitudeLogRelF0_sma3nz_amean', 'F2amplitudeLogRelF0_sma3nz_stddevNorm'),
                      ('F3amplitudeLogRelF0_sma3nz_amean', 'F3amplitudeLogRelF0_sma3nz_stddevNorm')],
        'llds': ['F1amplitudeLogRelF0_sma3nz', 'F2amplitudeLogRelF0_sma3nz', 'F3amplitudeLogRelF0_sma3nz']
    },
    'harmonic_difference_H1–H2': {
        'intervals': [('logRelF0-H1-H2_sma3nz_amean', 'logRelF0-H1-H2_sma3nz_stddevNorm')],
        'llds': ['logRelF0-H1-H2_sma3nz']
    },
    'Harmonic_difference_H1–A3': {
        'intervals': [('logRelF0-H1-A3_sma3nz_amean', 'logRelF0-H1-A3_sma3nz_stddevNorm')],
        'llds': ['logRelF0-H1-A3_sma3nz']
    },
    'mfcc_1–4': {
        'intervals': [('mfcc1_sma3_amean', 'mfcc4_sma3_stddevNorm')],
        'llds': ['mfcc1_sma3', 'mfcc2_sma3', 'mfcc3_sma3', 'mfcc4_sma3']
    },
    'sectral_flux': {
        'intervals': [('spectralFlux_sma3_amean', 'spectralFlux_sma3_stddevNorm'),
                      ('spectralFluxV_sma3nz_amean', 'spectralFluxV_sma3nz_stddevNorm'),
                      ('spectralFluxUV_sma3nz_amean', 'spectralFluxUV_sma3nz_amean')],
        'llds': ['spectralFlux_sma3']
    },
    'temporal_features': {
        'intervals': [('VoicedSegmentsPerSec', 'equivalentSoundLevel_dBp')],
        'llds': []
    }

}

LLD_PARAMETER_GROUP = {
    'frequency': ['pitch', 'jitter', 'formant_1-3_frequency', 'formant_1-3_bandwidth'],
    'energy_amplitude': ['shimmer', 'loudness', 'harmonics-to-noise_ratio'],
    'spectral_balance': ['alpha_ratio', 'hammarberg_index', 'spectral_slope',
                         'formant_1-3_relative_energy', 'harmonic_difference_H1–H2',
                         'Harmonic_difference_H1–A3', 'mfcc_1–4'],
    'temporal_features': ['temporal_features']
}

AUDIO_FEATURES_LEVELS = ['llds', 'functionals', 'llds_deltas']
