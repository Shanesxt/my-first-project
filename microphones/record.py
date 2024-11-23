import pyaudio
import wave
import keyboard  # 用于监听键盘事件
import datetime  # 导入datetime模块

# 设置录音参数
CHANNELS = 1
RATE = 16000
FORMAT = pyaudio.paInt16  # 16-bit音频格式
CHUNK = 1024  # 每次读取的音频块大小
OUTPUT_FOLDER = "recordings"

def get_output_filename():
    """
    生成包含当前日期和时间的输出文件名
    :return: 输出文件名字符串，格式为 YYYYMMDD_HHMMSS.wav
    """
    now = datetime.datetime.now()  # 获取当前时间
    return f"{OUTPUT_FOLDER}/{now.strftime('%Y%m%d_%H%M%S')}.wav"  # 格式化为指定的文件名格式

def record_audio():
    """
    使用麦克风录音并保存为 WAV 文件
    按 'q' 键停止录音
    """
    # 初始化pyaudio
    p = pyaudio.PyAudio()
    
    # 创建音频流
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    print("Recording... Press 'q' to stop.")
    
    frames = []  # 用于保存音频数据
    while True:
        # 读取音频块
        data = stream.read(CHUNK)
        frames.append(data)
        
        # 检查是否按下了 'q' 键
        if keyboard.is_pressed('q'):
            print("Recording stopped by user.")
            break
    
    # 停止音频流
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # 保存音频到 WAV 文件
    output_filename = get_output_filename()
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))  # 将录音数据写入文件
    
    print(f"Audio has been saved to {output_filename}")
    return output_filename

if __name__ == "__main__":
    output_filename = record_audio()
