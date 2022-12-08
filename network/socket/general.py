
import logging


"""
로그 셋팅
"""

logging.basicConfig(
    level=logging.INFO,

    # 로그 출력 형태
    # format="%(asctime)s [%(levelname)s] %(message)s",
    format = '[%(asctime)s] %(message)s'

    # 로그 파일 저장
    # handlers=[
    #     logging.FileHandler("debug.log"),
    #     logging.StreamHandler()
    # ]
)

def set_logging():
    logger = logging.getLogger()   
    logger.setLevel(logging.INFO)   # 로그 level 설정
    formatter = logging.Formatter('[%(asctime)s] %(message)s')  # 로그 출력 형태 구성
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)     # 로그 출력 형태 설정
    logger.addHandler(stream_handler)
    
    return logger

LOGGER = set_logging()


