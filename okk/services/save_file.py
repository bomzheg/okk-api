import typing
from pathlib import Path

from werkzeug.datastructures import ImmutableMultiDict, FileStorage
from werkzeug.utils import secure_filename

from okk.services import exceptions
from okk.models import Batch


def get_file(files: dict, file_key: str) -> FileStorage:
    """
    get file from dict files. if don't have that file raise Exception FileNotFound or FileNotCorrect
    :param files:
    :param file_key:
    :return:
    """
    try:
        file: FileStorage = files[file_key]
    except KeyError:
        raise exceptions.FileNotFound

    if file:
        return file
    else:
        raise exceptions.FileNotCorrect


def get_new_filename(filename_body: str, old_filename: Path) -> str:
    return filename_body + old_filename.suffix


class FileCheckerSaver:
    def __init__(self, extensions: typing.Iterable, files_path: Path):
        self.extensions = extensions
        self.files_path = files_path
        self.files_path.mkdir(parents=True, exist_ok=True)

    def check_and_save_file(self, files: ImmutableMultiDict, file_key: str, batch: Batch) -> Path:
        file = get_file(files, file_key)
        filename = Path(file.filename)
        self.check_allowed_filename(filename)
        path = self.make_path(filename, file_key, batch)
        with path.open("wb") as f:
            file.save(f)
        return path

    def make_path(self, filename: Path, file_key: str, batch: Batch) -> Path:
        filename = secure_filename(get_new_filename(file_key, filename))
        path = self.get_batch_path(batch)
        path.mkdir(parents=True, exist_ok=True)
        return path / filename

    def get_batch_path(self, batch: Batch) -> Path:
        return self.files_path / str(batch.partia.year) / str(batch.id)

    def check_allowed_filename(self, filename: Path):
        if filename.suffix not in self.extensions:
            raise exceptions.NotAllowedFilename
