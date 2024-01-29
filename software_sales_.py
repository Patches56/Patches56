##Jairo Gutierrez CIS 115 Intro to python
##Software Sales 
price_per_package = 99.99
discount_amount =0
discount_percentage =0
Quantity_purchased = float(input('\nEnter the number of packages: '))

display_message = ""

if Quantity_purchased <0 or Quantity_purchased >300:
    display_message = "Error"
else:
    discount_percentage = 0
    
    if Quantity_purchased < 10:
        discount_percentage = .0 #0%
    else:
        if Quantity_purchased >= 10 and Quantity_purchased <= 19:
            discount_percentage = .10 #10%
        else:
            if Quantity_purchased >= 20 and Quantity_purchased <= 49:
                discount_percentage = .20 #20%
            else:
                if Quantity_purchased >= 50 and Quantity_purchased <= 99:
                    discount_percentage = .30 #30%
                else:
                    if Quantity_purchased >= 100 and Quantity_purchased <= 300:
                        discount_percentage = .40 #40%

package_total = Quantity_purchased * price_per_package
discount_amount = (package_total) * discount_percentage
grand_total = package_total - discount_amount
##f-strings                    
if Quantity_purchased >=0 and Quantity_purchased <=300:
    
    display_message =f'Number of packages: {Quantity_purchased:,.0f}'
    print(f'Full price: {Quantity_purchased * price_per_package:,.2f}')
    print(f'Discount percentage: {discount_percentage:.0%}')
    print(f'Discount Amount: {(package_total) * discount_percentage:,.2f}')
    print(f'Grand Total: {package_total - discount_amount:,.2f}')

print("\n" + display_message + "\n")

##TEST OUTPUT
##Enter the number of packages: 55
##Full price: 5,499.45
##Discount percentage: 30%
##Discount Amount: 1,649.83
##Grand Total: 3,849.61
##
##Number of packages: 55
##
##
##==================================================== RESTART: /Users/jairogutierrezmanzo/Desktop/Python 115/Software_sales_assignment2_CH3 copy.py ===================================================
##
##Enter the number of packages: -1
##
##Error
##
##
##==================================================== RESTART: /Users/jairogutierrezmanzo/Desktop/Python 115/Software_sales_assignment2_CH3 copy.py ===================================================
##
##Enter the number of packages: 3000
##
##Error
##
##
##==================================================== RESTART: /Users/jairogutierrezmanzo/Desktop/Python 115/Software_sales_assignment2_CH3 copy.py ===================================================
##
##Enter the number of packages: 55
##Full price: 5,499.45
##Discount percentage: 30%
##Discount Amount: 1,649.83
##Grand Total: 3,849.61
##
##Number of packages: 55


