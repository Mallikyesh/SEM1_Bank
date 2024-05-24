# import pathlib
# import cv2

# cascade_path=pathlib.Path(cv2.__file__).parent.absolute()/"data/haarcascade_frontalface_default.xml"

# clf=cv2.CascadeClassifier(str(cascade_path))

# camera=cv2.VideoCapture(0) #use (0) for built-in webcm

# while True:
#     _, frame = camera.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = clf.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30,30),
#         flags=cv2.CASCADE_SCALE_IMAGE
        
#     )

#     for (x,y,width,height) in faces:
#         cv2.rectangle(frame,(x,y),(x+width, y+height), (255, 255, 0), 2)

#     cv2.imshow("Faces", frame)
#     if cv2.waitKey(1)== ord("q"):
#         break

# camera.release()
# cv2.destroyAllWindows







# import random
# print("Hello User , Welcome to Bank_Of_Pes")
# ("If u are an existing User , enter 1 or enter 2 for new account opening, 3 for customer care and Frequently Asked Questions")
# n=int(input("Enter 1 for new account opening or Enter 2 If u are an existing User"))
# if n==1:
#     print("Hello User , Welcome to Bank_Of_Pes")
#     print("Enter the following credentials to create an account in Bank_Of_Pes")
#     name=str(input("Enter your name"))
#     password=int(input("Enter your password"))
#     age=int(input("Enter your age"))
#     ph_no=int(input("Enter your Phone Number"))
#     gmail=str((input("Enter your Gmail ID"))) #need both str and int in input
#     aadhar=int(input("Enter your aadhar card number"))
#     Voter_ID=int(input("Enter your Voter Id number"))#remove
#     DL=int(input("Enter your Driving License card number"))#Remove
#     print("Thanks for your entering credentials")
#     x=int(input("Enter 1 for Opening a bank account, 2 for Fixed Deposit , 3 for taking a loan from the bank , 4 for policy and schemes"))
#     if x==1:
#         if(age>18):
#             print("To Open an acoount in the bank you must deposit a minimum amount of 10000 Rs and the minimum balance that must be in the account is 3000 Rs")
#             amt=int(input("Enter the amount you want to deposit to your account"))
#             if amt<10000:
#                 print("Insufficient amount deposited")
            
#                 if amt>=10000:
#                     x1=random.randint(1000,9999)
#                     x2=random.randint(1000,9999)
#                     x3=random.randint(1000,9999)
#                     x4=random.randint(1000,9999)
#                     cvv=random.randint(100,999)
#                     print("Your New card Number is ",x1," ",x2," ",x3," ",x4)
#                     print("Your CVV is = ",cvv)
#                     print("The amount in yourr account is = ",amt," Rs")
#                     print("Thanks for choosing Bank_Of_Pes")
#                 xtry=int(input("If u want to choose another option enter 2"))
                
#                 if xtry==2:
#                      amt=int(input("Enter the amount you want to keep for F.D"))
#             print("The interest rate in our bank is 10 percent for one year")
#             interest=10
#             dur=int(input("Enter the number of months you want to deposit for"))
#             interest=10+(0.4*((dur/10)))
#             amt=amt+((interest/100)*amt)
#             print("The final amount u get after ",dur," is ",amt," Rs")
# elif n==2:
#             print("Hello User , Welcome back please enter your credentials to login :-")
#             name=str(input("Enter your name"))
#             password1=int(input("Enter your password"))
#             if(password1==password):
#                print("Welcome back ",name)
#             print("The amount left in your account is ",amt," Rs")
#             y=int(input("Enter 1 for Deposition or 2 for Transaction or Enter 3 to view your current schemes or plans , or 4 for checking your loan history "))
#             if y==1:
#                 dep=int(input("Enter the amount u want to deposit to your bank account"))
#                 amt=amt+dep
#                 print("The total amount left in your account is =",amt," Rs")
#                 print("Thank you for choosing Bank_Of_Pes")
#             if y==2:
#                 wtd=int(input("Enter the amount you want to withdraw from your bank account"))
#                 amt=amt-wtd
#                 if amt>3000:
#                     print("The total amount left in your bank account is ",amt," Rs")
#                     print("Thank you for choosing Bank_Of_Pes")
#                 if amt<3000:
#                     print("You cant withdraw ",wtd," Rs because your account must have a minimum balance of 3000 rs")
                
#             if y==3:
#                 schm=str("none")#temp change
#                 print("Your current schemes are =",schm)
#                 fmlinc=int(input("Enter your family income"))
#                 cat=str(input("Enter your category"))
#                 ls=["GM","SC","ST","SNQ","A","B","G"]

#                 print("you are eligible for scheme: ")
#                 if fmlinc<=100000 and (cat=="SC" or cat=="ST" or cat=="A" or cat=="B" or cat=="G"):
#                   print("Eligible for schm1")
#                 if fmlinc >=100000 and (cat=="SC" or cat=="ST" or cat=="A" or cat=="B" or cat=="G"):
#                         print("Eligible for schm2")
#                 if fmlinc >=250000 and fmlinc<=1000000 and (cat=="SC" or cat=="ST" or cat=="A" or cat=="B" or cat=="G"):
#                            print("Eligible for schm3")

#                 else:
#                     print("You are not eligible for any scheme")

#                 print("The amount deposited is ",amt)

#                 print("The duration of your current scheme is ",dur)
#                 print("The interest for this scheme is ",interest)
#                 new_amt=(amt*(interest/ 100))+amt
#                 print("The final amount u will get after the duration of ",dur," is ",new_amt," Rs")
#                 print("Thank you for choosing Bank_Of_Pes")
#             if y==4:
#                 loan=20 
#                 loan_amt=20#temp change
        
#                 print("The loan u have selected is ",loan)# This is the loan data stored previously
#                 print("The loan amount you have taken from the bank is ",loan_amt," Rs")# This is the loan data stored previously
#                 print("The loan duration you have taken is ",dur)
#                 loan_int=(interest/100)*amt
#                 print("The loan interst you have to pay is ",loan_int," Rs")
#                 new_amt=loan_amt+loan_int# This is the loan data stored previously
#                 print("The total amount you have to pay to the bank is ",new_amt," Rs")

#                 #Loan
#                 L=(' Home loan',' Education loan',' Vehicle loan',' Personal loan')
#                 print('Loans available: ',L)
#                 L1=str(input("Loan type"))
#                 if L1=='Home':
#                     print("House loans available at x rate of interest",' ',"Calculate interest amount here" ,sep=' ')
#                     p=int(input("enter your principle amount"))
#                     cl=int(input("Enter Time duration"))
#                     rate=4
#                     intr=(p*cl*rate)/100
#                     print('interest recieved: ',intr)
#                     finamt=intr+p
#                     print('You will recieve: by the end of the term', finamt)

#                     if L1=='Education':
#                          print("Education loan available at x rate of interest")


#                          if L1=='Vehicle':
#                              print("Vehicle loan available at x rate of interest")

#                              if L1=='Personal':
#                                 print("Personal loan available at x rate of interest")

#             print("Thank you for choosing Bank_Of_Pes")
#             try_again=int(input("If u want to choose a different option , Enter 1"))
#             if try_again==1:
#                 print("Valid")#temp change
#             else:
#                 print("Invalid Username/Password")
                


import pathlib
import cv2
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Function to capture image
def capture_image():
    cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
    clf = cv2.CascadeClassifier(str(cascade_path))
    camera = cv2.VideoCapture(0)

    while True:
        _, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)

        cv2.imshow("Faces", frame)
        if cv2.waitKey(1) == ord("q"):
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            img_filename = f"user_image_{timestamp}.jpg"
            cv2.imwrite(img_filename, frame)
            break

    camera.release()
    cv2.destroyAllWindows()
    return img_filename, timestamp

# Function to send email
def send_email(to_email, img_filename, timestamp):
    from_email = "xyz@gmail.com"                                                 #put your email here (sender email)
    from_password = "oubb vfgm cvqw jihd"                                        #if the sender email is a gmail, then create app password 
    subject = "ATM Transaction Verification"                                     #on google settings and paste the code here
    body = f"An ATM transaction is being attempted. See the attached image captured at {timestamp}."

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(img_filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {img_filename}")
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()
    print(f"Email sent to {to_email}")

# Main ATM transaction function
def atm_transaction():
    print("Hello User, Welcome to Bank_Of_Pes")
    n = int(input("Enter 1 for new account opening or Enter 2 If you are an existing User: "))
    if n == 1:
        print("Hello User, Welcome to Bank_Of_Pes")
        print("Enter the following credentials to create an account in Bank_Of_Pes")
        name = input("Enter your name: ")
        password = int(input("Enter your password: "))
        age = int(input("Enter your age: "))
        ph_no = int(input("Enter your Phone Number: "))
        gmail = input("Enter your Gmail ID: ")
        aadhar = int(input("Enter your aadhar card number: "))

        print("Thanks for entering your credentials")
        if age > 18:
            print("To open an account in the bank you must deposit a minimum amount of 10000 Rs and the minimum balance that must be in the account is 3000 Rs")
            amt = int(input("Enter the amount you want to deposit to your account: "))
            if amt < 10000:
                print("Insufficient amount deposited")
            else:
                x1, x2, x3, x4 = random.randint(1000, 9999), random.randint(1000, 9999), random.randint(1000, 9999), random.randint(1000, 9999)
                cvv = random.randint(100, 999)
                print("Your New card Number is ", x1, " ", x2, " ", x3, " ", x4)
                print("Your CVV is = ", cvv)
                print("The amount in your account is = ", amt, " Rs")
                print("Thanks for choosing Bank_Of_Pes")

    elif n == 2:
        print("Hello User, Welcome back. Please enter your credentials to login :-")
        card_number = input("Enter your card number: ")
        password1 = int(input("Enter your password: "))
        
        # Assuming 'password' is a stored variable for the existing user, which you need to replace with actual password check
        password = 1234  # Replace with actual password checking mechanism
        if password1 == password:
            print("Welcome back!")
            
            img_filename, timestamp = capture_image()
            to_email = "pes1202201282@pesu.pes.edu"  # Replace with the reciever user's email
            send_email(to_email, img_filename, timestamp)
            
            user_approval = input("Enter 'yes' if you approve the transaction: ")
            if user_approval.lower() == 'yes':
                print("Transaction Approved.")
                # Proceed with the transaction
            else:
                print("Transaction Denied.")
        else:
            print("Invalid card number or password.")

# Run the ATM transaction function
atm_transaction()
