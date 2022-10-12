import os.path
import pandas as pd

from configs.conf import DATASET_AUDIO_FOLDER, OPEN_SMILE_DATASET_FOLDER, SESSION_PARTS, \
    AUDIO_PARAMETER_FEATURES_GROUPS, LLD_PARAMETER_GROUP


class AudioDatasetCreator:
    def __init__(self, session, feature_group='all', feature_level='functionals', feature_set='eGeMAPSv02'):
        self.session = session
        self.feature_group = feature_group
        self.feature_set = feature_set
        self.feature_level = feature_level
        self.input_folder = os.path.join(OPEN_SMILE_DATASET_FOLDER, self.session)
        self.feature_level_output_folders = {
            'functionals': os.path.join(DATASET_AUDIO_FOLDER, 'functionals', self.feature_group),
        }
        self.feature_level_input_file_names = {
            'functionals': f'{self.feature_set}_Functionals.csv',
        }

    def generate_features(self):
        """
        To generate all features type and feature levels from the current session number.
        It saves the datasets into the folder structure (/dataset/audio/feature_level/feature_type/session) for functionals
        It saves the datasets into the folder structure (/dataset/audio/feature_level/session) for llds and llds delta
        :return: None
        """
        if self.feature_group == 'all':
            feature_groups = LLD_PARAMETER_GROUP.keys()
        else:
            feature_groups = [self.feature_group]
        for feature_group in feature_groups:
            self.generate_feature_group(feature_group)

    def write_csv_dataset(self, df_to_save, session_part, feature_type):
        where_to_save = os.path.join(self.feature_level_output_folders[self.feature_level], feature_type, self.session)
        if not os.path.exists(where_to_save):
            os.makedirs(where_to_save)

        df_to_save.to_csv(
            os.path.join(where_to_save, f'{session_part}.csv'),
            index=False)

    def generate_feature_group(self, feature_group):
        """
        To generate one feature type from the current session number.
        Feature groups: frequency, energy_amplitude, spectral_balance, temporal_features
        It saves the dataset type into the folder (/dataset/audio/feature_level/feature_type/session)
        :return: None
        """
        for session_part in SESSION_PARTS[self.session]:
            df_features = pd.read_csv(
                os.path.join(self.input_folder,
                             session_part + '_' + self.feature_level_input_file_names[self.feature_level]))
            df_initial = pd.DataFrame()
            df_timestamp = df_features[['frametime']]
            df_initial = df_initial.assign(
                frametime=df_timestamp['frametime']
            )
            df_initial['frametime'] = session_part + '___' + df_initial['frametime'].astype(str)

            features_from_group = LLD_PARAMETER_GROUP[feature_group]
            for feature_in_group in features_from_group:
                intervals = AUDIO_PARAMETER_FEATURES_GROUPS[feature_in_group]['intervals']
                intervals_dfs = []
                for interval in intervals:
                    column_to_extract_start, column_to_extract_end = interval
                    temp_df = df_features.loc[:, column_to_extract_start:column_to_extract_end]
                    intervals_dfs.append(temp_df)
                final_intervals = pd.concat(intervals_dfs, axis=1)
                final = pd.concat([df_initial, final_intervals], axis=1)
                self.write_csv_dataset(final, session_part, feature_in_group)


def generate_features_all_sessions():
    for session in SESSION_PARTS.keys():
        audio_ds_creator = AudioDatasetCreator(session, feature_group='frequency')
        audio_ds_creator.generate_features()


if __name__ == '__main__':
    session_number = 'session_04_02'
    audio_dataset_creator = AudioDatasetCreator(session_number, feature_group='frequency')
    audio_dataset_creator.generate_features()

    # generate_features_all_sessions()
