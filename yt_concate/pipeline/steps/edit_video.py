# edit_video.py
from .step import Step

from moviepy import VideoFileClip, concatenate_videoclips

class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data: # found 的物件->yt 的 video_filepath物件 -->OOP導向

            start, end = self.parse_caption_time(found.time)

            clip = (
                VideoFileClip(found.yt.video_filepath)
                .subclipped(start, end)
                .with_volume_scaled(1.0)
            )


            clips.append(clip)

            if len(clips) >= inputs['limit']:
                break

        # Overlay the text clip on the first video clip
        final_video = concatenate_videoclips(clips, method="compose")
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_video.write_videofile(output_filepath, audio_codec="aac")



    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        end = end.split()[0]
        return self.parse_time_str(start), self.parse_time_str(end)



    def parse_time_str(self, time_str):
        h, m, s, = time_str.split(':')
        s, ms = s.split('.')
        return int(h), int(m), int(s) + int(ms) / 1000