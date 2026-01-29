import time
import numpy as np
import pandas as pd

def benchmark_solution(func, data):
    """
    The Ergodic Judge: Tests for Accuracy and Latency.
    """
    # 1. Accuracy Check
    try:
        # Pre-calculated 'Ground Truth' for the specific data
        expected_output = (data['bid_vol'] - data['ask_vol']) / (data['bid_vol'] + data['ask_vol'])
        user_output = func(data)
        
        if not np.allclose(user_output, expected_output, atol=1e-8):
            return "FAIL: Accuracy mismatch. Check your math."
    except Exception as e:
        return f"FAIL: Execution error - {str(e)}"

    # 2. Latency Benchmarking
    start_time = time.perf_counter()
    for _ in range(100):  # Run 100 times to get a stable average
        func(data)
    end_time = time.perf_counter()
    
    avg_latency_ms = ((end_time - start_time) / 100) * 1000
    
    return f"PASS: Avg Latency = {avg_latency_ms:.4f} ms"

# Example of what the 'User' would submit
def user_submission(df):
    return (df['bid_vol'] - df['ask_vol']) / (df['bid_vol'] + df['ask_vol'])

# Mock Data for testing
test_data = pd.DataFrame({
    'bid_vol': np.random.rand(1000000),
    'ask_vol': np.random.rand(1000000)
})

print(f"Result: {benchmark_solution(user_submission, test_data)}")
