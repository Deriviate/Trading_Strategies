import numpy as np
import matplotlib.pyplot as plt

def plot_strategy(prices, pnl, strategy_name, breakeven_lines=[]):
    plt.figure(figsize=(10, 6))
    
    
    plt.fill_between(prices, pnl, 0, where=(pnl >= 0), facecolor='green', alpha=0.3, label='Κέρδος')
    plt.fill_between(prices, pnl, 0, where=(pnl < 0), facecolor='red', alpha=0.3, label='Ζημιά')
    plt.plot(prices, pnl, color='black', linewidth=2)


    plt.axhline(0, color='black', linestyle='--') 
    plt.title(f"Διάγραμμα Κέρδους: {strategy_name}", fontsize=16, fontweight='bold')
    plt.xlabel("Τιμή Μετοχής στη Λήξη (€)", fontsize=12)
    plt.ylabel("Κέρδος / Ζημιά (€)", fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.show()



def long_call(S, K, premium):
    # Κέρδος = Max(S - K, 0) - Premium
    return np.maximum(S - K, 0) - premium

def long_put(S, K, premium):
    # Κέρδος = Max(K - S, 0) - Premium
    return np.maximum(K - S, 0) - premium

def short_stock(S, entry_price):
    # Short Selling: Κέρδος = Τιμή Εισόδου - Τωρινή Τιμή
    return entry_price - S

def protective_put(S, stock_entry, K, put_premium):
    # Κέρδος Μετοχής + Κέρδος Put
    stock_pnl = S - stock_entry
    put_pnl = np.maximum(K - S, 0) - put_premium
    return stock_pnl + put_pnl

def covered_call(S, stock_entry, K, call_premium):
    # Κέρδος Μετοχής + (Premium Call - Ζημιά Call αν ασκηθεί)
    stock_pnl = S - stock_entry
    short_call_pnl = call_premium - np.maximum(S - K, 0)
    return stock_pnl + short_call_pnl

def butterfly_spread(S, K_low, K_mid, K_high, net_debit):
    # Long Call (Low) + Long Call (High) - 2 * Short Call (Mid)
    payoff_low = np.maximum(S - K_low, 0)
    payoff_high = np.maximum(S - K_high, 0)
    payoff_mid = 2 * np.maximum(S - K_mid, 0)
    return (payoff_low + payoff_high - payoff_mid) - net_debit

def iron_condor(S, K1_put_long, K2_put_short, K3_call_short, K4_call_long, net_credit):
    
    
    # 1. Put Spread (Κάτω μέρος)
    put_long_payoff = np.maximum(K1_put_long - S, 0)
    put_short_payoff = -np.maximum(K2_put_short - S, 0) 
    
    # 2. Call Spread (Πάνω μέρος)
    call_short_payoff = -np.maximum(S - K3_call_short, 0)
    call_long_payoff = np.maximum(S - K4_call_long, 0)
    
    # Σύνολο + Αρχική Είσπραξη (Credit)
    return (put_long_payoff + put_short_payoff + call_short_payoff + call_long_payoff) + net_credit


# Δημιουργία εύρους τιμών μετοχής (π.χ. από 50€ έως 150€)
prices = np.arange(50, 150, 1)

# 1. ΠΑΡΑΔΕΙΓΜΑ: LONG CALL (Κερδοσκοπία Άνοδος)
# Στόχος 100€, Κόστος 3€
pnl_call = long_call(prices, K=100, premium=3)
plot_strategy(prices, pnl_call, "Long Call (Bullish)")

# 2. ΠΑΡΑΔΕΙΓΜΑ: PROTECTIVE PUT (Προστασία)
# Αγόρασες μετοχή στα 100€, Put Strike 95€, Κόστος Put 2€
pnl_prot = protective_put(prices, stock_entry=100, K=95, put_premium=2)
plot_strategy(prices, pnl_prot, "Protective Put (Hedging)")

# 3. ΠΑΡΑΔΕΙΓΜΑ: COVERED CALL (Εισόδημα)
# Έχεις μετοχή στα 100€, Πουλάς Call στο 110€, Εισπράττεις 3€
pnl_cov = covered_call(prices, stock_entry=100, K=110, call_premium=3)
plot_strategy(prices, pnl_cov, "Covered Call (Income)")

# 4. ΠΑΡΑΔΕΙΓΜΑ: BUTTERFLY SPREAD (Σκοπευτής)
# Strikes: 90-100-110. Πλήρωσες συνολικά 2€ για να το φτιάξεις
pnl_fly = butterfly_spread(prices, K_low=90, K_mid=100, K_high=110, net_debit=2)
plot_strategy(prices, pnl_fly, "Butterfly Spread (Neutral Precision)")

# 5. ΠΑΡΑΔΕΙΓΜΑ: IRON CONDOR (Ψαράς / Εύρος)
# Strikes: 85-90 (Puts) και 110-115 (Calls). Εισέπραξες συνολικά 4€
pnl_condor = iron_condor(prices, K1_put_long=85, K2_put_short=90, K3_call_short=110, K4_call_long=115, net_credit=4)
plot_strategy(prices, pnl_condor, "Iron Condor (Neutral Range)")

# 6. ΠΑΡΑΔΕΙΓΜΑ: SHORT SELLING (Ανοιχτή Πώληση)
# Πούλησες "αέρα" στα 100€
pnl_short = short_stock(prices, entry_price=100)
plot_strategy(prices, pnl_short, "Short Selling (Bearish)")