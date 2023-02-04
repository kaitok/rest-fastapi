from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import TIMESTAMP as Timestamp


class TimestampMixin(object):
    created_at = Column(
        Timestamp,
        nullable=False,
        server_default=text("current_timestamp"),
        comment="created_at",
    )
    updated_at = Column(
        Timestamp,
        nullable=False,
        server_default=text("current_timestamp on update current_timestamp"),
        comment="updated_at",
    )
