from Customer import Customer
from main import get_average_values
from main import get_deviation_values
from main import mahalanobis_distance


def get_customers_from_file(file_name):
    details = []
    with open(file_name, "r") as customers_file:
        for line in customers_file:
            details.append(line.split(" "))
    arr = []
    for d in details:
        c = Customer(d)
        arr.append(c)
    return arr


def main():
    c1 = 0.7
    c2 = 0.3

    customers = get_customers_from_file("question2.TXT")
    for c in customers:
        print(c)

    s_avg = get_average_values(customers[:2])
    r_avg = get_average_values(customers[2:5])
    s_div = get_deviation_values(customers[:2], s_avg)
    r_div = get_deviation_values(customers[2:5], r_avg)
    s_ma = mahalanobis_distance(customers[4], s_avg, s_div, c1)
    r_ma = mahalanobis_distance(customers[4], r_avg, r_div, c2)

    print("safe M= " + str(s_ma))
    print("risky M= " + str(r_ma))

    if s_ma > r_ma:
        print("risky customer")
    else:
        print("safe customer")


if __name__ == '__main__':
    main();
