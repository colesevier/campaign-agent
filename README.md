# Campaign Agent

A compact, extensible agent for planning and executing outreach campaigns using language models and simulated channels. This repository demonstrates practical experience integrating LLMs, designing modular agent pipelines, building testable simulation layers, and wiring external APIs (e.g., Mailchimp) — all useful evidence for a Citadel launch application.

## Quick pitch

- What it is: a Python-based campaign planning and execution agent that orchestrates LLM-based planners, parsers, and simulated channels to design and test outreach campaigns.
- Why it matters: shows end-to-end product thinking — from model prompts to orchestration, to external integrations and simulated feedback loops — with reproducible code and clear extension points.

## Highlights

- LLM integration and prompt engineering (files: `llama3.py`, `llama_parser.py`) — showcases prompt design, parsing, and deterministic output handling.
- Planner / agent architecture (`campaign_planner.py`, `agent.py`) — demonstrates separation of concerns, modular pipeline stages, and orchestrated decision-making.
- Execution layer and simulation (`execution.py`, `simulated_channel_runner.py`, `simulated_feedback.py`) — shows ability to create repeatable experiments, A/B tests, and simulate user feedback before real-world rollout.
- API client and real-world wiring: `mailchimp_client.py` — demonstrates working with external SaaS and building production connectors.
- Refinement loop: `refinement_agent.py` — shows experience with iterative improvements using model feedback.

## Architecture 

- agent.py — entrypoint and orchestration glue. Responsible for configuring and launching the pipeline.
- campaign_planner.py — builds campaign plans: audiences, messages, schedules, goals.
- llama3.py & llama_parser.py — LLM client wrappers and parsers which translate free-text model outputs to structured objects.
- execution.py — executes a plan: schedules messages and coordinates channels.
- simulated_channel_runner.py & simulated_feedback.py — a sandbox for safely running campaigns and collecting synthetic feedback.
- mailchimp_client.py — external email provider integration.
- refinement_agent.py — takes results/feedback and refines plans.

## Contract (what to expect)

- Inputs: campaign specification or high-level prompt (string or JSON), optional audience data.
- Outputs: structured campaign plans (JSON), execution logs, and simulated / real delivery results.
- Error modes: network/API errors, model API timeouts, malformed model outputs. All functions return exceptions or structured error values — exercises in fault handling.
- Success criteria: plan created, simulated sends executed, feedback collected and used to refine next plan.

## Edge cases and how the repo handles them

- Empty inputs / missing audience: validation at planner entry points.
- Rate limits / API failures: retry/backoff patterns are recommended around client calls (`mailchimp_client.py`).
- Non-deterministic model outputs: robust parsing in `llama_parser.py` and conservative fallbacks.

## Try it locally

1. Create a virtual environment and install dependencies (tested with Python 3.11+ / 3.12):

   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2. Run the main agent in a demo/simulated mode (if you want to avoid external API calls):

   python agent.py


## Tests & verification

- Add unit tests that assert planner outputs, parser robustness, and that simulated runs complete.
- Suggested quick tests:
  - Planner produces a plan for a small audience.
  - Parser converts noisy model output into expected JSON.
  - Simulated runner logs expected outcomes without external services.

Run tests (pytest assumed):

   pip install pytest
   pytest -q

