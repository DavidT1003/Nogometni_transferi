from flask import Flask, render_template, request, redirect, url_for
from pony.orm import Database, PrimaryKey, Required, db_session, Set, Optional

app = Flask(__name__)

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

class Klub(db.Entity):
    id = PrimaryKey(int, auto=True)
    ime = Required(str)
    drzava = Required(str)
    budzet = Required(float)
    igraci = Set('Igrac')

class Igrac(db.Entity):
    id = PrimaryKey(int, auto=True)
    ime = Required(str)
    prezime = Required(str)
    cijena = Required(float)
    pozicija = Required(str)
    klub = Optional(Klub, nullable=True)

db.generate_mapping(create_tables=True)

@app.route('/')
@db_session
def index():
    klubovi = Klub.select()
    igraci = Igrac.select()
    slobodni_igraci = [i for i in Igrac.select() if i.klub is None]
    return render_template('index.html', klubovi=klubovi, igraci=igraci, slobodni_igraci=slobodni_igraci)

@app.route('/dodaj_klub', methods=['POST'])
@db_session
def dodaj_klub():
    ime = request.form['ime']
    drzava = request.form['drzava']
    budzet = float(request.form['budzet'])
    klub = Klub(ime=ime, drzava=drzava, budzet=budzet)
    return redirect(url_for('index'))

@app.route('/dodaj_igraca', methods=['POST'])
@db_session
def dodaj_igraca():
    ime = request.form['ime']
    prezime = request.form['prezime']
    cijena = float(request.form['cijena'])
    pozicija = request.form['pozicija']
    igrac = Igrac(ime=ime, prezime=prezime, cijena=cijena, pozicija=pozicija)
    return redirect(url_for('index'))

@app.route('/kupi_igraca/<int:igrac_id>', methods=['POST'])
@db_session
def kupi_igraca(igrac_id):
    klubovi = Klub.select()
    slobodni_igraci = [i for i in Igrac.select() if i.klub is None]
    igrac = Igrac[igrac_id]

    if request.method == 'POST':
        klub_id = int(request.form['klub_id'])
        klub = Klub[klub_id]
        klub.budzet -= igrac.cijena
        klub.igraci.add(igrac)
        igrac.klub = klub
        return redirect(url_for('index'))

    return render_template('index.html', klubovi=klubovi, slobodni_igraci=slobodni_igraci)

@app.route('/prodaj_igraca/<int:igrac_id>', methods=['POST'])
@db_session
def prodaj_igraca(igrac_id):
    igrac = Igrac[igrac_id]
    if igrac.klub:
        klub = igrac.klub
        klub.budzet += igrac.cijena
        klub.igraci.remove(igrac)
        igrac.delete()
    return redirect(url_for('index'))

@app.route('/uredi_cijenu_igraca/<int:igrac_id>', methods=['POST'])
@db_session
def uredi_cijenu_igraca(igrac_id):
    nova_cijena = float(request.form['nova_cijena'])
    igrac = Igrac[igrac_id]
    igrac.cijena = nova_cijena
    return redirect(url_for('index'))

@app.route('/obrisi_klub/<int:klub_id>', methods=['POST'])
@db_session
def obrisi_klub(klub_id):
    klub = Klub[klub_id]
    for igrac in klub.igraci:
        igrac.klub = None
    klub.delete()
    return redirect(url_for('index'))

@app.route('/promijeni_ime_kluba/<int:klub_id>', methods=['POST'])
@db_session
def promijeni_ime_kluba(klub_id):
    klub = Klub[klub_id]
    novo_ime = request.form['novo_ime']
    klub.ime = novo_ime
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int("5000"),)

