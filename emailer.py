import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(from_email, to_email, smtp_user, smtp_password, subject, email_body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # or 465 for SSL

    # Create the email message
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # Attach the body text to the email
    message.attach(MIMEText(email_body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_user, smtp_password)
            server.send_message(message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Generate email body
def generate_email_body(results, new_results, brands, num_found, place, time_string):

    def get_price(result):
        try:
            return float(result['price'].replace('$', '').replace(',', ''))
        except ValueError:
            return float('inf')  # Treat invalid or missing prices as "infinity" (push them to the end)


    email_body = f"{time_string}\n{place}\n\n"
    email_body += f"There were: {len(new_results)} new results\n"

    
    for result in new_results:
        email_body += f"Title: {result['title']}\nBrand: {result['brand']}\nLink: {result['link']}\n"
        email_body += f"Price: {result['price']}\nLocation: {result['location']}\n"
        email_body += '---------------------------------------------------\n\n'
    
    email_body += f"\n\n\nThere were: {len(results)} total results\nHere is the breakdown:\n"
    for i in range(len(brands)):
        email_body += f"{brands[i]}   {num_found[i]}\n"
    
    email_body += "\n\n\n---------------------------------------------------\n\n"

    if brands[0] == "ALL BRANDS:"
        results = sorted(results, key = get_price)
    for result in results:
        email_body += f"Title: {result['title']}\nBrand: {result['brand']}\nLink: {result['link']}\n"
        email_body += f"Price: {result['price']}\nLocation: {result['location']}\n"
        email_body += '---------------------------------------------------\n\n'

    return email_body

