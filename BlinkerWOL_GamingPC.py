#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from Blinker import *
from Blinker.BlinkerDebug import *
#Device ID
auth = '977c9a407c04'
#Debug Mode
BLINKER_DEBUG.debugAll()
#WiFi Mode
Blinker.mode("BLINKER_WIFI")
#Add MiJia Plug
Blinker.miotType('BLINKER_MIOT_OUTLET')
Blinker.begin(auth)
#Define Button and Default status
button1 = BlinkerButton("btn-1")
oState = 'on'
 
def button1_callback(state):
    ''' Button Behavoir'''
    
    str00 = os.popen('etherwake  B0:25:AA:4E:46:55').readlines()[0]
    #Set Log Result    
    BLINKER_LOG('Get Button Status: ', state)
    button1.text('Powered ON')
    #Client Button Status
    button1.print(state)
    
def data_callback(data):
    ''' Data Callback '''
    str11 = os.popen(data).readlines()[0]
    #Show log and result
    BLINKER_LOG(data,str11)
 
 
def heartbeat_callback():
    ''' Heartbeat '''
    BLINKER_LOG("Heartbeat Log")
 
 
 
def miotPowerState(state):
    ''' Mijia switch '''
 
    global oState
 
    BLINKER_LOG('Set Status: ', state)
    oState = state
    BlinkerMIOT.powerState(state)
    BlinkerMIOT.print()
    if str(state) == 'true':
        #Change Mac Address Below
        str00 = os.popen('etherwake  B0:25:AA:4E:46:55').readlines()[0]
        BLINKER_LOG(str00)
 
def miotQuery(queryCode):
    ''' Mijia Query Method'''
 
    global oState
 
    BLINKER_LOG('MIOT Query codes: ', queryCode)
 
    if queryCode == BLINKER_CMD_QUERY_ALL_NUMBER :
        BLINKER_LOG('MIOT Query All')
        BlinkerMIOT.powerState(oState)
        BlinkerMIOT.print()
    elif queryCode == BLINKER_CMD_QUERY_POWERSTATE_NUMBER :
        BLINKER_LOG('MIOT Query Power State')
        BlinkerMIOT.powerState(oState)
        BlinkerMIOT.print()
    else :
        BlinkerMIOT.powerState(oState)
        BlinkerMIOT.print()
 
 
 
#按钮回调
button1.attach(button1_callback)
#数据回调
Blinker.attachData(data_callback)
#心跳回调
Blinker.attachHeartbeat(heartbeat_callback)
#米家控制回调
BlinkerMIOT.attachPowerState(miotPowerState)
#米家查询回调
BlinkerMIOT.attachQuery(miotQuery)
 
 
if __name__ == '__main__':
 
    while True:
        Blinker.run()