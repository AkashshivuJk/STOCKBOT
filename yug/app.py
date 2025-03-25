import yfinance as yf
from flask import Flask, render_template, request
from main import questions_and_answers  # Make sure this is correctly imported
import requests

app = Flask(__name__)

# Function to fetch stock price using Alpha Vantage API
def get_stock_price(ticker):
    api_key = "YOUR_API"  # Your provided API key
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={api_key}"
    
    try:
        r = requests.get(url)
        data = r.json()

        # Extract stock price if data is returned correctly
        if "Time Series (5min)" in data:
            time_series = data["Time Series (5min)"]
            latest_timestamp = next(iter(time_series))
            stock_price = time_series[latest_timestamp]["1. open"]
            return f"The latest price for {ticker} is ${stock_price}."
        else:
            return "Unable to fetch the stock price. Please check the ticker symbol or try again later."
    except Exception as e:
        return f"Error fetching stock price: {str(e)}"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/index')
def indexxx():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    answer = get_answer(user_input)
    return render_template('index.html', user_input=user_input, answer=answer)

# Function to match question with answers
def get_answer(user_input):
    # Check if it's a predefined question
    for qa in questions_and_answers:
        if user_input.lower() in qa["question"].lower():
            return qa["answer"]
    
    # If it's a stock price query, handle it here
    if "price of" in user_input.lower() or "current price of" in user_input.lower():
        stock_symbol = user_input.lower().split("price of")[-1].strip()
        stock_symbol = stock_symbol.upper()  # Convert to uppercase to match the format in Yahoo Finance
        
        # Attempt to fetch stock price using yfinance or Alpha Vantage
        try:
            # First try Yahoo Finance
            stock = yf.Ticker(stock_symbol + ".NS")  # Adding ".NS" for NSE-listed stocks
            stock_info = stock.history(period="1d")  # Get the latest data
            price = stock_info['Close'][0]  # Latest closing price
            return f"The current price of {stock_symbol} is ₹{price:.2f}"
        
        except Exception as yf_error:
            # Fallback to Alpha Vantage if Yahoo Finance fails
            return get_stock_price(stock_symbol)

    # Default response if no match
    return "Sorry, I don't have an answer to that question."

if __name__ == '__main__':
    app.run(debug=True)
