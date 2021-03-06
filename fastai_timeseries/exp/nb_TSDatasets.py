#AUTOGENERATED! DO NOT EDIT! file to edit: ./TSDatasets.ipynb (unless otherwise specified)
from pathlib import Path
import os
import numpy as np
import pandas as pd
from scipy.io import arff


try: from exp.nb_TSUtilities import *
except ImportError: from .nb_TSUtilities import *

try: from exp.nb_TSBasicData import *
except ImportError: from .nb_TSBasicData import *


import os
import tempfile
try: from urllib import urlretrieve
except ImportError: from urllib.request import urlretrieve
import shutil
from pyunpack import Archive


def decompress_from_url(url, target_dir=None, verbose=False):
    """Downloads a compressed file from its URL and uncompresses it.

    Parameters
    ----------
    url : string
        URL from which to download.
    target_dir : str or None (default: None)
        Directory to be used to extract downloaded files.
    verbose : bool (default: False)
        Whether to print information about the process (cached files used, ...)

    Returns
    -------
    str or None
        Directory in which the compressed file has been extracted if the process was
        successful, None otherwise
    """
    try:
        fname = os.path.basename(url)
        tmpdir = tempfile.mkdtemp()
        local_comp_fname = os.path.join(tmpdir, fname)
        urlretrieve(url, local_comp_fname)
    except:
        shutil.rmtree(tmpdir)
        if verbose:
            sys.stderr.write("Could not download url. Please, check url.\n")
    try:
        if not os.path.exists(target_dir): os.makedirs(target_dir)
        Archive(local_comp_fname).extractall(target_dir)
        shutil.rmtree(tmpdir)
        if verbose:
            print("Successfully extracted file %s to path %s" %
                  (local_comp_fname, target_dir))
        return target_dir
    except:
        shutil.rmtree(tmpdir)
        if verbose:
            sys.stderr.write("Could not uncompress file, aborting.\n")
        return None



def get_UCR_univariate_list():
    return sorted([
        'ACSF1', 'Adiac', 'AllGestureWiimoteX', 'AllGestureWiimoteY',
        'AllGestureWiimoteZ', 'ArrowHead', 'AsphaltObstacles', 'BME', 'Beef',
        'BeetleFly', 'BirdChicken', 'CBF', 'Car', 'Chinatown',
        'ChlorineConcentration', 'CinCECGTorso', 'Coffee', 'Computers',
        'CricketX', 'CricketY', 'CricketZ', 'Crop', 'DiatomSizeReduction',
        'DistalPhalanxOutlineAgeGroup', 'DistalPhalanxOutlineCorrect',
        'DistalPhalanxTW', 'DodgerLoopDay', 'DodgerLoopGame',
        'DodgerLoopWeekend', 'ECG200', 'ECG5000', 'ECGFiveDays',
        'EOGHorizontalSignal', 'EOGVerticalSignal', 'Earthquakes',
        'ElectricDevices', 'EthanolLevel', 'FaceAll', 'FaceFour', 'FacesUCR',
        'FiftyWords', 'Fish', 'FordA', 'FordB', 'FreezerRegularTrain',
        'FreezerSmallTrain', 'Fungi', 'GestureMidAirD1', 'GestureMidAirD2',
        'GestureMidAirD3', 'GesturePebbleZ1', 'GesturePebbleZ2', 'GunPoint',
        'GunPointAgeSpan', 'GunPointMaleVersusFemale',
        'GunPointOldVersusYoung', 'Ham', 'HandOutlines', 'Haptics', 'Herring',
        'HouseTwenty', 'InlineSkate', 'InsectEPGRegularTrain',
        'InsectEPGSmallTrain', 'InsectWingbeatSound', 'ItalyPowerDemand',
        'LargeKitchenAppliances', 'Lightning2', 'Lightning7', 'Mallat', 'Meat',
        'MedicalImages', 'MelbournePedestrian', 'MiddlePhalanxOutlineAgeGroup',
        'MiddlePhalanxOutlineCorrect', 'MiddlePhalanxTW',
        'MixedShapesRegularTrain', 'MixedShapesSmallTrain', 'MoteStrain',
        'NonInvasiveFetalECGThorax1', 'NonInvasiveFetalECGThorax2', 'OSULeaf',
        'OliveOil', 'PLAID', 'PhalangesOutlinesCorrect', 'Phoneme',
        'PickupGestureWiimoteZ', 'PigAirwayPressure', 'PigArtPressure',
        'PigCVP', 'Plane', 'PowerCons', 'ProximalPhalanxOutlineAgeGroup',
        'ProximalPhalanxOutlineCorrect', 'ProximalPhalanxTW',
        'RefrigerationDevices', 'Rock', 'ScreenType', 'SemgHandGenderCh2',
        'SemgHandMovementCh2', 'SemgHandSubjectCh2', 'ShakeGestureWiimoteZ',
        'ShapeletSim', 'ShapesAll', 'SmallKitchenAppliances', 'SmoothSubspace',
        'SonyAIBORobotSurface1', 'SonyAIBORobotSurface2', 'StarLightCurves',
        'Strawberry', 'SwedishLeaf', 'Symbols', 'SyntheticControl',
        'ToeSegmentation1', 'ToeSegmentation2', 'Trace', 'TwoLeadECG',
        'TwoPatterns', 'UMD', 'UWaveGestureLibraryAll', 'UWaveGestureLibraryX',
        'UWaveGestureLibraryY', 'UWaveGestureLibraryZ', 'Wafer', 'Wine',
        'WordSynonyms', 'Worms', 'WormsTwoClass', 'Yoga'
    ])


