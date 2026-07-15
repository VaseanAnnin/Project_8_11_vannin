import unittest
from song import Song

class TestSong(unittest.TestCase):



    def test_add_song(self):
        
        song = Song(
            "Freudian",
            "Daniel Caesar",
            "Guitar",
            "RNB",
            10
        )

        self.assertEqual(song.title, 'Freudian')

        self.assertEqual(song.artist, 'Daniel Caesar')

        self.assertEqual(song.instrument, 'Guitar')

        self.assertEqual(song.genre, 'RNB')

        self.assertEqual(song.progress, 10)

        
    def test_update_progress(self):

        song = Song(
            "Freudian",
            "Daniel Caesar",
            "Guitar",
            "RNB",
            10
        )

        song.update_progress(50)

        self.assertEqual(song.progress, 50)
    
