#N: Sebastian Deluca
#D: 06/12/20
#FN: PythonDayPlanner.py
#DESC.: Create a day-planner that allows the user to add an exceptionally customizable experience.
#   + unique features to make creating events much easier


from PrettyTable.prettytable import PrettyTable
import datetime

from urllib.request import urlopen

link = 'https://www.qppstudio.net/publicholidays2020/canada.htm'


eventFile = 'PythonDayPlanner_MyEvents.txt'
savedEvents = {} # Empty list for Added Events

def wS(times):
    for i in range(times):
        print('')

def remindUser(events): # A function that tells the user what events they have for the day
    todaysEvents = []
    date = str(datetime.datetime.today())  # Create a variable for todays date
    month = monthScreen(date)  # Get the month from the datetime function
    day = dayScreen(date).strip('th')  # Get the day from the datetime function
    day = day.strip('st') # Make sure the date is just the number
    day = day.strip('rd') # Make sure the date is just the number

    for days,event in events.items():

        if days == (month + ' ' + day):
            todaysEvents.append(event)
        else:
            pass
    if len(todaysEvents) != 0:
        print('Today you have ', end = ' ')
        for today in todaysEvents:
            if today == todaysEvents[-1]:
                print(today)
            else:
                print(today +', ', end = '')
    else:
        pass

def yearScreen(yearDate):  # A function that converts the YYYY into a year
    yearDate = (yearDate[:4])  # Turn the user date into it's own year
    return yearDate  # Return this value to the function

def addToDay(months): # Adds the events to the days
    global savedEvents
    for date, savedEvent in savedEvents.items():

        monDay = date.split()
        month = monDay[0].lower()
        day = int(monDay[1])
        #DET. THE MONTH
        if month == 'january':
            dictionary = months[0]
        elif month == 'february':
            dictionary = months[1]
        elif month == 'march':
            dictionary = months[2]
        elif month == 'april':
            dictionary = months[3]
        elif month == 'may':
            dictionary = months[4]
        elif month == 'june':
            dictionary = months[5]
        elif month == 'july':
            dictionary = months[6]
        elif month == 'august':
            dictionary = months[7]
        elif month == 'september':
            dictionary = months[8]
        elif month == 'october':
            dictionary = months[9]
        elif month == 'november':
            dictionary = months[10]
        elif month == 'december':
            dictionary = months[11]
        if dictionary[day] == None:
            dictionary[day] = savedEvent

        else:
            dictionary[day].append(savedEvent)

def saveEvents(eventDay,eventTime): # Appends
    global eventFile, savedEvents
    saveFile = open(eventFile, 'a')
    saveFile.write('DATE:' + eventDay + '\n')
    saveFile.write('EVENT:' + eventTime + '\n')
    if eventDay not in savedEvents:
        savedEvents[eventDay] = (eventTime)
    else:
        savedEvents[eventDay] += ', ' + (eventTime)
    saveFile.close()

def readEvents(): # Reads the .txt file with events
    global eventFile
    readFile = open(eventFile, 'r')
    for line in readFile:
        if line[:5] == 'DATE:':
            date = line[5:].strip('\n')
        elif line[:6] == 'EVENT:':
            if date not in savedEvents:
                savedEvents[date] = (line[6:].strip('\n'))
            else:
                savedEvents[date] += ', ' + (line[6:].strip('\n'))
    readFile.close()

def monthScreen(userDate):  # A function that converts the MM into a month
    userDate = (userDate[5:7])  # Slice all other characters in the string, leaving the day
    if userDate == '01':  # If the user entered January
        userDate = 'January'  # Make the month January
    elif userDate == '02':  # If the user enters February
        userDate = 'February'  # Make the month February
    elif userDate == '03':  # If the user entered March
        userDate = 'March'  # Make the month March
    elif userDate == '04':  # If the user entered April
        userDate = 'April'  # Make the month April
    elif userDate == '05':  # If the user entered May
        userDate = 'May'  # Make the month May
    elif userDate == '06':  # If the user enters June
        userDate = 'June'  # Make the month June
    elif userDate == '07':  # If the user enters July
        userDate = 'July'  # Make the month July
    elif userDate == '08':  # If the user enters August
        userDate = 'August'  # Make the month August
    elif userDate == '09':  # If the user enters September
        userDate = 'September'  # Make the month September
    elif userDate == '10':  # If the user enters October
        userDate = 'October'  # Make the month October
    elif userDate == '11':  # If the user enters November
        userDate = 'November'  # Make the month November
    elif userDate == '12':  # If the user enters December
        userDate = 'December'  # Make the month December
    return userDate  # Return this value to the program

