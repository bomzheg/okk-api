from pathlib import Path

from okk.models import Batch


def add_files_for_batchs(session, batch_id: int, passport_path: Path, approve_path: Path):
    b = Batch.query.filter_by(id=batch_id).first()
    b.passport_path = str(passport_path)
    b.approve_path = str(approve_path)
    session.add(b)
    session.commit()
