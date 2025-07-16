import random
import re

def simulate_campaign_feedback(ab_test_variants):
    """
    Expects a list of A/B test variant messages (strings).
    Returns list of dicts with simulated CTR and ROI for each.
    If given a single long string, it will try to extract variants using regex.
    """

    # Auto-fix if given one long markdown string
    if isinstance(ab_test_variants, str):
        ab_test_variants = re.findall(r"\*\*(?:Control|Variant [A-Z])\*\:?\s*(.+)", ab_test_variants)
    
    if not isinstance(ab_test_variants, list) or not ab_test_variants:
        print("Warning: simulate_campaign_feedback expected a list of messages, got invalid input.")
        return []

    clean_variants = [v for v in ab_test_variants if isinstance(v, str) and len(v.strip()) > 0]

    feedback_results = []

    for variant in clean_variants:
        result = {
            "message": variant.strip(),
            "CTR": f"{round(random.uniform(0.5, 5.0), 2)}%",
            "ROI": f"{round(random.uniform(1.0, 4.0), 2)}x"
        }
        feedback_results.append(result)


    return feedback_results

