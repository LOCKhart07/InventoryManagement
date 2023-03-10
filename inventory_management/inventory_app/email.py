import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def sendMail(emailAddress, order, myitems, totalCost):
    fromEmail = os.getenv("GMAIL_APP_EMAIL")
    fromPassword = os.getenv("GMAIL_APP_SECRET_PASSWORD")
    # print(fromEmail)
    msg = MIMEMultipart("alternative")

    msg["Subject"] = f"Your iManage Order Confirmation. ID : {order.transaction_id}"
    msg["From"] = fromEmail
    msg["To"] = emailAddress
    # print("message settt")

    text = "Your email client doesnt support html messages"
    html = f"""\
    <html>
    <head></head>
    <body>
    <h3>Transaction ID: {order.transaction_id}</h3>
    <h3>BU Code: {order.buCode}</h3>
    <h3>Date Ordered: {(order.date_ordered).date()}</h3>
    <h3>Ordered Items: {", ".join(myitems)}</h3>
    <h3>Order Cost: {totalCost}</h3>
    </body>
    </html>
    """

    html = f"""\
        <html>
    <head></head>
        <body>
    <center style="margin-bottom: 7%; margin-top: 2%">
      <h1>
        Woohoo!!🎉<br />
        ✨Order Placed Successfully✨
      </h1>
    </center>
    <center>
      <table style="border: 1px solid black; text-align: center">
        <tr>
          <th>Transaction ID:</th>
          <td>{order.transaction_id}</td>
        </tr>
        <tr>
          <th>BU Code:</th>
          <td>{order.buCode}</td>
        </tr>
        <tr>
          <th>Date Ordered:</th>
          <td>{ order.date_ordered }</td>
        </tr>
        <tr>
          <th>Ordered Items:</th>
          <td>{", ".join(myitems)}</td>
        </tr>
        <tr>
          <th>Order Cost:</th>
          <td>{totalCost}</td>
        </tr>
        </html>
        """

    # Record the MIME types of both parts - text/plain and text/html.

    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(fromEmail, fromPassword)
            print("sending mail to: ", emailAddress)
            smtp.sendmail(fromEmail, emailAddress, msg.as_string())
            print("Mail sent")
    except Exception as e:
        print("Email not sent; Error : ", e)
