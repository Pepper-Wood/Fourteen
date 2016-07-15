# Starting colors for terminal:
# Green font: rgb(55,161,64)
# Background: rgb(0,0,0)

#It'd be great to have an online doc that python continually reads to assess
# the damage to the ship or to the crew. Maybe hints at things too.

import time
import fourteen

TERMINALNUMBER = 2
GMFLAG = 1

def titlegenerator(TERMINALNUMBER):
    print "\t\t\t  _______     _____              _____ ____  _   _ _______ _____   ____  _        _____        _   _ ______ _        "
    print "\t\t\t |__   __|   |  __ \            / ____/ __ \| \ | |__   __|  __ \ / __ \| |      |  __ \ /\   | \ | |  ____| |     _ "
    print "\t\t\t    | |______| |__) |_____  __ | |   | |  | |  \| |  | |  | |__) | |  | | |      | |__) /  \  |  \| | |__  | |    (_)"
    print "\t\t\t    | |______|  _  // _ \ \/ / | |   | |  | | . ` |  | |  |  _  /| |  | | |      |  ___/ /\ \ | . ` |  __| | |       "
    print "\t\t\t    | |      | | \ \  __/>  <  | |___| |__| | |\  |  | |  | | \ \| |__| | |____  | |  / ____ \| |\  | |____| |____ _ "
    print "\t\t\t    |_|      |_|  \_\___/_/\_\  \_____\____/|_| \_|  |_|  |_|  \_\ ____/|______| |_| /_/    \_\_| \_|______|______(_)"
    print "\t\t\t______________________________________________________________________________________________________________________"
    if TERMINALNUMBER == 0:
        print "\t\t\t                          _______ ______ _____  __  __ _____ _   _          _      "
        print "\t\t\t                         |__   __|  ____|  __ \|  \/  |_   _| \ | |   /\   | |     "
        print "\t\t\t                            | |  | |__  | |__) | \  / | | | |  \| |  /  \  | |     "
        print "\t\t\t                            | |  |  __| |  _  /| |\/| | | | | . ` | / /\ \ | |     "
        print "\t\t\t                            | |  | |____| | \ \| |  | |_| |_| |\  |/ ____ \| |____ "
        print "\t\t\t                            |_|  |______|_|  \_\_|  |_|_____|_| \_/_/    \_\______|"
    elif TERMINALNUMBER == 1:
        print "\t\t\t                          _______ ______ _____  __  __ _____ _   _          _        __ "
        print "\t\t\t                         |__   __|  ____|  __ \|  \/  |_   _| \ | |   /\   | |      /_ |"
        print "\t\t\t                            | |  | |__  | |__) | \  / | | | |  \| |  /  \  | |       | |"
        print "\t\t\t                            | |  |  __| |  _  /| |\/| | | | | . ` | / /\ \ | |       | |"
        print "\t\t\t                            | |  | |____| | \ \| |  | |_| |_| |\  |/ ____ \| |____   | |"
        print "\t\t\t                            |_|  |______|_|  \_\_|  |_|_____|_| \_/_/    \_\______|  |_|"
    elif TERMINALNUMBER == 2:        
        print "\t\t\t                          _______ ______ _____  __  __ _____ _   _          _        ___  "
        print "\t\t\t                         |__   __|  ____|  __ \|  \/  |_   _| \ | |   /\   | |      |__ \ "
        print "\t\t\t                            | |  | |__  | |__) | \  / | | | |  \| |  /  \  | |         ) |"
        print "\t\t\t                            | |  |  __| |  _  /| |\/| | | | | . ` | / /\ \ | |        / / "
        print "\t\t\t                            | |  | |____| | \ \| |  | |_| |_| |\  |/ ____ \| |____   / /_ "
        print "\t\t\t                            |_|  |______|_|  \_\_|  |_|_____|_| \_/_/    \_\______| |____|"
                                                                 
    elif TERMINALNUMBER == 3:                                                             
        print "\t\t\t                          _______ ______ _____  __  __ _____ _   _          _        ____  "
        print "\t\t\t                         |__   __|  ____|  __ \|  \/  |_   _| \ | |   /\   | |      |___ \ "
        print "\t\t\t                            | |  | |__  | |__) | \  / | | | |  \| |  /  \  | |        __) |"
        print "\t\t\t                            | |  |  __| |  _  /| |\/| | | | | . ` | / /\ \ | |       |__ < "
        print "\t\t\t                            | |  | |____| | \ \| |  | |_| |_| |\  |/ ____ \| |____   ___) |"
        print "\t\t\t                            |_|  |______|_|  \_\_|  |_|_____|_| \_/_/    \_\______| |____/ "


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
    print "\nLoading.......\n"
    time.sleep(15)


print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
print "$ ld: Booting up..... type in 'listoptions' to begin"
titlegenerator(TERMINALNUMBER)
while True:
    input = raw_input("\nc:/users/drchickengeorge/terminal_" + str(TERMINALNUMBER) + "/",).lower()


    if input == "password":
        pswd = raw_input("c:/users/drchickengeorge/terminal_" + str(TERMINALNUMBER) + "/password/",).lower()
        if pswd == "roulette":
            pswd = fourteen.roulettepassword()
            print "c:/users/drchickengeorge/terminal_" + str(TERMINALNUMBER) + "/password/" + pswd
        print "$ ld: determining match...... "
        waitafterpswd(10) #300 is 5 minutes in seconds
        print fourteen.truepassword(pswd)


    elif input == "translate":
        docCode = raw_input("c:/users/drchickengeorge/terminal_" + str(TERMINALNUMBER) + "/translate/enterDocumentCode/",).lower()
        langCode = raw_input("c:/users/drchickengeorge/terminal_" + str(TERMINALNUMBER) + "/translate/" + docCode + "/enterLanguageCode/",).lower()      
        print "c:/users/drchickengeorge/terminal_" + str(TERMINALNUMBER) + "/translate/" + docCode + "/" + langCode + "/run.exe"
        print "$ ld: determining match...... "
        waitafterpswd(10) #wait 1 minutes for transcription or testing if exists
        # the function will transcribe the translation of the cryptotext super slowly
        fourteen.transcription(docCode,langCode,3) # this can be in the separate python module too


    elif input == "listoptions":
        print "$ ld: listoptions - current options:"
        print "\tpassword\n\ttranslate"
        option = ""
        while option != "1":
            option = raw_input("$ ld: type option to learn more (press 1 to exit): ").lower()
            if option == "password":
                print "$ \tPASSWORD = enter a password into the system to enable/disable components of the ship"
            elif option == "translate":
                print "$ \tTRANSLATE = enter document code and language code to translate a document to the English Alphabet"
            elif option == "1":
                print "$ EXITING....."
            else:
                print "$ ld: unrecognized option '" + option + "'"


    elif input == "gm":
        gminput = raw_input("c:/users/drchickengeorge/terminal_" + str(TERMINALNUMBER) + "/gm/")
        gminput = gminput.lower()
        GMFLAG = fourteen.gmfunc(gminput)
        print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
        print "$ ld: Booting up..... type in 'listoptions' to begin"
        titlegenerator(TERMINALNUMBER)


    else:
        print "$ ld: unrecognized option '" + input + "'"
