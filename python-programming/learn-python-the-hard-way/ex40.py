# create a class
class Song(object):
    
    # special __init__ function used to initiate a  class
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    # subsequent class attributes    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# instantiate songs          
happy_bday = Song(["Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
    "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()