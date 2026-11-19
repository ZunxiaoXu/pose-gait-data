import argparse
import io
from pathlib import Path
import re
import zipfile

import numpy as np


def main():
    parser = argparse.ArgumentParser(description="Inspect an original Gait3D SMPL frame.")
    parser.add_argument("path", type=Path, help="A sample ZIP package or a single NPZ file.")
    parser.add_argument("--member", help="NPZ member path inside a ZIP package.")
    args = parser.parse_args()
    if args.path.suffix.lower() == ".npz":
        member = args.path.name
        content = args.path.read_bytes()
    else:
        with zipfile.ZipFile(args.path) as archive:
            members = [name for name in archive.namelist() if name.endswith(".npz")]
            if not members:
                raise ValueError("The archive has no NPZ frames.")
            def frame_key(name):
                match = re.search(r"_f(\d+)\.npz$", name)
                return name.rsplit("/", 1)[0], int(match.group(1))
            member = args.member or min(members, key=frame_key)
            content = archive.read(member)
    with np.load(io.BytesIO(content), allow_pickle=True) as saved:
        results = saved["results"].item()
    print(member)
    for name, value in results.items():
        array = np.asarray(value)
        print(f"{name}: shape={array.shape}, dtype={array.dtype}")


if __name__ == "__main__":
    main()
