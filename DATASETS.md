# Dataset Registry

| Project | Dataset/input | Official source | Download/access |
|---|---|---|---|
| 01 | Authorized local documents | No external corpus required | Put `.txt` files in `documents/` |
| 02 | MovieLens latest-small | https://grouplens.org/datasets/movielens/ | https://files.grouplens.org/datasets/movielens/ml-latest-small.zip |
| 03 | Authorized CSV | No external corpus required | Pass a local CSV to `quality.py` |
| 04 | Authorized PDFs | No external corpus required | Put PDFs in `documents/` |
| 05 | scikit-learn Iris | https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html | Loaded by `sklearn.datasets.load_iris()` |

The projects intentionally avoid committing proprietary or sensitive corpora.