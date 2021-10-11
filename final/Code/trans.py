# import ffmpeg

# # ffmpeg.input('Rec 0001_1_1.wav').output('output.wav', ar=16000).run()
# ff = FFmpeg(
#         inputs={'fate.mkv': None},
#         outputs={'fate.m3u8': '-c:v libx264 -c:a aac -strict -2 -f hls -hls_list_size 0 -hls_time 2'}
#     )
# print(ff.cmd)
# # ffmpeg -i fate.mkv -c:v libx264 -c:a aac -strict -2 -f hls -hls_list_size 0 -hls_time 2 fate.m3u8
# ff.run()

# import ffmpeg

# ffmpeg.input('1.wav').output('2.wav', ar=16000).run()

# import librosa

# y, sr = librosa.load('1.wav',48000)
# # 需要修改的采样率
# y_16 = librosa.resample(y, sr, 16000)
# # 保存的音频路径和需要修改的采样率
# librosa.output.write_wav('2.wav', y_16, 16000)

# import sox

# def upsample_wav(file, rate):
#     tfm = sox.Transformer()
#     tfm.rate(rate)
#     out_path = file.split('.wav')[0] + "_new.wav"
#     tfm.build(file, out_path)
#     return out_path

# print(upsample_wav('1.wav',16000))

import librosa
import os

def resample_rate(path,new_sample_rate):
    
    signal, sr = librosa.load(path, sr=None)
    wavfile = path.split('/')[-1]
    wavfile = wavfile.split('.')[0]
    file_name = wavfile + '_new.wav'
    new_signal = librosa.resample(signal, sr, new_sample_rate) # 
    librosa.output.write_wav(file_name, new_signal , new_sample_rate)
    #命令行执行sox 1_new.wav -b 16 -e signed-integer 1_new.wav

resample_rate('向左.wav',16000)
