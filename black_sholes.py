import math

def black_scholes_calculator(S, K, T, r, sigma):
    """
    Υπολογίζει την τιμή Option και τα Greeks.
    S: Τρέχουσα Τιμή Μετοχής
    K: Τιμή Εξάσκησης 
    T: Χρόνος μέχρι τη λήξη
    r: Επιτόκιο 
    sigma: Μεταβλητότητα 
    """
    
    # 1. Υπολογισμός d1 και d2
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # Συνάρτηση Κανονικής Κατανομής (N) και Πυκνότητας Πιθανότητας (N')
    def N(x):
        return 0.5 * (1 + math.erf(x / math.sqrt(2)))
    
    def N_prime(x):
        return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x ** 2)

    # 2. Υπολογισμός Τιμών (Call & Put)
    call_price = S * N(d1) - K * math.exp(-r * T) * N(d2)
    put_price = K * math.exp(-r * T) * N(-d2) - S * N(-d1)

    # 3. Υπολογισμός Greeks (για Call Option)
    delta = N(d1)
    gamma = N_prime(d1) / (S * sigma * math.sqrt(T))
    vega = S * math.sqrt(T) * N_prime(d1)
    
    # Theta (Τύπος για ετήσια βάση, διαιρούμε συχνά με 365 για ημερήσιο)
    theta_part1 = -(S * N_prime(d1) * sigma) / (2 * math.sqrt(T))
    theta_part2 = -r * K * math.exp(-r * T) * N(d2)
    theta = theta_part1 + theta_part2

    # Εκτύπωση Αποτελεσμάτων
    print("-" * 30)
    print(f"📊 ΑΠΟΤΕΛΕΣΜΑΤΑ BLACK-SCHOLES")
    print("-" * 30)
    print(f"Τρέχουσα Τιμή (S): {S}€")
    print(f"Τιμή Στόχος (K):   {K}€")
    print(f"Χρόνος (T):        {T} έτη")
    print(f"Μεταβλητότητα:     {sigma*100}%")
    print("-" * 30)
    print(f"💰 Call Price:     {call_price:.2f}€")
    print(f"📉 Put Price:      {put_price:.2f}€")
    print("-" * 30)
    print(f"GREEKS (Δείκτες Ρίσκου):")
    print(f"Δ (Delta): {delta:.4f}  (Πιθανότητα & Ταχύτητα)")
    print(f"Γ (Gamma): {gamma:.4f}  (Επιτάχυνση)")
    print(f"v (Vega):  {vega/100:.4f}  (Ευαισθησία στο 1% volat.)")
    print(f"Θ (Theta): {theta/365:.4f} (Χασούρα ανά ημέρα)")
    print("-" * 30)

S = 80      # Τρέχουσα Τιμή
K = 85      # Τιμή Εξάσκησης
T = 2.0     # Χρόνος (σε έτη)
r = 0.05    # Επιτόκιο (5%)
sigma = 0.25 # Μεταβλητότητα (25%)

black_scholes_calculator(S, K, T, r, sigma)