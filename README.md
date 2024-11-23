# my-first-project
This is my first project on GitHub.

## 项目简介

这个项目结合了麦克风录音和使用 OpenAI 的 Whisper 模型进行语音转文本的功能。用户可以通过录音设备录制音频，录制结束后，程序会自动将音频文件保存，并使用 Whisper 模型对音频进行转录，最终输出文本内容。该项目适用于需要将音频转换为文本的场景，支持实时录音、文件保存和转录输出。
---

## 安装说明

1. **安装依赖库**  
   请确保您已经安装了 Python 3.7 或更高版本，然后使用以下命令安装项目所需的依赖库：  
   ```bash
   pip install torch whisper pyaudio keyboard
   ```

2. **下载 Whisper 模型**  
   您需要下载 Whisper 的预训练模型文件，并将其放置在项目中的 `whisper_models/` 文件夹内。  
   
   推荐使用以下模型：
   - **base** 模型
   - **turbo** 模型

   请访问 [OpenAI Whisper 模型库](https://github.com/openai/whisper) 下载相应的模型文件，并将 `.pt` 文件放入 `whisper_models/` 文件夹中。  

3. **运行项目**  
   安装完成后，您可以通过运行以下命令来启动录音和转录功能：  
   ```bash  
   python main.py
   ```  

---

这样，您就可以完成安装并开始使用本项目进行音频转录了！

---


# Whisper Audio Transcription with Custom Recording  

This project combines audio recording via a microphone with speech-to-text transcription using OpenAI's Whisper model.  

## Features  
- Real-time audio recording using a microphone.  
- Saves audio files with timestamped filenames.  
- Transcribes the recorded audio into text using the Whisper model.  

---

## Requirements  

### Python Dependencies  
The project requires Python 3.7 or higher and the following libraries:  

- `torch`  
- `whisper`  
- `pyaudio`  
- `keyboard`  

To install the dependencies, run:  
```bash  
pip install torch whisper pyaudio keyboard  
```  

---

## Installation  

1. **Download Whisper Model**  
   You will need to download the pre-trained Whisper model and place the `.pt` file in the `whisper_models/` folder of the project.  
   
   It is recommended to use either the **base** or **turbo** models for transcription.  
   
   You can download the models from the [OpenAI Whisper GitHub repository](https://github.com/openai/whisper). After downloading, place the model file (e.g., `large-v3-turbo.pt`) into the `whisper_models/` directory.  

2. **Install Dependencies**  
   Ensure you have Python 3.7 or higher, then install the required libraries by running the following command:  
   ```bash  
   pip install torch whisper pyaudio keyboard  
   ```  

3. **Run the Project**  
   Once dependencies are installed, run the script to start the recording and transcription process:  
   ```bash  
   python main.py  
   ```  

---

## File Structure  

```plaintext  
.  
├── main.py                # Main script for recording and transcribing audio  
├── microphones/record.py  # Utility module for handling audio recording  
├── whisper_models/        # Folder containing Whisper model files  
├── recordings/            # Folder where recorded audio files are saved  
└── README.md              # Project documentation (this file)  
```  

---

## Usage  

### Step 1: Record Audio  
Run the script to start recording:  
```bash  
python main.py  
```  
During the recording:  
- Press **`q`** to stop recording and save the audio file.  

The recorded audio will be saved in the `recordings/` directory with a timestamped filename.  

### Step 2: Transcribe Audio  
The script automatically transcribes the recorded audio using the Whisper model and prints the transcribed text to the console.  

---

## Example Workflow  

1. Start recording:  
   ```
   Recording... Press 'q' to stop.  
   ```  
2. After stopping, you'll see:  
   ```
   Audio has been saved to recordings/20241124_153012.wav  
   ```  
3. Transcription output:  
   ```
   Hello, this is a test transcription.  
   ```  

---

## Customization  

### Change Recording Parameters  
Modify the constants in `record_audio()` to adjust recording settings:  
- `RATE`: Sampling rate (default is 16 kHz).  
- `CHANNELS`: Number of audio channels (default is mono).  
- `CHUNK`: Size of audio chunks for buffering.  

### Change Model  
Update the `model_path` variable in the main script to use a different Whisper model file.  

---

## Troubleshooting  

1. **Error: Cannot detect microphone input**  
   Ensure your microphone is enabled and accessible.  

2. **PermissionError with keyboard module**  
   Run the script with administrator privileges.  

3. **PyAudio installation issues**  
   On some systems, `pyaudio` installation may require additional system packages. Refer to [PyAudio installation guide](https://people.csail.mit.edu/hubert/pyaudio/#downloads).  

---

## Acknowledgments  

- Whisper model by OpenAI  
- Audio handling by PyAudio  

---  

Feel free to modify the file further for your specific use case!


