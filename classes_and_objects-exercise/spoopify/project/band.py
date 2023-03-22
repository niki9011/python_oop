from project import Album
class Band:
    albums = []

    def __init__(self, name: str):
        self.name = name

    def add_album(self, album: Album):
        if album not in Band.albums:
            Band.albums.append(album)
            return f"Band {self.name} has added their newest album {album}."

        return f"Band {self.name} already has {album} in their library."

