#! /usr/bin/python
import os
import sys
import optparse
import time

desc = "The current Python file is notified with crontab every minute. This file has the intelligence to recognise the appropriate notifier to notify the user depending upon the minute. Currently, we support only one flag at a time."


# Option Parser Object Creation
p = optparse.OptionParser(description=desc)


# HELPER FUNCTIONS
def parse_min(mn, time_struct):
    if mn=="*":
        return 1
    else: 
        if mn.find('/')!=-1:
            num = int(mn[mn.find('/'):-1])
            if num%time_struct.tm_min==0:
                return 1
            else:
                return 0
        else:
            num = int(mn)
            if num == time_struct.tm_min:
                return 1
            else:
                return 0



def parse_hr(hr, time_struct):
    if hr=="*":
        return 1
    else: 
        if hr.find('/')!=-1:
            num = int(hr[hr.find('/'):-1])
            if num%time_struct.tm_hour==0:
                return 1
            else:
                return 0
        else:
            num = int(hr)
            if num == time_struct.tm_hour:
                return 1
            else:
                return 0

def parse_day(dy, time_struct):
    if dy=="*":
        return 1
    else: 
        if dy.find('/')!=-1:
            num = int(dy[dy.find('/'):-1])
            if num%time_struct.tm_mday==0:
                return 1
            else:
                return 0
        else:
            num = int(dy)
            if num == time_struct.tm_mday:
                return 1
            else:
                return 0

def addOptions():
    p.add_option('-s','--show',dest='show',default=False,action='store_true',help='lists the commands present')
    p.add_option('-r','--reg',dest='reg',help='registers new command')


def decideCmd(opts,time_struct):
    if opts.show:
        ''' Enlisting the commands '''
        print "============================================================"
        print "List of commands"
        print "============================================================"
        os.system('cat /home/anirudt/Projects/sys_notifier/master_notify.nt')
    
    if opts.reg:
        os.system('sed -i "$ a '+opts.reg+'" master_notify.nt')
        os.system('cat /home/anirudt/Projects/sys_notifier/master_notify.nt')

        
    else:
        """ Runs the scheduler """
        a1,a2,a3,cmd = [],[],[],[]
        with open('master_notify.nt', 'rb') as f:
            for line in f:
                line = line.strip('\n')
                words = line.split(' ')
                a1.append(words[0])
                a2.append(words[1])
                a3.append(words[2])
                cmd.append(' '.join(words[5:]))

                # Join the cmd words here
        i = 0
        while i<len(a1):
            ret1 = parse_min(a1[i], time_struct) 
            ret2 = parse_hr(a2[i], time_struct)
            ret3 = parse_day(a3[i], time_struct)
            if ret1+ret2+ret3 == 3:
                os.system("/usr/bin/notify-send '"+cmd[i]+"'");
            i+=1

if __name__ == "__main__":
    addOptions()
    (opts, args) = p.parse_args()
    localtime = time.localtime(time.time())
    decideCmd(opts,localtime)
