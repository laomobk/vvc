import time


VERSION_FILE = 'versions.ver'


class VimrcVersion:
    def __init__(self, name :str, content :str):
        self.name = name
        self.content = content
        self.time = time.time()

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self) -> str:
        return '< version \'%s\'  %s>' % (self.name, time.ctime(self.time))

    __repr__ = __str__


class VersionList(list):
    def __init__(self):
        super().__init__()

    def new_version(self, name :str, content :str):
        for b in self:
            if b.name == name:
                b.content = content
                return

        self.append(VimrcVersion(name, content))

    def get_version(self, name :str) -> VimrcVersion:
        for b in self:
            if b.name == name:
                return b
        return None

    def remove_version(self, name :str) -> bool:
        for b in self:
            if b.name == name:
                self.remove(b)
                return True
        return False
