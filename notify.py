#! /usr/bin/python
import os
import sys
import optparse

desc = "The current Python file is notified with crontab every second. This file has the intelligence to recognise the appropriate notifier to notify the user depending upon the minute. Currently, we support only one flag at a time."


# Option Parser Object Creation
p = optparse.OptionParser(description=desc)


# HELPER FUNCTIONS
def addOptions():
    p.add_option('-s','--show',dest='show',default=False,action='store_true',help='lists the commands present')
    p.add_option('-r','--reg',dest='reg',help='registers new command')


def decideCmd(opts):
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
                cmd.append(words[-1])
        print a1, a2, a3, cmd

#os.system("/usr/bin/notify-send"+string)

if __name__ == "__main__":
    addOptions()
    (opts, args) = p.parse_args()
    decideCmd(opts)
