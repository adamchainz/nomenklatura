from nomenklatura.model.data_types import DATA_TYPES
from nomenklatura.model.common import NamedMixIn, NKException


class Attribute(NamedMixIn):
    """ An attribute is a named property that a node in the graph
    may have assinged to it. """

    def __init__(self, name, data):
        self.name = name
        self.label = data.get('label')
        self.data_type = data.get('data_type')
        self.key = data.get('key') or name

    @property
    def converter(self):
        """ Instantiate a type converter for this attribute. """
        if self.data_type not in DATA_TYPES:
            raise NKException('Invalid data type: %s'
                              % self.data_type)
        return DATA_TYPES[self.data_type]

    def to_dict(self):
        return {
            'name': self.name,
            'label': self.label,
            'key': self.key,
            'data_type': self.data_type
        }

    def __repr__(self):
        return '<Attribute(%r,%r,%r)>' % (self.name, self.label,
                                          self.data_type)

    def __eq__(self, other):
        if hasattr(other, 'name'):
            return self.name == other.name
        return self.name == other

    def __unicode__(self):
        return self.label
