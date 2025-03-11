# preflight.py
from .step import Step
from yt_concate.settings import logger

log = logger

class Preflight(Step):
    def process(self, data, inputs, utils):
        log.info('in Preflight')
        utils.create_dirs()
