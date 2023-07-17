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
#print(visits_cart)
num_not_order = (visits_cart['cart_time'].isnull().sum())
percent_not_order = float(num_not_order) / float(len(visits_cart))
print(percent_not_order * 100)
cart_checkout = cart.merge(checkout, how = 'left')
#print(cart_checkout)
num_not_checkout = (cart_checkout['checkout_time'].isnull().sum())
percent_not_checkout = num_not_checkout / (float(num_not_checkout) + cart_checkout['checkout_time'].count())
print(percent_not_checkout * 100)

all_data = visits_cart.merge(cart_checkout, how='left').merge(purchase, how='left')
#print(all_data.head())

reached_checkout = all_data[~all_data['checkout_time'].isnull()]

#Ensure purchase time is not null and check that checkout time has a value
checkout_not_purchase = all_data[(all_data.purchase_time.isnull()) & (~all_data.checkout_time.isnull())]


checkout_not_purchase_percent = float(len(checkout_not_purchase)) / float(len(reached_checkout))
print(checkout_not_purchase_percent * 100)
# 16.8 percent
#The weakest part of the funnel is getting a user to add a t-shirt to their cart. Once this is achieved the next part of the process happens much more frequently. If Cool T-Shirts Inc. gets more people to add t-shirts to their cart then they will fix a large problem.

#Total time spent on the website
all_data['total_time'] = (all_data.purchase_time - all_data.visit_time)
print(all_data.total_time)

#Average time on website
avg_time = all_data.total_time.mean()
print(avg_time)
