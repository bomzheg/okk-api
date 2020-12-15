from okk.models import Cylinder, Batch
from okk.services.rzn_sender import RZNGaseous


def send_batch(batch: Batch, rzn_sender: RZNGaseous):
    cylinder = Cylinder(
        cylinder_volume=40,
        pressure=150,
        gas_volume=6.36,
        temperature=20,
        count_in_pack=1,
        single_cylinder_gas_volume=6.36
    )
    send_batch_part(batch, rzn_sender, cylinder, 15)


def send_batch_part(batch: Batch, rzn_sender: RZNGaseous, cylinder: Cylinder, count: int):
    rzn_sender.save_new_batch(
        batch.butch_number,
        count,
        cylinder,
        batch.partia,
        batch.passport_path,
        batch.approve_path
    )
