import os
from flask import render_template, session, redirect, url_for, flash, request
from . import terrain
from .. import db
from app.models import *
from .forms import DemandeForm, MutationForm, TitreForm
from datetime import date, datetime
from flask_login import current_user
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = '/home/marshall/Documents/Cadastre/app/uploads'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@terrain.route('/')
@terrain.route('/home')
def accueil():
    db.create_all()
    return render_template('terrain/home.html')


@terrain.route('/detail/<idTerrain>')
def detail(idTerrain):
    terrain = Terrain.query.get(int(idTerrain))
    if terrain is None:
        return redirect(url_for('notFound'))
    else:
        return render_template('terrain/detail.html', terrain = terrain)

@terrain.route('/a-vendre')
def sold():
    terrains = Terrain.query.all()
    return render_template('terrain/vente.html', terrains=terrains)

@terrain.route('/bail', methods=['POST', 'GET'])
def demandeBail():
    form = DemandeForm()
    types = TypeProprietaire.query.all()
    form.profil.choices = [(sec.id, sec.libelle) for sec in types]

    if form.is_submitted():
        terrain = Terrain.query.filter_by(numero=form.terrain.data).first()
        if terrain is None:
            flash('Terrain inexistant')
            return render_template('terrain/demande.html', form=form)
    
        demande = Demande()
        typeDemande = TypeDemande.query.filter_by(libelle="Bail").first()
        demande.type_demande = typeDemande.id
        demande.date = date.today()
        demande.numero = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        demande.etat = "En attente"
        demande.terrain_id = terrain.id
        acte = request.files['acte']
        if acte and allowed_file(acte.filename):
            filename = secure_filename(acte.filename)
            acte.save(os.path.join(UPLOAD_FOLDER, filename))
            demande.acte = os.path.join(UPLOAD_FOLDER, filename)
        plan = request.files['plan']
        if plan and allowed_file(plan.filename):
            filename = secure_filename(plan.filename)
            plan.save(os.path.join(UPLOAD_FOLDER, filename))
            demande.plan = os.path.join(UPLOAD_FOLDER, filename)

        if current_user.is_authenticated:
            demande.landlord_id = current_user.id  
        else:
            prop = Proprietaire.query.filter_by(identification=form.cin.data).first()    
            if prop is None:
                prop = Proprietaire(identification=form.cin.data, nom=form.nom.data, prenom=form.prenom.data, email=form.email.data,\
                password = form.password.data, type_proprio = form.profil.data)  
                db.session.add(prop)
                db.session.commit()  
            demande.landlord_id = prop.id
        db.session.add(demande)
        db.session.commit()
        flash('Demande envoyee')
    return render_template('terrain/demande.html', form=form)

@terrain.route('/titre', methods=['POST', 'GET'])
def demandeTitre():
    form = TitreForm()
    types = TypeProprietaire.query.all()
    form.profil.choices = [(sec.id, sec.libelle) for sec in types]

    if form.is_submitted():
        terrain = Terrain.query.filter_by(numero=form.terrain.data).first()
        if terrain is None:
            flash('Terrain inexistant')
            return render_template('terrain/demande.html', form=form)
    
        demande = Demande()
        typeDemande = TypeDemande.query.filter_by(libelle="Titre Foncier").first()
        demande.type_demande = typeDemande.id
        demande.date = date.today()
        demande.etat = "En attente"
        demande.numero = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        demande.terrain_id = terrain.id
        acte = request.files['acte']
        if acte and allowed_file(acte.filename):
            filename = secure_filename(acte.filename)
            acte.save(os.path.join(UPLOAD_FOLDER, filename))
            demande.acte = os.path.join(UPLOAD_FOLDER, filename)
        plan = request.files['plan']
        if plan and allowed_file(plan.filename):
            filename = secure_filename(plan.filename)
            plan.save(os.path.join(UPLOAD_FOLDER, filename))
            demande.plan = os.path.join(UPLOAD_FOLDER, filename)

        if current_user.is_authenticated:
            demande.landlord_id = current_user.id  
        else:
            prop = Proprietaire.query.filter_by(identification=form.cin.data).first()    
            if prop is None:
                prop = Proprietaire(identification=form.cin.data, nom=form.nom.data, prenom=form.prenom.data, email=form.email.data,\
                password = form.password.data, type_proprio = form.profil.data)  
                db.session.add(prop)
                db.session.commit()  
            demande.landlord_id = prop.id
        db.session.add(demande)
        db.session.commit()
        flash('Demande envoyee')
    return render_template('terrain/demande.html', form=form)

