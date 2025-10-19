# dictionary comprehensions

tea_prices_inr = {
    "Masala Tea" : 40,
    "Green Tea" : 80,
    "Lemon Tea" : 140,
}

tea_prices_usd = {tea :(price/80) for tea, price in tea_prices_inr.items()}

print(tea_prices_usd)
