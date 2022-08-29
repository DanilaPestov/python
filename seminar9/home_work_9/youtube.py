from pytube import YouTube

youtube_video_url = 'https://www.youtube.com/watch?v=4pwpTqKXz2Y&t=1s'
yt_obj = YouTube(youtube_video_url)

# # отображение потоков
# for stream in yt_obj.streams:
#     print(stream)

filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

for mp4_filter in filters:
    print(mp4_filter)

filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')

filters.get_highest_resolution().download()

yt_obj.streams.get_audio_only().download(
    output_path='/Users/pest', filename='audio')
print('downloaded successfully')
