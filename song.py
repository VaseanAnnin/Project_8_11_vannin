"This class represents an instance of a song that the user is learning"
class Song:
    def __init__(self, title, artist, instrument, genre, progress):
        self.title = title
        self.artist = artist
        self.instrument = instrument
        self.genre = genre
        self.progress = progress

    def update_progress(self, progress):
        self.progress = progress

    def update_dict(self):
        return{
            "title": self.title,
            "artist": self.artist,
            "instrument": self.instrument,
            "genre": self.genre,
            "progress": self.progress
        }
