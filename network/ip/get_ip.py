
import logging
import os


# 로그 설정  
def setLogging(name=None):
    logger = logging.getLogger(name)   
    logger.setLevel(logging.INFO)   # 로그 level 설정
    formatter = logging.Formatter('[%(asctime)s] %(message)s')  # 로그 출력 형태 구성
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)     # 로그 출력 형태 설정
    logger.addHandler(stream_handler)

    return logger

LOGGER = setLogging('get_ip')


def get_ip(type='Wi-Fi'):
    """ get ip function
    
    Args:
        type (str): 읽어올 ip 타입(어댑터) ex> 이더넷, wifi etc... 
                     ㄴ Defaults to 'Wi-Fi'.

    Returns:
        str: 원하는 어댑터의 ip주소
    """
    # cmd에서 ipconfig 수행한 후에 결과값 반환
    ipconfig = os.popen('ipconfig').read()

    # ipconfig에서 Wi-Fi 가 들어간 부분 떼오기
    ip_index = ipconfig.find(type)
    sub_ipconfig = ipconfig[ip_index:]
    ip = sub_ipconfig.split('\n')[:7]

    return ip


def checkDirPath(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            LOGGER.info('Directory created!')
    except OSError as e:
        LOGGER.info('OS Error raised!')
        LOGGER.info(e)


def save_file(file_path, data):
    with open(file_path, 'wb') as f:
        f.write(data)


def save_ip_in_nas(file_path):
    """
        피원격 pc ip NAS에 저장
    """
    
    # get ip
    wanna_ip = get_ip()
    
    # 나스 접속
    
    # 파일경로 있는지 확인, 없으면 생성
    checkDirPath(file_path)
    
    # ip 데이터를 원하는 경로에 파일로 저장
    save_file(file_path, wanna_ip)