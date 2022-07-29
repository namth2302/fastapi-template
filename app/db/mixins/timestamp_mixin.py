#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin:

    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=func.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime,
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )


class TimestampUrBoxMixin:

    @declared_attr
    def created(cls):
        return Column(DateTime, default=func.now(), nullable=False)

    @declared_attr
    def updated(cls):
        return Column(
            DateTime,
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )
