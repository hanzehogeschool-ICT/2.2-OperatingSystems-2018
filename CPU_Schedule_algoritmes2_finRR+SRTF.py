#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kobus
#
# Created:     21-08-2018
# Copyright:   (c) kobus 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import operator,re
from collections import Counter

class Process:

    def __init__(self,ID,AT,Prior,burst,name):

        self.AT = AT  # Arrival time
        self.Prior = Prior # Prioriteit (1 hoogst=default)
        self.burst = burst # hoeveelheid CPU time-units
        self.ID = ID
        self.name = name

        print('Proces {0}: CPU burst={1} tu, Arrival tijd= moment {2}, prioriteit = {3}, {4}'.format(self.ID,self.burst,self.AT,self.Prior,self.name))


    def CPU_burst(self):

        return self.burst

class Proces_Collect(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value


def FCFS():
    # return sorted(dict.items())
    D = Proces_Collect()
    D.add(P1.AT,P1.ID)
    D.add(P2.AT,P2.ID)
    D.add(P3.AT,P3.ID)
    D.add(P4.AT,P4.ID)
    L1 = []
    L2 = []
    Lburst = []
    Process_burst = Proces_Collect()
    ProcessMom = Proces_Collect()

    mom = 0
    ProcessMom.add(1,mom)
    D1 = sorted(D.items(), key=lambda x: x[0])
    for i in range(len(D1)):
        MomWT = mom
        L1.append(D1[i][0])
        L2.append(D1[i][1])
        if L2[i] == 1: Lburst.append(P1.burst)
        if L2[i] == 2: Lburst.append(P2.burst)
        if L2[i] == 3: Lburst.append(P3.burst)
        if L2[i] == 4: Lburst.append(P4.burst)
        Process_burst.add(L2[i],Lburst[i])
        mom +=Lburst[i]
        if i < (len(D)-1): ProcessMom.add(i+2,mom)
        if L2[i] == 1: P1_WT = MomWT - P1.AT
        if L2[i] == 2: P2_WT = MomWT - P2.AT
        if L2[i] == 3: P3_WT = MomWT - P3.AT
        if L2[i] == 4: P4_WT = MomWT - P4.AT

    P1_TT = P1_WT + P1.burst
    P2_TT = P2_WT + P2.burst
    P3_TT = P3_WT + P3.burst
    P4_TT = P4_WT + P4.burst
    Av_TT = (P1_TT+P2_TT+P3_TT+P4_TT)/4
    print('Turn around Time p/proces: P1 = {0}, P2 = {1}, P3 = {2}, P4 = {3} tu. Gemiddeld:{4} tu'.format(P1_TT, P2_TT, P3_TT, P4_TT, Av_TT))
    Av_WT = (P1_WT+P2_WT+P3_WT+P4_WT)/4
    print('Waiting Time p/proces: P1 = {0}, P2 = {1}, P3 = {2}, P4 = {3} tu. Gemiddeld:{4} tu'.format(P1_WT, P2_WT, P3_WT, P4_WT, Av_WT))


    print('Schedule FCFS=',Process_burst)
    print('ProcMom=',ProcessMom)

    Gantt(Process_burst, ProcessMom, 'FCFS')
    return P1_TT, P1_WT, Av_TT, Av_WT

def Prioriteit_nonpreemp(burst_tot):

    D1 = Proces_Collect()
    D1.add(P1.AT,P1.ID)
    D1.add(P2.AT,P2.ID)
    D1.add(P3.AT,P3.ID)
    D1.add(P4.AT,P4.ID)
    L1 = []
    L2 = []
    L3 = []
    L4 = []
    Lmom = []
    L7 = []
    P1vo = True
    P2vo = True
    P3vo= True
    P4vo = True
    Lburst = []
    Tburst = 0
    j = 0

    #print(P1.burst)
    Process_burst = Proces_Collect()
    ProcessMom = Proces_Collect()

    D2 = sorted(D1.items(), key=lambda x: x[0])
    for i in range(len(D1)):
        L1.append(D2[i][0])
        L2.append(D2[i][1])

    L3.append(P1.Prior)
    L3.append(P2.Prior)
    L3.append(P3.Prior)
    L3.append(P4.Prior)
    L5 = [1,2,3,4]
    tel = 0
    a = 0
    b = 0
    c = 0
    d = 0
    test = 0

    if P1.Prior == 1: a = 11
    if P2.Prior == 1: b = 11
    if P3.Prior == 1: c = 11
    if P4.Prior == 1: d = 11

    while j <= (burst_tot-1):
       #print(j)
       test = 0
       #print('Lburst:',Lburst)
       #print('L5 b:',L5)
       dev1 = 0
       dev2 = 0
       dev3 = 0
       dev4 = 0
       while test < 9:
                      dd = j
                      if (P1.AT <= j) and P1vo and (P1.ID in L5) and (dev1 <= -1):

                          Lburst.append(P1.burst)
                          P1vo = False
                          Lmom.append(j)
                          P1_WT= j - P1.AT
                          j += P1.burst

                          L7.append(P1.ID)
                          L5.remove(1)
                          break

                      if (P2.AT <=j) and P2vo and (P2.ID in L5) and (dev2 <= -1):

                          Lburst.append(P2.burst)
                          P2vo = False
                          Lmom.append(j)
                          P2_WT= j - P2.AT
                          j += P2.burst

                          L7.append(P2.ID)
                          L5.remove(2)
                          break

                      if (P3.AT <=j) and P3vo and (P3.ID in L5) and (dev3 <= -1):

                          Lburst.append(P3.burst)
                          P3vo = False
                          Lmom.append(j)
                          P3_WT= j - P3.AT
                          j += P3.burst

                          L7.append(P3.ID)
                          L5.remove(3)
                          break

                      if (P4.AT <= j) and P4vo and (P4.ID in L5) and (dev4 <= -1):

                         Lburst.append(P4.burst)
                         P4vo = False
                         Lmom.append(j)
                         P4_WT= j - P4.AT
                         j += P4.burst

                         L5.remove(4)
                         L7.append(P4.ID)
                         break
                      test += 1
                      dev1 = (j + P1.AT) - (test + dd + a)
                      dev2 = (j + P2.AT) - (test + dd + b)
                      dev3 = (j + P3.AT) - (test + dd + c)
                      dev4 = (j + P4.AT) - (test + dd + d)
                      #print('L5 n:',L5)
                      #print('j l:',j, 'test :',test)
                      #print(dev1,dev2,dev3,dev4)

    Av_WT = (P1_WT+P2_WT+P3_WT+P4_WT)/4
    print('Waiting Time p/proces: P1 = {0}, P2 = {1}, P3 = {2}, P4 = {3} tu. Gemiddeld:{4} tu'.format(P1_WT, P2_WT, P3_WT, P4_WT, Av_WT))
    P1_TT = P1_WT + P1.burst
    P2_TT = P2_WT + P2.burst
    P3_TT = P3_WT + P3.burst
    P4_TT = P4_WT + P4.burst
    Av_TT = (P1_TT+P2_TT+P3_TT+P4_TT)/4
    print('Turn around Time p/proces: P1 = {0}, P2 = {1}, P3 = {2}, P4 = {3} tu. Gemiddeld:{4} tu'.format(P1_TT, P2_TT, P3_TT, P4_TT, Av_TT))

    Process_burst = Proces_Collect()
    ProcessMom = Proces_Collect()

    for i in range(len(D1)):
        Process_burst.add(L7[i],Lburst[i])
        ProcessMom.add(i,Lmom[i])
    print('Schedule Prioriteit non-preemptive:',Process_burst)
    #print('ProcesMom:',ProcessMom)
    #print('L1 AT: ', L1)
    #print('L2 ProcesID: ', L2)
    #print('L3 prior: ', L3)
    #print('D2 Pr: ', D2)
    #print('Lburst Pr.:',Lburst)
    Gantt(Process_burst,ProcessMom,'Prioriteit non_preemptive')
    return P1_TT, P1_WT, Av_TT, Av_WT

def SRTF(burst_tot):

    D1 = Proces_Collect()
    D1.add(P1.AT,P1.ID)
    D1.add(P2.AT,P2.ID)
    D1.add(P3.AT,P3.ID)
    D1.add(P4.AT,P4.ID)
    L1 = []
    L2 = []
    L3 = []
    L4 = []
    Lmom = []
    L7 = []
    P1vo = True
    P2vo = True
    P3vo= True
    P4vo = True
    Lburst = []
    Tburst = 0
    j = 0
    dev1 = 2
    dev2 = 2
    dev3 = 2
    dev4 = 2
    #print(P1.burst)
    Process_burst = Proces_Collect()
    ProcessMom = Proces_Collect()
    mom = 0
    ProcessMom.add(1,mom)
    D2 = sorted(D1.items(), key=lambda x: x[0])
    for i in range(len(D1)):
        L1.append(D2[i][0])
        L2.append(D2[i][1])

    L3.append(P1.Prior)
    L3.append(P2.Prior)
    L3.append(P3.Prior)
    L3.append(P4.Prior)
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    tel = 0
    Lred = []
    test = 0
    redp1 = P1.burst
    redp2 = P2.burst
    redp3 = P3.burst
    redp4 = P4.burst
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    voorp1 = False
    voorp2 = False
    voorp3 = False
    voorp4 = False
    dev1 = 2
    dev2 = 2
    dev3 = 2
    dev4 = 2
    P1_WT =0
    P2_WT =0
    P3_WT =0
    P4_WT=0
    P1r = True
    P2r = True
    P3r = True
    P4r = True
    tel1 = 0
    tel2 = 0
    tel3 = 0
    tel4 = 0
    k = -1
    vw = False
    vw1 = False
    for j in range(burst_tot):
       print('j begin:',j)
       dd = j
       block1 = True
       if P1r: dev1 =2
       if P2r: dev2 =2
       if P3r: dev3 =2
       if P4r: dev4 =2
       block = True
       voorp1 = False
       voorp2 = False
       voorp3 = False
       voorp4 = False
       p1 = False
       p2 = False
       p3 = False
       p4 = False
       count = 0
       Lred.append(500)
       test = 0
       if P1r: Lred.append(redp1)
       if P2r: Lred.append(redp2)
       if P3r: Lred.append(redp3)
       if P4r: Lred.append(redp4)
       minRed = min(Lred)
       if minRed==redp1 and block:
          voorp1 = True
          block = False
       if minRed==redp2 and block:
          voorp2 = True
          block = False
       if minRed==redp3 and block:
          voorp3 = True
          block = False
       if minRed==redp4 and block:
          voorp4 = True
          block = False
       #print('dev b:',dev1,dev2,dev3,dev4, 'test:',test, 'r:',P1r,P2r,P3r,P4r)

       print(Lred,minRed, voorp1,voorp2,voorp3,voorp4,'vw1',vw1)
       while test <= 4:
          q = dev1+dev2+dev3+dev4
          print('q:',q)
          #if (dev1+dev2+dev3+dev4) > 27000 :
          if vw1:
            #vw = True
            if redp1 == 0:
                tel1 = 0

            if redp2 == 0:
                tel2 = 0

            if redp3 == 0:
                tel3 = 0

            if redp4 == 0:
                tel4 = 0

          if P1r and (voorp1 or dev1 < 0) and P1.AT <= j and block1:

             block1 = False
             tel1 +=1
             #if tel1 > 2: count1 += 1
             p1 = True
             count1 += 1
             test = 5

             redp1 -= 1
             print('p1')
             if redp1 == 0:
               P1r = False
               a1 = 10000
               P1_WT = j - (P1.burst+P1.AT) +1

               if count1 > 0:
                  Lmom.append(j-tel1+1)
                  L7.append(P1.ID+10)
                  Lburst.append(tel1)
                  print('p1 klaar!', j, tel1)
                  tel1 =0
               if vw1: p1 = False

          if P2r and (voorp2 or dev2 < 0) and (P2.AT <= j) and block1:
             block1 = False
             tel2 +=1
             k=j
             p2 = True
             count2 += 1
             test = 5
             redp2 -= 1
             print('p2')
             if redp2 == 0:
               P2_WT = j - (P2.burst + P2.AT) +1

               P2r = False
               a2 = 10000
               if count2 > 0:
                  Lmom.append(j-tel2+1)
                  L7.append(P2.ID+10)
                  Lburst.append(tel2)
                  print('p2 klaar!', j, tel2)
                  tel2 =0
               if vw1: p2 = False

          if P3r and (voorp3 or dev3 < 0) and (P3.AT <= j) and block1:
             block1 = False
             p3 = True
             k = j
             tel3 +=1
             count3 += 1
             test = 5
             redp3 -= 1
             print('p3',redp3)
             if redp3 == 0:
               P3_WT = j - (P3.burst + P3.AT) +1

               P3r = False
               a3 = 10000
               if count3 > 0:
                  Lmom.append(j-tel3+1)
                  L7.append(P3.ID+10)
                  Lburst.append(tel3)
                  print('p3 klaar!', j, tel3)
                  tel3 =0
               if vw1: p3 = False

          if P4r and (voorp4 or dev4 < 0) and (P4.AT <= j) and block1:
             block1 = False
             count4 +=1
             p4 = True
             k = j
             tel4 +=1
             test = 5
             redp4 -= 1
             print('p4')
             if redp4 == 0:
               P4_WT = j - (P4.burst + P4.AT) +1

               P4r = False
               a4 = 10000
               if count4 > 0:
                  Lmom.append(j-tel4+1)
                  L7.append(P4.ID+10)
                  Lburst.append(tel4)
                  print('p4 klaar!', j, tel4)
                  tel4 =0
               if vw1: p4 = False

          print('Tel bu:', tel1,tel2,tel3,tel4)
          dev1 = (j + P1.AT+ a1) - (dd+test)
          dev2 = (j + P2.AT+ a2) - (dd+test)
          dev3 = (j + P3.AT+ a3) - (dd+test)
          dev4 = (j + P4.AT+ a4) - (dd+test)

          #print('dev:',dev1,dev2,dev3,dev4,'test:',test,'dd:',dd,a1,a2,a3,a4)
          test +=1
       #if P1r: p1 = False
       #if P2r: p2 = False
       #if P3r: p3 = False
       #if P4r: p4 = False

       if tel1 > 0 and (not p1 or vw1):
            Lmom.append(j-tel1+1)
            L7.append(P1.ID)
            Lburst.append(tel1)
            if not vw1:tel1 =0
       if tel2 > 0 and (not p2 or vw1):
            Lmom.append(j-tel2+1)
            L7.append(P2.ID)
            Lburst.append(tel2)
            if not vw1: tel2 = 0
       if tel3 > 0 and (not p3 or vw1):
            Lmom.append(j-tel3+1)
            L7.append(P3.ID)
            Lburst.append(tel3)
            print('j:',j,'tel3:',tel3)
            if not vw1: tel3 =0
       if tel4 > 0 and (not p4 and vw1):
            Lmom.append(j-tel4+1)
            L7.append(P4.ID)
            Lburst.append(tel4)
            print('j:',j,'tel4:',tel4)
            if not vw1: tel4= 0


       if len(Lred) == 2: vw1 = True



       Lred[:] = []

    Av_WT = (P1_WT+P2_WT+P3_WT+P4_WT)/4
    print('Waiting Time p/proces: P1 = {0}, P2 = {1}, P3 = {2}, P4 = {3} tu. Gemiddeld:{4} tu'.format(P1_WT, P2_WT, P3_WT, P4_WT, Av_WT))
    P1_TT = P1_WT + P1.burst
    P2_TT = P2_WT + P2.burst
    P3_TT = P3_WT + P3.burst
    P4_TT = P4_WT + P4.burst
    Av_TT = (P1_TT+P2_TT+P3_TT+P4_TT)/4
    print('Turn around Time p/proces: P1 = {0}, P2 = {1}, P3 = {2}, P4 = {3} tu. Gemiddeld:{4} tu'.format(P1_TT, P2_TT, P3_TT, P4_TT, Av_TT))

    Process_burst = Proces_Collect()
    ProcessMom = Proces_Collect()
    Lmom[0] = 0
    for i in range(len(Lburst)):
        Process_burst.add(L7[i],Lburst[i])
        ProcessMom.add(i,Lmom[i])
    print('Lmom:',Lmom)
    print('Schedule SRTF:',Process_burst)
    print('ProcesMom:',ProcessMom)
    print('L7 AT: ', L7)
    print('L2 ProcesID: ', L2)
    #print('L3 prior: ', L3)
    #print('D2 Pr: ', D2)
    print('Lburst Pr.:',Lburst)
    Gantt(Process_burst,ProcessMom,'SRTF Preemptive')
    return P1_TT, P1_WT, Av_TT, Av_WT


def RoundRobin(burst_tot,QuatumT):

    D1 = Proces_Collect()
    D1.add(P1.AT,P1.ID)
    D1.add(P2.AT,P2.ID)
    D1.add(P3.AT,P3.ID)
    D1.add(P4.AT,P4.ID)
    L1 = []
    L2 = []
    L3 = []
    L4 = []
    Lmom = []
    L7 = []
    P1vo = True
    P2vo = True
    P3vo= True
    P4vo = True
    Lburst = []
    Tburst = 0
    j = 0

    #print(P1.burst)
    Process_burst = Proces_Collect()
    ProcessMom = Proces_Collect()

    D2 = sorted(D1.items(), key=lambda x: x[0])
    for i in range(len(D1)):
        L1.append(D2[i][0])
        L2.append(D2[i][1])

    L3.append(P1.Prior)
    L3.append(P2.Prior)
    L3.append(P3.Prior)
    L3.append(P4.Prior)
    L5 = [1,2,3,4,11,12,13,14]
    tel = 0

    test = 0
    redp1 = 0
    redp2 = 0
    redp3 = 0
    redp4 = 0

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    P1_WT =0
    P2_WT =0
    P3_WT =0
    P4_WT=0


    while j <= (burst_tot-1):
       #print(j)
       test = 0
       #print('Lburst:',Lburst)
       #print('L5 b:',L5)
       dev1 = 0
       dev2 = 0
       dev3 = 0
       dev4 = 0
       while test < 11:
                      dd = j
                      if (P1.AT <= j) and P1vo and (P1.ID in L5) and (dev1 <= -1):
                          if (P1.burst-redp1) <= (QuatumT):
                             P1_WT += j - P1.AT
                             if redp1 > 0:
                                 Lburst.append(redp1)
                                 Lmom.append(j)
                                 j += redp1
                                 L7.append(P1.ID+10)
                             else:
                                Lmom.append(j)
                                j += P1.burst
                                Lburst.append(P1.burst)
                                L7.append(P1.ID)
                             P1vo = False



                             L5.remove(1)
                             #print('P1c',Lmom)
                             break
                          else:
                             redp1 = P1.burst - QuatumT
                             Lburst.append(QuatumT)
                             Lmom.append(j)
                             j += QuatumT
                             P1_WT -= 5
                             L7.append(P1.ID)
                             q1 = 5
                             #print('P1q',Lmom)
                             break

                      if (P2.AT <=j) and P2vo and (P2.ID in L5) and (dev2 <= -1):

                          if (P2.burst-redp2) <= (QuatumT):
                             P2_WT += j - P2.AT
                             if redp2 > 0:
                                 Lburst.append(redp2)
                                 Lmom.append(j)
                                 j += redp2
                                 L7.append(P2.ID+10)
                             else:
                                Lmom.append(j)
                                j += P2.burst
                                Lburst.append(P2.burst)
                                L7.append(P2.ID)
                             P2vo = False



                             L5.remove(2)
                             #print('p2c',Lmom)
                             break
                          else:
                             redp2 = P2.burst - QuatumT
                             Lburst.append(QuatumT)
                             Lmom.append(j)
                             j += QuatumT
                             P2_WT -= QuatumT
                             L7.append(P2.ID)
                             q2 = 5
                             #print('p2q',Lmom)
                             break


                      if (P3.AT <=j) and P3vo and (P3.ID in L5) and (dev3 <= -1):

                          if (P3.burst-redp3) <= (QuatumT):
                             P3_WT += j - P3.AT
                             if redp3 > 0:
                                 Lburst.append(redp3)
                                 Lmom.append(j)
                                 j += redp3
                                 L7.append(P3.ID+10)

                             else:
                                Lmom.append(j)
                                j += P3.burst
                                Lburst.append(P3.burst)
                                L7.append(P3.ID)


                             P3vo = False

                             L5.remove(3)
                             #print('p3c',Lmom)
                             break
                          else:
                             redp3 = P3.burst - QuatumT
                             Lburst.append(QuatumT)
                             Lmom.append(j)
                             P3_WT -= QuatumT
                             j += QuatumT
                             L7.append(P3.ID)
                             q3 = 5
                             #print('p3q',Lmom)
                             break


                      if (P4.AT <= j) and P4vo and (P4.ID in L5) and (dev4 <= -1):

                         if (P4.burst-redp4) <= (QuatumT):
                             P4_WT += j - P4.AT
                             if redp4 > 0:
                                 Lburst.append(redp4)
                                 Lmom.append(j)
                                 j += redp4
                                 L7.append(P4.ID+10)
                             else:
                                Lmom.append(j)
                                j += P4.burst
                                Lburst.append(P4.burst)
                                L7.append(P4.ID)
                             P4vo = False


                             L5.remove(4)
                             #print('p4ç',Lmom)
                             break

                         else:
                             redp4 = P4.burst -QuatumT
                             Lburst.append(QuatumT)
                             Lmom.append(j)
                             P4_WT -= QuatumT
                             j += QuatumT
                             L7.append(P4.ID)
                             q4 = 5
                             #print('p4q',Lmom)
                             break

                      test += 1
                      dev1 = (j + P1.AT + q1) - (test + dd )
                      dev2 = (j + P2.AT + q2) - (test + dd )
                      dev3 = (j + P3.AT + q3) - (test + dd )
                      dev4 = (j + P4.AT + q4) - (test + dd )
                      #print('L5 n:',L5, 'test:',test,'dd:',dd)
                      #print('red:',redp1,redp2,redp3,redp4)
                      #print(dev1,dev2,dev3,dev4)

    Av_WT = (P1_WT+P2_WT+P3_WT+P4_WT)/4
    print('Waiting Time p/proces: P1 = {0}, P2 = {1}, P3 = {2}, P4 = {3} tu. Gemiddeld:{4} tu'.format(P1_WT, P2_WT, P3_WT, P4_WT, Av_WT))
    P1_TT = P1_WT + P1.burst
    P2_TT = P2_WT + P2.burst
    P3_TT = P3_WT + P3.burst
    P4_TT = P4_WT + P4.burst
    Av_TT = (P1_TT+P2_TT+P3_TT+P4_TT)/4
    print('Turn around Time p/proces: P1 = {0}, P2 = {1}, P3 = {2}, P4 = {3} tu. Gemiddeld:{4} tu'.format(P1_TT, P2_TT, P3_TT, P4_TT, Av_TT))

    Process_burst = Proces_Collect()
    ProcessMom = Proces_Collect()

    for i in range(len(Lburst)):
        Process_burst.add(L7[i],Lburst[i])
        ProcessMom.add(i,Lmom[i])
    print('Quatum tijd: {} tu bij RR.'.format(QuatumT))
    print('Schedule Round Robin:',Process_burst)
    #print('ProcesMom:',ProcessMom)
    #print('L7 AT: ', L7)
    #print('L2 ProcesID: ', L2)
    #print('L3 prior: ', L3)
    #print('D2 Pr: ', D2)
    #print('Lburst Pr.:',Lburst)
    Gantt(Process_burst,ProcessMom,'RoundRobin Preemptive')
    return P1_TT, P1_WT, Av_TT, Av_WT


def SJF(burst_tot):

    D1 = Proces_Collect()
    D1.add(P1.AT,P1.ID)
    D1.add(P2.AT,P2.ID)
    D1.add(P3.AT,P3.ID)
    D1.add(P4.AT,P4.ID)
    L1 = []
    L2 = []
    L3 = []
    L4 = []
    Lmom = []
    L7 = []
    P1vo = True
    P2vo = True
    P3vo= True
    P4vo = True
    Lburst = []
    Tburst = 0
    j = 0

    #print(P1.burst)
    Process_burst = Proces_Collect()
    ProcessMom = Proces_Collect()

    D2 = sorted(D1.items(), key=lambda x: x[0])
    for i in range(len(D1)):
        L1.append(D2[i][0])
        L2.append(D2[i][1])

    L3.append(P1.Prior)
    L3.append(P2.Prior)
    L3.append(P3.Prior)
    L3.append(P4.Prior)
    L5 = [1,2,3,4]
    tel = 0
    a = 0
    b = 0
    c = 0
    d = 0
    test = 0

    a = P1.burst
    b = P2.burst
    c = P3.burst
    d = P4.burst
    #print(a,b,c,d)

    while j <= (burst_tot-1):
       #print(j)
       test = 0
       #print('Lburst:',Lburst)
       #print('L5 b:',L5)
       dev1 = 0
       dev2 = 0
       dev3 = 0
       dev4 = 0
       while test < 15:
                      dd = j
                      if (P1.AT <= j) and P1vo and (P1.ID in L5) and (dev1 <= -1):

                          Lburst.append(P1.burst)
                          P1vo = False
                          Lmom.append(j)
                          P1_WT  = j - P1.AT
                          j += P1.burst

                          L7.append(P1.ID)
                          L5.remove(1)
                          break

                      if (P2.AT <=j) and P2vo and (P2.ID in L5) and (dev2 <= -1):

                          Lburst.append(P2.burst)
                          P2vo = False
                          Lmom.append(j)
                          P2_WT  = j - P2.AT
                          j += P2.burst

                          L7.append(P2.ID)
                          L5.remove(2)
                          break

                      if (P3.AT <=j) and P3vo and (P3.ID in L5) and (dev3 <= -1):

                          Lburst.append(P3.burst)
                          P3vo = False
                          Lmom.append(j)
                          P3_WT  = j - P3.AT
                          j += P3.burst

                          L7.append(P3.ID)
                          L5.remove(3)
                          break

                      if (P4.AT <= j) and P4vo and (P4.ID in L5) and (dev4 <= -1):

                         Lburst.append(P4.burst)
                         P4vo = False
                         Lmom.append(j)
                         P4_WT  = j - P4.AT
                         j += P4.burst

                         L5.remove(4)
                         L7.append(P4.ID)
                         break
                      test += 1
                      dev1 = a - test
                      dev2 = b - test
                      dev3 = c - test
                      dev4 = d - test
                      #print('L5 n:',L5)
                      #print('j l:',j, 'test :',test)
                      #print(dev1,dev2,dev3,dev4)

    Av_WT = (P1_WT+P2_WT+P3_WT+P4_WT)/4
    print('Waiting Time p/proces: P1 = {0}, P2 = {1}, P3 = {2}, P4 = {3} tu. Gemiddeld:{4} tu'.format(P1_WT, P2_WT, P3_WT, P4_WT, Av_WT))
    P1_TT = P1_WT + P1.burst
    P2_TT = P2_WT + P2.burst
    P3_TT = P3_WT + P3.burst
    P4_TT = P4_WT + P4.burst
    Av_TT = (P1_TT+P2_TT+P3_TT+P4_TT)/4
    print('Turn around Time p/proces: P1 = {0}, P2 = {1}, P3 = {2}, P4 = {3} tu. Gemiddeld:{4} tu'.format(P1_TT, P2_TT, P3_TT, P4_TT, Av_TT))


    Process_burst = Proces_Collect()
    ProcessMom = Proces_Collect()

    for i in range(len(D1)):
        Process_burst.add(L7[i],Lburst[i])
        ProcessMom.add(i,Lmom[i])
    print('Schedule SJF:',Process_burst)
    #print('ProcesMom:',ProcessMom)
    #print('L1 AT: ', L1)
    #print('L2 ProcesID: ', L2)
    #print('L3 prior: ', L3)
    #print('D2 Pr: ', D2)
    #print('Lburst Pr.:',Lburst)
    Gantt(Process_burst,ProcessMom,'SJF')
    return P1_TT, P1_WT, Av_TT, Av_WT

def Spacie(var):
    l = ' '
    var1 = round(var,1)
    for k in range(5-len(str(var1))): l += ' '
    return l, var1


def Gantt(Processes,mom,algoritme):

        window = Tk()
        window.title("Grantt diagram")

        frame1 = Frame(window)
        frame1.pack()
        canvas = Canvas(window, width = 600, height = 200)
        canvas.pack()
        Lid = list(Processes.keys())
        Lburst = list(Processes.values())
        Lmom = list(mom.values())
        #print(Lid)
        l = 40
        kleuren = []
        kleuren1 = ['red','blue','yellow','green','black','brown','white']
        Lname = []
        for h in range(len(Lid)):
            if Lid[h] == 1:
                Lname.append(P1.name)
                kleuren.append(kleuren1[0])

            if Lid[h] == 2:
                Lname.append(P2.name)
                kleuren.append(kleuren1[1])

            if Lid[h] == 3:
                Lname.append(P3.name)
                kleuren.append(kleuren1[2])

            if Lid[h] == 4:
                Lname.append(P4.name)
                kleuren.append(kleuren1[3])
            if Lid[h] == 11:
                Lname.append(P1.name)
                kleuren.append(kleuren1[0])

            if Lid[h] == 12:
                Lname.append(P2.name)
                kleuren.append(kleuren1[1])

            if Lid[h] == 13:
                Lname.append(P3.name)
                kleuren.append(kleuren1[2])

            if Lid[h] == 14:
                Lname.append(P4.name)
                kleuren.append(kleuren1[3])







        for i in range(len(Lid)):
           Box1 = canvas.create_rectangle(l, 160, Lburst[i]*20+(l-20), 180, fill=kleuren[i])
           Text1 = canvas.create_text(20+l, 140, fill="black", text='Proc.'+str(Lid[i]))
           Text3 = canvas.create_text(20+l, 120, fill="black", text=Lname[i])
           Text2 = canvas.create_text(0+l, 190, fill="blue", text=(Lmom[i]))
           l += Lburst[i]*20 -20
           #print('l=',l)
        Text3 = canvas.create_text(0+l, 190, fill="blue", text=(Lmom[i]+Lburst[i]))
        Text4 = canvas.create_text(0+l-80, 20, fill="blue", text= 'Algoritme: '+algoritme)



        window.mainloop()


print('CPU-scheduler (model); vier processen met een minimale tu van 2 en maximale tu van 9, Quantum RR 5')

# proc      ID AT P B
P1 = Process(1,2,2,5,'edge')  # 1,2,2,5     1,2,2,4      1,2,2,8    1,2,2,4  1,5,1,5   1,1,1,10
P2 = Process(2,3,1,7,'chrome') # 2,3,1,7     2,3,1,7      2,3,1,7    2,0,1,7  2,0,2,7   2,3,1,7
P3 = Process(3,4,2,8,'SSH')    # 3,4,2,8     3,4,2,5      3,4,2,4    3,4,2,8  3,4,1,8   3,0,1,8
P4 = Process(4,0,1,9,'Mplayer')# 4,0,1,9     4,0,1,9      4,0,1,6    4,1,1,9  4,2,2,9   4,2,1,5


CPU_burst_tot = P1.CPU_burst()+ P2.CPU_burst()+P3.CPU_burst()+P4.CPU_burst()
print("CPU burst totaal: ",CPU_burst_tot)


keuze = input('Welk algoritme voor een CPU-schedule? f = FCFS, r = RoundRobin, s = SJF, t = SRTF en p = Prioriteit non-preemptive')
if keuze == 'p' or keuze == 'P' :  TT_P1p, WT_P1p, TT_Avp, WT_Avp = Prioriteit_nonpreemp(CPU_burst_tot)
if keuze == 'f' or keuze == 'F' :  TT_P1, WT_P1, TT_Av, WT_Av = FCFS()
if keuze == 'r' or keuze == 'R' :  TT_P1r, WT_P1r, TT_Avr, WT_Avr= RoundRobin(CPU_burst_tot,5)
if keuze == 's' or keuze == 'S' :  TT_P1s, WT_P1s, TT_Avs, WT_Avs = SJF(CPU_burst_tot)
if keuze == 't' or keuze == 'T' :  TT_P1t, WT_P1t, TT_Avt, WT_Avt = SRTF(CPU_burst_tot)
if keuze == 'x':
     TT_P1p, WT_P1p, TT_Avp, WT_Avp = Prioriteit_nonpreemp(CPU_burst_tot)
     TT_P1, WT_P1, TT_Av, WT_Av = FCFS()
     TT_P1s, WT_P1s, TT_Avs, WT_Avs = SJF(CPU_burst_tot)
     TT_P1r, WT_P1r, TT_Avr, WT_Avr = RoundRobin(CPU_burst_tot,5)
     TT_P1t, WT_P1t, TT_Avt, WT_Avt = SRTF(CPU_burst_tot)

     l1,a = Spacie(WT_P1)
     l2,b = Spacie(TT_P1)
     l3,c = Spacie(WT_Av)
     l4,d = Spacie(TT_Av)
     l5,a1 = Spacie(WT_P1p)
     l6,b1 = Spacie(TT_P1p)
     l7,c1 = Spacie(WT_Avp)
     l8,d1 = Spacie(TT_Avp)
     l9,a2 = Spacie(WT_P1s)
     l10,b2 = Spacie(TT_P1s)
     l11,c2 = Spacie(WT_Avs)
     l12,d2 = Spacie(TT_Avs)
     l13,a3 = Spacie(WT_P1r)
     l14,b3 = Spacie(TT_P1r)
     l15,c3 = Spacie(WT_Avr)
     l16,d3 = Spacie(TT_Avr)
     l17,a4 = Spacie(WT_P1t)
     l18,b4 = Spacie(TT_P1t)
     l19,c4 = Spacie(WT_Avt)
     l20,d4 = Spacie(TT_Avt)






     print('+--------------------------------------------------------------------------------+')
     print('|  Algoritme:      | FCFS:   | Prioriteit: | SJF       | RoundRobin) |    SRTF   |')
     print('+--------------------------------------------------------------------------------+')
     print('| Wait Time P1     |{0}{1}   |{2}{3}       |{4}{5}     |{6}{7}       |{8}{9}     |'.format(l1,a,l5,a1,l9,a2,l13,a3,l17,a4))
     print('| Turnar. Time P1  |{0}{1}   |{2}{3}       |{4}{5}     |{6}{7}       |{8}{9}     |'.format(l2,b,l6,b1,l10,b2,l14,b3,l18,b4))
     print('| Wait Time gemidd.|{0}{1}   |{2}{3}       |{4}{5}     |{6}{7}       |{8}{9}     |'.format(l3,c,l7,c1,l11,c2,l15,c3,l19,c4))
     print('| Turnar. Time gem.|{0}{1}   |{2}{3}       |{4}{5}     |{6}{7}       |{8}{9}     |'.format(l4,d,l8,d1,l12,d2,l16,d3,l20,d4))
     print('+--------------------------------------------------------------------------------+')



