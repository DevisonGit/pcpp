import logging
import random

MESSAGE = 'TEMPERATURE_IN_CELSIUS UNIT'
FORMAT = '%(name)s - %(message)s => %(levelname)s - %(temperature)s c'

logging.basicConfig(level=logging.DEBUG, filename='battery_temperature.log', filemode='w', format=FORMAT)
logger = logging.getLogger('LEVEL_NAME')


def simulate_temperature():
    temperature = random.randint(20, 40)
    return temperature


def log_temperature():
    for _ in range(60):
        temperature = simulate_temperature()
        d = {'temperature': temperature}
        if temperature < 30:
            logger.debug(MESSAGE, extra=d)
        elif 30 <= temperature <= 35:
            logger.warning(MESSAGE, extra=d)
        elif temperature > 35:
            logger.critical(MESSAGE, extra=d)


log_temperature()
