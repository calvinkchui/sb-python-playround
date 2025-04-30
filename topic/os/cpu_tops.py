## Geneate by Gemini-1.5 Pro
## WIP - not work

import time
import numpy as np

def calculate_flops(size, iterations):
    """Calculates approximate FLOPS for matrix multiplication."""
    a = np.random.rand(size, size).astype(np.float32)  # Use float32 for single-precision
    b = np.random.rand(size, size).astype(np.float32)

    start_time = time.time()
    for _ in range(iterations):
        c = np.matmul(a, b)
    end_time = time.time()

    elapsed_time = end_time - start_time
    flops = (2  * size **3 ) * iterations  / elapsed_time  # 2*n^3 FLOPs for n x n matrix multiplication ; fix
    return flops

if __name__ == "__main__":
    matrix_size = 2048  # Adjust matrix size
    num_iterations = 10  # Adjust number of iterations

    flops = calculate_flops(matrix_size, num_iterations)
    tops = flops / 1e12  # Convert to TOPS

    print(f"Estimated FLOPS: {flops:.2e}")
    print(f"Estimated TOPS: {tops:.2e}")