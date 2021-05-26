###################
# Nombre: Erick Alberto Bustos Cruz
# Matricula: A01378966
###################

class Song:
    
    def __init__(self,title,artist,album,rating):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__rating = int(rating)
        
    @property
    def title(self):
        return self.__title
    
    @property
    def artist(self):
        return self.__artist
    
    @property
    def album(self):
        return self.__album
    
    @property
    def rating(self):
        return self.__rating
        
    @rating.setter
    def rating(self,rating):
        self.__rating = rating
      
    def __str__(self):
        stars = '★'
        return f'{self.__title} - {self.__artist} - {self.__album} - {self.__rating * stars}'


class Playlist:
    
    def __init__(self,name):
        self.__name = name
        self.__playlist = []
        self.actual = ''
    
    def add_to_playlist(self,song):
        if self.actual == '':
            self.__playlist.append(song)
            self.actual = song
        else:
            self.__playlist.append(song)
        
    def now_playing(self):
        if self.__playlist == []:
            return 'No songs to play'
        else:
            return f'Now playing: {self.actual}'
    
    def play_next(self):
        if self.actual == self.__playlist[-1]:
            self.actual = self.__playlist[0]
        else:
            for i in range(0,1,len(self.__playlist)+1):
                if self.__playlist[i] == self.actual:
                    self.actual = self.__playlist[i+1]
                  
    
    def play_previous(self):
        if self.actual == self.__playlist[0]:
            self.actual = self.__playlist[-1]
        else:
            for i in len(self.__playlist):
                if self.__playlist[i] == self.actual:
                    self.actual = self.__playlist[i-1]
                  
    
    def __str__(self):
        prtsongs = ''
        num = 1
        for i in self.__playlist:
            if i == self.__playlist[-1]:
                prtsongs += f'{num}. {i}'    
            else:
                prtsongs += f'{num}. {i}\n'  
            num += 1
        return f'{self.__name}\n{prtsongs}'
      


# Pruebas, no cambies nada a partir de aquí #
if __name__ == '__main__':
    plst = Playlist('Musica para examenes')
    s1 = Song('Flirtin With Disaster', 'Molly Hatchet', 'Flirtin With Disaster', 3)
    print(plst.now_playing(), '\n')
    
    plst.add_to_playlist(s1)
    print(plst.now_playing(), '\n')
    
    s2 = Song('In The End', 'Linkin Park', 'Hybrid Theory', 4)
    plst.add_to_playlist(s2)
    plst.play_next()
    print(plst.now_playing(), '\n')
    
    plst.play_next()
    print(plst.now_playing(), '\n')
    
    plst.play_next()
    print(plst.now_playing(), '\n')
    
    s2.rating = 2
    print(plst, '\n')
    
    s3 = Song('Glasgow 1877', 'Tuomas Holopainen', 'Music Inspired by the Life and Times of Scrooge', 4)
    s4 = Song('Flash', 'Queen', 'Flash Gordon', 5)
    plst.add_to_playlist(s3)
    plst.add_to_playlist(s4)
    print(plst)