# Features Extraction

This project works with the output of the OpenFace and OpenSMILE models to separate the extracted features into
organised categories.

OpenFace/OpenSMILE extract all the available features, this project separated each feature type into a different dataset
of
features, to help to work with features selection for a machine learning model.
It also round the timestamp, so it
becomes increments of 0.04 seconds, to be consistent throughout the dataset timestamp.

### How to use it

**The format for a session number is:** ```session_XX_YY```. Where XX represents the participant's number and YY
represents the session number for the participant, e.g., ```session_01_01``` refer to the first session with participant
number 1.

1. Put the .CSV files generated by OpenFace into the folder ```processed_csv/session_number``` according to the session
   number
2. You can create working dataset for all extracted features at once for a given session by running the
   function ```extract_all_features_from_session()``` on the ```build_dataset.py``` file.
3. You can also create working dataset for a specific feature by running the function ```extract_features()``` on
   the ```build_dataset.py``` file.
    * Types of features supported for video:
        * AU
        * gaze
        * 2d_eye_landmark
        * 3d_eye_landmark
        * head_pose
        * face_2d_landmarks
        * face_3d_landmark

The output is saved on the ```dataset/video/{{feature_type}}/{{session_number}}``` folder.

## Generate working dataset for all supported features

1. Run ```extract_all_features_from_session({{session_number}})``` function on the ```build_dataset.py``` file.

## Generate working dataset for a specific features from one session

1. Run the function ```extract_features({{session_number}}, {{feature}})``` on the ```build_dataset.py``` file.

## Licence

This repository is released for **non-commercial use only** under
the [3-Cause BSD Licence](https://opensource.org/license/bsd-3-clause/).

Please refer to [LICENSE.md](LICENSE.md) file for details on the licence.

You must comply with OpenFace and OpenSMILE licenses.

----

Author: Annanda Sousa

Author's contact: [annanda.sousa@gmail.com](mailto:annanda.sousa@gmail.com)

----