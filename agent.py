# agent.py (v4 - Goal-aware, Rationale, Polished)

from llama3 import call_ollama
from llama_parser import parse_llama_response
from simulated_feedback import simulate_campaign_feedback

GOAL_METRICS = {
    "New Markets": ["Market penetration", "Geo reach", "First-time users"],
    "Increase Sales": ["Conversion rate", "CAC", "AOV", "Sales uplift"],
    "Conversion": ["CTR", "Conversion rate", "Lead quality"],
    "Retention": ["Churn rate", "Repeat rate", "Customer LTV"],
    "Brand Awareness": ["Impressions", "Share of Voice", "Brand recall"],
    "Boost Engagement": ["Engagement rate", "Time on page", "CTR"]
}


def run_campaign_agent(company, product, goal, timeframe):
    metrics_list = GOAL_METRICS.get(goal, [])
    metrics_str = ", ".join(metrics_list)

    prompt = f"""
You are a senior marketing strategist and autonomous AI agent.

Design a multi-channel marketing campaign for:
- Company: **{company}**
- Product: **{product}**
- Goal: **{goal}**
- Timeframe: **{timeframe}**

The campaign must include:

## Overview
Concise summary of the campaign's name, positioning, and target audience.

## Platform Strategy
Which platforms to use (LinkedIn, Instagram, Email, etc.), why, and tactics for each.

## Creative Themes
Three distinct creative directions, each with messaging hooks and emotional appeal.

## Execution Timeline
Break down the campaign over time (weekly or monthly based on timeframe).

## Metrics & KPIs
List key success metrics tailored to the goal. Suggested: {metrics_str}

## Automation Tools
List AI tools or automation systems that will streamline execution (e.g., Zapier, Mailchimp AI, HubSpot workflows, etc.).

## A/B Test Variants
Design two message variants (Control + Variant) for one key platform. Include expected lift, hypothesis, and variable being tested.

## Feedback Loop
How to use signals like CTR, conversion, etc. to adapt campaign dynamically.

## Rationale
Explain the strategic thinking behind this campaign design in a concise paragraph.

Output everything in structured Markdown with headers matching the above.
"""

    raw_output = call_ollama(prompt)

    if not raw_output or not isinstance(raw_output, str):
        return {"Error": "LLaMA3 did not return a usable response."}

    parsed_output = parse_llama_response(raw_output)

    # Simulate performance metrics for A/B variants
    feedback_data = simulate_campaign_feedback(parsed_output)

    if feedback_data:
        parsed_output.update(feedback_data)

    return parsed_output
