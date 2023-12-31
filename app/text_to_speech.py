import configparser
import os
import shutil
import subprocess

import pandas as pd
import pyfiglet
from tqdm import tqdm

# LOAD CONFIGURATION FROM CONFIG.INI FILE
config = configparser.ConfigParser()
config.read("./app/config.ini")

# SET FILE PATHS
file_path_excel = config["FILE_PATHS"]["file_path_excel"]
audio_output_path = config["FILE_PATHS"]["audio_output_path"]

# SET MODEL PATHS
selectedModel = config["MODEL_CONFIGS"]["selectedModel"]
# encoderPath = config["MODEL_CONFIGS"]["encoderPath"]
encoderConfig = config["MODEL_CONFIGS"]["encoderConfig"]
speakerWav = config["MODEL_CONFIGS"]["speakerWav"]


# SET EXCEL COLUMN NAMES
col_name_1 = config["COL_NAMES"]["col_name_1"]
col_name_2 = config["COL_NAMES"]["col_name_2"]


def main():
    result = pyfiglet.figlet_format("Text to Speech", font="slant")
    print(result)
    # READ EXCEL FILE INTO A PANDAS DATAFRAME
    df = pd.read_excel(file_path_excel)

    start = 0
    end = len(df)
    # end = 1

    for i in tqdm(range(start, end)):
        text_from_csv = df[col_name_1][start:end][i]
        out_path_file_name = df[col_name_2][start:end][i]

        print("*" * 120)
        print(f"OUTPUT FILE NAME: {out_path_file_name}")
        # print("*"*120)
        # print("*"*120)
        print(f"TEXT FROM CSV FILE TO BE CONVERTED TO SPEECH: {text_from_csv}")
        # print("*"*120)

        model_name = selectedModel
        # encoder_path = encoderPath
        encoder_config = encoderConfig
        speaker_wav = speakerWav
        out_path = f"{audio_output_path}{out_path_file_name}.wav"
        language_idx = '"en"'
        text = '"' + text_from_csv + '"'

        # command = f"tts --model_name {model_name} --encoder_path {encoder_path} --encoder_config {encoder_config} --speaker_wav {speaker_wav} --text {text} --out_path {out_path} --language_idx {language_idx}"
        command = f"pipenv run tts --text {text}  --model_name {model_name} --out_path {out_path}"
        print(f"EXECUTING COMMAND NOW: {command}")
        subprocess.run(command, shell=True)
        print("*" * 120)


if __name__ == "__main__":
    main()
