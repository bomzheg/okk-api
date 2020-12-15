from sqlalchemy import UniqueConstraint

from .db import db


class Batch(db.Model):
    """
    Модель представляющая серию газообразного медицинского кислорода
    """
    id = db.Column(db.Integer, primary_key=True, comment="Первичный ключ")
    seria = db.Column(name="Серия", type_=db.String(10), nullable=False,
                      comment="Серия КЖМ из которого произведена данная серия КГМ")
    partia = db.Column(name="Партия", type_=db.Date, nullable=False, comment="Дата производства серии")
    suffix = db.Column(name="Суфикс", type_=db.String(5), comment="Суффикс отличается у нескольких серий в течении дня")
    show = db.Column(name="Показать", type_=db.Boolean, default=True)
    passport_path = db.Column(name="passport_path", type_=db.String(256), nullable=True, comment="Путь до PDF паспорта")
    approve_path = db.Column(name="approve_path", type_=db.String(256), nullable=True, comment="Путь до PDF разрешения")

    __tablename__ = "Партии"
    __table_args__ = (
        UniqueConstraint('Партия', 'Суфикс', name='_partia_suffix_uc'),
    )

    def __str__(self):
        result = f"batch id{self.id}, серия {self.butch_number} "
        result += f"произведена из {self.seria} "
        if self.passport_path:
            result += f"путь до паспорта: {self.passport_path} "
        if self.approve_path:
            result += f"путь до разрешения: {self.approve_path} "
        return result

    @property
    def butch_number(self):
        return self.partia.strftime("%d%m%y") + self.suffix

    def to_dict(self):
        return dict(
            id=self.id,
            seria=self.seria,
            partia=self.partia.isoformat(),
            suffix=self.suffix,
            passport=bool(self.passport_path),
            approve=bool(self.approve_path)
        )

    @classmethod
    def to_object(cls, data: dict):
        return cls(**data)
