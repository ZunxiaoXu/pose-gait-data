# CASIA-B and Gait3D pose data

These are the processed pose PKL files used by the current research dataset copies on 2026-11-20.

| Dataset | Sequence files | Identity directories | Archives |
| --- | ---: | ---: | --- |
| CASIA-B | 13592 | 124 | `CASIA-B_pose.zip` |
| Gait3D | 25309 | 4000 | `Gait3D_pose.part01.zip`, `Gait3D_pose.part02.zip`, `Gait3D_pose.part03.zip`, `Gait3D_pose.part04.zip` |

Each archive preserves the identity and sequence hierarchy under its dataset name. Gait3D is provided as independent ZIP parts, each at most 256 MB. Every part can be extracted and read on its own. Extract all Gait3D parts into the same directory to obtain the complete exported copy.

The source PKL bytes were preserved and verified individually against the source hashes. `download_manifest.json` and `SHA256SUMS.txt` describe the downloadable archives. The dataset manifests record original file sizes and hashes. `pose_file_index.csv` maps each sequence to its downloadable archive.

Representative arrays checked during export have shape `(T, 17, 3)` and dtype `float64`. T varies by sequence. These are existing processed 2D pose arrays. The CASIA-B export contains the 13,592 PKL files present in the research copy.

Install NumPy, then read a sequence directly from a ZIP.

```sh
python -m pip install numpy
python read_pose.py CASIA-B_pose.zip
python read_pose.py Gait3D_pose.part01.zip
```

Pass `--member` with a path from the file index to read a particular sequence. The original CCPG and SUSTech1K pose packages remain available in release `v2026.11.14`.
