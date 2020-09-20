import os 
import filetype
import pyjokes


def music():
    songs_dir = 'C:/Users/Michael J/Music'
    files = os.listdir(songs_dir)
    songs = []
    for file in files:
        try:
            if filetype.is_audio(os.path.join(songs_dir, file)):
                songs.append(file)
        except PermissionError:
            continue
    os.startfile(os.path.join(songs_dir, songs[0])) 
    

def jokes():
    return (pyjokes.get_joke())
