class PlayerPitchableMeta( type ):
    # a player metaclass...
    def __instancecheck__( self, instance ):
        return self.__subclasscheck__( type( instance ) )

    def __subclasscheck__( self, subclass ):
        return ( hasattr( subclass, 'pitch' ) and callable( subclass.pitch ) )

class UpdatedInformalPlayerPitchableInterface( metaclass = PlayerPitchableMeta ):
    pass