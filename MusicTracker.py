"""
Program: Music Collection and Practice Tracker

Author: Vasean Annin

Purpose: This aplication will store and manage the users
music collection as well as track their progress as they practice
the songs in the collection

Date: 07/15/2026

"""
from menu import menu
from tracker import add_song, view_songs, search_songs, update_progress, delete_song
from storage import load_songs


"""
    example data
    {
    "title": "Freudian",
    "artist": "Daniel Caesar",
    "instrument":"Guitar",
    "genre": "Neo Soul",
    "progress": 79
    }

"""
songs = load_songs()
"""
def menu():
    ## This function is for the main menu
    print("\n=====================================")
    print("1. Add Song")
    print("2. View Songs")
    print("3. Search Song")
    print("4. Update Progress")
    print("5. Delete Song")
    print("6. Exit")"""

"""
def add_song():
    ## This function is for adding a new song
    title = input("Song title: ")
    artist= input("Artists: ")
    instrument = input("Instruments: ")
    genre = input("Genre: ")
    progress = int(input("Progress: "))

    song = {
        "title": title,
        "artist": artist,
        "instrument": instrument,
        "genre": genre,
        "progress": progress
    }
    songs.append(song)

    print("=========Song added=========")

def view_songs():
    ##This function displays the current songs within the app

    if(len(songs)) == 0:
        print("No songs in database")
        return
    
    for i, song in enumerate(songs, start = 1):
        print(f"\nSong {i}")
        print(f"title: {song['title']}")
        print(f"artist: {song['artist']}")
        print(f"instrument: {song['instrument']}")
        print(f"genre: {song['genre']}")
        print(f"progress: {song['progress']}%")

def search_songs():
    ##Search a song within the database
    search = input("song title: ")
    found = False

    for song in songs:
        if song["title"].lower() == search.lower():
            print(f"\n============Song============")
            print(f"title: {song['title']}")
            print(f"artist: {song['artist']}")
            print(f"instrument: {song['instrument']}")
            print(f"genre: {song['genre']}")
            print(f"progress: {song['progress']}%")
            found = True
            return song
    
    if found ==False:
        print("Can't find song")



running = True

def update_progress():
    ##Function updates the progress of a song after searching
    song = search_songs()

    if song is None:
        return 

    progress = int(input("Progress: "))

    song["progress"] = progress

def delete_song():
    ## This function deletes the song after searching for it
    song = search_songs()

    if song is None:
        return 
    songs.remove(song)
"""
while running:
    menu()
    user_input = input("Enter your choice: ")
    if user_input == "1":
        add_song(songs)
    elif user_input == "2":
        view_songs(songs)
    elif user_input == "3":
        search_songs(songs)
    elif user_input == "4":
        update_progress(songs)
    elif user_input =="5":
        delete_song(songs)
    elif user_input == "6":
        print ("Keep practicing see you soon!")
        running = False
    
    else:
        print("Selection not recognized please try again")
