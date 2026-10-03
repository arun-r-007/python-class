"""The brain of our lemonade stand. Pure maths, easy to test.""" 
 
 
def total_sales(cups, price_per_cup): 
    """Money we collect from customers.""" 
    if cups < 0: 
        raise ValueError("Cups sold cannot be negative") 
    if price_per_cup <= 0: 
        raise ValueError("Price must be more than zero") 
    return cups * price_per_cup 
 
 
def profit(cups, price_per_cup, cost_per_cup): 
    """Money we keep after paying for lemons and sugar.""" 
    return total_sales(cups, price_per_cup) - cups * cost_per_cup