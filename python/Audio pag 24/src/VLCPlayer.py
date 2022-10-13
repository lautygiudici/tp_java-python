from src.Player import Player

class VLCPlayer( Player ):
    def __init__():
        super().__init__()
        
        # private atributes of the class 
        _pitch = 0.0
        _filePath = ""
    
    def filePath( self, aFilePath ):
        self.filePath = aFilePath

    def open( self, aFilePath ):
        self.isOpen = True
        self.filePath = aFilePath
        print( "The audiofile: " , self.filePath , " is open." )

    def pitch( self, value ):
        self.pitch = value
    
    def pitch( self, this ):
        return this._pitch
