# Import required modules
import requests
import smtplib
from email.mime.text import MIMEText


# separate module to encapsulate all the logic related to sending the email from the contact form.
# Custom EmailController class which handles the api communication for the contact form

class EmailController:

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    @staticmethod
    def send_email(name, email, message):
        """Send email with data from emailData parameter
           :param emailData: EmailData object containing name, email and message fields
           :return: JSON object with "message" and "data" keys. "message" contains a success message, and "data" contains
            a message indicating whether the email was sent successfully or not.
        """
        # Define the sender, recipient, and text file
        # sender
        me = email
        # recipient
        you = "info@corpy.co.jp"
        # Create a MIME message
        msg = MIMEText(f"From: {name} Contact email:<{email}>\n\n{message}")
        msg['From'] = f"{name}  {me}"
        msg['To'] = you
        msg['Subject'] = 'Contact form from CovidStats'

        # Try to send the message
        try:
            # Connect to the SMTP server
            with smtplib.SMTP(EmailController.smtp_server, EmailController.smtp_port) as server:
                # Identify yourself to the server
                server.ehlo()

                # Start TLS encryption (if supported)
                server.starttls()

                # Re-identify yourself to the server
                server.ehlo()

                # Login (if required)
                if EmailController.smtp_username and EmailController.smtp_password:
                    server.login(EmailController.smtp_username,
                                 EmailController.smtp_password)

                # Send the message
                server.sendmail(me, [you], msg.as_string())

            return {"status": "successfully", "message": "Email sent successfully"}

        except Exception as e:

            return {"status": "failed", "error": e}
