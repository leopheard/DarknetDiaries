from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.megaphone.fm/darknetdiaries"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://images.megaphone.fm/qWgH8AlNBPLs2BBdDKqkDSJ_Y2Dh3wJYPUf4YIOnU7c/plain/s3://megaphone-prod/podcasts/29bed80a-d8cc-11e8-b199-aba552a0bbdf/image/uploads_2F1562951997273-pdd2keiryql-99f75240ab90a579e25720d85d3057b2_2Fdarknet-diaries-rss.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://images.megaphone.fm/qWgH8AlNBPLs2BBdDKqkDSJ_Y2Dh3wJYPUf4YIOnU7c/plain/s3://megaphone-prod/podcasts/29bed80a-d8cc-11e8-b199-aba552a0bbdf/image/uploads_2F1562951997273-pdd2keiryql-99f75240ab90a579e25720d85d3057b2_2Fdarknet-diaries-rss.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
