# Windows Event Log Viewer
# Original script by FB36 found on 
# https://code.activestate.com/recipes/577499-windows-event-log-viewer/
# Modified by George Suarez 06/10/21
# This program logs an event ID from the Event Viewer app.
# It also appends the event to a .txt when it is ran and
# also sends out an email. The script can be used as a .bat file
# to be automated in Task Scheduler. I have modified this script
# to log power failures at my company. This program triggers when
# the Event Viewer logs event ID 41. 

import smtplib, ssl 
import win32evtlog # requires pywin32 pre-installed

port = 465 #for SSL
smtp_server = "smtp.gmail.com"
sender_email = "yours@email.com" #enter your address
receiver_email = "theirs@email.com" #enter receiver address
#receiver_email_2 = "" #define as many email addresses as needed
password = "*******" #enter in sender's email password

#Write your message here
message = """ \                                     
Subject: Power Failure

The power has failed at your_company. """

context = ssl.create_default_context()
server = 'localhost' # name of the target computer to get event logs
logtype = 'System' # 'Application' # 'Security'
hand = win32evtlog.OpenEventLog(server,logtype)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = win32evtlog.GetNumberOfEventLogRecords(hand)
sys = "Power Failure"

#send email
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server: 
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
                #server.sendmail(sender_email, receiver_email_2, message)

#look for specific event ID/s
while True:
     events = win32evtlog.ReadEventLog(hand, flags,0)
     if events:
        for event in events:
            if event.EventID == 41 and event.SourceName == "Microsoft-Windows-Kernel-Power":
                
                    print ("Power Failure")
                    print ('Event Category:', event.EventCategory)
                    print ('Time Generated:', event.TimeGenerated)
                    print ('Source Name:', event.SourceName)
                    print ('Event ID:', event.EventID)
                    print ('Event Type:', event.EventType)

            
        #save to .txt file
            with open('glitch.txt', 'a') as outfile:
                
                if event.EventID == 41 and event.SourceName == "Microsoft-Windows-Kernel-Power":
                    outfile.write('%s\n' % sys)
                    outfile.write('%s' % "Event ID: ")
                    outfile.write('%s\n' % event.EventID)
                    outfile.write('%s' % "Time Stamp: ")
                    outfile.write('%s\n' % event.TimeGenerated)
                    outfile.write('%s' % "Source Name: ")
                    outfile.write('%s\n' % event.SourceName)
                    outfile.write('\n')
         
            

                    
                    
                                        

                        

                        
