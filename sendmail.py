
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.message import EmailMessage
from keyboard import press_and_release
from Body.Listen import Listen
from Body.Speak import Speak

# Setup port number and server name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = "niteshsaini824@gmail.com"
email_list = {
    'nitesh': 'niteshsmarty111@gmail.com',
    'tanu'  :  'triptidhingra824@gmail.com',
    'naman' : 'jainnaman868589@gmail.com',
    'khemchand' : "khemu12121@gmail.com",
    'harsh' : "mittalofficial25@gmail.com",
    'amit'  :  "amitver2000@gmail.com",
    'nisha' : "rohillanisha74@gmail.com",
    'jyoti' : "jinnysaini111@gmail.com"
    }



# Define the password (better to reference externally)
pswd = 'sozaxkopxjawrsvj' 


# name the email subject
subject = "New email from Nitesh Saini with attachments!!"



# Define the email function (dont call it email!)
def send_emails(receiver, subject, message,filename):

   

      

        # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = receiver
        msg['Subject'] = subject

        # Attach the body of the message
        msg.attach(MIMEText(message, 'plain'))

        # Define the file to attach
        

        # Open the file in python as a binary
        attachment= open(filename, 'rb')  # r for read and b for binary

        # Encode as base 64
        attachment_package = MIMEBase('application', 'octet-stream')
        attachment_package.set_payload((attachment).read())
        encoders.encode_base64(attachment_package)
        attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
        msg.attach(attachment_package)

        # Cast as string
        text = msg.as_string()

        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(email_from, pswd)
        print("Succesfully connected to server")
        print()


        # Send emails to "person" as list is iterated
        print(f"Sending email to: {receiver}...")
        TIE_server.sendmail(email_from, receiver, text)
        print(f"Email sent to: {receiver}")
        print()

    # Close the port
        TIE_server.quit()

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('niteshsaini824@gmail.com','wvlzjbpbwomkdfje')
    email = EmailMessage()
    email['From'] = 'niteshsaini824@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
# Run the function
def get_email_info():
    Speak('To Whom you want to send email')
    name = Listen()
    receiver = email_list[name]
    print(receiver)
    Speak('What is the subject of your email')
    subject = Listen()
    Speak('Tell me the text in your email')
    message = Listen()
    Speak("You want to add some attactments?")
    attachments= Listen()
    if 'yes' in attachments:
     Speak("Enter the path of file with file name")
     
     Speak("For example:")
     print("For example: \n D:\KDE shared items\socket\socket.pdf")
     press_and_release("Win+E")
     filename= str(input("Enter the path: "))
     
     send_emails(receiver, subject, message,filename)
    elif "no" in attachments:
     send_email(receiver, subject, message)
     
    Speak('Your email is sent')
    Speak('Do you want to send more email?')
    send_more =Listen()
    if 'yes' in send_more:
        get_email_info()






        




