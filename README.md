<h2>This script only works with gmail accounts</h2>


In order for the Script to work, you just change the .env file with your account details.

One more step is required, because you have to Sign up with App Passwords for security reasons. [Learn More](https://support.google.com/mail/answer/185833).

```bash
# Open the .env file and change these
EMAIL=YOUR_EMAIL_LOGIN
PASSWORD=YOUR_EMAIL_PASSWORD
TITLE=TITLE_OF_EMAIL
```

All .csv files in the main folder will be read by the script and the emails will be sent. The emails must be in the first field on the CSV file.

The content inside "body.html" will be sent as the body of the email.

Any files inserted into attachment folder will be attached to the email.
