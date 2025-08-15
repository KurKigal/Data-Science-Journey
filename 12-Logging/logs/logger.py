import logging

logging.basicConfig(
    filename='app.log', ## Log messages will be saved to this file
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True ## force=True to override any previous configuration
    )