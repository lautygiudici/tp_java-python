
from src.Vlc import VLC
from src.mypackage.MetaPlayer           import UpdatedInformalPlayerInterface

def main():
    
    print ( issubclass( VLC, UpdatedInformalPlayerInterface ) )

    vlc = VLC

    vlc.open( VLC, "./sources/orchestra.ogg" )
    vlc.pitch = 3.2
    print( vlc.pitch )

if __name__ == '__main__':
    main()