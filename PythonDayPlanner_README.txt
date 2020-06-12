******************************************************************************
		              2020 DAYPLANNER
******************************************************************************

Author -  Sebastian Deluca

******************************************************************************

CREATED ON: 06/12/2020

******************************************************************************

Version - V 1.2

******************************************************************************

Programming Language - Python 3.7.x

******************************************************************************

Problem Description – Create a program that successfully utilizes either
	recursion or an external module, and can read and write to files.

******************************************************************************

Program Assumptions -
Keyboard Required
Python 3.x.x Installed

******************************************************************************

			-- FEATURES --
 - Compulsive Help Menu 
	A help menu that helps the user navigate through the program,
	and also allows them to get help for only what they want help for.

- A visible Calendar
	Using the PrettyTable module, the program displays a 2020 
	Calendar

- Saves & writes all Custom Events
	Uses the read/write capabilities of Python to save and read
	any entered events.

- Daily Reminders
	Tells the user what events they have planned for the day when
	it is that day.

- Easier-than-ever to use Menu
	Input-dependent menus are now easier to use, as they accept
	more inputs than any other program I've written before

- Dictionaries (and Lists inside)
	Dictionaries hold lists that are the events for that day.
	(This is how I including 2D Arrays as well)

- Recursion
	Recursion was the simplest way to achieve a repeating
	calendar.

- Exception Handling
	Utilizes exception handling to prevent the user from crashing
	the program

- Predictive Event Creation
	When creating a work event, it asks the user if they have any
	other days at work where it begins at the same time.


******************************************************************************

Restrictions –
    Does not correct user's timestamp should they enter a single-digit minute
    time. (i.e entering '11:0' will save as 11:0)

    Cannot remove saved events from within the program, but it is very easy
    to remove from the text-file, which in turn, removes them from the program.

******************************************************************************
--- NOTE: 
	This was created in a short time-frame. Had I enough time, I
	would have further improved the program, added more features,
	and fixed any bugs within the program.

Known Errors --
   Putting an invalid date using the 'WORK SYSTEM' i.e (April 31st,2020) will
   cause a crash. [This date is invalid because April only has 30 days.]

******************************************************************************

Implementation Details / How to build the program - For the user to run
                                                    the program they must
    1. have Python 3.x.x installed or they can find it here
        (https://www.python.org/downloads/)

    2. After being installed the user must open Python IDLE.

    3. After that the user must go to File > Open >
       (select PythonDayPlanner.py ) to open.

    4. Then the user must Hit f5 on their keyboard or Run > Run Module.

******************************************************************************
~~ Additional Files ~~
PythonDayPlanner_MyEvents.txt
******************************************************************************