import typing
from pathlib import Path

from flask import Flask, request, jsonify

from okk.models import Batch
from okk.routes.errors import ok
from okk.services.batchs import get_batch
from okk.services.save_file import FileCheckerSaver
from okk.services.add_files_for_batch import add_files_for_batchs
from okk.models.db import db


class FileLoader:
    def __init__(self, file_checker_saver: FileCheckerSaver):
        self.file_checker_saver = file_checker_saver

    def upload_file(self, batch_id: int):
        paths = {}
        batch = get_batch(batch_id)
        for file in ('passport', 'approve'):
            path = self.file_checker_saver.check_and_save_file(files=request.files, file_key=file, batch=batch)
            paths[file] = path

        add_files_for_batchs(db.session, batch_id, paths['passport'], paths['approve'])

        result_dict = ok
        result_dict['data'] = batch.to_dict()
        response = jsonify(result_dict)

        response.status_code = 200
        return response


def setup_upload_file(app: Flask, extensions: typing.Iterable, files_path: Path):
    file_loader = FileLoader(FileCheckerSaver(extensions, files_path))
    app.add_url_rule(
        "/batchs/<int:batch_id>/files",
        "AddFilesToBatch",
        file_loader.upload_file,
        methods=['PUT']
    )
