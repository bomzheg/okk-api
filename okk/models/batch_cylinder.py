from .db import db


class BatchCylinder(db.Model):
    batch_id = db.Column(db.Integer, db.ForeignKey('batch.id'), name="ID партии")
    cylinder_id = db.Column(db.Integer, db.ForeignKey('cylinder.id'), name="ID баллона")
    count = db.Column(db.Integer, name="Количество")

    __tablename__ = "Баллоны в партиях"

    def __str__(self):
        result = f"ID партии {self.batch_id}, ID баллона {self.cylinder_id} "
        result += f"количество {self.count}"
        return result
