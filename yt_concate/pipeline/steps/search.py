#  search.py

from .step import Step
from yt_concate.model.found import Found
from yt_concate.settings import logger

log = logger
class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found (yt, caption, time)
                    found.append(f)
        log.info(len(found))
        return found