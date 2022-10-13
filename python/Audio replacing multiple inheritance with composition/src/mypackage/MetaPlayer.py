class PlayerMeta( type ):
    # a player metaclass...
    def __instancecheck__( self, instance ):
        return self.__subclasscheck__( type( instance ) )

    def __subclasscheck__( self, subclass ):
        return ( hasattr( subclass, 'open' )     and 
                    callable( subclass.open )    and
                 hasattr( subclass, 'stop' )     and
                    callable( subclass.stop )    and
                 hasattr( subclass, 'play' )     and
                    callable( subclass.play )    and
                 hasattr( subclass, 'volume' )   and 
                    callable( subclass.volume ))
    
class UpdatedInformalPlayerInterface( metaclass = PlayerMeta ):
    pass