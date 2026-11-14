"""Read one pose sequence directly from an exported ZIP archive."""
import argparse
import pickle
import zipfile


def read_pose(archive_path, member=None):
    with zipfile.ZipFile(archive_path) as archive:
        if member is None:
            member = next(name for name in archive.namelist() if name.endswith(".pkl"))
        with archive.open(member) as source:
            return member, pickle.load(source)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive")
    parser.add_argument("--member")
    arguments = parser.parse_args()
    member, pose = read_pose(arguments.archive, arguments.member)
    print("Sequence", member)
    print("Array type", type(pose).__name__)
    print("Shape", pose.shape)
    print("Data type", pose.dtype)
    print("First frame", pose[0])
