class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listened = set()

    def how_many(self, arr):
        new = 0
        for p in arr:

            if p.lower() not in self.listened:
                new += 1
            self.listened.add(p.lower())
        return new