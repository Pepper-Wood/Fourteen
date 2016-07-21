import time
import random
import winsound

WAITINGFLAG = 3
ERRORFLAG = 1
LOADINGFLAG = 1
#barbara and roulette cannot be spun for
ROULETTE_PASSWORDS = ["19CY0A95-01", "61CY0A31-02", "51CY0A88-03", "44CY0A63-04", "94CY0A59-05", "751T3M98-01", "641T3M37-02", "711T3M78-03", "151T3M21-04", "441T3M71-05", "971T3M87-06", "351T3M69-07", "421T3M99-08", "121T3M57-09", "731T3M09-10", "671T3M53-11", "601T3M54-12", "321T3M18-13", "701T3M25-14", "441T3M19-15", "481T3M85-16", "871T3M51-17", "511T3M31-18", "051T3M69-19", "381T3M78-20", "571T3M26-21", "761T3M04-22", "051T3M69-23", "991T3M06-24", "751T3M47-25", "391T3M32-26", "751T3M89-27", "671T3M04-28", "011T3M45-29", "651T3M69-30", "731T3M28-31", "431T3M88-32", "521T3M93-33", "091T3M06-34", "341T3M39-35", "681T3M61-36", "081T3M72-37"]

#----------------------------------------------------------------------------------------
def update_progress(progress):
    # bar where each # represents 10%
    #print '\r[{0}] {1}%'.format('#'*(progress/10) + '-' * (10-(progress/10)), progress)
    # bar where each # represents 5%
    progress_bar = '\r[{0}] {1}%'.format('#'*(progress/5) + '-' * (20-(progress/5)), progress)
    return progress_bar

#----------------------------------------------------------------------------------------
def transcribescript(docname, pause):
    fulldocname = 'Transcriptions/' + docname + '.txt'
    document = open(fulldocname, 'r')
        for line in document:
            print line,
            time.sleep(pause)

#----------------------------------------------------------------------------------------
def transcription(docCode, langCode, pause):
    if docCode == "12345" and langCode == "ENGLISH":
        transcribescript('testpoem')
    elif docCode == "67890": # barbara document has all four languages written into it
        print "$ ld: ERROR: multiple languages detected in document-'" + docCode + "'"
    else:
        print "$ ld: invalid match document-'" + docCode + "' and language-'" + langCode + "'"

#----------------------------------------------------------------------------------------
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
    print "\nLoading.......\n"
    time.sleep(LOADINGFLAG)

#----------------------------------------------------------------------------------------
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

#----------------------------------------------------------------------------------------
# This will be implemented later to read from a google document
# with information about the current condition of the ship
def gmfunc(gmflag):
    # The returned value alters at what point the status of the ship is.
    if gmflag == "asdf":
        return 2

#----------------------------------------------------------------------------------------
def roulettepassword():
    print "$ ld: determining match...... "
    waitafterpswd(WAITINGFLAG)
    print "$ ls: Randomly selecting password. Loading...."
    return random.choice(PASSWORDS.keys())

#----------------------------------------------------------------------------------------
def passwordresult(pswd,TERMINALNUMBER):
    if pswd == "roulette":
        print "$ ls: Randomly selecting password. Loading...."
        pswd = random.choice(ROULETTE_PASSWORDS)
        waitafterpswd(WAITINGFLAG)
        print "c:/users/drchickengeorge/terminal_" + str(TERMINALNUMBER) + "/password/" + pswd
        
    print "$ ld: determining match...... "
    waitafterpswd(WAITINGFLAG)

    if pswd == "barbara":
        winsound.PlaySound('Sounds/drcg.wav',winsound.SND_FILENAME) # play indicating jingle
        errormessage(ERRORFLAG)
        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    elif pswd == "19CY0A95-01" or pswd == "61CY0A31-02" or pswd == "51CY0A88-03" or pswd == "44CY0A63-04" or pswd == "94CY0A59-05":
        winsound.PlaySound('Sounds/cyoa.wav',winsound.SND_FILENAME) # play indicating jingle
        print "$ Match found for " + pswd + ". Please see GM"
    elif pswd in ROULETTE_PASSWORDS:
        winsound.PlaySound('Sounds/roulette.wav',winsound.SND_FILENAME) # play indicating jingle
        print "$ Match found for " + pswd + ". Please see GM"
    else:
        winsound.PlaySound('Sounds/wrong.wav',winsound.SND_FILENAME) # play indicating jingle
        print "$ ld: invalid password-'" + pswd + "'"
