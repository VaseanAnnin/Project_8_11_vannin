from song import Song
from storage import save_songs

def add_song(songs):
    ## This function is for adding a new song
    title = input("Song title: ")
    artist= input("Artists: ")
    instrument = input("Instruments: ")
    genre = input("Genre: ")
    progress = int(input("Progress: "))

    song = Song(title=title,
               artist=artist,
               instrument=instrument,
               genre=genre,
               progress=progress)
    song.append(song)
    save_songs(songs)

    print("=========Song added=========")

def view_songs(songs):
    ##This function displays the current songs within the app

    if(len(songs)) == 0:
        print("No songs in database")
        return
    
    for i, song in enumerate(songs, start = 1):
        print(f"\nSong {i}")
        print(f"title: {song.title}")
        print(f"artist: {song.artist}")
        print(f"instrument: {song.instrument}")
        print(f"genre: {song.genre}")
        print(f"progress: {song.progress}%")

def search_songs(songs):
    ##Search a song within the database
    search = input("song title: ")
    found = False

    for song in songs:
        if song.title.lower() == search.lower():
            print(f"\n============Song============")
            print(f"title: {song.title}")
            print(f"artist: {song.artist}")
            print(f"instrument: {song.instrument}")
            print(f"genre: {song.genre}")
            print(f"progress: {song.progress}%")
            return song
    
    if found ==False:
        print("Can't find song")


def update_progress(songs):
    ##Function updates the progress of a song after searching
    song = search_songs(songs)
    if song is None:
        print("Song was not found")
        return
    progress = int(input("Progress: "))
    song.update_progress(progress)
   

def delete_song(songs):
    ## This function deletes the song after searching for it
    song = search_songs(songs)

    if song is None:
        return 
    songs.remove(song)
    
