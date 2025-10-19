# generator comprehension

sales = [1,2,3,10,8,5,6,7]

# total sales
total_sales = sum(x for x in sales if x > 5)

print(total_sales)