from setuptools import setup

setup(
    name='features_extraction',
    version='0.1',
    description='Creating working dataset from video and audio features',
    author='Annanda Sousa',
    author_email='annanda.sousa@insight-centre.org',
    packages=['configs', 'video_dataset_creation_from_features', 'audio_dataset_creation_from_features'],
    zip_safe=False
)
