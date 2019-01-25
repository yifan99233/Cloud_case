import case2

Url = 'http://qyfh.ops.hzmantu.com'
def Bpoupload():
    #for i in random(1,100):
    c = case2.test(url = Url,data = {'user':'sys','pass':123})
    c.BpoUpload(10)
    #c.HistoryPhotographer(page=2)
    #c.XpsUpload()
#Bpoupload()
def testphoto():
    c = case2.test(url = Url,data = {'user':'sys','pass':123})
    c.testphoto()
#testphoto()

def Sys () :
    c = case2.test(url = Url , data = {'user' : 'sys' ,
                'pass' : '123'
               })
    c.SysUpload(   aid = 2019012518399152 , time = 3 )

Sys()
def Xps():
    c = case2.test(url = Url , data = {'user' : 'mxps520' ,
                'pass' : '123'
               })
    c.XpsUpload(time=5)
#Xps()
def Review():
    c = case2.test(url = Url,data = {'user':'xpszz','pass':123})
    c.Review(time=500)
#Review()
def kpsReview():
    c = case2.test(url = Url,data = {'user':'kps','pass':123})
    c.kpsReview(time=50)
#kpsReview()








