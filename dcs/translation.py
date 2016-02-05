class String:
    def __init__(self, _id='', translation=None):
        self.translation = translation
        self.id = _id

    def __del__(self):
        self.translation.delete_string(self.id)

    def set(self, text, lang='DEFAULT'):
        self.translation.set_string(self.id, text, lang)
        return str(self)

    def str(self, lang='DEFAULT'):
        return self.translation.strings[lang][self.id]

    def __str__(self):
        return self.str('DEFAULT')

    def __repr__(self):
        return self.id + ":" + str(self)


class Translation:
    def __init__(self):
        self.strings = {}  # type: dict[str,dict[str,str]]
        self.max_dict_id = 0

    def set_string(self, _id, string, lang='DEFAULT'):
        if lang not in self.strings:
            self.strings[lang] = {}
        self.strings[lang][_id] = string
        return _id

    def create_string(self, s, lang='DEFAULT'):
        _id = 'DictKey_Translation_{dict_id}'.format(dict_id=self.max_dict_id)
        self.max_dict_id += 1
        self.set_string(_id, s, lang)
        return String(_id, self)

    def delete_string(self, _id):
        for lang in self.strings:
            del self.strings[lang][_id]

    def languages(self) -> [str]:
        return self.strings.keys()

    def dict(self, lang='DEFAULT'):
        if lang in self.strings:
            return {x: self.strings[lang][x] for x in self.strings[lang]}
        return {}

    def __str__(self):
        return str(self.strings)

    def __repr__(self):
        return repr(self.strings)
