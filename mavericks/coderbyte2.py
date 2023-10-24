def StringChallenge(strParam):
    # code goes here
    # char is either alpha/ num/ space/ symbol
    num_index = None
    # swap, need to handle consecutive number, cause must at least 1 letter/ alphabet
    # must handle 3-4 should not swap
    alpha_exist = False
    ans = []
    for i, v in enumerate(strParam):
        if v.isalpha():
            # alphabet
            ans.append(v.swapcase())
            if num_index is not None:
                alpha_exist = True
        elif v.isspace():
            # space
            ans.append(v)
            if num_index is not None:
                num_index = None
            if alpha_exist:
                alpha_exist = False
        elif not v.isdigit():
            # symbols
            ans.append(v)
        else:
            # numbers
            if num_index is None:
                num_index = i
                ans.append(v)
            else:
                # swap
                if alpha_exist:
                    ans.append(ans[num_index])
                    ans[num_index] = v
                    num_index = None
                    alpha_exist = False
                else:
                    ans.append(v)
                    num_index = i
    return "".join(ans)


def main():
    ss = [
        "",
        "Hello -5LOL6",
        "2S 6 du5d4e",
        " 1s2 3-4 5 6 7a8b9c10 11de12f13G144-155h",
    ]
    for s in ss:
        ans = StringChallenge(s)
        print(f"ans={ans}")


if __name__ == "__main__":
    main()
