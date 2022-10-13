from src.mypackage.MetaPlayerPitchable import *
from src.mypackage.MetaPlayer          import *

class VLCPitchable:
    def __init__( self ):
        _pitch = 0.0

    def pitch( self, value ):
        self.pitch = value

    def pitch( self ):
        return self.pitch

class VLC:
    def __init__( self ):
        _isOpen     = False
        _isPlaying  = False
        _volume     = 0.0
        _playerPitchable = VLCPitchable
    
    def pitch( self, value ):
        self.playerPitchable.pitch = value

    def pitch( self ):
        return self.playerPitchable.pitch

    def open( self, filePath ):
        self.isOpen = True
        print( "The audiofile: " , filePath , " is open." )

    def play( self ):
        if( self.isOpen ):
            self.isPlaying = True
            print( "The audiofile is playing." )

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



