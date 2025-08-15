import logging

## Logging configuration

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")

def add(x, y):
    logger.debug(f"Adding {x} + {y}")
    return x + y

def subtract(x, y):
    logger.debug(f"Subtracting {x} - {y}")
    return x - y

def multiply(x, y):
    logger.debug(f"Multiplying {x} * {y}")
    return x * y

def divide(x, y):
    try:
        result = x / y
        logger.debug(f"Dividing {x} / {y}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    

add(10, 5)
subtract(10, 5)
multiply(10, 5)
divide(10, 5)

"""
Output:

2025-08-16 00:41:21 - ArithmeticApp - DEBUG - Adding 10 + 5
2025-08-16 00:41:21 - ArithmeticApp - DEBUG - Subtracting 10 - 5
2025-08-16 00:41:21 - ArithmeticApp - DEBUG - Multiplying 10 * 5
2025-08-16 00:41:21 - ArithmeticApp - DEBUG - Dividing 10 / 5
"""