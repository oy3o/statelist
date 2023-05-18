from __future__ import annotations
import json

class StateList(list):
    def __init__(self, states:list|str = []) -> None:
        super().__init__(json.loads(states) if type(states) == str else [(state, {}) for state in states])

    def _get(self, key):
        return next(filter(lambda it:it[0] == key, self), None)

    def get(self, key):
        try:
            return self.__getitem__(key)
        except:
            return None

    def append(self, item, /, state = {}):
        super().append((item, state))

    def remove(self, target):
        super().remove(self._get(target))

    def update(self, target, /, patch: dict):
        self.get(target).update(patch)

    def dumps(self):
        return json.dumps(self, ensure_ascii=False)

    def  __getitem__(self, key):
        return self._get(key)[1]

    def __setitem__(self, key, value):
        target = self.get(key)
        if target == None:
            self.append(key, value)
        else:
            target.update(value)

    def __delitem__(self, key):
        self.remove(key)