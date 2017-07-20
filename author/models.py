from django.db import models
from django.contrib.auth.models import User


class BlogUser(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    blog_id = models.IntegerField(default=0)
    token = models.CharField(max_length=20, blank=True, null=True, default=None)




class Blog(models.Model):
    owner = models.ForeignKey(BlogUser, blank=True, null=True)
    posts_words = models.CharField(max_length=20, blank=True, null=True, default=None)









class WordsString:

    words_string=''
    words_dict={}

    # def __init__(self,words_string):
    #     self.words_string=words_string
    #     self.words_dict=self.make_dict(words_string)

    def make_dict(self,ws): # make dictionary out of ws
        dict={}
        # import ast
        # ast.literal_eval("{'x':1, 'y':2}")
        # = > {'y': 2, 'x': 1}
        #word1-3,word2-4,word3-1,word4-2
        #Stachoverflow!
        # s = 'word1-3,word2-4,word3-1,word4-2'
        # d = dict(item.split('-') for item in s.split(','))
        # print(d)  # >> {'word4': '2', 'word1': '3', 'word3': '1', 'word2': '4'}
        return dict

    def dict_to_ws(self,dict): # mske ws out of dictionary
        ws=''
        for key in dict:
            ws=str(key)+'-'+str(dict[key])+','
        return ws



################## SET POSTS_WORDS
    def count_word(self,word,ws): # returns the number of a given word a ws
        dict=self.make_dict(self, ws)
        return dict.get(word,0)

    def count_word2(self,word): # returns the number of a given word a ws
        return self.words_dict.get(word,0)

    def count_text_to_dict(self,txt): # count a given text words number as a dict
        dict={}
        for word in txt.split():
            if dict.get(word,0) is 0:
                dict[word] = 1
            else:
                n=int(dict[word])+1
                dict[word] = n
        return dict

    def updade_by_text(self,txt,ws): # add a text words number to a given ws returns new_ws
        new_dict=self.count_text_to_dict(txt)
        dict=self.make_dict(ws)
        comb_dict=dict
        for key in new_dict:
            if comb_dict.get(key, 0) is 0:
                comb_dict[key] = new_dict[key]
            else:
                n = int(new_dict[key]) + int(comb_dict[key])
                dict[key] = n
        new_ws= self.dict_to_ws(comb_dict)
        return new_ws


    def updade_by_text2(self,txt): # add a text words number to a given ws returns new_ws
        new_dict=self.count_text_to_dict(txt)
        dict=self.words_dict
        comb_dict=dict
        for key in new_dict:
            if comb_dict.get(key, 0) is 0:
                comb_dict[key] = new_dict[key]
            else:
                n = int(new_dict[key]) + int(comb_dict[key])
                dict[key] = n
        new_ws= self.dict_to_ws(comb_dict)
        return new_ws


################## SEARCH POSTS_WORDS TODO

    def search_blogs(self,searched_words): # search given words in all blogs, rate them and return top ten
        blogs = []
        sp_words = searched_words.split()
        return blogs



