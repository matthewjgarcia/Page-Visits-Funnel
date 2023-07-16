import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#inspect the data frames
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

#left merge
visits_cart = visits.merge(cart, how='left')
print(visits_cart)
print(visits_cart['cart_time'].isnull().sum())
