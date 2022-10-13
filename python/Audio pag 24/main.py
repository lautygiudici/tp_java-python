from src.VLCPlayer import VLCPlayer as Vlc
from src.Winamp    import Winamp    as Wamp

def main():

    vlc = Vlc

    vlc.open( Vlc, "birds.ogg" )
    vlc.play( Vlc )
    vlc.stop( Vlc )
    vlc.volume = 13.2
    vlc.pitch = 1.0

    print( "the volume is: " , vlc.volume )
    print( "the pitch is: " ,  vlc.pitch )

    print("\n\n\n")

    winamp = Wamp

    winamp.open( Wamp, "dogs.flac" )
    winamp.play( Wamp )
    winamp.stop( Wamp )
    winamp.volume = 10.2

    print( "the volume is: " , winamp.volume )

if __name__ == '__main__':
    main()