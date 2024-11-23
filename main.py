import whisper
import torch
from microphones.record import record_audio

# 录制音频并保存文件
output_filename = record_audio()

# 加载保存的模型权重
model_path = "whisper_models/large-v3-turbo.pt"
model = whisper.load_model(model_path)


# 进行转录
result = model.transcribe(output_filename)

# 输出转录结果
print(result["text"])

