"""
Program: Music Collection and Practice Tracker

Author: Vasean Annin

Purpose: This aplication will store and manage the users
music collection as well as track their progress as they practice
the songs in the collection. It also stores the data using JSON persistence

Date: 07/15/2026

"""
from menu import menu
from tracker import add_song, view_songs, search_songs, update_progress, delete_song
from storage import load_songs

running = True
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
