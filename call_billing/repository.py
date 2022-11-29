import abc
from typing import List

from django.contrib.auth.models import User


class BaseRepository:
    @property
    @abc.abstractmethod
    def model(self):
        pass

    @classmethod
    def _apply_query_optimization(cls, queryset, **kwargs):
        only_fields = kwargs.get('only_fields', [])
        defer_fields = kwargs.get('defer_fields', [])
        select_related_fields = kwargs.get('select_related_fields', [])
        prefetch_related_fields = kwargs.get('prefetch_related_fields', [])
        order_by_fields = kwargs.get('order_by_fields', [])
        if select_related_fields:
            queryset = queryset.select_related(*select_related_fields)
        if prefetch_related_fields:
            queryset = queryset.prefetch_related(*prefetch_related_fields)
        if only_fields:
            queryset = queryset.only(*only_fields)
        if defer_fields:
            queryset = queryset.defer(*defer_fields)
        if order_by_fields:
            queryset = queryset.order_by(*order_by_fields)
        return queryset

    @classmethod
    def get_or_create(cls, defaults=None, **kwargs):
        return cls.model.objects.get_or_create(defaults=defaults, **kwargs)

    @classmethod
    def update_or_create(cls, defaults=None, **kwargs):
        return cls.model.objects.update_or_create(defaults=defaults, **kwargs)

    @classmethod
    def get_all(cls, **kwargs):
        queryset = cls.model.objects.all()
        queryset = cls._apply_query_optimization(queryset, **kwargs)
        return queryset

    @classmethod
    def get_by_id(cls, object_id: int):
        return cls.model.objects.get(id=object_id)

    @classmethod
    def find_by_id(cls, object_id: int):
        return cls.model.objects.filter(id=object_id).first()

    @classmethod
    def create_object(cls, **data):
        return cls.model.objects.create(**data)

    @classmethod
    def get_first(cls, order_by='pk'):
        return cls.model.objects.order_by(order_by).last()

    @classmethod
    def get_last(cls, order_by='pk'):
        return cls.model.objects.order_by(order_by).last()

    @classmethod
    def count(cls, **condition):
        return cls.model.objects.filter(**condition).count()

    @classmethod
    def find_by_list_of_ids(cls, list_of_ids: List[int]):
        return cls.model.objects.filter(id__in=list_of_ids)


class UserRepository(BaseRepository):
    model = User

    @classmethod
    def get_by_username(cls, username: str):
        return cls.model.objects.filter(username=username).first()