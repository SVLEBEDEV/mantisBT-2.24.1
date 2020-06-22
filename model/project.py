from sys import maxsize


class Project:

    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return 'id: %s __ name: %s __ description: %s' % (self.id, self.name, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.description == other.description

    def sorted_by_name(self):
        return self.name

    def sorted_by_id(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize