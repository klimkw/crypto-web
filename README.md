# Take-Home Test for Chainalysis

## Live Link:

https://stormy-meadow-72770.herokuapp.com/

## Stack:

- Backend: Python + Flask
- Frontend: React

## Exchanges:

1. Kraken
2. Gemini

## Build + Run (in development):

`cd chain-api && python3 -m venv .env && source .env/bin/activate && pip install -r requirements.txt && deactivate && cd ..`

`npm install`

`yarn start`

`yarn start-api`

## Explaining the Implementation:
Backend is built on Python + Flask, pulling in bid/ask price of BTC from Kraken and Gemini, using their free REST APIs. Computation of which buy/sell price is recommended is done in the Python layer on processing each exchange information and storing it in the dictionary before returning in the form of a JSON as a REST API call.

Frontend is built on React, using reactstrap for layout organization. It make API calls to the backend in 1s intervals to simulate an almost-live stream. Based on the result of the API call, the frontend will return a button that is flashing for recommended buys or sells and a regular button otherwise.

## Answers to Questionnaire:

1. In implementing the webpage, a REST API was used where the frontend makes calls at 1s intervals to refresh the prices (and recommendations). However, a websocket API (both between frontend/backend and backend/exchanges) would have been more ideal to support a live stream of data (crucial for market prices), but would require an account to those exchanges and embedding credentials in a secure manner.

2. I tried my best to keep the project's implementation to a minimum, despite how tempting it was, due to limited time and not wanting to overly bloat the implementation. (aside from the background, which I thought gave the project some visual appeal)

3. If scaling the current implementation to 100 users/second, I would use nginx, implementing a load balancer to handle concurrency and prevent overloading a particular server. 

4. Given more time, I would first swap out the REST APIs for websocket APIs. Next, I would bring in more analytical features such as graphs (using libraries such as Plotly) to plot the price trends of both exchanges against one another, highlighting every point they intersect (= recommendation change). I would also add in a daily price delta, showing the % change and raw price change since the start of the day. Finally, I would also improve asthetics using animation libraries in React.
