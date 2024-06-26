import requests
import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from operator import itemgetter
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
if r.status_code == 200:
    subm_ids = r.json()
else:
    print("Failed: get url.")


subm_dicts = []
names, comments = [], []
for subm_id in subm_ids[:30]:
    ri = requests.get('https://hacker-news.firebaseio.com/v0/item/' + str(subm_id) + '.json')
    if ri.status_code != 200:
        print("Failed: " + str(subm_id) + " request.")
        continue
    print("Get: " + str(subm_id))
    ri_read = ri.json()
    subm_dict = {
        'url':ri_read['url'],
        'title':ri_read['title'],
        'score':ri_read.get('score',0),
        'comments':ri_read.get('descendants',0),}
    subm_dicts.append(subm_dict)
    names.append(ri_read['title'])
    comments.append(ri_read.get('descendants',0))
    
subm_dicts = sorted(subm_dicts,key=itemgetter('comments'),reverse=True)
comments = sorted(comments,reverse=True)

with open('hn_submissios.json','a') as f:
    for subm_dict in subm_dicts:
        f.write(json.dumps(subm_dict))

my_style = LS('#112299',base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 20
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 25
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most popular articles on Hacker-News'
chart.x_labels = names


chart.add('',comments)
chart.render_in_browser()