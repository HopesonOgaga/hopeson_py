house_price = 1000000
credit_score_good = False
if credit_score_good:
    down_payment = house_price * 0.1
else:
     down_payment= house_price * 0.2
print(f"down payment:${round(down_payment)}")