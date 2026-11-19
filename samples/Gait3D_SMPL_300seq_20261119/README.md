# Gait3D SMPL samples

本批包含 300 个身份各 1 条完整序列，共 34,978 个原始 NPZ 帧文件。序列长度为 25 至 473 帧，中位数为 88.5 帧。原始 NPZ 文件字节与源分卷一致。

下载文件位于 [本批 GitHub Release](https://github.com/ZunxiaoXu/pose-gait-data/releases/tag/gait3d-smpl-300seq-20261119)。将全部 ZIP 分包解压到同一个目录即可恢复数据层级。每个 ZIP 均可独立打开和解压，并包含完整序列。单包大小上限为 256,000,000 字节（256 MB）。

| 分包 | 序列数 | 帧文件数 | 压缩字节数 |
| --- | ---: | ---: | ---: |
| Gait3D_SMPL_300seq_20261119.max256MB.part01.zip | 48 | 6,239 | 245,104,224 |
| Gait3D_SMPL_300seq_20261119.max256MB.part02.zip | 57 | 6,237 | 245,800,382 |
| Gait3D_SMPL_300seq_20261119.max256MB.part03.zip | 51 | 6,277 | 247,271,104 |
| Gait3D_SMPL_300seq_20261119.max256MB.part04.zip | 57 | 6,335 | 249,002,428 |
| Gait3D_SMPL_300seq_20261119.max256MB.part05.zip | 56 | 6,240 | 245,487,306 |
| Gait3D_SMPL_300seq_20261119.max256MB.part06.zip | 31 | 3,650 | 143,466,123 |

目录层级为 `3D_SMPLs/身份ID/camid摄像头编号_videoid视频编号/seq序列编号/human_crop_f帧编号.npz`。按文件名中 `f` 后面的整数排列帧顺序。序列长度按 NPZ 文件数量统计，帧编号可能存在间隔。

`sequence_index.csv` 逐序列登记身份、摄像头、视频、序列编号、帧数与所在分包。`file_index.csv` 逐帧登记原始路径、帧号、大小、CRC32、SHA256 与所在分包。`sample_manifest.json` 记录来源、抽样方式、数量和压缩包信息。`SHA256SUMS.txt` 用于核对下载文件。

本批从 `3D_SMPLs_part.z12` 中完整存放的 2,143 条序列、352 个身份组成的候选池抽取。保留之前的 3 条样本，再按固定随机种子 `20261119` 选择另外 297 个不同身份，每个身份随机选择 1 条完整序列。抽样范围为这个分卷中的候选池。

数据来源为 [Gait3D 项目](https://gait3d.github.io/) 和用户提供的 [Google Drive 目录](https://drive.google.com/drive/folders/1Ej9pJykl6Hzx85TG4ug17F5RSN-yWJJS)。原论文为 Jinkai Zheng 等的 “Gait Recognition in the Wild with Dense 3D Representations and a Benchmark”, CVPR 2022。数据使用遵循原数据集协议。

每个 NPZ 的内容组织为 `results` 字典。已抽查文件中的主要字段包括 `poses (72,)`、`betas (10,)`、`cam (3,)`、`j3d_smpl24 (24, 3)` 和 `verts (6890, 3)`。可使用附带的 `read_smpl.py` 查看指定帧的字段、形状和数据类型。

```sh
python read_smpl.py Gait3D_SMPL_300seq_20261119.max256MB.part01.zip
python read_smpl.py Gait3D_SMPL_300seq_20261119.max256MB.part01.zip --member 3D_SMPLs/0012/camid30_videoid2/seq0/human_crop_f5822.npz
```

读取脚本需要 NumPy。逐帧文件已通过源 ZIP CRC32 和 NPZ 内部 CRC 校验，发布压缩包已通过 ZIP 完整性校验。
