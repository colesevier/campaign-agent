# execution.py (Enhanced with Feedback Loop + Visualization Data Generation)

import random
from mailchimp_client import add_contact_to_list, send_campaign


# In-memory campaign store
campaigns = []

# Launches a campaign and appends it to the list
def launch_ad(platform, message):
    ctr = round(random.uniform(0.03, 0.09), 3)
    roi = round(random.uniform(1.2, 3.5), 2)
    campaigns.append({
        "platform": platform,
        "message": message,
        "CTR": ctr,
        "ROI": roi,
        "optimized": False
    })

# Returns all live campaigns
def get_all_campaigns():
    return campaigns

# Pulls performance metrics
def get_performance():
    return [
        {
            "platform": c["platform"],
            "message": c["message"],  # Include the message for display
            "CTR": c["CTR"],
            "ROI": c["ROI"],
            "optimized": c["optimized"]
        }
        for c in campaigns
    ]


# Optimizes campaigns by boosting ROI & CTR
def agent_optimize():
    for c in campaigns:
        if not c["optimized"]:
            c["CTR"] = round(c["CTR"] * 1.2, 3)
            c["ROI"] = round(c["ROI"] * 1.15, 2)
            c["optimized"] = True

# Generate graph-ready performance data
def get_time_series_data():
    time_series = []
    for idx, c in enumerate(campaigns):
        ctr_series = [round(c["CTR"] * (1 + 0.02 * i), 3) for i in range(4)]
        roi_series = [round(c["ROI"] * (1 + 0.015 * i), 2) for i in range(4)]
        time_series.append({
            "platform": c["platform"],
            "message": c["message"],
            "CTR_series": ctr_series,
            "ROI_series": roi_series
        })
    return time_series

# Prototype engagement mockup for visuals\B post simulation
def get_mock_post_engagements():
    return [
        {"platform": "Instagram", "likes": 320, "comments": 45, "shares": 78},
        {"platform": "LinkedIn", "likes": 120, "comments": 30, "shares": 18},
        {"platform": "Email", "opens": 1600, "clicks": 210, "unsubscribes": 5}
    ]

def launch_email_campaign():
    # Dummy test data
    add_contact_to_list("testuser@example.com", "Test", "User")

    content_html = "<h1>Welcome to the Tesla Campaign</h1><p>This is a test run from the autonomous agent.</p>"
    send_campaign(
        subject="Tesla Retention Campaign Launch",
        from_name="Tesla AI Agent",
        reply_to="noreply@tesla.com",
        content_html=content_html
    )
