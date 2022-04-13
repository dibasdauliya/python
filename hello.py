
# input
bill_amt = input("What is your bill amount?")
tip_amt = input('How much tip do you wanna give us? 15%, 18% or 20%?')

# input filtration
final_bill_amt = bill_amt.replace("$", "")
final_tip_amt = tip_amt.replace("%", "")

# calculations
final_bill_value = float(final_bill_amt)
final_tip_value = final_bill_value * (int(final_tip_amt) / 100)

grand_final_bill = final_bill_value + final_tip_value


print(f"Your bill amount is: {final_bill_value:.2f} \nYour tip amount is: {final_tip_value:.2f} \nYour FINAl amount is: {grand_final_bill:.2f} \nWe'd love to see you again. 😊")