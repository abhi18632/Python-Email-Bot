# Importing Some Bunch Of Stuff
import email, smtplib, ssl
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Function to send email to multiple recipients 
def send_email(subject,sender_email,receiver_email,body1,body2,html):

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body1, "plain"))
    message.attach(MIMEText(html, "html"))
    message.attach(MIMEText(body2, "plain"))

    filename = "Abhishek's Resume.pdf"  # include your resume file , In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:

        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

# Prepairing Content to be mailed 

body1= '''
Abhishek Gupta
+91 9650618632
''' 

html = '''<a href="https://www.linkedin.com/in/abhishek18632/">https://www.linkedin.com/in/abhishek18632/</a><br/>
<br/>
'''

body2 = '''
I am writing to you to express my interest as a SDE Intern in your esteemed organization. I am currently pursuing B.Tech in Computer Science in final year from Maharaja Agrasen Institute of Technology which is affiliated with GGSIP University, Delhi.

I am an experienced Mentor with a demonstrated history of working in the e-learning industry, presently a Mentor and Growth Hacker Lead at Coding Club where I am applying my problem-solving skills to help over 100 learners in the community and responsible for conducting workshops and webinars on competitive coding.
Besides that, I am a coding enthusiast with strong knowledge of Data Structures and Algorithms, Skilled in Java, C/C++, Python, Shell Scripting, also having an extensive experience in Machine Learning and Backend development using Spring MVC.

I am seeking an opportunity to implement my programming and development skills in a practical application which will give me exposure to the actual design and execution processes of an industry. I would love to associate with such an organization where I can utilize my skills and gain further experience while enhancing the company’s productivity and reputation.

I am confident that my experience and skill set that I have gained would be a great fit for this position. I appreciate your consideration and look forward to hearing from you.
Kindly find the attached resume.

Sincerely
Abhishek Gupta
'''

# Person_Name EmailId CompanyName 
sender_email = "abhishekgupta18632@gmail.com"
password = getpass.getpass() 

with open("./emails","r") as f:
	for line in f:
		w=line.split()
		body3='Respected '+w[0]+body2
		subject="SDE Intern Referral"
		#"Application for SDE-1 @" + w[2]
		receiver_email=w[1]
		send_email(subject,sender_email,receiver_email,body1,body3,html)
