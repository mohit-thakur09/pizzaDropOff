import csv


def order_pizza(fp, order_l):
    order_dict = {}
    for item in fp:
        print(f"{item[0]}\t\t{item[1]}\t\t\t{item[2]}")

    num = input("Enter number: ")
    for item in fp:
        if num == item[0]:
            order_dict['pizza'] = item[1]
            order_dict['pizza_price'] = int(item[2])
    print("Pizza is Booked")
    order_l.append(order_dict)


def order_cold_drinks(fp, order_l):
    order_dict = {}
    for item in fp:
        print(f"{item[0]}\t\t{item[5]}\t\t\t{item[6]}")

    num = input("Enter number: ")
    for item in fp:
        if num == item[0]:
            order_dict['drink'] = item[5]
            order_dict['drink_price'] = int(item[6])
    print("cold drink is Booked")
    order_l.append(order_dict)


def genarate_bill(order_l):
    with open("Pizza_bill.csv", "w") as fp2:
        total = []
        for i in order_l:
            fields = [x for x in i]
            fields.append('total_amt')
            file_writer = csv.DictWriter(fp2, fieldnames=fields)
            file_writer.writeheader()
            file_writer.writerow(i)
            amt = [v if ('price' in k) else 0 for k, v in i.items()]
            total.append(sum(amt))
        file_writer.writerow({"total_amt": sum(total)})


def open_csv_file():
    fp = open("pizzaDetails.csv", "r")
    fp_reader = csv.reader(fp)
    return fp, fp_reader


def close_csv_file(fp):
    fp.close()


if __name__ == "__main__":
    order_items = []
    pointer, file_reader = open_csv_file()
    file_reader = list(file_reader)

    while True:
        print("\n******************************** PIZZA FOOD APP *******************************")
        print("****************************** PLACED YOUR ORDER ******************************")
        print("\n\t1. Pizza")
        print("\t2. Cold Drinks")
        print("\t3. Exit and Get Bill")
        print("\n================================================================================")
        print("\t press 0 for cancel order.")
        print("================================================================================")

        n = int(input("\tWhat do you want: "))

        if n == 1:
            order_pizza(file_reader, order_items)
        elif n == 2:
            order_cold_drinks(file_reader, order_items)
        elif n == 3:
            genarate_bill(order_items)
            close_csv_file(pointer)
            print("\t**** thank you ****")
            break
        elif n == 0:
            print("\n\tOrder cancel ... ")
            order_items.clear()
            if input("Do you want to buy again?? (Y/N)").lower() == 'n':
                close_csv_file(pointer)
                print("\t**** thank you ****")
                exit(0)
        else:
            print("invalid number...")
