from src.AudioPlayer import AudioPlayer
from src.VLC         import VLC

def endl():
    print('\n')

def main():

    endl()
    
    player = AudioPlayer
    player.open( AudioPlayer, "./resources/orchestral.ogg" )
    player.play( AudioPlayer )
    player.stop( AudioPlayer )
    player.volume = 4
    print( "the volume of the player is: " , player.volume )

    endl()

    vlc = VLC
    vlc.open( VLC, "./resources/orchestral.ogg" )
    vlc.play( VLC )
    vlc.pitch = 10
    print( "the pitch of the vlc is: " , vlc.pitch )
    vlc.stop( VLC )
    vlc.volume = 13  # is calling the method volume for accessign the private atribute
    print( "the volume of the vlc is: " , vlc.volume )
#
# Main...
#
if __name__ == '__main__':
    main()