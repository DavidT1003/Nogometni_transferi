# Nogometni_transferi
Aplikacija omogućuje korisnicima dodavanje i uređivanje informacija o klubovima i igračima te omogućuje kupnju i prodaju igrača između klubova.

### Funkcionalnosti
1. dodaj_klub - Dodavanje novog kluba putem POST zahtjeva.
2. dodaj_igraca - Dodavanje novog igrača putem POST zahtjeva.
3. kupi_igraca - Kupnja igrača i dodjela mu kluba putem POST zahtjeva.
4. prodaj_igraca - Prodaja igrača i oslobađanje ga iz kluba putem POST zahtjeva.
5. uredi_cijenu_igraca - Uređivanje cijene igrača putem POST zahtjeva.
6. obrisi_klub - Brisanje kluba i oslobađanje igrača putem POST zahtjeva.
7. promijeni_ime_kluba - Promjena imena kluba putem POST zahtjeva.

### Pokretanje aplikacije
Za pokretanje aplikacije, potrebno je slijediti ove korake:
Prvo, instalirali Docker na svom računalu, te preuzeti sve datoteke koje su dostupne na GitHub repozitoriju i sačuvati ih u odabranu mapu na svom računalu.
Nakon toga otvoriti CMD na svom računalu. Navigirati do mape sa spremljenim datotekama uz naredbu cd kako bismo je premjestili u direktorij gdje smo sačuvali preuzete datoteke.
Upotrijebiti sljedeću naredbu kako bismo stvorili Docker image: docker build -t transferi/pis-flask:0.0.1.RELEASE .
Ova naredba stvara Docker image imenovanu transferi/pis-flask verzije 0.0.1.RELEASE iz trenutnog direktorija (.).
Nakon što smo izgradili Docker image, treba pokrenuti kontejner koristeći sljedeću naredbu: docker container run -d -p 5000:5000 transferi/pis-flask:0.0.1.RELEASE
Ova naredba pokreće Docker kontejner na portu 5000 i usmjerava ga na port 5000 unutar kontejnera. Kontejner je izgrađen na temelju image koju smo prethodno stvorili.
Nakon što je kontejner pokrenut, pristupamo aplikaciji putem web preglednika. 
Otvorite preglednik i unijeti sljedeću adresu: http://localhost:5000
Sada možemo koristiti aplikaciju i pristupiti njezinim funkcionalnostima putem web preglednika.




