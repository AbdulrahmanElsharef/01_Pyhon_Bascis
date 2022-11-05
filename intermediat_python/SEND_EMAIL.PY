
import smtplib
def send_mail():
    ''' function creat smtp session for send mail
    args:send_mail,token_mail,reciv_mail,message
    return:sendmail(send_mail, reciv_mail, message)'''
    # creates SMTP session
    sms = smtplib.SMTP('smtp.gmail.com', 587)
    # start TLS for security
    sms.starttls()
    send_mail="nour70331@gmail.com" # sender mail
    token_mail="wxgbbvaengzrypoj"   # mail_pass_token
    # Authentication
    sms.login(send_mail, token_mail)
    # message to be sent
    reciv_mail="abdoelsharef1@gmail.com" #recive mail
    message = f"welcom mr {reciv_mail} we have job offer for you please click button to view job offer ".title()
    # sending the mail
    sms.sendmail(send_mail, reciv_mail, message)
    # terminating the session
    sms.quit()
    print(f"send mail to {reciv_mail} is done ...".title())


send_mail() # run function

# Send Mail To Abdoelsharef1@Gmail.Com Is Done ...

# (بدون موضوع)
# البريد الوارد

# nour70331@gmail.com
# 12:23 م ‎(قبل 0 دقيقة)‎

# Welcom Mr Abdoelsharef1@Gmail.Com We Have Job Offer For You Please Click Button To View Job Offer

