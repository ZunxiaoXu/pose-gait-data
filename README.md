# Pose gait data

CCPG and SUSTech1K pose keypoint packages exported from the data directories used by the current research experiments on 2026-11-14.

## Download

Download the data ZIP files from the repository's Releases page. Each archive preserves the original identity, sequence and view hierarchy beneath a dataset directory.

| Dataset | ZIP | Pose files | Uncompressed file bytes |
| --- | --- | ---: | ---: |
| CCPG | CCPG_pose.zip | 16,365 | 717,945,744 |
| SUSTech1K | SUSTech1K_pose.zip | 25,239 | 947,248,897 |

`manifest.json` contains archive sizes, SHA256 checksums and source directory information. `SHA256SUMS.txt` contains checksums for both archives. All archived files passed ZIP integrity checks, and their counts and total uncompressed sizes matched the source inventory.

## Read pose sequences

Install NumPy in the Python environment used for analysis.

```sh
python -m pip install numpy
python read_pose.py CCPG_pose.zip
python read_pose.py SUSTech1K_pose.zip
```

To select a sequence, pass its archive path with `--member`. `pose_file_index.csv` lists all member paths and file sizes.

```sh
python read_pose.py CCPG_pose.zip --member CCPG/000/U0_D0/01_0/pose_01_0.pkl
```

The representative sequences checked during export were NumPy arrays with shapes `(233, 17, 3)` for CCPG and `(95, 17, 3)` for SUSTech1K. These dimensions describe frames, joints and channels. Sequence lengths vary.

## Use with an online AI

Provide this README, the file index and `read_pose.py` with the data packages. The analysis environment needs access to the downloaded ZIP files and Python with NumPy. This repository and its published release assets are publicly accessible.

<!-- gait3d-smpl-300seq-20261119 -->
## Gait3D SMPL samples

300 subjects, one complete sequence per subject, with 34,978 original NPZ frames. Sequence lengths range from 25 to 473 frames. The sample includes the three sequences extracted earlier.

[Data and indexes](samples/Gait3D_SMPL_300seq_20261119/README.md) and [download packages](https://github.com/ZunxiaoXu/pose-gait-data/releases/tag/gait3d-smpl-300seq-20261119) are available for this batch. The data comes from the `.z12` volume of the original Gait3D SMPL archive.
