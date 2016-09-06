# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2016-07-29 18:39:33
# @Last Modified by:   Administrator
# @Last Modified time: 2016-09-06 19:27:02
import requests
import md5
import json
from bs4 import BeautifulSoup


class HPlogin(object):
    """docstring for Hupu"""

    def __init__(self, un, pw):
        self.un = un
        self.pw = pw
        self.login_url = 'http://passport.hupu.com/pc/login?project=bbs&from=pc'
        self.post_url = 'http://passport.hupu.com/pc/login/member.action'
        self.verifyimg_url = 'http://passport.hupu.com/pc/verifyimg'
        self.session = requests.session()
        self.post_header = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'passport.hupu.com',
            'Origin': 'http://passport.hupu.com',
            'Referer': 'http://passport.hupu.com/pc/login?project=www&from=pc',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.8 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

    def get_verifycode(self):
        r = self.session.get(self.verifyimg_url, )
        with open('verifyimg.jpg', 'wb') as f:
            f.write(r.content)
        verifycode = raw_input('plz enter authcode: \n')
        return verifycode

    def login_hupu(self):
        m1 = md5.new()
        m1.update(self.pw)
        password = m1.hexdigest()
        verifycode = self.get_verifycode()
        postdata = {
            'username': self.un,
            'password': password,
            'verifyCode': verifycode
        }
        login_page = self.session.post(
            self.post_url, data=postdata, headers=self.post_header)
        hjson = login_page.json()
        if hjson['code'] == 1000:
            print '登陆成功'
            # return self.session
        else:
            print '登陆失败'
            # return


if __name__ == '__main__':
    username = 'xxxxx'
    password = 'xxxxxx'
    HP = HPlogin(username, password)
    HP.login_hupu()