def get_UCR_multivariate_list():
    return sorted([
        'ArticularyWordRecognition', 'AtrialFibrillation', 'BasicMotions',
        'CharacterTrajectories', 'Cricket', 'DuckDuckGeese', 'ERing',
        'EigenWorms', 'Epilepsy', 'EthanolConcentration', 'FaceDetection',
        'FingerMovements', 'HandMovementDirection', 'Handwriting', 'Heartbeat',
        'InsectWingbeat', 'JapaneseVowels', 'LSST', 'Libras', 'MotorImagery',
        'NATOPS', 'PEMS-SF', 'PenDigits', 'PhonemeSpectra', 'RacketSports',
        'SelfRegulationSCP1', 'SelfRegulationSCP2', 'SpokenArabicDigits',
        'StandWalkJump', 'UWaveGestureLibrary'
    ])


def get_UCR_univariate(sel_dataset, parent_dir='data/UCR', verbose=False, drop_na=False, check=True):
    if check and sel_dataset not in get_UCR_univariate_list():
        print('This dataset does not exist. Please select one from this list:')
        print(get_UCR_univariate_list())
        return None, None, None, None
    if verbose: print('Dataset:', sel_dataset)
    src_website = 'http://www.timeseriesclassification.com/Downloads/'
    tgt_dir = Path(parent_dir) / sel_dataset
    if verbose: print('Downloading and decompressing data...')
    if not os.path.isdir(tgt_dir):
        decompress_from_url(
            src_website + sel_dataset + '.zip', target_dir=tgt_dir, verbose=verbose)
    if verbose: print('...data downloaded and decompressed')
    fname_train = sel_dataset + "_TRAIN.arff"
    fname_test = sel_dataset + "_TEST.arff"

    train_df = pd.DataFrame(arff.loadarff(os.path.join(tgt_dir, fname_train))[0])
    test_df = pd.DataFrame(arff.loadarff(os.path.join(tgt_dir, fname_test))[0])
    unique_cats = train_df.iloc[:, -1].unique()
    mapping = dict(zip(unique_cats, np.arange(len(unique_cats))))
    train_df = train_df.replace({train_df.columns.values[-1]: mapping})
    test_df = test_df.replace({test_df.columns.values[-1]: mapping})
    if drop_na:
        train_df.dropna(axis=1, inplace=True)
        test_df.dropna(axis=1, inplace=True)

    X_train = train_df.iloc[:, :-1].values.astype(np.float32)
    X_test = test_df.iloc[:, :-1].values.astype(np.float32)
    y_train = train_df.iloc[:, -1].values.astype(int)
    y_test = test_df.iloc[:, -1].values.astype(int)

    X_train = To3dArray(X_train)
    X_test = To3dArray(X_test)

    if verbose:
        print('Successfully extracted dataset')
        print('X_train:', X_train.shape)
        print('y_train:', y_train.shape)
        print('X_valid:', X_test.shape)
        print('y_valid:', y_test.shape, '\n')
    return X_train, y_train, X_test, y_test



