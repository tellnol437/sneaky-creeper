import random
import struct
import wave
import os, re, urllib

requiredParams = {
        'sending': {
            'ID':'Application ID for Soundcloud API',
            'secret': 'Application secret for Soundcloud API',
            'username': 'Username of Soundcloud account to post data to',
            'password': 'Password of Soundcloud account to post data to',
            'song_name': 'Name to be shown for "song" on soundcloud'
            },
        'receiving': {
            'username': 'Username for user to download sound from.',
            'song_name':'Name of the sound file to be downloaded'
            }
        }

dependencies = ['soundcloud']

def send(data, params):
    import soundcloud
    client = soundcloud.Client(
        client_id=params['ID'],
        client_secret=params['secret'],
        username=params['username'],
        password=params['password']
    )

    frames = []

    for i in data:
        frames.append(i)
        frames.append(',')

    wf = wave.open('output.wav', 'wb')
    wf.setnchannels(1)
    wf.setframerate(44100)
    wf.setsampwidth(2)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Done creating sound file")
    track = client.post('/tracks', track={
        'title': params['song_name'],
        'sharing':'public',
        'asset_data': open('output.wav','rb'),
        'tag_list':'tag1 \"hip hop\"',
        'downloadable': 'true' })
    print("Done uploading")

    os.remove('output.wav')

    return

def receive(params):
    import soundcloud
    urllib.urlretrieve("http://soundcloud.com/" + params['username'] +\
            "/" + params['song_name']+ "/download", 'file.wav')
    wf = wave.open('file.wav', 'r')
    data = wf.readframes(wf.getnframes())
    return [data]

if __name__ == "__main__":
    #send(1,1)
    print(receive({'username':'user255215947', 'song_name':'channeltest2'}))
