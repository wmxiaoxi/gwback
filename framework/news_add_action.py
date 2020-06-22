from framework.login_action import *
from common_fuc.pageobj.news_obj import *

def news_addbtn(*loc):
    #login(username[0], password[0])
    newmethod.click(*loc)

def news_name(value,*loc):
    newmethod.send_keys(value,*loc)

def news_date(value,*loc):
    newmethod.send_keys(value,*loc)

def news_click_add(*loc):
    newmethod.click(*loc)


def news_sumarry(value,*loc):
    newmethod.send_keys(value, *loc)

def news_url(value,*loc):
    newmethod.send_keys(value, *loc)


def news_context_loc(loc):
    newmethod.switch_frame(loc)

def news_context(value,*loc):
    newmethod.send_keys_nclear(value, *loc)


def front_save(*loc):
    newmethod.click(*loc)

def look(*loc):
    newmethod.click(*loc)

def save(*loc):
    newmethod.click(*loc)

def sleep(second):
    newmethod.sleep(second)

def context_frame(*loc):
    return newmethod.find_element(*loc)




