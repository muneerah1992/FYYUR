from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, ValidationError, BooleanField, IntegerField
from wtforms.validators import DataRequired, URL, Length, Regexp
from choicesenum import ChoicesEnum


class States(ChoicesEnum):
    AL = 'AL'
    AK = 'AK'
    AZ = 'AZ'
    AR = 'AR'
    CA = 'CA'
    CO = 'CO'
    CT = 'CT' 
    DE = 'DE'
    DC = 'DC'
    FL = 'FL'
    GA = 'GA'
    HI = 'HI'
    ID = 'ID'
    IL = 'IL'
    IN = 'IN'
    IA = 'IA'
    KS = 'KS'
    KY = 'KY'
    LA = 'LA'
    ME = 'ME'
    MT = 'MT'
    NE = 'NE'
    NV = 'NV'
    NH = 'NH'
    NJ = 'NJ'
    NM = 'NM'
    NY = 'NY'
    NC = 'NC'
    ND = 'ND'
    OH = 'OH'
    OK = 'OK'
    OR = 'OR'
    MD = 'MD'
    MA = 'MA'
    MI = 'MI'
    MN = 'MN'
    MS = 'MS'
    MO = 'MO'
    PA = 'PA'
    RI = 'RI'
    SC = 'SC'
    SD = 'SD'
    TN = 'TN'
    TX = 'TX'
    UT = 'UT'
    VT = 'VT'
    VA = 'VA'
    WA = 'WA' 
    WV = 'WV'
    WI = 'WI'
    WY = 'WY'

class Genres(ChoicesEnum):
    Alternative = 'Alternative'
    Blues = 'Blues'
    Classical = 'Classical'
    Country = 'Country'
    Electronic = 'Electronic'
    Folk = 'Folk'
    Funk = 'Funk'
    HipHop = 'Hip-Hop'
    HeavyMetal = 'Heavy Metal'
    Instrumental = 'Instrumental'
    Jazz = 'Jazz'
    Musical_Theatre = 'Musical Theatre'
    Pop = 'Pop'
    Punk = 'Punk'
    RandB = 'R&B'
    Reggae = 'Reggae'
    RocknRoll = 'Rock n Roll'
    Soul = 'Soul'
    Other = 'Other'

class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(Form):

    name = StringField(
        'name', validators=[DataRequired(),Length(max=120)]
    )
    city = StringField(
        'city', validators=[DataRequired(),Length(max=120)]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices= States.choices()
    )
    address = StringField(
        'address', validators=[DataRequired(),Length(max=120)]
    )
    phone = StringField(
        'phone', validators=[DataRequired(), Length(max=13,min=10)]
    )
    image_link = StringField(
        'image_link', validators=[URL(), Length(max=500), DataRequired()]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices= Genres.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(), DataRequired()]
    )
    website = StringField(
        'website', validators=[URL()]
    )
    seeking_talent = BooleanField(
        'seeking_talent'
    )
    seeking_description = StringField(
        'seeking_description', validators=[URL(),Length(max=500)]
    )

class ArtistForm(Form):
    
    name = StringField(
        'name', validators=[DataRequired(),Length(max=120)]
    )
    city = StringField(
        'city', validators=[DataRequired(),Length(max=120)]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices= States.choices()
    )
    phone = StringField(
        'phone', validators=[DataRequired(), Length(max=13,min=10)]
    )
    image_link = StringField(
        'image_link', validators=[URL(), Length(max=500), DataRequired()]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices= Genres.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(), DataRequired()]
    )
    website = StringField(
        'website', validators=[URL()]
    )
    seeking_venue = BooleanField(
        'seeking_venue'
    )
    seeking_description = StringField(
        'seeking_description', validators=[URL(),Length(max=500)]
    )