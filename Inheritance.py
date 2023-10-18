

class File:
    def __init__(self, size, extension, name):
            self.__size = size
            self.__extension = extension
            self.__name = name
            
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def size(self):
        return self.__size
    
    @property
    def extension(self):
        return self.__extension
    
class Picture(File):
    def __init__(self, size, extension, name, resolution_x, resolution_y):
        super().__init__(size, extension, name)
        self.__resolution_x = resolution_x
        self.__resolution_y = resolution_y
        
    @property
    def resolution_x(self):
        return self.__resolution_x
    
    @property
    def resolution_y(self):
        return self.__resolution_y
    
class GIF(Picture):
    def __init__(self, size, extension, name, resolution_x, resolution_y, owner):
        super().__init__(size, extension, name, resolution_x, resolution_y)
        self.__owner = owner
    
    @property
    def owner(self):
        return self.__owner
        
class Movie(File):
    def __init__(self, size, extension, name, title, time, year):
        super().__init__(size, extension, name)
        self.__title = title
        self.__time = time
        self.__year = year
        
    @property
    def title(self):
        return self.__title
    
    @property
    def time(self):
        return self.__time
    
    @property
    def year(self):
        return self.__year
    
class Music(File):
    def __init__(self, size, extension, name, title, artist, time):
        super().__init__(size, extension, name)
        self.__title = title
        self.__artist = artist
        self.__time = time
    
    @property
    def title(self):
        return self.__title
    
    @property
    def artist(self):
        return self.__artist
    
    @property
    def time(self):
        return self.__time
    
class Pdf(File):
    def __init__(self, size, extension, name):
        super().__init__(size, extension, name)

class Car:
    def __init__(self, brand, engine):
        self.__brand = brand
        self.__engine = engine

class Player:
    def play(file):
        if isinstance(file, Music):
            print("title: ", file.title)
            print("artist:" , file.artist)
            print("time: ", file.time)
            print("size: ",file.size)
            print("extension: ", file.extension)
            print("name: ", file.name)
            print()
        elif isinstance(file,Movie):
            print("time: ",file.time)
            print("size: ",file.size)
            print("extension: ",file.extension)
            print("name: ",file.name)
            print("title: ",file.title)
            print("time: ",file.time)
            print("year: ",file.year)
            print()
        elif isinstance(file, GIF):
            print("size: ",file.size)
            print("extension: ",file.extension)
            print("name: ",file.name)
            print("resolution x: ",file.resolution_x)
            print("resolution y: ",file.resolution_y)
            print("owner: ",file.owner)
            print()
        elif isinstance(file, Picture):
            print("size: ",file.size)
            print("extension: ",file.extension)
            print("name: ",file.name)
            print("resolution x: ",file.resolution_x)
            print("resolution y: ",file.resolution_y)
            print()
        elif isinstance(file, Pdf):
            print("format unknown")
            print()
        elif isinstance(file, File):
            print("size: ",file.size)
            print("extension: ",file.extension)
            print("name: ",file.name)
            print()
        else:
            print("format unknow")
            print()
        
ms1 = Music("600MB", "mp3", "Hobbit", "Blunt the Knives", "Howard Shore", "1 minute 2 seconds")
g1 = GIF("160MB", "gif", "Funny_car", 720, 480, "user1")
m1 = Movie("2GB", "mov", "movie1", "Scent of a Woman", "2 hour 37 minutes", 1992)
f1 = File("500MB", "docx", "Notes")
p1 = Picture("8MB", "png", "Tree", 1920, 1080)
pd1 = Pdf("100MB", "pdf", "book")
c1 = Car("Ferrari", "expensive")


Player.play(ms1)
Player.play(g1)
Player.play(m1)
Player.play(f1)
Player.play(p1)
Player.play(pd1)
Player.play(c1)

ms1.name = "An Unexpected Journey"

Player.play(ms1)

    
