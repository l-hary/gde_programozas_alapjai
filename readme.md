# GDE Programozási alapok 2024 projekt feladat

A program elérhető [ezen](https://progal-ksh-lhary.streamlit.app/) a linken is, viszont az ingyenes felhasználói fiókokra érvényes korlátozások miatt szükség lehet az applikáció "felébresztésére".

Amennyiben ez sikertelen, a lenti lépésekkel saját számítógépen is tesztelhető a program.

Az instrukcióknál feltételezzük a Git és egy Python telepítés (lehetőleg 3.10+) meglétét. 

1. Hozzuk létre a repositoryt saját gépünkön a `git clone https://github.com/l-hary/gde_programozas_alapjai` paranccsal majd lépjünk be a könyvtárba.
2. A könyvtárban hozzunk létre egy Python virtuális környezetet. Ezt legkönnyebben a `python -m venv venv` paranccsal tehetjük meg. Operációs rendszertől és telepítéstől függően lehetséges, hogy a Pythont más paranccsal kell meghívnunk, legvalószínűbb a `python3` vagy telepített verzió egzakt specifikálása, például `python3.12`
3. Aktiváljuk a virtuális környezetet;
   Windowson: `\venv\scripts\activate`
   Linuxon/Macen: `source venv/bin/activate`
4. A virtuális környezet sikeres aktviálása után telepítsük a szükséges modulokat: 
   `pip install -r requirements.txt`
5. A programot az alábbi paranccsal futtathatjuk: 
    `streamlit run main.py`
6. Modulok megfelelő telepítése esetén egy új böngészőablakban megnyílik a program. 
