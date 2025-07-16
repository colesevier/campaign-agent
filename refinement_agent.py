from llama3 import call_ollama

def refine_campaign_variant(winning_message, original_campaign_brief):
    prompt = (
        f"{original_campaign_brief}\n\n"
        f"The A/B testing results show that this message performed best:\n"
        f"> {winning_message}\n\n"
        f"Based on this, refine and enhance the campaign's messaging and platform strategy. "
        f"Update creative themes and calls to action to align with the high-performing message. "
        f"Keep it concise and actionable. Output in markdown with headers."
    )
    return call_ollama(prompt)
