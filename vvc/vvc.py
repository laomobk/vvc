import pickle
import time

from .rcversion import VersionList, VERSION_FILE
from .path import relative


class VimrcVersionController:
    def __init__(self, vimrc_path :str):
        self.__vimrc_path = vimrc_path

    def __try_load_version_list(self) -> VersionList:
        try:
            return pickle.load(
                    open(relative(VERSION_FILE), 'rb'))
        except FileNotFoundError:
            return None

    def __update_version_list(self, version_list :VersionList):
        pickle.dump(version_list,
                open(relative(VERSION_FILE), 'wb'))

    def new_version(self, name :str) -> int:
        vlist = self.__try_load_version_list()
        if vlist is None:
            vlist = VersionList()

        vlist.new_version(name, open(self.__vimrc_path).read())

        self.__update_version_list(vlist)

        print('[A] new version \'%s\'' % name)

        return 0

    def change_version(self, name :str) -> int:
        vlist = self.__try_load_version_list()

        if vlist is None:
            print('[E] version \'%s\' not found! (version file not found)' % name)
            return 1

        target = vlist.get_version(name)

        if target is None:
            print('[E] version \'%s\' not found!' % name)
            return 1

        with open(self.__vimrc_path, 'w') as f:
            f.write(target.content)

        print('[A] successfully change vimrc version to \'%s\'' % name)

        return 0

    def remove_version(self, name :str):
        vlist = self.__try_load_version_list()

        if vlist is None:
            print('[E] version file not found!')
            return 1

        b = vlist.remove_version(name)

        if b :
            print('[A] version \'%s\' deleted' % name)
            self.__update_version_list(vlist)

        else:
            print('[E] version \'%s\' not found' % name)
            return 1

        return 0

    def list_version(self):
        vlist = self.__try_load_version_list()

        if vlist is None:
            print('[e] version file not found!')
            return 1

        print('list all version:')

        for b in vlist:
            print('\t%s' % b)

    def now_vimrc_version(self):
        vlist = self.__try_load_version_list()

        if vlist is None:
            print('[e] version file not found!')
            return 1
        
        with open(self.__vimrc_path) as f:
            now_vimrc_content = f.read()

        not_matched = True

        for b in vlist:
            if b.content == now_vimrc_content:
                not_matched = False

                print('now vimrc version match:')
                print('\t%s' % b)

        if not_matched:
            print('[E] no version match.')
            return 1

        return 0