def dayScreen(userDate):  # A function that converts DD into a day of the month
    userDate = (userDate[8:10])  # Turn the users date into a month value
    dateCheck = (userDate[0:1])  # Create a variable that checks the date
    if dateCheck == '0':  # If the first number is 0
        dateCheck = (userDate[1:])  # Create a 2nd variable that is just the second digit
        if userDate[:1] == '0':  # If the first digit of the day is 0
            userDate = (userDate[1:])  # Turn the day into its own date
        if dateCheck == '1':  # If the last digit is 1
            userDate += 'st'  # Add the suffix st to the date
        elif dateCheck == '2':  # If the last digit is 2
            userDate += 'nd'  # Add the suffix nd to the date
        elif dateCheck == '3':  # If the last digit is 3
            userDate += 'rd'  # Add the suffix rd to the date
        else:  # If the last digit is 0, or 4-10
            userDate += 'th'  # Add the suffix th to the date
        return userDate  # Return the day to the program

    else:  # if the first number isnt 0
        dateCheck = (userDate[0:2])  # Consider the first digit
        if dateCheck == '11':  # If the last digit is 1
            userDate += 'th'  # Add the suffix st to the date
        elif dateCheck == '12':  # If the last digit is 2
            userDate += 'th'  # Add the suffix nd to the date
        elif dateCheck == '13':  # If the last digit is 3
            userDate += 'th'  # Add the suffix rd to the date
        if dateCheck == '21':  # If the last digit is 1
            userDate += 'st'  # Add the suffix st to the date
        elif dateCheck == '22':  # If the last digit is 2
            userDate += 'nd'  # Add the suffix nd to the date
        elif dateCheck == '23':  # If the last digit is 3
            userDate += 'rd'  # Add the suffix rd to the date
        elif dateCheck == '31':  # If the last digit is 3
            userDate += 'st'  # Add the suffix rd to the date
        else:  # If the last digit is 0, or 4-10
            userDate += 'th'  # Add the suffix th to the date
        return userDate  # Return the day to the program

def dateScreen(day, month, year):  # A function that converts the DDMMYYYY into a day
    convertedDate = 'the ' + day + ' of ' + month + ', ' + year  # Create a final date for the user
    return convertedDate  # Return this string to the program

def eventCreator(eType, time): # A function that determines the proper timing of the event
    hour = time[0:2]
    min = time[3:5]

    ###TIME DETERMINING
    if hour == '12':
        newTime = ('12:' + min + ' PM')
    elif hour == '13':
        newTime = ('1:' + min+ ' PM' )
    elif hour == '14':
        newTime = ('2:' + min + ' PM')
    elif hour == '15':
        newTime = ('3:' + min + ' PM')
    elif hour == '16':
        newTime = ('4:' + min + ' PM')
    elif hour == '17':
        newTime = ('5:' + min + ' PM')
    elif hour == '18':
        newTime = ('6:' + min + ' PM')
    elif hour == '19':
        newTime = ('7:' + min + ' PM')
    elif hour == '20':
        newTime = ('8:' + min + ' PM')
    elif hour == '21':
        newTime = ('9:' + min + ' PM')
    elif hour == '22':
        newTime = ('10:' + min + ' PM')
    elif hour == '23':
        newTime = ('11:' + min + ' PM')
    elif hour == '24':
        newTime = ('12:' + min + ' AM')
    else:
        if hour[0] == '0': # Removing 0 from beginning of timestamp
            newTime = (hour[1:] + ':' + min + ' AM')
        else:
            newTime = (hour + ':' + min + ' AM')

    if eType == 'W': # Work is the event
        event = 'Work at ' + newTime
    else:
        event = (eType) + ' at ' + newTime
    print(event)
    return event

def mainMenu(): # Display a Main Menu to the User
    date = str(datetime.datetime.today())  # Create a variable for todays date
    month = monthScreen(date)  # Get the month from the datetime function
    year = yearScreen(date)  # Get the year from the datetime function
    day = dayScreen(date)  # Get the day from the datetime function
    date = dateScreen(day, month, year)  # Create a date for the user
    wS(10)
    print((' O0o o 0 oO | 2020 Day Planner | Oo 0 o o0O').center(150))
    wS(1)
    print(('  Today is ' + date).center(150))  # Show todays date to the user
    wS(1)

    wS(1)
    print(('Enter H for Help').center(150))
    print(('Enter Q to Quit').center(150))
    print(('Press any other Key to View Calendar').center(150))
    userInput = input() # Get user input
    if userInput == 'H' or userInput =='h':
        helpMenu()
    elif userInput == 'Q' or userInput == 'q':
        exit()
    else:
        readEvents()

        genCalendar()

def genCalendar(): # Generates a calendar to the user
    global savedEvents
    #WEEK LISTS [For Display]
    week1 = [1,2,3,4,5,6,7]
    week2 =[8,9,10,11,12,13,14]
    week3 = [15,16,17,18,19,20,21]
    week4 = [22,23,24,25,26,27,28]
    oddWeek5 = [29,30,31]
    evenWeek5 = [29,30]

    #MONTHS W/ HOLIDAYS

    january = {1:['New Years Day'],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[],
               14:[],15:[],16:[],17:[],18:[],19:[],20:[],21:[],22:[],23:[],24:[],25:[],
               26:[],27:[],28:[],29:[],30:[],31:[]}
    february = {1:[], 2:['Groundhog Day'], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[],
               11:[], 12:[], 13:[],14:['Valentine\'s Day'], 15:[], 16:[], 17:['Family Day'], 18:[], 19:[], 20:[], 21:[], 22:[],
               23:[], 24:[], 25:[],26:[], 27:[], 28:[], 29:[]}
    march = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:['Daylight Savings Begins'], 9:[], 10:[],
               11:[], 12:[], 13:[],14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[],
               23:[], 24:[], 25:[],26:[], 27:[], 28:[], 29:[], 30:[], 31:[]}
    april = {1:['April Fools Day'], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:['Vimy Ridge Day'], 10:['Good Friday'],11:[], 12:[], 13:[],
               14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[],23:[], 24:[], 25:[],
               26:[], 27:[], 28:[], 29:[], 30:[]}
    may = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:['Mother\'s Day'], 11:[], 12:['Easter Sunday'], 13:['Easter Monday'],
             14:[], 15:[], 16:[], 17:[], 18:['Victoria Day'], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[], 25:[],
             26:[], 27:[], 28:[], 29:[], 30:[], 31:[]}
    june = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[],
             14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:['Father\'s Day'], 22:[], 23:[], 24:[], 25:[],
             26:[], 27:[], 28:[], 29:[], 30:[]}
    july = {1:['Canada Day'], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[],
             14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[], 25:[],
             26:[], 27:[], 28:[], 29:[], 30:[], 31:[]}
    august = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[],
             14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[], 25:[],
             26:[], 27:[], 28:[], 29:[], 30:[], 31:[]}
    september = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:['Labour Day'], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[],
             14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[], 25:[],
             26:[], 27:[], 28:[], 29:[], 30:[]}
    october = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:['Thanksgiving Day'], 13:[],
             14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[], 25:[],
             26:[], 27:[], 28:[], 29:[], 30:[], 31:['Halloween']}
    november = {1:['Daylight Savings Ends'], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:['Remembrance Day'], 12:[], 13:[],
             14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[], 25:[],
             26:[], 27:[], 28:[], 29:[], 30:[]}
    december = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[],
             14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:['Christmas Eve'], 25:['Christmas Day'],
             26:['Boxing Day'], 27:[], 28:[], 29:[], 30:[], 31:['New Year\'s Eve']}
    months = [january,february,march,april,may,june,july,august,september,october,november,december]
    addToDay(months)
    ###CREATING MONTH CALENDAR
    monthCalender = PrettyTable()
    monthCalender.field_names = ['Month','Week 1', 'Week 2', 'Week 3', 'Week 4','Week 5']
    monthCalender.add_row(['January', week1,week2,week3,week4,oddWeek5])
    monthCalender.add_row(['February', week1,week2,week3,week4,[29]])
    monthCalender.add_row(['March', week1,week2,week3,week4,oddWeek5])
    monthCalender.add_row(['April', week1,week2,week3,week4,evenWeek5])
    monthCalender.add_row(['May', week1,week2,week3,week4,oddWeek5])
    monthCalender.add_row(['June', week1,week2,week3,week4,evenWeek5])
    monthCalender.add_row(['July', week1,week2,week3,week4,oddWeek5])
    monthCalender.add_row(['August', week1,week2,week3,week4,oddWeek5])
    monthCalender.add_row(['September', week1,week2,week3,week4,evenWeek5])
    monthCalender.add_row(['October', week1,week2,week3,week4,oddWeek5])
    monthCalender.add_row(['November', week1,week2,week3,week4,evenWeek5])
    monthCalender.add_row(['December', week1,week2,week3,week4,oddWeek5])
    print(monthCalender) # Display Calendar
    inputLoop = True
    while inputLoop:
        wS(1)
        remindUser(savedEvents)
        print(('Select a Month').center(150))
        print(('NOTE: Enter either Month abbreviation or full name, Either Titlecased or uncapitalized. [e.g \'jan\' = January, & \'Jan\' = January]').center(150))
        print(('You can also enter \'B\' to return to the Main Menu').center(150))
        monthSel = input() # Get user month

        ###SELECTED MONTH IF STATEMENTS
        if monthSel == 'jan' or monthSel == 'Jan' or monthSel == 'january' or monthSel == 'January': # User wants to add an event to January
            wS(1)
            print('Here are your events for January:')
            for day, events in january.items():
                print('January ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders +',', end = ' ')
                wS(1)
            wS(1)
            dayLoop = True # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(150)) # Prompt for input
                try: # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    if day <=31:
                        print(january[day])
                        dayLoop = False
                    else:
                        wS(1)
                        input('Incorrect Day Number [Press Enter]')
                except:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))

                if day <= 31:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ') # Get user input
                    if eventType == 'W' or eventType == 'w': # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop: # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[:2] == '00':
                                eventTime = '01' + eventTime[2:]
                            if eventTime[2] == ':': # Ensure user entered appropriate time
                                if int(eventTime[:2]) <=24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        event = eventCreator('W', eventTime)
                        theDate = 'January ' + str(day)
                        saveEvents(theDate,event)

                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(('Are there any other days you\'re working at that same time? Enter them now.').center(150)) # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ') # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no': # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:

                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'January ' + str(days)
                                        saveEvents(theDate, event)
                                        january[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c': # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ') # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input() # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else: # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'January ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o': # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'January ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'feb' or monthSel == 'Feb' or monthSel == 'Febraury' or monthSel == 'february': # User wants to add an event to February
            wS(1)
            print('Here are your events for February:')
            for day, events in february.items():
                print('February ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders +',', end = ' ')
                wS(1)
            wS(1)
            dayLoop = True # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(150)) # Prompt for input
                try: # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    if day <=29:
                        print(february[day])
                        dayLoop = False
                    else:
                        wS(1)
                        input('Incorrect Day Number [Press Enter]')
                        dayLoop = True
                except ValueError:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))
                if day <= 29:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ') # Get user input
                    if eventType == 'W' or eventType == 'w': # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop: # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[2] == ':': # Ensure user entered appropriate time
                                if int(eventTime[:2]) <=24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator('W', eventTime)
                        theDate = 'February ' + str(day)
                        saveEvents(theDate,event)

                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(('Are there any other days you\'re working at that same time? Enter them now.').center(150)) # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ') # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no': # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:

                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'February ' + str(days)
                                        saveEvents(theDate, event)
                                        february[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c': # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ') # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input() # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else: # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'February ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o': # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'February ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'mar' or monthSel == 'Mar' or monthSel == 'March' or monthSel == 'march': # User wants to add an event to march
            wS(1)
            print('Here are your events for March:')
            for day, events in march.items():
                print('March ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders +',', end = ' ')
                wS(1)
            wS(1)
            dayLoop = True # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(150)) # Prompt for input
                try: # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    print(march[day])
                    dayLoop = False
                except:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))

                if day <= 31:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ') # Get user input
                    if eventType == 'W' or eventType == 'w': # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop: # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[2] == ':': # Ensure user entered appropriate time
                                if int(eventTime[:2]) <=24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator('W', eventTime)
                        theDate = 'March ' + str(day)
                        saveEvents(theDate,event)

                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(('Are there any other days you\'re working at that same time? Enter them now.').center(150)) # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ') # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no': # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:

                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'March ' + str(days)
                                        saveEvents(theDate, event)
                                        march[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c': # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ') # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input() # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else: # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'March ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o': # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'March ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'apr' or monthSel == 'Apr' or monthSel == 'April' or monthSel == 'april': # User wants to add an event to April
            wS(1)
            print('Here are your events for April:')
            for day, events in april.items():
                print('April ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders +',', end = ' ')
                wS(1)
            wS(1)
            dayLoop = True # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(150)) # Prompt for input
                try: # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    print(april[day])
                    dayLoop = False
                except:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))

                if day <= 30:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ') # Get user input
                    if eventType == 'W' or eventType == 'w': # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop: # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[2] == ':': # Ensure user entered appropriate time
                                if int(eventTime[:2]) <=24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator('W', eventTime)
                        theDate = 'April ' + str(day)
                        saveEvents(theDate,event)

                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(('Are there any other days you\'re working at that same time? Enter them now.').center(150)) # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ') # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no': # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:

                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'April ' + str(days)
                                        saveEvents(theDate, event)
                                        april[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c': # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ') # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input() # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else: # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'April ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o': # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'April ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'May' or monthSel == 'may': # User wants to add an event to May
            wS(1)
            print('Here are your events for May:')
            for day, events in may.items():
                print('May ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders +',', end = ' ')
                wS(1)
            wS(1)
            dayLoop = True # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(150)) # Prompt for input
                try: # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    print(may[day])
                    dayLoop = False
                except:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))

                if day <= 31:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ') # Get user input
                    if eventType == 'W' or eventType == 'w': # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop: # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[2] == ':': # Ensure user entered appropriate time
                                if int(eventTime[:2]) <=24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator('W', eventTime)
                        theDate = 'May ' + str(day)
                        saveEvents(theDate,event)
                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(('Are there any other days you\'re working at that same time? Enter them now.').center(150)) # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ') # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no': # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:

                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'May ' + str(days)
                                        saveEvents(theDate, event)
                                        may[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c': # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ') # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input() # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else: # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'May ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o': # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'May ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'jun' or monthSel == 'Jun' or monthSel == 'June' or monthSel == 'june':  # User wants to add an event to June
            wS(1)
            print('Here are your events for June:')
            for day, events in june.items():
                print('June ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders + ',', end=' ')
                wS(1)
            wS(1)
            dayLoop = True  # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(
                    150))  # Prompt for input
                try:  # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    print(june[day])
                    dayLoop = False
                except:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))

                if day <= 30:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ')  # Get user input
                    if eventType == 'W' or eventType == 'w':  # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator('W', eventTime)
                        theDate = 'June ' + str(day)
                        saveEvents(theDate, event)

                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(
                                ('Are there any other days you\'re working at that same time? Enter them now.').center(
                                    150))  # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ')  # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no':  # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:
                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'June ' + str(days)
                                        saveEvents(theDate, event)
                                        june[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c':  # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'June ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o':  # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'June ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'jul' or monthSel == 'Jul' or monthSel == 'July' or monthSel == 'july':  # User wants to add an event to July
            wS(1)
            print('Here are your events for July:')
            for day, events in july.items():
                print('July ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders + ',', end=' ')
                wS(1)
            wS(1)
            dayLoop = True  # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(
                    150))  # Prompt for input
                try:  # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    print(july[day])
                    dayLoop = False
                except:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))

                if day <= 31:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ')  # Get user input
                    if eventType == 'W' or eventType == 'w':  # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator('W', eventTime)
                        theDate = 'July ' + str(day)
                        saveEvents(theDate, event)

                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(
                                ('Are there any other days you\'re working at that same time? Enter them now.').center(
                                    150))  # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ')  # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no':  # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:
                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'July ' + str(days)
                                        saveEvents(theDate, event)
                                        july[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c':  # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'July ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o':  # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'July ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'aug' or monthSel == 'Aug' or monthSel == 'August' or monthSel == 'august':  # User wants to add an event to August
            wS(1)
            print('Here are your events for August:')
            for day, events in august.items():
                print('August ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders + ',', end=' ')
                wS(1)
            wS(1)
            dayLoop = True  # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(
                    150))  # Prompt for input
                try:  # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    print(august[day])
                    dayLoop = False
                except:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))

                if day <= 31:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ')  # Get user input
                    if eventType == 'W' or eventType == 'w':  # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator('W', eventTime)
                        theDate = 'August ' + str(day)
                        saveEvents(theDate, event)

                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(
                                ('Are there any other days you\'re working at that same time? Enter them now.').center(
                                    150))  # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ')  # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no':  # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:
                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'August ' + str(days)
                                        saveEvents(theDate, event)
                                        august[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c':  # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'August ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o':  # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'August ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'sept' or monthSel == 'Sept' or monthSel == 'September' or monthSel == 'september':  # User wants to add an event to September
            wS(1)
            print('Here are your events for September:')
            for day, events in september.items():
                print('September ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders + ',', end=' ')
                wS(1)
            wS(1)
            dayLoop = True  # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(
                    150))  # Prompt for input
                try:  # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    print(september[day])
                    dayLoop = False
                except:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))

                if day <= 30:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ')  # Get user input
                    if eventType == 'W' or eventType == 'w':  # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator('W', eventTime)
                        theDate = 'September ' + str(day)
                        saveEvents(theDate, event)

                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(
                                ('Are there any other days you\'re working at that same time? Enter them now.').center(
                                    150))  # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ')  # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no':  # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:
                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'September ' + str(days)
                                        saveEvents(theDate, event)
                                        september[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c':  # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'September ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o':  # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'September ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'oct' or monthSel == 'Oct' or monthSel == 'October' or monthSel == 'october':  # User wants to add an event to October
            wS(1)
            print('Here are your events for October:')
            for day, events in october.items():
                print('October ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders + ',', end=' ')
                wS(1)
            wS(1)
            dayLoop = True  # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(
                    150))  # Prompt for input
                try:  # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    print(october[day])
                    dayLoop = False
                except:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))

                if day <= 31:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ')  # Get user input
                    if eventType == 'W' or eventType == 'w':  # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator('W', eventTime)
                        theDate = 'October ' + str(day)
                        saveEvents(theDate, event)

                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(
                                ('Are there any other days you\'re working at that same time? Enter them now.').center(
                                    150))  # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ')  # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no':  # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:
                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'October ' + str(days)
                                        saveEvents(theDate, event)
                                        october[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c':  # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'October ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o':  # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'October ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'nov' or monthSel == 'Nov' or monthSel == 'November' or monthSel == 'november':  # User wants to add an event to November
            wS(1)
            print('Here are your events for November:')
            for day, events in november.items():
                print('November ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders + ',', end=' ')
                wS(1)
            wS(1)
            dayLoop = True  # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(
                    150))  # Prompt for input
                try:  # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    print(november[day])
                    dayLoop = False
                except:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))

                if day <= 30:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ')  # Get user input
                    if eventType == 'W' or eventType == 'w':  # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator('W', eventTime)
                        theDate = 'November ' + str(day)
                        saveEvents(theDate, event)

                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(
                                ('Are there any other days you\'re working at that same time? Enter them now.').center(
                                    150))  # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ')  # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no':  # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:
                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'November ' + str(days)
                                        saveEvents(theDate, event)
                                        november[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c':  # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'November ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o':  # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'November ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'dec' or monthSel == 'Dec' or monthSel == 'December' or monthSel == 'december':  # User wants to add an event to December
            wS(1)
            print('Here are your events for December:')
            for day, events in december.items():
                print('December ' + str(day) + ': ')
                for reminders in events:
                    if reminders == events[-1]:
                        print(reminders)
                    else:
                        print(reminders + ',', end=' ')
                wS(1)
            wS(1)
            dayLoop = True  # Activate input loop
            while dayLoop:
                print(('Which day would you like to add an event to? [Enter \'B\' to go Back.]').center(
                    150))  # Prompt for input
                try:  # Exception Handling
                    dayNum = (input())
                    day = int(dayNum)
                    print(december[day])
                    dayLoop = False
                except:
                    if dayNum == 'B' or dayNum == 'b':
                        dayLoop = False
                        genCalendar()
                        break
                    else:
                        wS(1)
                        print(('Please Enter a Number.').center(150))

                if day <= 31:
                    eventLoop = True
                else:
                    eventLoop = False
                while eventLoop:
                    wS(1)
                    print(('Which Type of Event are you Creating?').center(150))
                    wS(1)
                    print(('Work | Celebration | Other').center(150))
                    eventType = input('W / C / O: ')  # Get user input
                    if eventType == 'W' or eventType == 'w':  # Work
                        eventLoop = False
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is Work? (00:00 Military Time)').center(150))
                            eventTime = input()
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator('W', eventTime)
                        theDate = 'December ' + str(day)
                        saveEvents(theDate, event)

                        newDayLoop = True
                        while newDayLoop:
                            wS(1)
                            print(
                                ('Are there any other days you\'re working at that same time? Enter them now.').center(
                                    150))  # Prompt for user input
                            print(('Please separate them with commas. Enter \'No\' to continue.').center(150))
                            otherDates = input('[12,14,15,...]: ')  # Get user input for other dates of working
                            if otherDates == 'NO' or otherDates == 'No' or otherDates == 'no':  # User does not want to add more
                                newDayLoop = False

                            else:
                                try:
                                    dateList = otherDates.split(',')
                                    datesList = []
                                    print(dateList)
                                    for dates in dateList:
                                        num = int(dates)
                                        datesList.append(num)
                                    for days in datesList:
                                        theDate = 'December ' + str(days)
                                        saveEvents(theDate, event)
                                        december[days] += event
                                    newDayLoop = False
                                except:
                                    wS(1)
                                    print('Something went wrong. Re-enter the dates.')

                    elif eventType == 'C' or eventType == 'c':  # Celebration
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Celebrating? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'December ' + str(day)
                        saveEvents(theDate, event)
                    elif eventType == 'O' or eventType == 'o':  # Other
                        eventLoop = False
                        wS(1)
                        eventName = input('What are you Doing? [Enter Name Here] ')  # Get event name
                        timeLoop = True
                        while timeLoop:  # Force user to enter an appropriate time
                            wS(1)
                            print(('What Time is ' + eventName + '? (00:00 Military Time)').center(150))
                            eventTime = input()  # Get the time of the event
                            if eventTime[2] == ':':  # Ensure user entered appropriate time
                                if int(eventTime[:2]) <= 24 and int(eventTime[3:5]) <= 59:
                                    timeLoop = False
                                else:  # User entered invalid time
                                    wS(1)
                                    print('Not A Valid Time. Please Re-Enter.')
                            else:
                                pass
                        if eventTime[:2] == '00':
                            eventTime = '01' + eventTime[2:]
                        event = eventCreator(eventName, eventTime)
                        theDate = 'December ' + str(day)
                        saveEvents(theDate, event)
                    else:
                        wS(1)
                        print(('Please Enter a Valid Event Option. [W / C / O]').center(150))

        elif monthSel == 'b' or monthSel == 'B' or monthSel == 'Q' or monthSel == 'q' or monthSel == 'back' or monthSel == 'Back': # User wants to return to main menu
            inputLoop = False
            break

        elif monthSel == 'del' or monthSel == 'Del' or monthSel == 'Delete' or monthSel == 'delete' or monthSel == 'd' or monthSel == 'D': # User wants to delete events
            wS(1)
            print(('To Delete Events, delete them from the Deluca_CA_MyEvents.txt file.').center(150))
            input(('-- Press Enter to Continue --').center(150))
        genCalendar()
    mainMenu()

def helpMenu(): # A help menu to help guide the user through the program
    wS(1)
    inputLoop = True
    while inputLoop:
        wS(25)
        print(('THE 2020 DAY PLANNER - HELP').center(150))  # Header
        wS(1)
        print(('\'C\' for Calendar, \'E\' for Event Creating, \'T\' Time Setting, and \'G\' for General Help').center(150)) # Tell user how to navigate
        print(('\'B\' to return to Main Menu').center(150))
        userChoice = input('{]: ') # Get user input
        if userChoice == 'C' or userChoice == 'c': # User wants to view calendar
            wS(1)
            print(('To Navigate the Calendar months, you can enter any of the following options:').center(150))
            print(('JANUARY: \'jan\',\'Jan\',\'January\',\'january\'').center(150))
            print(('FEBRUARY: \'feb\',\'Feb\',\'February\',\'february\'').center(150))
            print(('MARCH: \'mar\',\'Mar\',\'March\',\'march\'').center(150))
            print(('APRIL: \'apr\',\'Apr\',\'April\',\'april\'').center(150))
            print(('MAY: \'may\',\'May\'').center(150))
            print(('JUNE: \'jun\',\'Jun\',\'June\',\'june\'').center(150))
            print(('JULY: \'jul\',\'Jul\',\'July\',\'july\'').center(150))
            print(('AUGUST: \'aug\',\'Aug\',\'August\',\'august\'').center(150))
            print(('SEPTEMBER: \'sept\',\'Sept\',\'September\',\'september\'').center(150))
            print(('OCTOBER: \'oct\',\'Oct\',\'October\',\'october\'').center(150))
            print(('NOVEMBER: \'nov\',\'Nov\',\'November\',\'november\'').center(150))
            print(('DECEMBER: \'dec\',\'Dec\',\'December\',\'december\'').center(150))
            wS(1)
            print(('To navigate through a given month\'s days, just enter the day number. (i.e January 31st, enter \'31\')').center(150))
            input(('Press Enter to Continue').center(150))

        elif userChoice == 'e' or userChoice == 'E': # User wants to see event creating
            wS(1)
            print(('-- WORK --').center(150))
            print(('To create a \'Work Event\', you can Enter \'W\' after selecting a date.').center(150))
            print(('After selecting a time, you can enter other days where you will be working at the same time.').center(150))
            print(('You can enter the days by typing the number of the day. (i.e the 14th would be \'14\'.)').center(150))
            wS(1)
            print(('-- CELEBRATION --').center(150))
            print(('To create a \'Celebration Event\', you can enter \'C\' after selecting the date.').center(150))
            print(('You will be prompted to enter a name for the event and a time after selecting the date.').center(150))
            wS(1)
            print(('-- OTHER --').center(150))
            print(('To create an \'Other Event\', you can enter \'O\' after selecting the date.').center(150))
            print(('Like the \'Celebration Event\', you will be prompted to enter a name and time for the event.').center(150))
            input(('Press Enter to Continue').center(150))

        elif userChoice == 'T' or userChoice == 't': # User wants to view time setting
            wS(1)
            print(('To set a time for any created event, after selecting the date and name, you will be prompted for a time.').center(150))
            print(('You MUST enter the time in Military Time. Here is a guide for Military time.').center(150))
            wS(1)
            print(('01:00 - 1:00AM        13:00 - 1:00PM').center(150))
            print(('02:00 - 2:00AM        14:00 - 2:00PM').center(150))
            print(('03:00 - 3:00AM        15:00 - 3:00PM').center(150))
            print(('04:00 - 4:00AM        16:00 - 4:00PM').center(150))
            print(('05:00 - 5:00AM        17:00 - 5:00PM').center(150))
            print(('06:00 - 6:00AM        18:00 - 6:00PM').center(150))
            print(('07:00 - 7:00AM        19:00 - 7:00PM').center(150))
            print(('08:00 - 8:00AM        20:00 - 8:00PM').center(150))
            print(('09:00 - 9:00AM        21:00 - 9:00PM').center(150))
            print((' 10:00 - 10:00AM       22:00 - 10:00PM').center(150))
            print((' 11:00 - 11:00AM       23:00 - 11:00PM').center(150))
            print((' 12:00 - 12:00PM       24:00 - 12:00AM').center(150))
            print(('NOTE: Entering \'00:xx\' will be corrected to \'01:xx\' automatically.').center(150))
            wS(1)
            print(('For minutes, you can enter any number from 00 to 59. (i.e 1:30PM is \'13:30\')').center(150))
            input(('Press Enter to Continue').center(150))

        elif userChoice == 'g' or userChoice == 'G': # user wants general help
            wS(1)
            print(('2020 DAILY PLANNER - FAQ').center(150))
            wS(1)
            print(('Q: WHERE CAN I FIND MY EVENTS OUTSIDE OF THE PROGRAM?').center(150))
            print(('A: You can find all events you\'ve created in a file').center(150))
            print(('    titled \'Deluca_CA_MyEvents.txt\'. It is easy-to-read.   ').center(150))
            wS(1)
            print(('Q: HOW DO I KNOW WHAT I HAVE PLANNED FOR TODAY?').center(150))
            print(('A: When viewing the Calendar, the program will ').center(150))
            print(('   remind you what you have planned for the day').center(150))
            print(('   under the calendar.                         ').center(150))
            wS(1)
            print(('Q: HOW DO I REMOVE AN EVENT?').center(150))
            print(('A: Though not neccessary, to delete an event ').center(150))
            print(('          you can remove it in the \'Deluca_CA_MyEvents.txt\'').center(150))
            print(('file in the Directory.                 ').center(150))
            wS(1)
            input('Press Enter to Continue')
        elif userChoice == 'B' or userChoice == 'b': # User wants to go back
            inputLoop = False
            mainMenu()

        else:
            input(('Invalid Input - Please Try Again. [Press Enter to Continue]'))

mainMenu()
