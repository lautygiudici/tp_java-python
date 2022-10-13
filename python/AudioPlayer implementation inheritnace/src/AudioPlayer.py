class AudioPlayer():
    def __init__( self ):
        print( "The audioPlayer constructor was invoked" )
        _isOpen = False
        _isPlaying = False
        _volume = 0.0
        self.volume = 10.0
    
    def open( self, filePath ):
        self.isOpen = True
        print( "The audiofile: " , filePath , "is open." )

    def play( self ):
        if( self.isOpen ):
            self.isPlaying = True

    def stop( self ):
        if( self.isPlaying ):
            self.isPlaying = False
        print( "The audiofile is stopped." )

    def volume( self, value ):
        self.volume = value

    def isOpen( self, value ):
        self.isOpen = value

    def isPlaying( self, value ):
        self.isPlaying = value

    def volume( self ):
        return self.volume

    def isOpen( self ):
        return self.isOpen
    
    def isPlaying( self ):
        return self.isPlaying
