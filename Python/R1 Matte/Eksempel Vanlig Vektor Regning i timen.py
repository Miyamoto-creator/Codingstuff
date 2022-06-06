"Først må vi importere array fr abiblioteket. Brukes for å kunne skrive vektorer i python"
"Eksempel vanlig vektor regning"

from numpy import array

while True:
    # U-VEKTOR
    x_u = float(input("Gi x-verdi til u-vektor: "))
    y_u = float(input("Gi y-verdi til u-vektor: "))

    # V-VEKTOR
    x_v = float(input("Gi x-verdi til v-vektor: "))
    y_v = float(input("Gi y-verdi til v-vektor: "))

    # SUMMER
    u = array([x_u, y_u])
    v = array([x_v, y_v])

    print(f"u + v = {u + v}\n"
          f"u - v = {u - v}\n"
          f"3u + 2v = {3 * u + 2 * v}")
