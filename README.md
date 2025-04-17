# Assignment3test
The following document demonstrates both the functionality and purpose of the provided Python script. The programming code enables staff to enter product prices alongside total cost calculations while verifying request approval status for products referred to as requisitions. The final decision depends on the complete cost of all chosen items.

1. Staff and Requisition Identification
The program requires staff users to provide their ID and requisition ID before the code starts. The provided functionality helps track both the requesting staff member and monitors individual purchase requests from workforce members.
2. Entering Product Prices
The program demands two price entries following the entry of identification numbers. The program saves these product prices into two variables named price1 and price2. The program attempts to find the total cost through an addition of price1 along with price2 and price3. The program contains a programming error because price3 is missing from the input requests to the user. The program will run into an error since price3 has not been defined. Either the price3 entry needs removal or the user should input the price through the program.

3. Approval or Pending Status
The program executes a condition to verify whether the total price stands below $500. The program sets the requisition status to "approved" when total price surpasses $500. A total price of $500 or above marks the requisition status as "pending". The automatic approval system of tiny purchases while controlling extensive payments makes this feature beneficial to organizations that need it.

4. Displaying Information
After obtaining staff ID and requisition ID together with total cost and status the program generates a basic report that displays all information to the user.

5. Additional Product Details
The following segment of the program requests information about three products along with their corresponding prices. The code stores all necessary details in product_1, product_2, product_3 and price_1, price_2, price_3 variables. The program collects the entered prices before computing and showing the complete total expense.
