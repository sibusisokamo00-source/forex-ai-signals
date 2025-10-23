from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from datetime import datetime
import ta

app = Flask(__name__)
CORS(app)

class AISignalGenerator:
    def generate_signal(self, symbol):
        # Generate mock price data
        np.random.seed(hash(symbol) % 10000)
        prices = np.cumsum(np.random.randn(100) * 0.001) + 1.1200
        
        # Simple signal logic
        signals = ['STRONG_BUY', 'BUY', 'HOLD', 'SELL', 'STRONG_SELL']
        weights = [0.2, 0.25, 0.1, 0.25, 0.2]
        signal = np.random.choice(signals, p=weights)
        confidence = np.random.uniform(0.6, 0.95)
        
        return {
            'symbol': symbol,
            'signal': signal,
            'confidence': round(confidence, 3),
            'price': round(prices[-1], 5),
            'timestamp': datetime.now().isoformat()
        }

ai_generator = AISignalGenerator()

@app.route('/')
def home():
    return jsonify({"message": "Forex AI Signals API", "status": "active"})

@app.route('/api/signals')
def get_all_signals():
    symbols = ['EURUSD', 'GBPUSD', 'USDJPY', 'XAUUSD']
    signals = []
    
    for symbol in symbols:
        signal = ai_generator.generate_signal(symbol)
        signals.append(signal)
    
    return jsonify(signals)

if __name__ == '__main__':
    app.run(debug=True)
