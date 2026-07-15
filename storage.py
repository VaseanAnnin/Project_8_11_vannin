"""This file manages saving songs and writing them to the json file as well as populating a list of songs when asked by the application"""
import json
from song import Song

def load_songs():
    try:
        with open("songs.json","r") as file:
            data = json.load(file)
            return [Song(title=song["title"],artist=song["artist"],instrument=song["instrument"],genre=song["genre"],progress=song["progress"]) for song in data]
    
    except FileNotFoundError:
        return[]

def save_songs(song_list):
    with open("songs.json", "w") as file:
        json.dump([song.to_dict() for song in song_list],
                  file)
