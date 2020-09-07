from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import EmailField


class DemandeForm(FlaskForm):
    cin = StringField("CIN", validators=[DataRequired()])
    nom = StringField("Nom", validators=[DataRequired()])
    prenom = StringField("Prenom", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    adresse = TextAreaField("Adresse", validators=[DataRequired()])
    profil = SelectField("Type")
    acte = FileField("Demande de bail", validators=[DataRequired("Choisir un fichier")])
    plan = FileField("Plan du terrain", validators=[DataRequired("Choisir un fichier")])
    terrain = StringField("Numero du terrain", validators=[DataRequired()])
    submit = SubmitField("Envoyer")

class MutationForm(FlaskForm):
    cin = StringField("CIN", validators=[DataRequired()])
    nom = StringField("Nom", validators=[DataRequired()])
    prenom = StringField("Prenom", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    adresse = TextAreaField("Adresse", validators=[DataRequired()])
    profil = SelectField("Type")
    acte = FileField("Acte de vente ou de donation", validators=[DataRequired("Choisir un fichier")])
    plan = FileField("Plan du terrain", validators=[DataRequired("Choisir un fichier")])
    terrain = StringField("NICAD", validators=[DataRequired()])
    submit = SubmitField("Envoyer")

class TitreForm(FlaskForm):
    cin = StringField("CIN", validators=[DataRequired()])
    nom = StringField("Nom", validators=[DataRequired()])
    prenom = StringField("Prenom", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    adresse = TextAreaField("Adresse", validators=[DataRequired()])
    profil = SelectField("Type")
    acte = FileField("Acte de vente ou de donation", validators=[DataRequired("Choisir un fichier")])
    plan = FileField("Plan du terrain", validators=[DataRequired("Choisir un fichier")])
    terrain = StringField("Numero du terrain", validators=[DataRequired()])
    submit = SubmitField("Envoyer")