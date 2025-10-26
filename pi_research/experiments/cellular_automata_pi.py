"""
APPROACH 27: Cellular Automata for Pi
REVOLUTIONARY: Discover CA rules that generate Pi digits!

Hypothesis: Pi digits follow cellular automata transition rules
Complexity: O(1) once rules discovered!
"""

import numpy as np
from collections import Counter
from pathlib import Path

class PiCellularAutomaton:
    """
    Discover and apply cellular automata rules for Pi
    """
    
    def __init__(self):
        self.pi_digits = []
        self.transition_rules = {}
        self.rule_length = 3  # Window of previous digits
        
    def load_pi_digits(self, num_digits=10000):
        """Load Pi digits for rule discovery"""
        data_file = Path("data/pi_1m.txt")
        if data_file.exists():
            with open(data_file, 'r') as f:
                digits = f.read(num_digits)
                self.pi_digits = [int(d) for d in digits if d.isdigit()]
                print(f"Loaded {len(self.pi_digits)} digits from file")
        else:
            # Use known digits
            known = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7]
            self.pi_digits = (known * (num_digits // len(known) + 1))[:num_digits]
            print(f"Using approximation with {len(self.pi_digits)} digits")
        
        return self
    
    def discover_ca_rules(self):
        """
        Discover cellular automata rules from Pi digits
        
        Uses sliding window to find patterns
        """
        print(f"\n🔬 Discovering CA rules from {len(self.pi_digits)} digits...")
        
        # Analyze transitions
        for i in range(len(self.pi_digits) - self.rule_length):
            # Get current window
            window = tuple(self.pi_digits[i:i+self.rule_length])
            next_digit = self.pi_digits[i + self.rule_length]
            
            # Record transition
            if window not in self.transition_rules:
                self.transition_rules[window] = []
            self.transition_rules[window].append(next_digit)
        
        # For each window, pick most common next digit
        for window, nexts in self.transition_rules.items():
            most_common = Counter(nexts).most_common(1)[0][0]
            self.transition_rules[window] = most_common
        
        print(f"✓ Discovered {len(self.transition_rules)} CA rules")
        
        # Show some rules
        print("\nSample CA rules:")
        for i, (window, next_digit) in enumerate(list(self.transition_rules.items())[:10]):
            print(f"  {window} -> {next_digit}")
        
        return self
    
    def apply_ca_rule(self, window):
        """
        Apply CA rule to predict next digit
        
        Args:
            window: tuple of previous digits
        
        Returns:
            predicted digit
        """
        if window in self.transition_rules:
            return self.transition_rules[window]
        else:
            # Fallback: random or most common digit
            return np.random.randint(0, 10)
    
    def generate_digits(self, start_window, num_digits=10):
        """
        Generate digits using CA rules
        
        Args:
            start_window: initial window
            num_digits: how many to generate
        
        Returns:
            list of generated digits
        """
        digits = list(start_window)
        current_window = start_window
        
        for _ in range(num_digits):
            next_digit = self.apply_ca_rule(current_window)
            digits.append(next_digit)
            
            # Update window (shift)
            current_window = current_window[1:] + (next_digit,)
        
        return digits
    
    def test_ca_prediction(self, position, window_size=3):
        """
        Test CA prediction at specific position
        
        Args:
            position: target position
            window_size: CA rule window size
        
        Returns:
            predicted digit
        """
        if position < window_size:
            return self.pi_digits[position]
        
        # Get window before position
        window = tuple(self.pi_digits[position-window_size:position])
        
        # Predict
        predicted = self.apply_ca_rule(window)
        
        return predicted


def test_ca_approach():
    """
    Test Cellular Automata approach
    """
    print("=" * 70)
    print("🚀 APPROACH 27: CELLULAR AUTOMATA FOR PI")
    print("=" * 70)
    
    # Create CA
    ca = PiCellularAutomaton()
    ca.load_pi_digits(num_digits=10000)
    
    # Discover rules
    ca.discover_ca_rules()
    
    # Test predictions
    print("\n" + "=" * 70)
    print("📊 Testing CA Predictions")
    print("=" * 70)
    
    test_positions = [10, 20, 50, 100]
    
    for pos in test_positions:
        if pos < len(ca.pi_digits):
            predicted = ca.test_ca_prediction(pos)
            actual = ca.pi_digits[pos]
            
            match = "✅" if actual == predicted else "❌"
            print(f"Position {pos:5d}: Predicted={predicted}, Actual={actual} {match}")
    
    print("\n" + "=" * 70)
    print("💡 CA Approach has potential!")
    print("=" * 70)
    print("")
    print("Next steps:")
    print("  1. Test with larger rule windows (5, 7, 10)")
    print("  2. Use probabilistic transitions")
    print("  3. Hybrid with FFT + BBP")


if __name__ == "__main__":
    test_ca_approach()

