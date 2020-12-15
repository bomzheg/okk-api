import typing
from datetime import date

from okk.models import Batch


def get_batch(batch_id: int) -> Batch:
    batch: Batch = Batch.query.get_or_404(batch_id)
    return batch


def patch_batch_service(batch_id: int, data: dict, session) -> typing.Tuple[Batch, bool]:
    batch = get_batch(batch_id)
    patched = False
    if 'seria' in data:
        batch.seria = data['seria']
        patched = True
    if 'partia' in data:
        batch.partia = data['partia']
        patched = True
    if 'suffix' in data:
        batch.suffix = data['suffix']
        patched = True
    if patched:
        session.add(batch)
        session.commit()
    return batch, patched


def prepare_batch_args(data: dict) -> dict:
    return dict(
        seria=data["seria"],
        partia=date.fromisoformat(data["partia"]),
        suffix=data.get("suffix", ""),
    )


def process_batch_creation(seria: str, partia: date, suffix: str, session) -> Batch:
    batch = Batch(seria=seria, partia=partia, suffix=suffix)
    session.add(batch)
    session.commit()
    return batch
