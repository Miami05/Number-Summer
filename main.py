SUM_LIMIT = 1000


def main():
    """
    Main function
    """
    total = 0

    while total < SUM_LIMIT:
        try:
            total += int(input("Please enter a number: "))
        except ValueError:
            print("Oops! That doesn't look like an integer. Please try again.")

    print(f"Final sum: {total}")


if __name__ == "__main__":
    main()
