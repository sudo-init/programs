import logging


logging.basicConfig(
    level=logging.DEBUG,
    # format="%(asctime)s [%(levelname)s] %(message)s",
    format = '[%(asctime)s] %(message)s',
    # handlers=[
    #     logging.FileHandler("debug.log"),
    #     logging.StreamHandler()
    # ]
)

# logging.INFO('hello world')
msg = 'hello world'
print(msg)
logging.info(msg)