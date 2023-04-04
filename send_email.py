import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "yusufabdurrasheed539@gmail.com"
    password = "cqnbczrbijsejyph"
    receiver = "yusufabdurrasheed539@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



