from project import Song
class Album:
    def __init__(self, name: str):
        self.name = name
        self.published = False
        self.songs = []

    def add_song(self, song: Song):
        if song not in self.songs:
            self.songs.append(song)
            return f"Song {song} has been added to the album {self.name}."

        if song in self.songs:
            return "Song is already in the album."

        if self.published:
            return "Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song}. It's a single"

    def remove_song(self, song_name: str):
        if song_name in self.songs:
            self.songs.remove(song_name)
            return f"Removed song {song_name} from album {self.name}."

        if song_name not in self.songs:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):
        return f"Album {self.name}\n" + "\n".join(["== {s}" for s in self.songs])

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D")
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
