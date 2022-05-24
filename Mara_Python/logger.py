from logging import getLogger, Logger, DEBUG, FileHandler, Formatter
from os.path import join as joinpath


logger: Logger = getLogger('discord')

def to_log(msg: str, *args, **kwargs) -> None:
    print(msg, *args, **kwargs)
    logger.info("MARA: "+msg, *args, **kwargs)


def set_log() -> None:
    """Setter of the log at the ``discord.log`` file."""

    logger.setLevel(DEBUG)

    handler: FileHandler = FileHandler(filename=joinpath('Mara_Python','temp','discord.log'), encoding='utf-8', mode='w')
    handler.setFormatter(Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)