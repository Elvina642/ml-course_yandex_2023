import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    v = np.random.rand(data.shape[1])
    for i in range(num_steps):
        v_new = data.dot(v)
        lam = (v.dot(v_new)) / (v.dot(v))
        v = v_new / np.linalg.norm(v_new)

    return float(lam), v