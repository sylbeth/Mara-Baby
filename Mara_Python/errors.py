from discord.ext.commands import ExtensionError


class ExtensionBanned(ExtensionError):
    """An exception raised when an extension has been banned.
    
    This inherits from :exc:`ExtensionError`
    """
    def __init__(self, name):
        super().__init__('Extension {!r} has been banned.'.format(name), name=name)


class ExtensionAlreadyBanned(ExtensionError):
    """An exception raised when an extension has already been banned.
    
    This inherits from :exc:`ExtensionError`
    """
    def __init__(self, name):
        super().__init__('Extension {!r} is already banned.'.format(name), name=name)


class ExtensionNotBanned(ExtensionError):
    """An exception raised when an extension was not banned.
    
    This inherits from :exc:`ExtensionError`
    """
    def __init__(self, name):
        super().__init__('Extension {!r} has not been banned.'.format(name), name=name)