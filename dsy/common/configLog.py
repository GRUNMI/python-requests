import logging
import sys
import os
import time

# current_path = sys.path[0]
current_path = os.getcwd()
# print(current_path)
current_file_abspath = str(os.path.realpath(__file__))
# print(os.path.realpath(__file__))
log_path = os.path.join(current_file_abspath.replace(current_file_abspath.split('dsyWebAPI')[-1], '\\dsy\\logs'))
# print(log_path)
if not os.path.exists(log_path):
    os.mkdir(log_path)


class Log:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s----  %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logFileName = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        fh = logging.FileHandler(self.logFileName, mode='a', encoding='utf-8')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        # self.logger.removeHandler(handler)

    def get_logger(self):
        return self.logger


if __name__ == '__main__':
    mylogger = Log().get_logger()
    mylogger.debug("test debug")
    mylogger.info("test info")
    mylogger.error('haha')
    mylogger.error('hahha')