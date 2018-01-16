from django.utils.html import strip_tags

import datetime
import math
import re


def count_words(html_string):
    word_string = strip_tags(html_string)
    matching_words = re.findall(r'\w+', word_string)
    count = len(matching_words)
    # count = len(re.findall(r'\w+', word_string))
    return count


def get_read_time(html_string):
    count = count_words(html_string)
    read_time_min = math.ceil(count / 200.0)
    return int(read_time_min)





# def get_read_time(html_string):
#     count = count_words(html_string)
#     read_time_min = math.ceil(count / 200.0)
#     read_time = str(datetime.timedelta(minutes=read_time_min))
#     return read_time


# def get_read_time(html_string):
#     count = count_words(html_string)
#     read_time_min = (count / 200.0)
#     read_time_sec = read_time_min * 60
#     read_time = str(datetime.timedelta(seconds=read_time_sec))
#     return read_time
