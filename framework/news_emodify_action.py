
from framework.news_add_action import *



def edit_btn(*loc):
    newmethod.click(*loc)


def edit_name(value,*loc):
    newmethod.send_keys(value,*loc)


def edit_date(value,*loc):
    newmethod.send_keys(value,*loc)


def edit_sumarry(value,*loc):
    newmethod.send_keys(value, *loc)


def edit_url(value,*loc):
    newmethod.send_keys(value, *loc)



def edit_context(loc,value):
    newmethod.switch_frame(loc,value)

