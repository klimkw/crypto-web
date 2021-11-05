# Take-Home Test for Chainalysis

## Stack:

- Backend: Python + Flask
- Frontend: React

## Exchanges:

1. Kraken
2. Gemini

## Build:

`cd chain-api && python3 -m venv .env && source .env/bin/activate && pip install -r requirements.txt && deactivate && cd ..`

## Run:

`npm install`

`yarn start`

`yarn start-api`

## Explaining the Implementation:

## Answers to Questionnaire:

1. In implementing the webpage, a REST API was used where the frontend makes calls at 1s intervals to refresh the prices (and recommendations). However, a websocket API would have been more ideal, but would require an account to those exchanges and embedding credentials in a secure manner.

2. I tried my best to keep the project's implementation to a minimum, despite how tempting it was, due to limited time and not wanting to overly bloat the implementation. (aside from the background, which I thought gave the project some visual appeal)

3. If scaling the current implementation to 100 users/second, 