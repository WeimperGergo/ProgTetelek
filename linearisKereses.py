def lin_kereses():
    also = 42
    felso = 67
    i = also
    while i <= felso and not i % 10 == 0:
        i += 1
    van = i <= felso    # MI <- van?
    if van:
        print("Van 0-ra végződő szám: " + str(i))
    else:
        print("Nincs 0-ra végződő szám.")


lin_kereses()