@terrain.route('/mutation', methods=['POST', 'GET'])
def demandeMutation():
    form = MutationForm()
    types = TypeProprietaire.query.all()
    form.profil.choices = [(sec.id, sec.libelle) for sec in types]

    if form.is_submitted():
        titre = TitreFoncier.query.filter_by(numero=form.terrain.data).first()
        if terrain is None:
            flash('Titre Foncier inexistant')
            return render_template('terrain/demande.html', form=form)
    
        demande = Demande()
        typeDemande = TypeDemande.query.filter_by(libelle="Mutation").first()
        demande.type_demande = typeDemande.id
        demande.date = date.today()
        demande.etat = "En attente"
        demande.numero = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
        demande.terrain_id = terrain.id
        acte = request.files['acte']
        if acte and allowed_file(acte.filename):
            filename = secure_filename(acte.filename)
            acte.save(os.path.join(UPLOAD_FOLDER, filename))
            demande.acte = os.path.join(UPLOAD_FOLDER, filename)
        plan = request.files['plan']
        if plan and allowed_file(plan.filename):
            filename = secure_filename(plan.filename)
            plan.save(os.path.join(UPLOAD_FOLDER, filename))
            demande.plan = os.path.join(UPLOAD_FOLDER, filename)

        if current_user.is_authenticated:
            demande.landlord_id = current_user.id  
        else:
            prop = Proprietaire.query.filter_by(identification=form.cin.data).first()    
            if prop is None:
                prop = Proprietaire(identification=form.cin.data, nom=form.nom.data, prenom=form.prenom.data, email=form.email.data,\
                password = form.password.data, type_proprio = form.profil.data)  
                db.session.add(prop)
                db.session.commit()  
            demande.landlord_id = prop.id
        db.session.add(demande)
        db.session.commit()
        flash('Demande envoyee')
    return render_template('terrain/demande.html', form=form)

@terrain.route('/espace-client/avoir')
def espace():
    data = db.session.query(Terrain, Proprietaire, Bail, TitreFoncier, Region, Departement, Arrondissement, Secteur)\
        .filter(Terrain.id == TitreFoncier.terrain_id, Terrain.id == Bail.terrain_id,\
            Proprietaire.id == TitreFoncier.proprietaire_id, Proprietaire.id == Bail.owner_id,\
                Terrain.secteur_id == Secteur.id, Secteur.arrondissement_id == Arrondissement.id,\
                    Arrondissement.departement_id == Departement.id, Departement.region_id == Region.id).all()
    return render_template('terrain/espace.html', data=data)

@terrain.route('/vente/<idTerrain>')
def vente(idTerrain):
    terrain = Terrain.query.filter_by(id=idTerrain)
    if terrain is None:
        return redirect(url_for('notFound'))
    else:
        terrain.etat = True
        db.session.add(terrain)
        db.session.commit()
        return redirect(url_for('terrain.espace'))

@terrain.route('/espace-client/demande')
def espace1():
    data = db.session.query(Terrain, Proprietaire, Demande, TypeDemande, Region, Departement, Arrondissement, Secteur)\
        .filter(Terrain.id == Demande.terrain_id, TypeDemande.id == Demande.type_demande,\
            Proprietaire.id == Demande.landlord_id,\
                Terrain.secteur_id == Secteur.id, Secteur.arrondissement_id == Arrondissement.id,\
                    Arrondissement.departement_id == Departement.id, Departement.region_id == Region.id).all()
    return render_template('terrain/espace_.html', data=data)


@terrain.route('/annuler/<idDemande>')
def cancel(idDemande):
    demande = Demande.query.filter_by(id=idDemande)
    if demande is None:
        return redirect(url_for('notFound'))
    else:

        db.session.delete(demande)
        db.session.commit()
        return redirect(url_for('terrain.espace1'))