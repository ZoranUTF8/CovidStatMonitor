# Importing required modules
from controllers.EmailController import EmailController
from fastapi import APIRouter, HTTPException
from models.email import EmailData

import requests


# Importing controllers and requests module

# Create an instance of the APIRouter class
router = APIRouter()


# Define the routes in the router instance:


# Send email
@router.post("/send")
def sendEmail(emailData: EmailData):

    try:

        return {"message": "Success", "data":  EmailController().send_email(name=emailData.name,
                                                                            email=emailData.email,
                                                                            message=emailData.message)}
    except requests.exceptions.RequestException as e:
        error_message = f"Error sending the email, Reason: {e}"
        raise HTTPException(status_code=500, detail=error_message)


# Export the router instance:
__all__ = ["router"]
