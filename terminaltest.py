# Starting colors for terminal:
# Green font: rgb(55,161,64)
# Background: rgb(0,0,0)

#It'd be great to have an online doc that python continually reads to assess
# the damage to the ship or to the crew. Maybe hints at things too.

import time

def update_progress(progress):
    # bar where each # represents 10%
    #print '\r[{0}] {1}%'.format('#'*(progress/10) + '-' * (10-(progress/10)), progress)
    # bar where each # represents 5%
    progress_bar = '\r[{0}] {1}%'.format('#'*(progress/5) + '-' * (20-(progress/5)), progress)
    return progress_bar

#new goal: only show printed countdown when the % actually increments
def waitafterpswd(total_time):
    countdown = total_time
    current_percent = 0
    while countdown > 0:
        progress = int((((total_time - countdown)/float(total_time)*100)))
        if progress >= current_percent:
            print update_progress(progress)
            current_percent = progress + 1
        #print countdown
        countdown -= 1
        time.sleep(1)
    print "[####################] 100%"
    print "\n\n\nLoading.......\n\n\n"
    time.sleep(15)

def errormessage(duration):
    stop = time.time()+duration
    while time.time() < stop:
        # the below print statement is actually the regex for email verification
        print '(?:(?:/r/n)?[ /t]ERROR)*(?:(?:(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|"(?:[^/"/r//]|//.|(?:(?:/r/n)?[',
        print '/t]))*"(?:(?:/r/n)?[/t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;ERROR://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|"(?:[^/',
        print '"/r//]|//.|(?:(?:/r/n)?[ /t]))*"(?:(?:/r/n)?[ /t])*))*@(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://ERROR"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt',
        print ';@,;://"ERROR./[/]]))|/[([^/[/]/r//ERROR]|//.)*/](?:(?:/r/n)?[ /t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:ERROR/r/n)?[/t])+|/Z|(?=[/["(',
        print ')&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/nERROR)?[ /t])*))*|(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;',
        print '://"./[/]]))|"(?:[^/"/r//]|//.|(?:(?:/r/n)?[ /t]))*"(?:(?:/r/n)?[ /t])*)*/&lt;(?:(?:/r/n)?[ /t])*(?:@(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?',
        print '[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/n)?[ /t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/]/000-/031]+(?:(?:(',
        print '?:/r/n)?[ ERROR/t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](ERROR?:(?:/r/n)?[ /t])*)ERROR)*(?:,@(?:(?:/r/n)?[/t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/03',
        print '1]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/[ERROR()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/n)?[ /t])*)(?:/.(?:(?ERROR:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/]',
        print '/000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/n)?[ /t])*))*)*:(?:(?:/r/n)?[ /t])*)?(?:[^()&lt;&gt;@',
        print ',;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|"(?:[^/"/r//]|//.|(?:(?:/r/n)?[ /t]))*"(?:(?:/r/n)?[ /t])*)(?:/.(?:(?:/r',
        print '/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|"(?:[^/"/r//]|//.|(?:(?ERROR:/r/n)?[ /t]))*"(?:(?:',
        print '/r/n)?[ /t])*))*@(?:ERROR(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /ERROR000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*',
        print '/](?:(?:/rERROR/n)?[ /t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(ERROR?:(?:(?:/r/n)?[/t]ERROR+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r',
        print '//]|//.)*/](?:(?:/r/n)?[ /t])*))*/&gt;(?:(?:/r/n)?[ /t])*)|(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]',
        print '))|"(?:[^/"/r//]|//.|(?:(?:/r/n)?[ /t]))*"(?:(?:/ERRORr/n)?[ /t])*)*:(?:(?:/r/n)?[/t])*(?:(?:(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(',
        print 'ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR',
        print 'ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR',
        print 'ERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERRORERROR',
        print '?=[/["()&lt;&gt;@,;://"./[/]]))|"(?:[^ERROR/"/r//]|//.|(?:(?:/r/n)?[/t]))*"(?:(?:/r/n)?[/t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?',
        print ':(?:(?:ERROR/r/n)?[/t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|"(?:[^/"/r//]|//.|(?:(?:/r/n)?[ /t]))*"(?:(?:/r/n)?[ /t])*))*@(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,',
        print ';://"./[/]/000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?ERROR:/r/n)?[ /t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&',
        print 'lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,ERROR;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/n)?[ /t])*))*|(?:[^()&lt;&gt;@,;:',
        print '//"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|"(?:[^/"/r//]|//.|(?:(?:/r/n)?[ /t]))*"(?:(?:/r/n)?[ /t])*)*/&lt;(?:(?:/r/n',
        print ')?[ /t])*(?:@(?:[^()&lt;ERROR&gt;@,;://"./[/] /000-ERROR/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/n)?[ /t])*)(',
        print '?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/]ERROR(?:(?:/r/n)',
        print '?[ /t]ERROR*))*(?:,@(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[/t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/]',
        print '(?:(?:/r/n)?[ /t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/ERRORn)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r/',
        print '/]|//.)*/](?:(?:/r/n)?[ /t])*))*)*:(?:(?:/r/n)?[ /t])*)?(?:[^()&lt;&gt;ERROR@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|',
        print '"(?:[^/"/r//]|//.|(?:(?:ERROR/r/n)?[ /t]))*"(?:(?ERROR:/r/n)?[ /t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/]/000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["',
        print '()&lt;&gt;@,;://"./[/]]))|"(?:[^/"/r//]|//.|(?:(?:/r/n)?[ /t]))*"(?:(?:/r/n)?[ /t])*))*@(?:(?:/r/n)?[ /tERROR])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?',
        print ':/r/n)?ERROR[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/n)?[ /t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031',
        print ' ]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/n)?[ /t])*))*/&gt;(?:(?:/r/n)?[ /t])*)(?:,/s*(?:(?:[^()&lt;&gt',
        print ' ;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"ERROR./[/]]))|"(?:[^/"/r//]|//.|(?:(?:/r/n)?[ /t]))*"ERROR(?:(?:/r/n)?[ /t])*)(?:/.(?:(?:',
        print ' /r/n)?[ /t])*(?:[^()&lt;&gt;@,ERROR;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./ERROR[/]]))|"(?:[^/"/r//]|//.|(?:(?:/r/n)?[ /t]))*"(?:(',
        print ' ?:/r/n)?[ /t])*))*@(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.',
        print ' )*/](?:(ERROR?:/r/n)?[ /t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/',
        print ' ]/r//]|//.)*/](?:ERROR(?:/r/n)?[ /t])*))*|(?:[^()&lt;&gt;ERROR@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|"(?:[^/"/r//]|//.|(',
        print ' ?:(?:/r/n)?[ /t]))*"(?:(?:/r/n)?[ /t])*)*/&lt;(?:(?:/r/n)?[ /t])*(?:@(?:[^(ERROR)&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=ERROR[/["()&lt;&gt;@,;',
        print ' ://"./[/]]))|/[([^/[/]/r//]|//.ERROR)*/](?:(?:/r/n)?[/t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[/t])+|/Z|(?=[/["()&lt',
        print ' ;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/n)?ERROR[ /t])*))*(?:,@(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/]/000-/031]+(?:(?:(?:/rERROR/n)?[ /t])+|/Z|(',
        print ' ?=[/["()ERROR&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/n)?[ /t])*)(?:/.(?:(?:/r/n)?[ /t])*ERROR(?:[^()&lt;&gt;@,;:ERROR//"./[/] /000-/031]+(?:(?:(?:/r/n)?[ ',
        print ' /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/n)?[ /t])*))*)*:(?:(?:/r/n)?[ /t])*)?(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?',
        print ' :(?:/r/n)?[ /t])+|/Z|(ERROR?=[/["()&lt;&gt;@,;://"./[/]]))|"(?:[^/"/r//]|//.|(?:(ERROR?:/r/n)?[ /t]))*"(?:(?:/r/n)?[ /t])*)(?:/.(?:(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,',
        print ' ;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(ERROR?=[/["()&lt;&gt;@,;://"./[/]]))|"(?:[^/"/r//]|//.|(?:(?:/r/n)?[ /t]))*"(?:(?:/r/n)?ERROR[/t])*))*@(?:(?:/r/n)?',
        print ' [ /t])*(?:[^()ERROR&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[(ERROR[^/[/]/r//]|//.)*/](?:(?:/r/n)?[ /t])*)(?:/.(?',
        print ' :(?:/r/n)?[ /t])*(?:[^()&lt;&gt;@,;://"./[/] /000-/031]+(?:(?:(?:/r/n)?[ /t])+|/Z|(?=[/["()&lt;&gt;@,;://"./[/]]))|/[([^/[/]/r//]|//.)*/](?:(?:/r/n)?[ /t]',
        print ' )*))*/&gt;(?:(?:/r/n)ERROR?[ /t])*))*)?;/s*)',

def truepassword(pswd):
    if pswd == "hi":
        return "\n\nDUN DUN DUNNN"
    else:
        return "\n\nPassword invalid"

# This will be implemented later to read from a google document
# with information about the current condition of the ship
def captainslog():
    print "hi"

while True:
    input = raw_input("\nc:/drchickengeorge/terminal_1/",)
    if input == "password":
        pswd = raw_input("c:/drchickengeorge/terminal_1/password/",)
        if pswd == "barbara":
            errormessage(20)
            print "\n\nREBOOTING........\n"
            waitafterpswd(280)
        else:
            waitafterpswd(10) #300 is 5 minutes in seconds
        print truepassword(pswd)
    else:
        print "$ ld: unrecognized option '" + input + "'"
