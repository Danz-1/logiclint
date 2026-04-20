def calculate_final_total(original_price, coupons):
    """
    Calculates the final order value after applying discount coupons.
    original_price: float
    coupons: list of floats (e.g., [0.20, 0.40] for 20% and 40% discount)
    """
    if original_price <= 0:
        return 0.0

    total_discount = sum(coupons)
    
    # Applies the discount directly (LOGIC FLAW HERE)
    # Does not check if the discount exceeds 50% according to the business rule
    final_price = original_price - (original_price * total_discount)
    
    return final_price

# Order simulation
cart_price = 100.0
# Customer applied a 30% coupon and a 40% coupon (Total: 70%)
applied_coupons = [0.30, 0.40] 

print(f"Final price: ${calculate_final_total(cart_price, applied_coupons)}")
# Current output: $30.00 (Should be $50.00 due to the 50% limit rule)