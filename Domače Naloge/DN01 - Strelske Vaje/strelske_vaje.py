import math
# Rok za oddajo: sreda, 12. oktober 2022, 11.15

"""
Napiši program za izračun dolžine strela s topom (ki brez trenja izstreljuje točkaste krogle v brezzračnem prostoru,
a pustimo trivio). Program od uporabnika ali uporabnice zahteva, da mu ta vpiše hitrost izstrelka in kot, pod katerim
je izstreljena (krogla, ne uporabnica). Program izračuna in izpiše, kako daleč bo letela krogla.

Preverite tole: krogla leti najdalj, če jo izstrelimo pod kotom 45 stopinj. Poskusite, kako daleč gre pod kotom 45 in
kako daleč pod 46 stopinj - po 45 mora leteti dlje. In če pod kotom 50 stopinj leti nazaj (razdalja je negativna), ste
ga gotovo nekje polomili. Kaj, točno, je narobe, vam lahko hitro sčveka kolega, ki je že rešil problem, vendar vam
priporočam, da ga poskusite odkriti sami - za vajo v sledenju programu. Za namig lahko poškilite na del Wikipedijine
strani o kotih.

(Če je g enak 9.807, mora krogla, izstreljena z 10 m/s po kotom 45 stopinj preleteti približno 10.196798205363516
metrov. Če je g 10, pa 10 metrov.)
"""

hitrost_izstrelka = float(input("Vnesite hitrost izstrelka: "))
kot_izstrelka = float(input("Vnesite kot izstrelka: "))
g = 9.807

#https://physics.stackexchange.com/questions/107933/how-to-calculate-distance-travelled-from-velocity-vector-and-angle
dolzina_strela = (hitrost_izstrelka**2 * math.sin(2 * math.radians(kot_izstrelka))) / g

print("Dolžina strela s topom je: " + str(dolzina_strela) + " m")
