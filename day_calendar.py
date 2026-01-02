def zeller_calculator():
    print("--- Υπολογισμός Ημέρας (Zeller's Algorithm) ---")
    
    try:
        # 1. Εισαγωγή δεδομένων από τον χρήστη
        d = int(input("Δώσε Ημέρα (π.χ. 25): "))
        m = int(input("Δώσε Μήνα (π.χ. 3): "))
        y = int(input("Δώσε Έτος (π.χ. 1821): "))

        # Κρατάμε τις αρχικές τιμές για τον έλεγχο του ημερολογίου
        original_day, original_month, original_year = d, m, y

        # 2. Προσαρμογή για τον αλγόριθμο του Zeller
        # Αν είναι Ιανουάριος (1) ή Φεβρουάριος (2), θεωρούνται μήνες 13 και 14 του προηγούμενου έτους
        if m < 3:
            m += 12
            y -= 1

        K = y % 100      # Έτος στον αιώνα (π.χ. 21 για το 1821)
        J = y // 100     # Αιώνας (π.χ. 18 για το 1821)
        q = d            # Ημέρα του μήνα

        # 3. Επιλογή Ημερολογίου
        # Το Γρηγοριανό εφαρμόστηκε στις 15 Οκτωβρίου 1582
        # Ελέγχουμε αν η ημερομηνία είναι πριν ή μετά από αυτήν
        
        is_gregorian = False
        
        if original_year > 1582:
            is_gregorian = True
        elif original_year == 1582:
            if original_month > 10:
                is_gregorian = True
            elif original_month == 10 and original_day >= 15:
                is_gregorian = True
        
        # 4. Υπολογισμός (h)
        if is_gregorian:
            # Τύπος Γρηγοριανού
            # h = (q + 13*(m+1)/5 + K + K/4 + J/4 - 2*J) mod 7
            h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)) % 7
            calendar_type = "Γρηγοριανό"
        else:
            # Τύπος Ιουλιανού
            # h = (q + 13*(m+1)/5 + K + K/4 + 5 - J) mod 7
            h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + 5 - J) % 7
            calendar_type = "Ιουλιανό"

        # 5. Αντιστοίχιση αποτελέσματος σε ημέρες
        # 0=Σάββατο, 1=Κυριακή, ... , 6=Παρασκευή
        days_mapping = {
            0: "Σάββατο",
            1: "Κυριακή",
            2: "Δευτέρα",
            3: "Τρίτη",
            4: "Τετάρτη",
            5: "Πέμπτη",
            6: "Παρασκευή"
        }

        result_day = days_mapping[h]

        print("-" * 30)
        print(f"Ημερομηνία: {original_day}/{original_month}/{original_year}")
        print(f"Ημερολόγιο που χρησιμοποιήθηκε: {calendar_type}")
        print(f"Η ημέρα είναι: ** {result_day} **")
        print("-" * 30)

    except ValueError:
        print("Σφάλμα: Παρακαλώ εισάγετε μόνο ακέραιους αριθμούς.")

# Εκτέλεση της συνάρτησης
if __name__ == "__main__":
    zeller_calculator()