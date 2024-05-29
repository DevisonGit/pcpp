import logging

logger = logging.getLogger()
hello_logger = logging.getLogger('hello')
hello_world_logger = logging.getLogger('hello.word')
recommended_logger = logging.getLogger(__name__)
