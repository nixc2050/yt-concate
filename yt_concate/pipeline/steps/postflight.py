from .step import Step

from yt_concate.settings import logger

log = logger
class Postflight(Step):
    def process(self, data, inputs, utils):
        log.info('in Postflight')

