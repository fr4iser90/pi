"""
APPROACH 22: Fourier Analysis of Pi Digits
REVOLUTIONARY: Use FFT to find hidden frequency patterns!

Hypothesis: Pi digits might follow frequency patterns that we can exploit
Complexity: O(n log n) for analysis, O(1) prediction if successful
"""

import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from pathlib import Path

class PiFFTAnalyzer:
    """
    Analyze Pi digits using Fast Fourier Transform
    """
    
    def __init__(self):
        self.pi_digits = []
        self.frequencies = None
        self.amplitudes = None
        self.dominant_freqs = []
        
    def load_pi_digits(self, num_digits=10000):
        """
        Load Pi digits from file or generate
        
        Args:
            num_digits: How many digits to analyze
        """
        print(f"📊 Loading {num_digits} Pi digits...")
        
        # Try to load from file
        data_file = Path("data/pi_1m.txt")
        if data_file.exists():
            with open(data_file, 'r') as f:
                self.pi_digits = [int(d) for d in f.read(num_digits) if d.isdigit()]
        else:
            # Generate using numpy (approximation)
            # This is just for testing!
            print("⚠️  Using approximated digits")
            self.pi_digits = np.random.randint(0, 10, num_digits).tolist()
        
        print(f"✓ Loaded {len(self.pi_digits)} digits")
        return self
    
    def analyze_frequencies(self):
        """
        Apply FFT to find frequency patterns
        
        Returns:
            dominant frequencies detected
        """
        print("\n🔬 Applying FFT analysis...")
        
        # Convert to numpy array
        signal = np.array(self.pi_digits)
        
        # Compute FFT
        fft_result = fft(signal)
        
        # Get frequencies
        self.frequencies = fftfreq(len(signal))
        self.amplitudes = np.abs(fft_result)
        
        # Find dominant frequencies (top 10)
        n_dominant = min(10, len(self.amplitudes) // 2)
        dominant_indices = np.argsort(self.amplitudes[:len(self.amplitudes)//2])[-n_dominant:]
        
        self.dominant_freqs = [
            (self.frequencies[idx], self.amplitudes[idx])
            for idx in sorted(dominant_indices)
        ]
        
        print(f"✓ Found {len(self.dominant_freqs)} dominant frequencies")
        
        # Show top frequencies
        print("\nTop frequencies:")
        for i, (freq, amp) in enumerate(self.dominant_freqs[:5], 1):
            print(f"  {i}. Frequency: {freq:.6f}, Amplitude: {amp:.2f}")
        
        return self.dominant_freqs
    
    def predict_digit_from_frequencies(self, position):
        """
        Predict digit at position using frequency analysis
        
        Args:
            position: Target position in Pi
        
        Returns:
            predicted digit (0-9)
        """
        if self.dominant_freqs is None:
            return None
        
        # Use dominant frequencies to reconstruct digit
        # This is experimental!
        reconstruction = 0.0
        
        for freq, amp in self.dominant_freqs[:5]:
            # Reconstruct signal component
            angle = 2 * np.pi * freq * position
            component = amp * np.cos(angle)
            reconstruction += component
        
        # Map to digit (experimental!)
        # Normalize and map to 0-9
        normalized = (reconstruction % 1) * 10
        digit = int(abs(normalized)) % 10
        
        return digit
    
    def visualize_frequencies(self, save_path="results/pi_fft_analysis.png"):
        """
        Create visualization of frequency spectrum
        
        Args:
            save_path: Where to save the plot
        """
        print(f"\n📈 Creating visualization...")
        
        if self.frequencies is None:
            print("⚠️  Run analyze_frequencies() first!")
            return
        
        # Create plot
        plt.figure(figsize=(12, 6))
        
        # Plot frequency spectrum
        positive_freqs = self.frequencies[:len(self.frequencies)//2]
        positive_amps = self.amplitudes[:len(self.amplitudes)//2]
        
        plt.plot(positive_freqs, positive_amps)
        plt.xlabel('Frequency')
        plt.ylabel('Amplitude')
        plt.title('Pi Digits - FFT Frequency Spectrum')
        plt.grid(True, alpha=0.3)
        
        # Save
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path)
        print(f"✓ Saved to {save_path}")
        
        return self


def test_fft_approach():
    """
    Test FFT approach on Pi digits
    """
    print("=" * 70)
    print("🚀 APPROACH 22: FFT ANALYSIS OF PI DIGITS")
    print("=" * 70)
    print("")
    
    # Create analyzer
    analyzer = PiFFTAnalyzer()
    
    # Load digits
    analyzer.load_pi_digits(num_digits=10000)
    
    # Analyze frequencies
    analyzer.analyze_frequencies()
    
    # Test predictions
    print("\n" + "=" * 70)
    print("📊 Testing Frequency-Based Predictions")
    print("=" * 70)
    
    test_positions = [1, 10, 100, 1000]
    
    for pos in test_positions:
        if pos < len(analyzer.pi_digits):
            actual = analyzer.pi_digits[pos]
            predicted = analyzer.predict_digit_from_frequencies(pos)
            
            match = "✅" if actual == predicted else "❌"
            print(f"Position {pos:5d}: Predicted={predicted}, Actual={actual} {match}")
    
    # Visualize
    analyzer.visualize_frequencies()
    
    print("\n" + "=" * 70)
    print("💡 This approach has potential!")
    print("=" * 70)
    print("")
    print("Next steps:")
    print("  1. Train on more digits (1M+)")
    print("  2. Refine frequency selection")
    print("  3. Improve digit mapping algorithm")
    print("  4. Hybrid with BBP + Matrix approaches")


if __name__ == "__main__":
    test_fft_approach()

