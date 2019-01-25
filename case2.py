import  requests
import random
import SQL
from bs4 import BeautifulSoup



class test ( object ) :



    def __init__ ( self , url , data ) :
        #登陆
        self.url = url
        LoginUrl = '/User/checkLogin'
        self.PostRequests ( url = LoginUrl ,data =data )
        #获取cookie 、 header
        self.cookie = { 'PHPSESSID' : self.r.cookies [ 'PHPSESSID' ] }
        self.header = self.r.request.headers
        #print(self.cookie,self.header)
    #摄影师上传历史记录



    def BpoUpload(self,time):
        for i in  range(time):
            cookie = {'thinkphp_show_page_trace':'0|0','PHPSESSID':'filulnucc0apk5snlrejnt0q65'}
            getaccount = 'http://bpo.qyfh.ops.hzmantu.com/Api/startAccount'
            get = requests.get(url = getaccount,cookies = cookie)
            if get.json()['msg'] == "接单成功" or get.json()['msg'] =='接单失败,不可重复接单,请不要多次点击确认按钮':
                get = requests.get(url = 'http://bpo.qyfh.ops.hzmantu.com/Index/handle',cookies = cookie).text
                soup = BeautifulSoup(get,'html.parser')
                aid = str(soup.find('td').text.strip())[0:17]
                list = soup.find_all('label')
                mlist = []
                [mlist.append(x.text[5:].strip()) for x in list]
                num = 0
                data = {}
                hlist = self.RandomPhoto(len(mlist))
                data['aid'] = aid
                for i in mlist:
                    data['photo[%d][oldname]'%num] = i
                    data['photo[%d][newname]'%num] = hlist[num][0]
                    num+=1
                #print(data)
                r = requests.post(url = 'http://bpo.qyfh.ops.hzmantu.com/Api/submitPhoto',data =data,cookies = cookie,headers = self.header)
                print(aid,r.json())
            else:
                print("暂无订单可以上传")


    def testphoto(self):
        sql = "select CP_Path from cloud_photo"
        v = SQL.Sql().Select(sql)
        n = 'http://cloud.cdn.hzmantu.com/upload_dev/'
        list  = SQL.Sql().Select("SELECT photo FROM photo")
        for x in v :
            pinsert = 'INSERT INTO photo (photo) value ("%s")' % x[0]
            #pinsert = 'INSERT INTO photo (photo) value ("2a03f5d846788102e2b682b9c4e2e985.jpg")'
            url='{}{}''!test'.format(n,x[0])
            get = requests.get(url=url)
            if not x in list:

                if  get.status_code == 200 :
                    SQL.Sql().Update(pinsert)
                else:
                    print("200"+pinsert)
            else:
                print("已存在下"+x[0])


    def HistoryPhotographer(self,page = 1 ):
        list = []
        for x in range(page):
            url = '/Account/uploadedAccount/p/%d'%x
            m = self.GetRequests(url = url,cookie= self.cookie).text
            soup = BeautifulSoup(m, 'html.parser')
            [list.append(i.text) for i in soup.find_all("td")[0::5]]
        return list




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
    def Random(self , a =1,b = 5,time = 1  ):
        list = []
        for i in range(time):
            num = random.randint(a, b)
            if not num in list:
                list.append(num)
            else:
                list.append(random.randint(a, b))
        return list



    def RandomPhoto( self , count = 1 ):
        id = str(self.Random( a= 1 , b = 400 , time= count))[1:-1]
        sql = "select photo from photo where id in(%s)"%id
        v = SQL.Sql().Select(sql)
        list = []
        [list.append(x) for x in v]
        return list



    def SysUpload ( self ,  aid , count = 4,time=1 ) :
        # 查找订单接口
        searchAccountUrl = '/Remote/searchAccount'
        searchAccountData = {'aidKey':aid}
        PtypeUrl = '/Remote/getAccountType'
        ptype = self.GetRequests(url=PtypeUrl,cookie=self.cookie).json()['msg'][0]['accountType']
        v = self.PostRequests ( url=searchAccountUrl , data=searchAccountData , header=self.header , cookie=self.cookie )
        if v.json()['msg'] == '暂无相关订单':
            print('订单不存在')
        else:
            for i in range(time):
                p = v.json()['msg'][0]
                pid = p['productIdArr'][0]['AI_Pid']
                list = self.RandomPhoto(count = count)
                # 摄影师上传提交的参数
                try:
                    SubmitData = {}
                    num = 0
                    for i in list:
                        SubmitData['photoData[%d][path]' % num] = i
                        SubmitData['photoData[%d][count]' % num] = random.randint(1, 1)
                        SubmitData['photoData[%d][productId]' % num] = pid
                        SubmitData['photoData[%d][group]' % num] = ''
                        num+=1
                    SubmitData['name'] = p['A_Name']
                    SubmitData['phone'] = p['A_Phone']
                    SubmitData['note'] = p['note']
                    SubmitData['areye'] = 1
                    SubmitData['arface'] = 1
                    SubmitData['ardot'] = 1
                    SubmitData['isToday'] = 1
                    SubmitData['ptype'] = ptype
                    SubmitData['haimatiAid'] = aid
                    SubmitData['productArr[]'] = pid
                except:
                    print("参数生成失败")
                try:

                    # 摄影师上传提交接口地址
                    PsersubmitAccount = '/Pser/submitAccount'
                    #sys上传调 post请求
                    self.PostRequests ( header = self.header , url = PsersubmitAccount , data = SubmitData , cookie = self.cookie )
                    print("摄影师已成功上传1单，流水号为："+self.HistoryPhotographer()[0])
                except:
                    print("提交失败")



    def XpsUpload ( self , time = 1 ) :
        SearchAccountCount = '/Cser/getPhotoQueue' #查看能接多少单
        RequestsAccountUrl = '/Cser/requestAccount' # 接单接口
        GetHandAccount = '/Cser/getHandleAccount'   #接单后查询接口
        XpsSubmitUrl = '/Cser/submitAccount'
        RequestsAccountData = { 'isMainto' : 0 } #接单 参数
        for i in  range ( time ) :
            #查询可接单数
            self.PostRequests(url = SearchAccountCount , cookie = self.cookie )
            msg = self.r.json()['msg']
            if msg['needCount']>0:
                #接单
                self.PostRequests( url = RequestsAccountUrl , data = RequestsAccountData , cookie = self.cookie , header = self.header )
                msv = self.r.json()['msg']
                if msv=='接单成功' or msv =='不可重复接单,请不要多次点击确认按钮':
                    #查询流水信息
                    self.PostRequests ( url = GetHandAccount , cookie = self.cookie , header = '' , data = '' )
                    photoid = {}
                    photoid['aid'] = self.r.json()['msg']['CA_Id']
                    data = self.r.json()['msg']['photoData']
                    num = 0
                    list = self.RandomPhoto(len(data))
                    for x in data:
                        photoid['photo[%d][id]'%num] = x['CP_Id']
                        photoid['photo[%d][path]'%num] = list[num][0]
                        photoid['photo[%d][modelPath]'%num] = ''
                        num+=1
                    self.PostRequests( url = XpsSubmitUrl , data = photoid  ,header= self.header,cookie = self.cookie )
                    print("流水号："+photoid['aid']+"---已被修片师"+self.r.json()['msg'])
                else:
                    print(msv)
            else:
                print("暂无可接订单")



    def Review(self , time = 1 , caid = '' ):
        #返回审核页面订单信息的接口 name ''   page   leader -1
        RCaidInforUrl = '/Cker/getCheckList'
        #审核详情界面的接口 aid
        AccountInforUrl = '/Cker/getCheckAccount'
        changestate = '/Cker/changePhotoState'
        changestatedata = { "plant" : "" , "weed" : "" }
        #通过审核的接口
        RPassUrl = '/Cker/passAccount'
        if caid == '' :
            for x in range(1,time+1):
                RCaidInforData = {'name': '', 'page': x , 'leader': -1}
                self.PostRequests(url=RCaidInforUrl, header=self.header, cookie=self.cookie, data=RCaidInforData)
                caid = self.r.json()["msg"]["list"]
                for i in range(10):
                    Caid = caid[i]['CA_Id']
                    AccountInforData = {'aid': Caid}
                    self.PostRequests(url=AccountInforUrl, header=self.header, cookie=self.cookie,data=AccountInforData)
                    RPassData = {'aid': Caid, 'goodNote': '', 'badNote': '', 'isVisa': 0, 'splPrty': 0}
                    self.PostRequests(url=RPassUrl, data=RPassData, header=self.header, cookie=self.cookie)
                    if self.r.json()['msg'] == '操作成功':
                        print('%s该流水号修片师组长已审核'%Caid)
                    else:
                        print('审核失败')
        else:
            AccountInforData = { 'aid' : caid }
            self.PostRequests(url=AccountInforUrl, header=self.header, cookie=self.cookie,data=AccountInforData)
            data = {'aid': caid, 'goodNote': '', 'badNote': '', 'isVisa': 0, 'splPrty': 0}
            self.PostRequests(url = RPassUrl, data=data, header=self.header, cookie=self.cookie)
            if self.r.json()['msg'] == '操作成功':
                print('%s该流水号修片师组长已审核' % caid)
            else:
                print('审核失败')



    def kpsReview(self , cnum = '' , time = 1 ):
        RCaidInforurl = '/Cker/getCheckAccountList'
        AccountInforUrl = '/Account/doCheckAccount'
        pj = '/Cker/appraiseCserAccount'
        if cnum == '' :
            for x in range(1,time+1):
                RCaidInforData = {'type': 3, 'key': '' , 'state': 'all' , 'page':x}
                self.PostRequests(url=RCaidInforurl, header=self.header, cookie=self.cookie, data=RCaidInforData)
                caid = self.r.json()["msg"]["list"]
                print(caid[0]['aid'])
                for i in range(10):
                    Caid = caid[i]['aid']
                    RPassData = 'score=5&comment=456&aid=%s'%Caid
                    self.PostRequests(url=pj, data=RPassData,  header=self.header, cookie=self.cookie)
                    AccountInforData = {'aid': Caid , 'isAgreeShare' : 1 }
                    self.PostRequests(url=AccountInforUrl, header=self.header, cookie=self.cookie,data=AccountInforData)
                    m = self.r.json()['msg']
                    self.PostRequests(url=pj, data=RPassData, header=self.header, cookie=self.cookie)
                    if m == '微信通知未发送,该用户未关注微信公众号或已取消关注':
                        print(Caid+'该流水号看片师已审核')
                    else:
                        print(Caid+'看片师审核失败')
        else:
            Caid = cnum
            RPassData = 'score=5&comment=456&aid=%s' % Caid
            self.PostRequests(url=pj, data=RPassData, header=self.header, cookie=self.cookie)
            AccountInforData = {'aid': Caid, 'isAgreeShare': 1}
            self.PostRequests(url=AccountInforUrl, header=self.header, cookie=self.cookie, data=AccountInforData)
            m = self.r.json()['msg']
            self.PostRequests(url=pj, data=RPassData, header=self.header, cookie=self.cookie)
            if m == '微信通知未发送,该用户未关注微信公众号或已取消关注':
                print(Caid + '该流水号看片师已审核')
            else:
                print(Caid + '看片师审核失败')


