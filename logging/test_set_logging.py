# 로그의 형태를 정하여 출력하기

import logging
from datetime import datetime

# def main():
#     logger = logging.getLogger()
#     logger.setLevel(logging.INFO)

#     formatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)s} %(levelname)s - %(message)s')

#     try:
#         stream_handler = logging.StreamHandler()
#         stream_handler.setFormatter(formatter)
#         logger.addHandler(stream_handler)

#         file_path = './log/'
#         file_name = datetime.now().strftime('%Y%m%d_%H%M%S') + '_log_test.log'
#         file_handler = logging.FileHandler(file_path + file_name)
#         file_handler.setFormatter(formatter)
#         logger.addHandler(file_handler)
        
#     except Exception as e:
#         logging.exception(e)
        
#     logger.info('hello')


# main()
# print(datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))
# print(datetime.now().strftime('%Y-%m-%d_%H:%M:%S'))

class Logger:
    
    def __init__(self, level=logging.INFO, formatter=None):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)    # 로그 level 설정 (INFO, ERROR 등등)
        
        if formatter == None:
            self.formatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)s} %(levelname)s - %(message)s')
        else:
            self.formatter = formatter
            
        self.stream_handler = logging.StreamHandler()
        self.stream_handler.setFormatter(self.formatter)     # 로그 출력 형태 설정
        self.logger.addHandler(self.stream_handler)
        
        file_path = ''
        
    
    def setFormatter(self, formatter):
        self.stream_handler.setFormatter(formatter)
        
    def info(self, msg):
        self.logger.info(msg)


def test():
    formatter1 = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)s} %(levelname)s - %(message)s')
    formatter2 = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
    
    logger = Logger(formatter=formatter2)
    
    logger.info('hello')
    
    logger.setFormatter(formatter=formatter1)
    
    logger.info('hello2')
    

test()