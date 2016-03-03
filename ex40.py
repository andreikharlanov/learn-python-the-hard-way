class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

ya_ya_moo = Song(["I'm the moo,",
                  "I'd like to moo."])

hit_song_lyrics = ["Come here and dance with me,", "I'm the queen of this town,",
            "Is it so hard to understand?", "Don't fool around,",
            "Don't fool around."]

hit_song = Song(hit_song_lyrics)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

ya_ya_moo.sing_me_a_song()

hit_song.sing_me_a_song()
