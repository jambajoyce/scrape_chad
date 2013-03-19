
from HTMLParser import HTMLParser
import os

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(file_name):
    f = open(file_name)
    s = MLStripper()
    s.feed(f.read())
    return s.get_data()

out_dir = "/Users/joyceliu/Dropbox/info290corpus/nohtml/"
in_dir = "/Users/joyceliu/Dropbox/info290corpus/"

for file_name in os.listdir(in_dir):
    if ".txt" in file_name:
        print file_name
        raw_text = strip_tags(in_dir+file_name)
        lines = raw_text.split("\n")
        lines_without_header = lines[777:]
        text_without_header = "\n".join(lines_without_header)
        out_file = open(out_dir + file_name, 'w')
        out_file.write(text_without_header)
        out_file.close()

