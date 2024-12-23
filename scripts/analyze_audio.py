import librosa
import numpy as np
import os

# # スクリプトのディレクトリを基準に相対パスを解決
# script_dir = os.path.dirname(__file__)
# print(script_dir,"aaaaa")
# file_path = os.path.join(script_dir, '../data/shimi.mp3')

# # 音声ファイルのパス
# file_path = '../data/shimi.mp3'
file_path = r'C:\Users\mnbsou\Desktop\dev\play-hero\data\shimi.mp3'

# ファイルの存在確認
if os.path.exists(file_path):
    print(f"File exists: {file_path}")
else:
    print(f"File not found: {file_path}")

# 音声ファイルを読み込む
y, sr = librosa.load(file_path)

# 音声のオンセット（音の始まり）を検出
onset_frames = librosa.onset.onset_detect(y=y, sr=sr)

# フレームを時間に変換
onset_times = librosa.frames_to_time(onset_frames, sr=sr)

# ギターイントロの開始と終了を推定
# ここでは最初のオンセットを開始、次のオンセットを終了と仮定
intro_start = onset_times[0]
intro_end = onset_times[1] if len(onset_times) > 1 else None

print(f"ギターイントロの開始時間: {intro_start}秒")
if intro_end:
    print(f"ギターイントロの終了時間: {intro_end}秒")
else:
    print("ギターイントロの終了時間を検出できませんでした。")