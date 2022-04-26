# CMPE131Project
#### Team 4:

Thomas Tran/Dokkam (https://github.com/Dokkam)
An Le/meow2501 (https://github.com/meow2501)
Khanh Chung/khch1997 (https://github.com/khch1997)
Travis Lincoln/TravLincoln (https://github.com/TravLincoln)

#### Main Github repository:

https://github.com/TravLincoln/CMPE131ProjectTeam4



## **Use Case #1 Description**

**Date:** 9/14/2021

**Product Name:** Studious

**Problem Statement:** There Is currently no way to create an account on Studious

**Non-functional Requirements:**

Incorrect email

Email is already Used

Password Strength

Username is taken



**Use Case Name:** Account Creation

Allow User to create an account in Studious



##### Actors

1. User



##### Preconditions

* User requires a unique Email
* User is on the "Sign up/Sign in" page

 

##### Triggers

* User clicks on the "Sign Up" button

 

##### Primary Sequence

1. User is redirected to Signup
2. User enters information required for account set up
3. User Clicks on "Create Account"

 

##### Primary Postconditions

* User is redirected to their profile page

* Message will appear at the top "Account Created"

* Confirmation email is sent to user



##### Alternate Trigger



##### Alternative Sequences

1. 



##### Alternate Postconditions

* 



## **Use Case #2 Description**

**Date:** 9/14/2021

**Product Name:** Studious

**Problem Statement:** Currently Studious does not have a way for the users to sign in & sign out

**Non-functional Requirements:**

Forgot Password?

###### Notifications:

Wrong username/password

Caps Lock is ON

Password has been changed

**Use Case Name:** Sign In/Out



##### Actors

1. User



##### Preconditions

* User must already have an existing account

* User is on the "Sign up/ Sign in" page

* User is already logged in to be able to sign out

  

##### Triggers

User would have to click on the "sign in" button that is located on the "sign up/sign in" page


##### Primary Sequence

1. User is redirected to sign in page
2. User enters information to sign in
3. User clicks "sign in" button

 

##### Primary Postconditions

* User is redirected to their profile page



##### Alternate Trigger

User clicks on the "sign out" button at the top left of the page

##### Alternative Sequences

1. A message would appear asking the user if they wish to sign out
2. User clicks sign out



##### Alternate Postconditions

* User is redirected back to the "Sign up/Sign in" page



## **Use Case #3 Description**

**Date:** 9/14/2021

**Product Name:** Studious

**Problem Statement:** Studious currently does not have a way to import markdown files and create flash cards out of them

**Non-functional Requirements:**

File Type is .md

###### Notifications:

Wrong File Type

File Cannot Be Converted

**Use Case Name:** Convert Markdown Files to Flash Cards



##### Actors

1. User
2. Software



##### Preconditions

* User has a markdown file ready to input

 

##### Triggers

User clicks a "Upload" button

 

##### Primary Sequence

1. System asks if their file is for flash cards or notes
2. System asks for file to upload
3. User clicks on file they want to upload
4. User clicks Import

 

##### Primary Postconditions

* Message appears indicating whether the upload was successful or not



##### Alternate Trigger

A file has been successfully uploaded

##### Alternative Sequences

1. File is read

2. System sorts out the file

3. System creates flash cards according to the file

   

##### Alternate Postconditions

* Message appears telling the user that flash cards have been successfully created
* User can now access their flashcards



## **Use Case #4 Description**

**Date:** 9/14/2021

**Product Name:** Studious

**Problem Statement:** User's cannot share flashcards or add other user flashcards to their own library/profile

**Non-functional Requirements:**

Able to private their flash cards or notes

**Use Case Name:** Sharing Flash Cards



##### Actors

1. User



##### Preconditions

* User has a set of flash cards 
* Flash cards are not private

 

##### Triggers

User clicks the "share button"

 

##### Primary Sequence

1. Message pops up asking if they want to share permissions 
2. Message pops up giving the user a url to their flash cards

 

##### Primary Postconditions

* User now has a sharable link to their flash cards

  

##### Alternate Trigger

User clicks "Add to my library"

##### Alternative Sequences

1. Confirmation message appears
2. Message "Flash Cards Successfully Added To Library" appears on user screen

##### Alternate Postconditions

* User is now able to access the added flash cards through their profile/library



## **Use Case #5 Description**

**Date:** 9/14/2021

**Product Name:** Studious

**Problem Statement:** Studious is not able to render markdown notes

**Non-functional Requirements:** 

File Type is .md

###### Notifications:

Wrong File Type

**Use Case Name:** Import Notes



##### Actors

1. User



##### Preconditions

* User has a markdown file ready to upload

 

##### Triggers

User Clicks "Upload" button



##### Primary Sequence

1. System asks if their file is for flash cards or notes
2. System asks for file to upload
3. User clicks on the file they want to upload
4. File is read and sorted

 

##### Primary Postconditions

* Message tells user their notes have been uploaded
* user can now access their notes on Studious



##### Alternate Trigger



##### Alternative Sequences

1. 



##### Alternate Postconditions

* 



## **Use Case #6 Description**

**Date:** 9/14/2021

**Product Name:** Studious

**Problem Statement:** Studious cannot convert notes to pdf

**Non-functional Requirements:**

File type is .md

**Use Case Name:** Notes to PDF



##### Actors

1. User



##### Preconditions

* User have already uploaded their notes onto Studious

 

##### Triggers

User clicks "PDF" button

 

##### Primary Sequence

1. System asks user to choose which notes they want to convert into PDF
2. User selects notes
3. User clicks continue

 

##### Primary Postconditions

* The user's notes are now converted into pdf



##### Alternate Trigger



##### Alternative Sequences

1. 



##### Alternate Postconditions

* 



## **Use Case #7 Description**

**Date:** 9/15/21

**Product Name:** Studious

**Problem Statement:**  Our students have imported their notes, but have no way of viewing them.

**Non-functional Requirements:**

File type is .md

Display notes in a GUI format rather than on a command line



**Use Case Name:** Render Notes



##### Actors

1. User



##### Preconditions

* User must have uploaded notes prior to using this function

 

##### Triggers

User chooses which notes they want to have presented by clicking or entering file of their choice

 

##### Primary Sequence

1. User chooses notes of their choice
2. Notes appear on screen through a markdown editor, or terminal

 

##### Primary Postconditions

* User is presented the notes they want to have shown



##### Alternate Trigger



##### Alternative Sequences

1. 



##### Alternate Postconditions

* 



## **Use Case #8 Description**

**Date:** 9/15/21

**Product Name:** Studious

**Problem Statement:** Students would like to know how long they have been studying for

**Non-functional Requirements:** 

User must have one of the three features in use to record

**Use Case Name:** Record Study



##### Actors

1. User



##### Preconditions

* User must be actively using app

* One of three main features Memorizing, Note taking, and Time-Management must be in use

  

 

##### Triggers

App records use of app from behind the scenes.

 

##### Primary Sequence

1.  When app is being used beyond login, the recording of time will start

 

##### Primary Postconditions

* Time of using app beyond login will be placed into a data file



##### Alternate Trigger



##### Alternative Sequences

1. 



##### Alternate Postconditions

* 



## **Use Case #9 Description**

**Date:** 9/15/21

**Product Name:** Studious

**Problem Statement:** Our users would like to challenge themselves by having a countdown timer

**Non-functional Requirements:** 

Timer can either be displayed or hidden for user



**Use Case Name:** Pomodoro Timer



##### Actors

1. User



##### Preconditions

* Student must be using a feature like Note Taking, or Memorizing to use

 

##### Triggers

Timer can be presented with a user input before entering a task

Timer can also be paused/canceled in the event user needs to do another task

 

##### Primary Sequence

1. User enters task they would like to perform
2. Pomodoro Timer is present on task screen before entering a feature like Note Taking, or Memorizing

 

##### Primary Postconditions

* Timer will alert user when the time has run out



##### Alternate Trigger

Timer can be present in the Menu of the app, and can be used throughout entire use of the app

##### Alternative Sequences

1. User can have Timer present during their tasks



##### Alternate Postconditions

* 



## **Use Case #10 Description**

**Date:** 9/15/21

**Product Name:** Studious

**Problem Statement:** User would like to have the notes they have taken displayed in a mindmap to interact with other notes

**Non-functional Requirements:** Map can be displayed in a GUI feature showing which notes they have taken



**Use Case Name:** Mindmap Notes



##### Actors

1. User



##### Preconditions

* User must have more than one notes saved in their file on app

 

##### Triggers

Button can be displayed showing user if they want to have Mindmap displayed

 

##### Primary Sequence

1. User selects Mindmap button
2. Mindmap is presented in GUI showing user notes

 

##### Primary Postconditions

* User is presented with their notes on either a GUI or other image displayer



##### Alternate Trigger

An entire page can be dedicated to previous notes taken, almost like an instant message tab. Then adds to the Mindmap every time a user adds a new note

##### Alternative Sequences

1. User adds notes
2. User selects Mindmap tab on app
3. Mindmap is displayed showing all notes taken on app



##### Alternate Postconditions

* 



## **Use Case #11 Description**

**Date:** 9/15/2021

**Product Name:** Studious

**Problem Statement:** Change order of flash cards based on how often user got answer correct

**Non-functional Requirements:** 
Flash cards must be displayed from left to right based on how often user got answer correct



**Use Case Name:** Change order of flash cards



##### Actors

1. User



##### Preconditions

* User has logged in
* User must have at least one set of flash card saved in their file on app



##### Triggers

Every flash card has correct and incorrect button during memorizing mode
Sort flash cards in order after user memorizing mode ends



##### Primary Sequence

1. User clicks memorize button to enter memorizing mode
2. Click on flash cards to reveal answers
3. User either clicks on correct or incorrect button on each flash card after revealed



##### Primary Postconditions

* Flash cards are sorted in order after user memorizing mode ends



##### Alternate Trigger


##### Alternative Sequences

1. 



##### Alternate Postconditions

* 



## **Use Case #12 Description**

**Date:** 9/15/2021

**Product Name:** Studious

**Problem Statement:** User would like to find text in files

**Non-functional Requirements:** User must see highlighted text in files if available



**Use Case Name:** Find text in files



##### Actors

1. User



##### Preconditions

* User has logged in
* User must have at least one note saved in their file on app

 

##### Triggers

User can enter text on search bar


 
##### Primary Sequence

1. User clicks on search bar
2. Enter keys on search bar
3. Press enter or click on search button

 

##### Primary Postconditions

* Shows files with text highlighted



##### Alternate Trigger


##### Alternative Sequences

1. 



##### Alternate Postconditions

* The app displays no files available if text is not avaiable



## **Use Case #13 Description**

**Date:** 9/15/2021

**Product Name:** Studious

**Problem Statement:** User would like to rename multiple files quicklly

**Non-functional Requirements:** The app displays renamed files



**Use Case Name:** Quickly rename files using regular expressions



##### Actors

1. User



##### Preconditions

* User has logged in
* User must have at least one file saved in their file on app

 

##### Triggers
Rename files button is displayed for user to click



##### Primary Sequence

1. User clicks rename files button
2. User enter new name on rename bar
3. User clicks change
4. User confirms action
 

##### Primary Postconditions

* The name of selected files is changed



##### Alternate Trigger



##### Alternative Sequences

1. 



##### Alternate Postconditions

* 



## **Use Case #14 Description**

**Date:** 9/15/2021

**Product Name:** Studious

**Problem Statement:** User would like to navigate between notes

**Non-functional Requirements:** The app displays the notes that user navigated



**Use Case Name:** Add ability to navigate between notes using this syntax [[this other note]]


##### Actors

1. User



##### Preconditions

* User has logged in
* User must have more than one notes saved in their file on app

 

##### Triggers
User uses this syntax [[name note]] to navigate to that note



##### Primary Sequence

1. User enters this syntax [[name note]] on search bar
2. User enters or click search

 

##### Primary Postconditions

* User at the navigated notes



##### Alternate Trigger



##### Alternative Sequences

1. 



##### Alternate Postconditions

* The app won't navigate if there is no note found



## **Use Case #15 Description**

**Date:** 09/15/2021

**Product Name:** Studious

**Problem Statement:** User want to track of how many hours they have studied

**Non-functional Requirements:**
- Able to see the clock
- User must work on the apps

**Use Case Name:**
Track hours worked per week

##### Actors
User
Time management

##### Preconditions
The user must be login
At least one flash card or note must be in the account
User must work on flash card or note

##### Triggers
User click on the "Track hours" button


##### Primary Sequence
User works on the flash card


##### Primary Postconditions
System automatically updates the track hours
System updates every time a user is working
System show the hours at the end off a week

##### Alternate Trigger
##### Alternative Sequences
##### Alternate Postconditions


## **Use Case #16 Description**

**Date:** 09/15/2021

**Product Name:** Studious

**Problem Statement:** User want to know or plan what they have to do

**Non-functional Requirements:**
Display the todo list

**Use Case Name:** Add todo list

#####  Actors
User

##### Preconditions
User must login

##### Triggers
User selected “Add todo list”
User add the list they want to do

##### Primary Sequence
User works on the list

##### Primary Postconditions
System show the todo list
System update the new things in todo list

##### Alternate Trigger
##### Alternative Sequences
##### Alternate Postconditions


## **Use Case #17 Description**

**Date:** 09/15/2021

**Product Name:** Studious

**Problem Statement:** User want to organize and manage work

**Non-functional Requirements:**
Able to see the time
User must work on the apps

**Use Case Name:** Visualize hours worked and projects

##### Actors
User


##### Preconditions
User must be active


##### Triggers
User click the "Visualize Hours"

##### Primary Sequence
User select "Visualize Hours"
User click day, week, or month
User click on detail button

##### Primary Postconditions
System show the average hours

##### Alternate Trigger
##### Alternative Sequences
##### Alternate Postconditions
=====
