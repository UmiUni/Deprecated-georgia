# -*- coding: UTF-8 -*-
import datetime
def init():

  global chatGroups
  global vT
  global usersDict
  global admins 
  global ADMIN
  global previousDay

  chatGroups =[
    u'亚特兰大租房二手万能总群',
  ]

  v0= u"您好,亚特兰大加群建群小助手为您服务:)\n"
  v00=u"每天只能加1个群哦;\n"
  v1= u"回复 0 加亚特兰大租房二手万能总群;\n"
  v2= u"回复 99 查看【北美加群小助手Jogchat.com】\n微信公众号, 加纽约、硅谷等地群\n"
  vT =v0+v00+v1+v2
 
  usersDict = {}
  admins = []
  ADMIN = u'Geogia加群小助手'

  previousDay = datetime.datetime.now().day
