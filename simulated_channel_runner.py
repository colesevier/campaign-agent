import random

def simulate_campaign_execution(campaign_dict):
    """
    Simulates execution of a campaign across platforms.
    Returns fake but structured performance metrics.
    """
    performance = {}

    for key, value in campaign_dict.items():
        # You can assign metrics based on key type
        if "Platform" in key or "Strategy" in key:
            performance[key] = {
                "CTR": f"{round(random.uniform(1.5, 6.0), 2)}%",
                "ROI": f"{round(random.uniform(1.2, 4.0), 2)}x",
                "Engagement": f"{random.randint(1000, 10000)} interactions"
            }

    return performance

