import  requests
import random
class test ( object ) :
    def __init__ ( self , url , data ) :
        #登陆
        self.url = url
        LoginUrl = '/User/checkLogin'
        self.PostRequests ( url = LoginUrl ,data =data )
        #获取cookie 、 header
        self.cookie = { 'PHPSESSID' : self.r.cookies [ 'PHPSESSID' ] }
        self.header = self.r.request.headers

    #get 请求
    def GetRequests ( self , url , header = '' , cookie  = '' ) :
        url = self.url + url
        self.Get_r = requests.get ( url = url , headers = header , cookies = cookie )
        return self.Get_r
    # post 请求
    def PostRequests ( self , url , header = '' , cookie = '' , data = '' ) :
        url = self.url + url
        self.r = requests.post ( url = url , headers = header , cookies = cookie , data = data )
        #print ( self.r.status_code , self.r.reason , self.r.json () )
        return self.r
    # 随机生成一个浮点数
    def Random(selfa , a ,b ):
        num = random.randint( a , b )
        return num
    def SysUpload ( self ,  aid , time=1 ) :
        # 查找订单接口
        searchAccountUrl = '/Remote/searchAccount'
        searchAccountData = {'aidKey': aid}
        v = self.PostRequests(url=searchAccountUrl, data=searchAccountData, header=self.header, cookie=self.cookie)
        print('*' * 50)
        p = v.json()['msg'][0]
        pid = p['productIdArr'][0]['AI_Pid']
        print(pid)
        # 摄影师上传提交的参数
        SubmitData = {'name': p['A_Name'], 'phone': p['A_Phone'],
                      'note': p['note'], 'areye': 1, 'arface': 1,
                      'ardot': 1, 'isToday': 1, 'ptype': 1, 'haimatiAid': aid,
                      'productArr[]': pid,
                      'photoData[0][path]': 'a47a41e745b4df402f6033061911d5d6.jpg',
                      'photoData[0][count]': 1, 'photoData[0][productId]': pid, 'photoData[0][group]': '',
                      'photoData[1][path]': 'e69c2b30ae2282c8a479fe1986be662e.jpg',
                      'photoData[1][count]': 2, 'photoData[1][productId]': pid , 'photoData[1][group]': '',
                      'photoData[2][path]': '901c7d40870697c82873c2fc26a669be.jpg',
                      'photoData[2][count]': 4, 'photoData[2][productId]': pid, 'photoData[2][group]': '',
                      'photoData[3][path]': '59ede256cbb1caf9f83fd4a2a9dad48b.jpg',
                      'photoData[3][count]': 5, 'photoData[3][productId]': pid, 'photoData[3][group]': '',

                      }
        for i in range ( time ) :
            # 摄影师上传提交接口地址
            PsersubmitAccount = '/Pser/submitAccount'
            #self.test()
            #sys上传调 post请求
            self.PostRequests ( header = self.header , url = PsersubmitAccount , data = SubmitData , cookie = self.cookie )
if __name__ == '__main__':
    c = test()
Url = 'http://qyfh.ops.hzmantu.com'
# sys登陆参数

'''
aid1 = 2019010269750081 #证件照---1001
aid2 = 2019010269657142 #签证照---1001
aid3 = 2019010253822579 #证件---1067
aid4 = 2019010243380113 #签证照---1067
aid = 2019010269657142#化妆师多人
aid = 'K2018010271015510'#kids
aid = 2019010327554860 #化妆老人
aid = 2019010381234728 #化妆师新人
技术专家A：
            化妆区域督导A：
                        杭州和达城店---1001
            化妆区域督导B：
                        杭州湖滨银泰in77店---1002
                        义乌之心店---1003
化妆技术专家B:
            化妆区域督导C:
                        义乌之心店---1003
                        杭州城西银泰店---1004
'''

# hz1 = 2019010474957110 #杭州城西银泰店
# hz2 = 2019010494378920 #义乌之心店
# hz3 = 2019010477214195 #杭州湖滨银泰in77店
# hz4 = 2019010327554860 #杭州和达城店
def hz1():
    c = test(url = Url , data = {'user':'ytsys','pass':'123'})
    c.SysUpload(   aid = 2019010474957110 , time = 5 )
def hz2():
    c = test(url = Url , data = {'user':'ywsys','pass':123})
    c.SysUpload(   aid = 2019010494378920 , time = 5 )
def hz3():
    c = test(url = Url , data = {'user':'syshb','pass':123})
    c.SysUpload(   aid = 2019010477214195 , time = 5 )
def hz4():
    c = test(url = Url , data = {'user':'sys','pass':123})
    c.SysUpload(   aid = 2019010327554860 , time = 2 )
# hz1()
# hz2()
hz3()
#hz4()

#
# 'K2019010665341021'#拜年照
# 'K2019010631024948'#新年亲子照
# 'K2019010625649957'#新年迷你照
# 'K2019010669755498'#新年纯真照
#aid = 2019010234714385
#aid = 'K2019010275355410'#sysc3
#aid = 2018122572584418#(金标---1)
#aid = 2019010282934570 #syse结婚
#aid = 2019010253822579 #syse证件---1005
# aid = 2019010221457140 #sysa1结婚dengji---1067
#aid = 2019010234714385 #sysa1证件照---1067
#aid = 2019010243380113 #签证照---1067
#aid = 2019010253822579 #证件---1067
#aid = 2019010269657142 #签证照---1001
#aid = 2019010269750081 #证件照---1001