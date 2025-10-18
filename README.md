# dlcsubmissiontool
for DeepLearningCompetition

**D**eep**L**earning**C**ompetition_**submissiontool**：<br>
このリポジトリは，講義「深層学習」内で実施するコンペティションを実施するにあたり，<br>
推論結果を集めた提出用のCSVファイルを生成する関数をライブラリとして提供するためのものです．<br>
インストールとインポートは以下のように行います．
```
# 提出用ツールのインストール
! pip install -q git+https://github.com/Taiga10969/dlcsubmissiontool.git
```
```
from dlcsubmissiontool import create_submission_file
```

※DLC：**D**eep**L**earning**C**ompetitionのプロジェクトページは[こちら](https://github.com/Taiga10969/DeepLearningCompetition)です．<br>
※本プロジェクトは，特定の大学の講義用に設計されたものになります．汎用的なツールではありません．
