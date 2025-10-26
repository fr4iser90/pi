"""
Bailey-Borwein-Plouffe Algorithm
Calculates nth HEXADECIMAL digit of Pi in O(log n)
Reference: https://www.maa.org/sites/default/files/pdf/upload_library/22/Chauvenet/Plouffe1996.pdf
"""
import decimal
from decimal import Decimal, getcontext

# Set precision for calculations
getcontext().prec = 100

def pi_bbp_digit_single(n, b=16):
    """
    Calculate the nth hexadecimal digit of Pi
    Returns single digit at position n
    
    Formula:
    π = Σ(k=0 to ∞) [1/(16^k)] * [4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6)]
    
    Args:
        n: digit position (1-indexed)
        b: base (default 16 for hexadecimal)
    
    Returns:
        hexadecimal digit (0-15)
    """
    def S(j, n):
        """Helper function for BBP formula"""
        s = Decimal(0)
        k = 0
        # Calculate sum up to n terms
        while k <= n:
            if 8 * k + j != 0:
                s += Decimal(1) / (16 ** k * (8 * k + j))
            k += 1
        return s
    
    # BBP formula
    result = (4 * S(1, n) - 2 * S(4, n) - S(5, n) - S(6, n))
    
    # Extract fractional part
    fractional = result % 1
    
    # Get digit: multiply by 16 and take integer part
    digit_value = int((fractional * 16) % 16)
    
    return hex(digit_value)[2:]  # Return as hex character


def pi_bbp_digits(n, num_digits=1):
    """
    Get multiple hex digits starting from position n
    
    Args:
        n: starting position
        num_digits: how many digits to return
    """
    digits = []
    for i in range(num_digits):
        digit = pi_bbp_digit_single(n + i)
        digits.append(digit)
    return ''.join(digits)


def bbp_to_decimal_approximation(hex_digits):
    """
    Convert hex string to decimal approximation
    Note: This is approximate, not exact
    
    Args:
        hex_digits: string of hex digits
    
    Returns:
        decimal approximation
    """
    total = Decimal(0)
    for i, char in enumerate(hex_digits):
        value = int(char, 16)
        total += value / (Decimal(16) ** (i + 1))
    return float(total)


if __name__ == "__main__":
    # Test with known positions
    print("Testing BBP Algorithm:")
    print("=" * 50)
    
    test_positions = [1, 2, 3, 10, 100, 1000, 10000]
    
    for pos in test_positions:
        hex_digit = pi_bbp_digit_single(pos)
        print(f"Position {pos:6d}: Hex = {hex_digit}")
    
    print("\nMultiple digits:")
    print(pi_bbp_digits(1, 20))

