    # -*- coding: UTF-8 -*-
    from weibopy.auth import OAuthHandler
    from weibopy.api import API
    import urllib, urllib2, cookielib, hashlib,threading,BeautifulSoup,webbrowser,getpass
    import re, os, time, random，sys

    reload(sys)
    sys.setdefaultencoding('utf-8')

    print "Python for weibo.com sender\n"


    id=raw_input("input your weibo.com username:")
    passwd=getpass.getpass("input your weibo.com password:")

    def log(s):
            s = "\n" + str(s)
            f = open('log.txt', 'a+')
            f.write(s)
            f.close()
            sys.stdout.write(s)
            sys.stdout.flush()


    class WeiboCn:
            all = ('python weibo.com sender')
            url = 'http://www.weibo.com'
            header = {
                    'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            }
            def __init__(self, username, password, keyword = None, *args):
                    self.user = username
                    self.keyword = keyword
                    self.all = args or self.all
                    self.cj = cookielib.LWPCookieJar()
                    self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
                    urllib2.install_opener(self.opener)
                    self.tryLogin(username, password)

            def tryLogin(self, username, password):
                    bodies = dict(_=int(time.time()),callback='sinaSSOController.preloginCallBack',client='ssologin.js(v1.3.12)',entry='miniblog',user=id)
                    print "pre-login,get servertime&nonce arg(secret password)"
                    preloadurl = 'http://login.sina.com.cn/sso/prelogin.php?' + urllib.urlencode(bodies)
                    content = self._request(preloadurl)[1].read()
                    bodies = eval(re.findall('\{.*?\}',content)[0])
                    password = hashlib.sha1(hashlib.sha1(hashlib.sha1(password).hexdigest()).hexdigest() + str(bodies['servertime']) + bodies['nonce']).hexdigest()
                    print "Hash Password<%s>" % password
                    bodies.update(dict(client='ssologin.js(v1.3.12)',encoding='utf-8',entry='miniblog',gateway='1',password=password,pwencode='wsse',returntype='META',savestate='7',service='miniblog',ssosimplelogin='1',url='http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',username=username,useticket=1))
                    response = self._request('http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.3.12)', bodies)[1]
                    content = response.read()
                    moreurl = re.findall('replace\([\'|"](.*?)[\'|"]\)', content)
                    if len(moreurl) == 0: print "Login Failed!"
                    content = self._request(moreurl[0], dict(Referer='http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.3.12)',Host='weibo.com'))[1].read()
                    if username in content:
                            print "Login Successed"
                            self.afterLogin()
           
            def afterLogin(self):
                    content = self._request('http://weibo.com/')[1].read()
                    #self.uid = re.findall('\$uid.*?"(\d+)"', content)[0]
                    #self.uid=[1265020392]
           
                   
            def _request(self, url, bodies = {}, headers = {}):
                    request = urllib2.Request(url, urllib.urlencode(bodies), headers = headers)
                    return (request, self.opener.open(request))

            def _readMainPage(self):
                    return self._request(self.url)[1].read()

            def sinaapp(self,app_key,app_secret):
                    auth = OAuthHandler(app_key, app_secret)  ##认证
                    auth_url = auth.get_authorization_url()    ##返回授权页面链接，用浏览器打开
                    #webbrowser.open(auth_url)
                    content = self._request(auth_url)[1].read()        
                    soup=BeautifulSoup.BeautifulSoup(''.join(content))
                    #print content
                    pin=soup.span.string   #自动获取pin码
                    #print 'Please authorize: ' + auth_url  ##输入获得的Pin码
                    #verifier = raw_input('输入您在浏览器页面显示的PIN码: ').strip()
                    auth.get_access_token(pin)
                    api = API(auth)  #整合函数
                    connent=raw_input('What are you want to say?')
                    status = api.update_status(status=connent)#发布微博
                    print "Send Successed"
                    raw_input('Press enter to exit ......')

    login=WeiboCn(id,passwd)
    login.sinaapp('3837289606','14416dc6caadc1b14c4b0b09f58cc459')