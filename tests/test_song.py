import unittest
from song import Song

class TestSong(unittest.TestCase):

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