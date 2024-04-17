def calculate_product():
    # Calculate the average of three numbers obtains from the user. Then
    # multiply the result by 4.17, and assign it to the product variable.
    #
    # Return the value passed to the product variable and use it
    # for the subsequent x to y calculations to speed up the process.
    sum_numbers = 0

    for number in range(0, 3):
        number = float(input("Enter a number"))
        sum_numbers += number

    average = (sum_numbers / 3) * 4.17
    product = average
    return product


product_calc = calculate_product()

print(f"Product {product_calc}")
