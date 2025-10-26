"""
POC: Matrix Exponentiation Approach
Revolutionary idea: Represent Pi digits as Markov Chain

Hypothesis: Each digit position is the result of a hidden Markov process
If we can find the transition matrix M, then:
- digit at position n = (M^n)[initial_state]

Complexity: O(log n) via fast matrix exponentiation!
"""

import numpy as np
from scipy.linalg import expm

class PiMatrixExponentiation:
    """
    Revolutionary approach using Matrix Exponentiation
    """
    
    def __init__(self, training_data=None):
        """
        Initialize with transition matrix
        
        Args:
            training_data: List of known Pi digits to learn transition patterns
        """
        self.M = None  # Transition matrix
        
        if training_data:
            self.learn_transition_matrix(training_data)
        else:
            # Initialize with random/standard transition matrix
            self.M = self._initialize_matrix()
    
    def _initialize_matrix(self):
        """
        Initialize 10x10 transition matrix (digits 0-9)
        Starts with equal probabilities
        """
        # Uniform distribution (will be replaced with learned data)
        return np.ones((10, 10)) / 10
    
    def learn_transition_matrix(self, digits):
        """
        Learn transition matrix from known Pi digits
        
        Args:
            digits: list of known Pi digits (e.g., [3,1,4,1,5,9,...])
        """
        M = np.zeros((10, 10))
        
        # Count transitions
        for i in range(len(digits) - 1):
            current = digits[i]
            next_digit = digits[i + 1]
            M[current][next_digit] += 1
        
        # Normalize rows (convert to probabilities)
        row_sums = M.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1  # Avoid division by zero
        self.M = M / row_sums
        
        print(f"Learned transition matrix from {len(digits)} digits")
        print("Top transitions:")
        for i in range(10):
            top_j = np.argmax(self.M[i])
            print(f"  {i} -> {top_j} (prob = {self.M[i][top_j]:.3f})")
    
    def calculate_digit(self, n, initial_state=None):
        """
        Calculate nth digit using matrix exponentiation
        
        Args:
            n: position
            initial_state: starting distribution over digits
        
        Returns:
            predicted digit
        """
        if initial_state is None:
            # Start with uniform distribution
            initial_state = np.ones(10) / 10
        
        # Fast matrix exponentiation: M^n
        # Instead of calculating M^n directly, we use exponentiation
        # M^n = exp(n * log(M))
        
        try:
            # Method 1: Direct exponentiation
            M_power_n = np.linalg.matrix_power(self.M, n)
        except:
            # Fallback: exponential formula
            M_power_n = expm(n * np.log(self.M + 1e-10))
        
        # Apply to initial state
        final_state = M_power_n @ initial_state
        
        # Return most likely digit
        predicted_digit = int(np.argmax(final_state))
        confidence = float(np.max(final_state))
        
        return predicted_digit, confidence, final_state
    
    def calculate_digit_range(self, n_start, n_end):
        """
        Calculate multiple digits efficiently
        """
        results = []
        for n in range(n_start, n_end):
            digit, confidence, _ = self.calculate_digit(n)
            results.append(digit)
        return results


def test_matrix_approach():
    """
    Test matrix exponentiation approach
    """
    print("=" * 60)
    print("MATRIX EXPONENTIATION POC")
    print("=" * 60)
    
    # For testing, we need some known Pi digits
    # In production, download from PILookup
    known_pi_digits = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7]
    
    # Initialize model
    model = PiMatrixExponentiation(training_data=known_pi_digits[:30])
    
    # Test predictions
    print("\nPredictions:")
    for n in [1, 5, 10, 15, 20]:
        digit, confidence, distribution = model.calculate_digit(n)
        actual = known_pi_digits[n-1] if n-1 < len(known_pi_digits) else "?"
        print(f"Position {n:2d}: Predicted={digit}, Actual={actual}, Confidence={confidence:.3f}")
    
    print("\n" + "=" * 60)
    print("NOTE: This is a POC - needs more data and refinement!")
    print("=" * 60)


if __name__ == "__main__":
    test_matrix_approach()

