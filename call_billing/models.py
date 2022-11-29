"""This file contains only abstract models."""

from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    def update_fields(self, **kwargs):
        self.__class__.objects.filter(id=self.id).update(**kwargs)

    class Meta:
        abstract = True


class CreatedAbstractModel(models.Model):
    created_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(class)s_created",
        editable=False,
    )

    created_at = models.DateTimeField(
        "Created_at",
        blank=True,
        null=True,
        auto_now_add=True,
        db_index=True,
        editable=False,
    )

    class Meta:
        abstract = True


class ModifiedAbstractModel(models.Model):
    modified_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(class)s_modified",
        editable=False,
    )

    modified_at = models.DateTimeField(
        "Modified_at",
        blank=True,
        null=True,
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True


class TrackingAbstractModel(
    BaseModel, CreatedAbstractModel, ModifiedAbstractModel
):

    class Meta:
        abstract = True