def get_UCR_multivariate(sel_dataset, parent_dir='data/UCR', verbose=False, check=True):
    if sel_dataset.lower() == 'mphoneme': sel_dataset = 'Phoneme'
    if check and sel_dataset not in get_UCR_multivariate_list():
        print('This dataset does not exist. Please select one from this list:')
        print(get_UCR_multivariate_list())
        return None, None, None, None
    if verbose: print('Dataset:', sel_dataset)
    src_website = 'http://www.timeseriesclassification.com/Downloads/'
    tgt_dir = Path(parent_dir) / sel_dataset

    if verbose: print('Download and decompressing data...')
    if not os.path.isdir(tgt_dir):
        decompress_from_url(
            src_website + sel_dataset + '.zip', target_dir=tgt_dir, verbose=verbose)
    if verbose: print('...data downloaded and decompressed')
    if verbose: print('Extracting data...')
    X_train_ = []
    X_test_ = []
    for i in range(10000):
        if not os.path.isfile(
                f'{parent_dir}/{sel_dataset}/{sel_dataset}Dimension'
                + str(i + 1) + '_TRAIN.arff'):
            break
        train_df = pd.DataFrame(
            arff.loadarff(
                f'{parent_dir}/{sel_dataset}/{sel_dataset}Dimension'
                + str(i + 1) + '_TRAIN.arff')[0])
        unique_cats = train_df.iloc[:, -1].unique()
        mapping = dict(zip(unique_cats, np.arange(len(unique_cats))))
        train_df = train_df.replace({train_df.columns.values[-1]: mapping})
        test_df = pd.DataFrame(
            arff.loadarff(
                f'{parent_dir}/{sel_dataset}/{sel_dataset}Dimension'
                + str(i + 1) + '_TEST.arff')[0])
        test_df = test_df.replace({test_df.columns.values[-1]: mapping})
        X_train_.append(train_df.iloc[:, :-1].values)
        X_test_.append(test_df.iloc[:, :-1].values)

    if verbose: print('...extraction complete')
    X_train = np.stack(X_train_, axis=-1)
    X_test = np.stack(X_test_, axis=-1)

    # In this case we need to rearrange the arrays ()
    X_train = np.transpose(X_train, (0, 2, 1))
    X_test = np.transpose(X_test, (0, 2, 1))

    y_train = np.array([int(float(x)) for x in train_df.iloc[:, -1]])
    y_test = np.array([int(float(x)) for x in test_df.iloc[:, -1]])

    if verbose:
        print('Successfully extracted dataset')
        print('X_train:', X_train.shape)
        print('y_train:', y_train.shape)
        print('X_valid:', X_test.shape)
        print('y_valid:', y_test.shape, '\n')
    return X_train, y_train, X_test, y_test


def get_UCR_data(dsid, parent_dir='data/UCR', verbose=False, check=True):
    if dsid in get_UCR_univariate_list():
        return get_UCR_univariate(dsid, verbose=verbose, check=check)
    elif dsid in get_UCR_multivariate_list():
        return get_UCR_multivariate(dsid, verbose=verbose, check=check)
    else:
        print(f'This {dsid} dataset does not exist. Please select one from these lists:')
        print('\nunivariate datasets')
        print(get_UCR_univariate_list())
        print('\nmultivariate datasets')
        print(get_UCR_multivariate_list(), '\n')
        return None, None, None, None


def create_UCR_databunch(dsid, bs=64, scale_type='standardize', scale_by_channel=False,
                         scale_by_sample=False, scale_range =(-1, 1), verbose=False, check=True):
    X_train, y_train, X_valid, y_valid = get_UCR_data(dsid, verbose=verbose, check=check)
    data = (ItemLists('.', TSList(X_train), TSList(X_valid)).label_from_lists(y_train, y_valid)
            .databunch(bs=min(bs, len(X_train)), val_bs=min(bs, len(X_valid)))
            .scale(scale_type=scale_type, scale_by_channel=scale_by_channel,
                   scale_by_sample=scale_by_sample,scale_range=scale_range)
         )
    return data


def create_seq_optimized(n_samples=1000, seq_len=100, channels=True, seed=1):
    np.random.seed(seed)
    y = np.random.randint(seq_len, size=n_samples)
    X = np.eye(seq_len)[y]
    if channels:
        X = np.expand_dims(X, 1)
    return X, y

def get_translation_invariance_data(n_samples, seq_len, seed):
    X_train, y_train = create_seq_optimized(
        n_samples=n_samples, seq_len=seq_len, channels=True, seed=seed)
    X_test, y_test = create_seq_optimized(
        n_samples=n_samples, seq_len=seq_len, channels=True, seed=seed + 1)
    print(X_train.shape, y_train.shape, X_test.shape, y_test.shape, '\n')
    return X_train, y_train, X_test, y_test