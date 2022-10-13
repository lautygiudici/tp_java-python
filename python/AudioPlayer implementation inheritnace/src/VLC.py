from src.AudioPlayer import AudioPlayer

class VLC( AudioPlayer ):
    def __init__( self ):
        print( "The VLC constructor was invoked" )
        self.volume = 10
        self.pitch = 0

        # private atributes of the class...
        _pitch = 0.0

    def pitch( self, value ):
        self.pitch = value

    def pitch( self ):
        return self.pitch