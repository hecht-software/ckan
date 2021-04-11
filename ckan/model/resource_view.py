# encoding: utf-8

from typing import Collection, Dict, KeysView, List, Optional, Tuple

import sqlalchemy as sa

from ckan.model import meta
from ckan.model import types as _types
from ckan.model import domain_object
from ckan.types import Query

__all__ = ['ResourceView', 'resource_view_table']


resource_view_table = sa.Table(
    'resource_view', meta.metadata,
    sa.Column('id', sa.types.UnicodeText, primary_key=True,
              default=_types.make_uuid),
    sa.Column('resource_id', sa.types.UnicodeText,
              sa.ForeignKey('resource.id')),
    sa.Column('title', sa.types.UnicodeText, nullable=True),
    sa.Column('description', sa.types.UnicodeText, nullable=True),
    sa.Column('view_type', sa.types.UnicodeText, nullable=False),
    sa.Column('order', sa.types.Integer, nullable=False),
    sa.Column('config', _types.JsonDictType))


class ResourceView(domain_object.DomainObject):
    id: str
    resource_id: str
    title: Optional[str]
    description: Optional[str]
    view_type: str
    order: int
    config: Dict

    @classmethod
    def get(cls, reference: str) -> Optional["ResourceView"]:
        '''Returns a ResourceView object referenced by its id.'''
        if not reference:
            return None

        view = meta.Session.query(cls).get(reference)

        return view

    @classmethod
    def get_columns(cls) -> List[str]:
        return resource_view_table.columns.keys()

    @classmethod
    def get_count_not_in_view_types(cls, view_types: Collection[str]) -> List[Tuple[str, int]]:
        '''Returns the count of ResourceView not in the view types list'''
        view_type = cls.view_type  # type: ignore
        query: 'Query[Tuple[str, int]]' = meta.Session.query(view_type,
                                   sa.func.count(cls.id)) \
                    .group_by(view_type) \
                    .filter(sa.not_(view_type.in_(view_types)))

        return query.all()

    @classmethod
    def delete_not_in_view_types(cls, view_types: Collection[str]) -> int:
        '''Delete the Resource Views not in the received view types list'''
        query = meta.Session.query(cls) \
                    .filter(sa.not_(cls.view_type.in_(view_types)))  # type: ignore

        return query.delete(synchronize_session='fetch')

    @classmethod
    def delete_all(cls, view_types: Collection[str]=[]) -> int:
        '''Delete all Resource Views, or all of a particular type'''
        query = meta.Session.query(cls)

        if view_types:
            query = query.filter(cls.view_type.in_(view_types))  # type: ignore

        return query.delete(synchronize_session='fetch')


meta.mapper(ResourceView, resource_view_table)
