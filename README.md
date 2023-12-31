<table style="width:100%" align="center">
  <tr>
    <td><img src="https://i.imgur.com/Ku7jCo0.jpg"/></td>
  </tr>
</table>

### Overview

The Text to Speech (TTS) project is a Python-based application that converts text data from an Excel file into speech audio files. The system uses a pre-trained TTS model, providing users with the ability to customize various parameters, such as the selected TTS model, encoder configuration, and speaker information.

### Features

1. Customization via Configurations:

   - The project uses a configuration file (config.ini) to set file paths, model configurations, and column names in the Excel file.
   - Users can easily configure the input Excel file path, audio output path, selected TTS model, and other relevant parameters.

2. Excel Data Processing:

   - The application reads text data from an Excel file into a Pandas DataFrame.
   - Users can customize the names of the columns containing text and output file names.

3. TTS Model Integration:

   - The system integrates with the [Coqui TTS](https://github.com/coqui-ai/TTS) library, allowing users to leverage various TTS models for speech synthesis.

4. Command-Line Execution:

- Users can run the project via the command line, specifying the desired text, TTS model, and output path.
- The provided examples in the README showcase various command-line options, including multilingual models, voice conversion, and more.

# Quick Start Guide

### INSTALLATION

- `git clone https://github.com/mm-mazhar/text_to_speech.git`
- cd in to the directory where the project folder is
- Open command prompt and run `pip install pipenv`
- Setup the environment `pipenv sync` or `pipenv install`
- other useful commands:
- `pipenv graph`
- `pipenv shell`

### INSTALL DEPENDENCIES

- `pipenv install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 tts==0.17.4 pandas==2.1.1 openpyxl==3.1.2 tqdm==4.66.1 ipykernel==6.25.2 pyfiglet==1.0.2`

or

- Install from the Pipfile.lock `pipenv install --ignore-pipfile`

### CONFIGURATION

Do the following settings in `./app/config.ini` file.

1.  Set excel file path: e.g. `file_path_excel = ./app/data/text_to_speech.xlsx`
2.  Set Text Column e.g. `col_name_1 = Text`
3.  Set Output File Name e.g. `col_name_2 = Output_FileName`
4.  Set output folder i.e. where audio files will be saved e.g. `audio_output_path = ./app/audio_outputaudio_output/`

### RUN

    pipenv run python ./app/text_to_speech.py

### RESOURCES

> [TTS Github](https://github.com/coqui-ai/TTS)

> [TTS Notebook](https://github.com/coqui-ai/TTS/blob/dev/notebooks/Tutorial_1_use-pretrained-TTS.ipynb)

> [TTS Documentation](https://tts.readthedocs.io/en/latest/inference.html)

# NEED MORE CUSTOMIZATION

### RUN VIA CLI

RUN MULTILINGUAL MODEL

To use this, you may need to download `model_se.pth.tar` file and place it in `./app/config/` folder and also comment off `encoderPath = ./app/configs/model_se.pth.tar` line in `./app/config.ini` file and line number 20, 52, 59 in `./app/text_to_speech.py`

`pipenv run tts --model_name tts_models/multilingual/multi-dataset/xtts_v1 --encoder_path ./app/configs/model_se.pth.tar --encoder_config ./app/configs/config_se.json --speaker_wav ./app/configs/LJ001-0001.wav --text "Are we not allowed to dim the lights so people can see that a bit better?" --out_path ./app/output/output.wav --language_idx "en"`

VOICE CONVERSION

`pipenv run tts --text "Enter some text here" --model_name "voice_conversion_models/multilingual/vctk/freevc24" --source_wav "./app/configs/LJ001-0001.wav" --target_wav "./app/configs/LJ001-0001.wav" --out_path ./app/output/output.wav`

LIST MODELS

`pipenv run tts --list_models`

LIST THE POSSIBLE SPEAKER IDs

`pipenv run tts --model_name "tts_models/en/vctk/vits" --list_speaker_idxs`

RUN WITH COCODER

`pipenv run tts --text "Sample text"  --out_path spkr-out.wav --model_name "tts_models/en/ljspeech/glow-tts" --vocoder_name "vocoder_models/en/ljspeech/univnet"`

SYNTHESIZE SPEECH USING SPEAKER ID

`pipenv run tts --text "Trying out specific speaker voice" --out_path spkr-out.wav --model_name "tts_models/en/vctk/vits" --speaker_idx "p341"`

RUN MULTI-SPEAKER TTS MODEL FROM RELEASED MODELS LIST

List the possible speaker IDs.

`pipenv run tts --model_name "<model_type>/<language>/<dataset>/<model_name>"  --list_speaker_idxs`

    e.g.
    pipenv run tts --model_name "tts_models/multilingual/multi-dataset/bark" --list_speaker_idxs

    e.g.
    pipenv run tts --model_name "tts_models/multilingual/multi-dataset/xtts_v1" --list_speaker_idxs

    tts --text "Text for TTS." --out_path output/path/speech.wav --model_name "tts_models/<language>/<dataset>/<model_name>"  --speaker_idx "<speaker_id>"

### MODELS INFORMATION

- `pipenv run tts -h`

- `pipenv run tts-server -h`

- `pipenv run tts-server --model_name "<type>/<language>/<dataset>/<model_name>"`

- `pipenv run tts --model_info_by_name <model_type>/<language>/<dataset>/<model_name>`

  e.g.

  - pipenv run tts --model_info_by_name tts_models/en/ljspeech/glow-tts

  - pipenv run tts --model_info_by_name vocoder_models/en/ljspeech/hifigan_v2

### WHERE MODELS GETTS DOWNLOADED

- `C:\Users\<Enter User Name>\AppData\Local\tts\tts_models--multilingual--multi-dataset--xtts_v1`

### LIST OF MODELS

Name format: type/language/dataset/model

- `1: tts_models/multilingual/multi-dataset/xtts_v1`
- `2: tts_models/multilingual/multi-dataset/your_tts`
- `3: tts_models/multilingual/multi-dataset/bark`
- `9: tts_models/en/ek1/tacotron2`
- `10: tts_models/en/ljspeech/tacotron2-DDC`
- `11: tts_models/en/ljspeech/tacotron2-DDC_ph`
- `12: tts_models/en/ljspeech/glow-tts`
- `13: tts_models/en/ljspeech/speedy-speech`
- `14: tts_models/en/ljspeech/tacotron2-DCA`
- `15: tts_models/en/ljspeech/vits`
- `16: tts_models/en/ljspeech/vits--neon`
- `17: tts_models/en/ljspeech/fast_pitch`
- `18: tts_models/en/ljspeech/overflow`
- `19: tts_models/en/ljspeech/neural_hmm`
- `20: tts_models/en/vctk/vits`
- `21: tts_models/en/vctk/fast_pitch`
- `22: tts_models/en/sam/tacotron-DDC`
- `23: tts_models/en/blizzard2013/capacitron-t2-c50`
- `24: tts_models/en/blizzard2013/capacitron-t2-c150_v2`
- `25: tts_models/en/multi-dataset/tortoise-v2`
- `26: tts_models/en/jenny/jenny`

Name format: type/language/dataset/model

- `1: vocoder_models/universal/libri-tts/wavegrad`
- `2: vocoder_models/universal/libri-tts/fullband-melgan`
- `3: vocoder_models/en/ek1/wavegrad`
- `4: vocoder_models/en/ljspeech/multiband-melgan`
- `5: vocoder_models/en/ljspeech/hifigan_v2`
- `6: vocoder_models/en/ljspeech/univnet`
- `7: vocoder_models/en/blizzard2013/hifigan_v2`
- `8: vocoder_models/en/vctk/hifigan_v2`
- `9: vocoder_models/en/sam/hifigan_v2`

Name format: type/language/dataset/model

- `1: voice_conversion_models/multilingual/vctk/freevc24`
