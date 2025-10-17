import re
import csv
from pathlib import Path
import uuid

def create_submission_file(submission_rows, output_dir=".", interactive=True, student_id=None, unique_id=None):
    """
    学生番号を入力して形式を確認し、提出用CSVファイルを生成する関数。

    Parameters
    ----------
    submission_rows : list
        [["id", "label"], ...] のような提出データ行。
    unique_id : str
        学生ごとのUUIDなど一意なID。
    output_dir : str, optional
        出力先ディレクトリ。デフォルトはカレントディレクトリ。
    interactive : bool, optional
        True の場合は入力プロンプトを使用。False の場合は引数 student_id を使用。
    student_id : str, optional
        interactive=False の場合に使用する学生番号。

    Returns
    -------
    str
        作成されたファイルのパス。
    """
    pattern = r"^AR\d{5}$"

    if unique_id is None:
        unique_id = str(uuid.uuid4())

    if interactive:
        while True:
            student_id = input("あなたの学生番号を入力してください（例：AR22999）: ").strip()
            if re.match(pattern, student_id):
                print("✅ 学生番号を受け付けました:", student_id)
                break
            else:
                print("❌ 形式が正しくありません。AR+数字5桁で入力してください。")
    else:
        if not student_id or not re.match(pattern, student_id):
            raise ValueError("student_id が不正です。AR+数字5桁の形式で指定してください。")

    file_path = Path(output_dir) / f"submission_{student_id}.csv"
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "label"])
        writer.writerows(submission_rows)
        writer.writerow([student_id, unique_id])
        print(f"📄 提出用ファイルを作成しました: {file_path}")

    return str(file_path)
