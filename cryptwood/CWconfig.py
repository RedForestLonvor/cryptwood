import os
import configparser

class CWconfig:
    @staticmethod
    def exist():
        config = configparser.ConfigParser()
        if not config.read('config.ini'):
            print('Config file not found.')
            print('Creating config.ini...')
            config_file_path = 'config.ini'
            config['PATH'] = {'keyPath': 'HOME'}
            with open(config_file_path, 'w') as config_file:
                config.write(config_file)
            print('config.ini created in '+os.getcwd()+os.sep+config_file_path)
        else:
            return True
        return False

    @staticmethod
    def getCustomPath():
        if not CWconfig.exist():
            return None
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config.get('PATH', 'keyPath')

    @staticmethod
    def setPath(customPath):
        CWconfig.exist()
        if not os.path.exists(customPath):
            if os.path.isabs(customPath):
                print("path not exists,creating directory(s)")
                if not os.path.exists(customPath):
                    os.makedirs(customPath)
            else:
                raise Exception(r"illegal key path!(\ for windows /for linux)")
        elif os.path.isfile(customPath):
            raise Exception(r"expected directory path not file path")
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.set('PATH', 'keyPath', customPath)
        with open('config.ini', 'w') as config_file:
            config.write(config_file)