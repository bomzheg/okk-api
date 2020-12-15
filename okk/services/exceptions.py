"""
Исключения используемые в проекте
"""


class OKKAPIError(Exception):
    pass


class FileError(OKKAPIError):
    pass


class FileNotFound(FileError):
    pass


class FileNotCorrect(FileError):
    pass


class NotAllowedFilename(FileNotCorrect):
    pass
