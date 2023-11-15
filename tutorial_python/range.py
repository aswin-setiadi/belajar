def main():
    # these won't be printed
    for i in range(1, 1):
        print(i)
    for i in range(0):
        print(i)
    # 2,1,0
    for j in range(2, -1, -1):
        print(j)


if __name__ == "__main__":
    main()
