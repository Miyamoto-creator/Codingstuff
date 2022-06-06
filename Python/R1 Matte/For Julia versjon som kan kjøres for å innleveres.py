while True:
    print("====================================")
    år = int(input("Tast inn ditt år her"))
    if år % 400 == 0:
        print(f'{år} er et skuddår')
    elif år % 4 == 0 and not år % 100 == 0:
        print(f'{år} er et skuddår')
    else:
        print(f'{år} er ikke et skuddår')