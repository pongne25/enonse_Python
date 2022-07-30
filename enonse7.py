# ranplase charakte avan vwayel yo pa asteriks

def ranplaseVwayel(test_str, K):
    vwayelYo = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    nouvoLis = []

    lisVwayel = list(test_str)

    for char in lisVwayel:

        for char2 in vwayelYo:

            if char == char2:
                nouvoLis.append(char)

                break


        else:
            nouvoLis.append(K)

    return (''.join(nouvoLis))


mo = "Melissa"

K = "*"

print("mo a te:", mo)
print("asteriks la:", K)

print("Nouvo mo an se:",
      ranplaseVwayel(mo, K))