# eventLog

What This Project Does --
  
  This project can parse an event ID and its details from Windows Event Viewer.
  The user can edit which ID they would like to call. If a user wants to call more than one
  event, adding nested 'for loops' inside the first one will work. After the program calls the 
  event ID/s it then outputs the event to a .txt file.
  
  I configured this program to run automatically as a .bat file in the event that there is a sudden power loss.
  In Windows Event Viewer, the system logs an ID (41) for this event. This most likely happens when the power 
  is restored and your system turns back on. To run a .bat file with a specific trigger case I followed this 
  tutorial on using the Task Scheduler app...
  https://towardsdatascience.com/automate-your-python-scripts-with-task-scheduler-661d0a40b279
  
  For converting your python script into a .bat file follow this tutorial...
  https://datatofish.com/batch-python-script/
  

Why This Project Is Useful --
  
  This project can be useful for different reasons such as alerting specific personnel 
  that there has been a power loss, and if certain equipment needs to be properly reset in person 
  there will be less time loss to preserve that equipment's functionality. 
  
  Other uses can include automatically logging events that have more to do with your computer security,
  for example, failed login attempts to your device, unrecognized new user profiles, or event log clearing
  (usually an indication someone is trying to cover their tracks). 
  

How You Can Get Started With This Project --
  
  All you need to do is copy and paste into your development environment of choice. I used Visual Studio Code with
  Python 3.7 as my interpreter. You can follow this tutorial for setting up python in Visual Studio Code...
  https://code.visualstudio.com/docs/python/python-tutorial
  
Other Helpful Links --

  Some helpful links I used for getting the code to run,
  Sending an email with python...
  https://realpython.com/python-send-email/
  
  Understanding Event Viewer...
  https://www.tenforums.com/tutorials/78335-read-shutdown-logs-event-viewer-windows.html
  
  Another version of the original code...
  https://stackoverflow.com/questions/11219213/read-specific-windows-event-log-event
  
Who Maintains This Project --
  
  For this specific code I am the only contributer and editor, but please feel free to send suggestions and comments.
  If you want to collaborate send me an email at the address on my profile page. 
  
  
