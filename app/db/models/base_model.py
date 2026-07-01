from app.db.base import Base
from app.db.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin


class BaseModel(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin):
    __abstract__ = True