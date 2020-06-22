import configparser
import os
from common_fuc.logger import Logger


class Read_conf():

    path = os.path.dirname(os.path.abspath('.'))
    confpath = os.path.join(path, 'config\config.ini')
    cf=configparser.ConfigParser()
    cf.read(confpath)
    def get_http(self,name):
        http_value=self.cf.get('Http',name)
        return http_value

    def get_db(self,name):
        db_value=self.cf.get('Database',name)
        return db_value

    def get_browser(self,name):
        browser_value=self.cf.get('browserType',name)
        return browser_value