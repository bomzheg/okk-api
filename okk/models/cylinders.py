from .db import db


class Cylinder(db.Model):
    """
    Модель представляющая упаковку для кислорода газообразного медицинского КГМ.
    """
    id = db.Column(db.Integer, name="ID", primary_key=True, comment="Первичный ключ")
    cylinder_volume = db.Column(db.Numeric(4, 2), name="Объём баллона, л", nullable=False, comment="Объём баллона, л")
    pressure = db.Column(db.Integer, name="Давление, ат", nullable=False, comment="Давление, ат")
    gas_volume = db.Column(db.Numeric(7, 2), name="Объём газа, м3", nullable=False, comment="Объём газа, м3")
    temperature = db.Column(db.Integer, name="Температура, °С", nullable=False, comment="Температура, °С")
    count_in_pack = db.Column(db.Integer, name="Колличество в связке", nullable=False, comment="Колличество в связке")
    single_cylinder_gas_volume = db.Column(db.Numeric(5, 2), name="Объём газа в одном баллоне, м3", nullable=False,
                                           comment="Объём газа в одном баллоне, м3")

    __tablename__ = "СоотношениеОбъёмов"

    def __str__(self):
        result = f"{self.count_name} id{self.id}, {self.cylinder_formula}, "
        result += f"объём газа: {self.gas_volume} м3 при температуре {self.temperature} °С, "
        result += f"давление газа: {self.pressure} ат."
        return result

    @property
    def count_name(self):
        return "баллон" if self.is_monoblock else "моноблок"

    @property
    def cylinder_formula(self):
        if self.is_monoblock:
            return f"{self.count_in_pack} × {self.single_cylinder_gas_volume} л"
        else:
            return f"{self.cylinder_volume} л"

    @property
    def is_monoblock(self) -> bool:
        return self.count_in_pack == 1
