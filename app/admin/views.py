from flask import render_template, session, redirect, url_for, request, flash, jsonify
from . import admin as adminbp
from .. import db
from flask_login import login_required, login_user, logout_user
from app.models import Proprietaire, User, Secteur, Terrain, TypeProprietaire
from .forms import *
import sys
from pprint import pprint

@adminbp.route('/login', methods=['GET', 'POST'])
def login():
    form = PropLogin()
    if form.validate_on_submit():
        prop = Proprietaire.query.filter_by(email = form.email.data).first()
        if prop is not None and prop.verify_password(form.password.data):
            login_user(prop)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('terrain.accueil')
            return redirect(next) 
        flash('Login ou mot de passe incorrect')
    return render_template('admin/userlogin.html', form=form)

@adminbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@adminbp.route('/register', methods=['GET', 'POST'])
def register():
    form = PropRegister()
    types = TypeProprietaire.query.all()
    form.profil.choices = [(sec.id, sec.libelle) for sec in types]
    if form.is_submitted():
        prop = Proprietaire()
        prop.identification = form.cin.data
        prop.nom = form.nom.data
        prop.prenom = form.prenom.data
        prop.adresse = form.adresse.data
        prop.email = form.email.data
        prop.password = form.password.data
        prop.type_proprio = form.profil.data
        db.session.add(prop)
        db.session.commit()
        flash('Inscription Réussie')
        return redirect('login')

    return render_template('admin/userregister.html', form=form)

@adminbp.route('/admin', methods=['GET', 'POST'])
def adminLog():
    form = AdminLogin()

    if form.validate_on_submit():
        user = User.query.filter_by(login = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('admin.dashboard')
            return redirect(next) 
        flash('Login ou mot de passe incorrect')

    return render_template('admin/adminlogin.html', form=form)


@adminbp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = NewTerrain()
    secteurs = Secteur.query.all()
    form.secteur.choices = [(sec.id, sec.numero) for sec in secteurs]

    


    if form.is_submitted():
        terrain = Terrain()
        terrain.numero = form.numero.data
        terrain.largeur = form.largeur.data
        terrain.longueur = form.longueur.data
        terrain.secteur_id = form.secteur.data
        db.session.add(terrain)
        db.session.commit()
        flash('Terrain ajouté avec succès')

    terrains = Terrain.query.all()
    return render_template('admin/dashboard.html', form=form, array=terrains)

