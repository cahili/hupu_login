# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-07-30 11:37:55
# @Last Modified by:   Administrator
# @Last Modified time: 2016-09-06 19:27:19
import requests
from loginhupu import HPlogin
from urllib import urlencode
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')


class ReplyHP(HPlogin):
    """docstring for ReplyHP"""

    def __init__(self, un, pw, get_url, post_content):
        HPlogin.__init__(self, un, pw)
        self.login_hupu()
        self.get_url = get_url
        self.post_content = post_content
        self.post_url_ = 'http://bbs.hupu.com/post.php?'

    def reply_post(self):
        request_header = {'Host': 'bbs.hupu.com',
                          'Origin': 'http://bbs.hupu.com',
                          'Referer': self.get_url,
                          'Upgrade-Insecure-Requests': '1',
                          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.8 Safari/537.36'
                          }

        postdata = {
            'atc_content': self.post_content,
            'usevote': '0',
            'douid': '1',
            'votetype': 'bbs',
            'votetitle': '',
            'votename[]': '',
            'votename[]': '',
            'votename[]': '',
            'editnum': '3',
            'nowitnum': '3',
            'voteclass': '',
            'postfast': '2',
            'atc_title': 'Re:哈梅斯·罗德里格斯[James Rodríguez]  右 脚 得 分 。',
            'atc_usesign': '1',
            'atc_convert': '1',
            'atc_autourl': '1',
            'step': '2',
            'action': 'reply',
            'fid': '2543',
            'tid': '10508449',
            'subject': '哈梅斯·罗德里格斯[James Rodríguez]  右 脚 得 分 。',
            'editor': '0',
            'atc_attachment': 'none',
            'replayofpage': '',
            'replaymeta': '1'
        }
        page = self.session.post(
            self.post_url_, data=postdata, headers=request_header)
        page.encoding = 'gbk'

if __name__ == '__main__':
    username = 'xxxx'
    password = 'xxxxx'
    data = '&#x52FE;&#x7F57;&#x5A01;&#x6B66;&#x9738;&#x6C14;&#x554A;'
    post_content = data
    get_url = 'http://bbs.hupu.com/10508449.html'
    g = ReplyHP(username, password, get_url, post_content)
    g.reply_post()
