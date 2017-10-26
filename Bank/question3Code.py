from Customer import Customer
from main import get_average_values
from main import get_deviation_values
from main import mahalanobis_distance
from main import get_customers_from_file


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

    for i, customer in enumerate(new_customers):
        low_risk = mahalanobis_distance(customer, safe_average, safe_div, C1)
        high_risk = mahalanobis_distance(customer, risky_average, risky_div, C2)

        customer.low = low_risk
        customer.high = high_risk

    with open("output_data_q3.TXT", "w") as output:
        output.write("safe" + "\t" + "1" + "\n" + "risky" + "\t" + "0" + "\n")
        for i, c in enumerate(new_customers):
            safe = 1
            if c.low > c.high:
                safe = 0
            output.write(str(i) + "\t" + str(safe) + "\n")


if __name__ == '__main__':
    main()
