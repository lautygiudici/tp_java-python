class Player:
    # abstract member of the class... kindof ~(-_-)~
    def open( filePath ):
        pass

    def __init__():
        # private atributes of a class...
        _isOpen     = False
        _isPlaying  = False
        _volume     = 0.0

    def play( self ):
        if( self.isOpen ): 
            self.isPlaying = True
            print( "The audiofile is playing." )
    
    def stop( self ):
        if( self.isPlaying ): 
            self.isPlaying = False
            print( "The audiofile is stoped." )

    def volume( self, value ):
        self._volume = value

    def isPlaying( self, value ):
        self._isPlaying = value
    
    def isOpen( self, value ):
        self._isOpen = value

    def volume( self ):
        return self._volume

    def isPlaying( self ):
        return self.isPlaying

    def isOpen( self ):
        return self._isOpen
    