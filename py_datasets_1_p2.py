import numpy as np
from sklearn import datasets as skdata

##### Update this path: #####
ca_houses_fpath_out = '../data/ca_houses_arrs.npz'

def fetch_sklearn_ca_housing_dataset():
    """Download California Housing dataset using sklearn. Return a dict of
    arrays with keys: 'data', 'target', 'feature_names'"""
    data_bunch = skdata.fetch_california_housing()
    arrs = [data_bunch.data, data_bunch.target,
            np.array(data_bunch.feature_names)]
    return dict(zip(['data', 'target', 'feature_names'], arrs))


def dict_of_arrs2npz_file(fpath_out, arrs_dict):
    """Save a dictionary of NumPy arrays to disk in .npz format. The dict keys
    are retained and used when loading the data back into Python with np.load.
    """
    np.savez(fpath_out, *arrs_dict)

if __name__ == '__main__':
    ca_houses = fetch_sklearn_ca_housing_dataset()
    dict_of_arrs2npz_file(ca_houses_fpath_out, ca_houses)

    # delete files downloaded via skdata.fetch_
    skdata.clear_data_home()