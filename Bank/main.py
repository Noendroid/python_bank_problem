import math

from Customer import Customer


def get_customers_from_file(file_name):
    details = []
    with open(file_name, "r") as customers_file:
        for line in customers_file:
            details.append(line.split("\t"))
    arr = []
    for d in details[2:]:
        c = Customer(d)
        arr.append(c)
    return arr


def get_average_values(customers):
    average_values = []
    for i in range(len(customers[0].attributes)):
        average_values.append(0)

    num_of_customers = len(customers)

    for customer in customers:
        for i, item in enumerate(customer.attributes):
            average_values[i] += float(item)

    average_values = [x / num_of_customers for x in average_values]

    return average_values


def get_deviation_values(customers, average_values):
    #   to calculate the divination we need to:
    #   1) for each number: subtract the Mean and square the result     -> (Xi - u)^2
    #   2) work out the mean of those squared differences               -> sum = ((x1-u)^2 + ... + (xN-u)^2)) / (N - 1)
    #   3) Take the square root of that                                 -> sqrt(sum)

    div = []
    for i in range(len(average_values)):
        div.append(0)

    num_of_customers = len(customers)

    for customer in customers:
        for i, xi in enumerate(customer.attributes):
            v = math.pow(xi - average_values[i], 2)
            div[i] += v

    div = [xi / (num_of_customers - 1) for xi in div]
    div = [math.sqrt(xi) for xi in div]
    return div


# def distribution(customer, averages, deviations):
#     for i in range(len(averages)):
#         customer.distribution.append(0)
#
#     for i in range(len(averages)):
#         part1 = (1 / (math.sqrt(2 * math.pi) * deviations[i]))
#         part2 = math.pow(math.e, -0.5 * math.pow(customer.attributes[i] - averages[i], 2))
#         d = part1 * part2
#         customer.distribution[i] = d
#     print(customer.distribution)


def mahalanobis_distance(new_customer, average, deviation, c):
    part1 = 0
    for i, a in enumerate(new_customer.attributes):
        part1 += math.pow(((a - average[i]) / deviation[i]), 2)

    part2 = 0
    for i, d in enumerate(deviation):
        part2 += math.log(d)
    part2 *= 2

    part3 = 2 * math.log(c)

    return part1 + part2 - part3


def main():
    safe_customers = get_customers_from_file("customers_safe.TXT")
    risky_customers = get_customers_from_file("customers_risky.TXT")
    new_customers = get_customers_from_file("customers_new.TXT")

    # low risk - 0.8 | high risk - 0.2
    C1 = 0.7
    C2 = 0.3

    #   calculate the average values to x1,...,x6 for risky and safe customers
    safe_average = get_average_values(safe_customers)
    risky_average = get_average_values(risky_customers)

    #   calculate the deviation values to x1,...,x6 for risky and safe customers
    safe_div = get_deviation_values(safe_customers, safe_average)
    risky_div = get_deviation_values(risky_customers, risky_average)

    new_low_customers = []
    new_high_customers = []

    low_risk = mahalanobis_distance(new_customers[0], safe_average, safe_div, C1)
    high_risk = mahalanobis_distance(new_customers[0], risky_average, risky_div, C2)

    low_min = low_risk
    low_max = low_risk
    high_min = high_risk
    high_max = high_risk

    for i, customer in enumerate(new_customers):
        low_risk = mahalanobis_distance(customer, safe_average, safe_div, C1)
        high_risk = mahalanobis_distance(customer, risky_average, risky_div, C2)

        customer.low = low_risk
        customer.high = high_risk

        if low_risk >= high_risk:
            new_low_customers.append(customer)
        else:
            new_high_customers.append(customer)

        if low_min > low_risk:
            low_min = low_risk

        if low_max < low_risk:
            low_max = low_risk

        if high_min > high_risk:
            high_min = high_risk

        if high_max < high_risk:
            high_max = high_risk

    with open("output_data_q1.TXT", "w") as output:
        output.write("safe" + "\t" + "1" + "\t" + "risky" + "\t" + "0" + "\n")
        for i, c in enumerate(new_customers):
            safe = 1
            if c.low > c.high:
                safe = 0
            output.write(str(i) + "\t" + str(safe) + "\n")

        print("number of LOW risk customers:\t" + str(len(new_low_customers)))
        print("number of HIGH risk customers:\t" + str(len(new_high_customers)))

        print("LOW RISK CUSTOMERS - \tL\t\t\t\t\tH")
        for c in new_low_customers:
            print("\t\tCustomer " + str(new_customers.index(c)) + "\t\t" + str(c.low) + "\t" + str(c.high))
        print("HIGH RISK CUSTOMERS - \tL\t\t\t\t\tH")
        for c in new_high_customers:
            print("\t\tCustomer " + str(new_customers.index(c)) + "\t\t" + str(c.low) + "\t" + str(c.high))


if __name__ == '__main__':
    main()
