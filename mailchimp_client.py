import os
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from dotenv import load_dotenv


load_dotenv()  # Load from .env

MAILCHIMP_API_KEY = os.getenv("MAILCHIMP_API_KEY")
MAILCHIMP_LIST_ID = os.getenv("MAILCHIMP_LIST_ID")
MAILCHIMP_SERVER_PREFIX = os.getenv("MAILCHIMP_SERVER_PREFIX")

print("DEBUG >> MAILCHIMP_LIST_ID:", MAILCHIMP_LIST_ID)

client = Client()
client.set_config({
    "api_key": MAILCHIMP_API_KEY,
    "server": MAILCHIMP_SERVER_PREFIX
})


def add_contact_to_list(email, first_name="", last_name=""):
    try:
        response = client.lists.add_list_member(MAILCHIMP_LIST_ID, {
            "email_address": email,
            "status": "subscribed",
            "merge_fields": {
                "FNAME": first_name,
                "LNAME": last_name
            }
        })
        return response
    except ApiClientError as error:
        print(f"Error adding contact: {error.text}")
        return None


def send_campaign(subject, from_name, reply_to, content_html):
    try:
        # Step 1: Create campaign
        campaign = client.campaigns.create({
            "type": "regular",
            "recipients": {"list_id": MAILCHIMP_LIST_ID},
            "settings": {
                "subject_line": subject,
                "from_name": from_name,
                "reply_to": reply_to
            }
        })

        campaign_id = campaign["id"]

        # Step 2: Set content
        client.campaigns.set_content(campaign_id, {
            "html": content_html
        })

        # Step 3: Send it
        client.campaigns.send(campaign_id)
        return campaign_id

    except ApiClientError as error:
        print(f"Error sending campaign: {error.text}")
        return None
