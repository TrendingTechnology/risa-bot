import json
import re
from hentai import Hentai, Utils, Format
from risa_settings import *


hentai_utils = Utils()

class RisaUtils:
    def __init__(self):
        self.homepage = hentai_utils.get_homepage()
        self.popular = self.homepage.popular_now
        self.newest = self.homepage.new_uploads
        self.search_data = dict()

    def clean_strip(self, string):
        res = string.strip().replace('#', '')
        return res

    def get_source_by_id(self, id):
        id = self.clean_strip(id)
        try:
            res = Hentai(id)
            return res

        except Exception:
            return False

    def capitalize_and_join(self, str_list):
        capitalized_list = list()
        for string in str_list:
            string = string.capitalize()
            capitalized_list.append(string)
        res = ', '.join(capitalized_list)
        
        return res

    def convert_upload_date(self, datetime_obj):
        res = datetime_obj.strftime("%B %d, %Y")

        return res

    def extract_urls(self, obj_list):
        res = list()
        for obj in obj_list:
            res.append(obj.url)

        return res

    
    def extract_names(self, obj_list):
        res = list()
        for obj in obj_list:
            res.append(obj.name)

        return res

    def extract_titles(self, obj_list):
        res = list()
        for obj in obj_list:
            res.append(obj.title(Format.Pretty))

        return res

    def extract_url_from_descrip(self, string):
        res = re.findall(r"g/([0-9]+)", string)[0]
        return res

    def extract_curr_page_from_footer(self, string):
        res = re.findall(r"([0-9]+)/[0-9]+", string)[0]
        return res

    def remove_banned_tags(self, obj_list):
        safe_list = list()
        for obj in obj_list:
            res = self.check_for_banned_tags(obj)
            if not res:
                safe_list.append(obj)

        return safe_list
    
    def check_for_banned_tags(self, obj):
        tags = self.extract_names(obj.tag)
        for banned_tag in BANNED_TAGS:
            if banned_tag in tags:
                return True
        else:
            return False

    
    def get_safe_source(self):
        while True:
            id = hentai_utils.get_random_id()
            book = Hentai(id)
            if not self.check_for_banned_tags(book):
                return book

    def save_search_data(self, query, data):
        self.search_data[query] = data
    
    def retrieve_search_data(self, query_string):
        print(query_string)
        query = re.findall(r'`(.*?)`', query_string)[0]
        for key, res in self.search_data.items():
            if key == query:
                return res

    def normalize_page_index(self, index, max_page):
        if index >= max_page:
            return  max_page
        elif index <= 1:
            return 1
        else:
            return index
    
    def inject_to_query(self, query, queries):
        queries = ' '.join(queries)
        res = query + queries
        return res
            


