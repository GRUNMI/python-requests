import configparser
import os
from dsyWebAPI.dsy.common.configLog import Log
log = Log().get_logger()
current_path = os.getcwd()
# configPathFile = os.path.join(current_path, 'cfg.ini')
configPathFile = os.path.join(current_path, 'cfg.conf')

config = configparser.ConfigParser()
config.read(configPathFile, encoding='utf-8')
name = config.get("user", "name")
log.info('name=%s' % name)
# print(name)
pwd = config.get("user", "pwd")
log.info('pwd=%s' % pwd)
# print(pwd)
