
import secrets, os
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail

def send_reset_email(user):
    ''' Sends a message to the user with the token necessary to reset email
    '''
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='martinobag@gmail.com',
                    recipients=[user.email])
    msg.body = f''' To reset your password , visit the following link
{url_for('users.reset_token', token=token, _external=True)}. Ignore this email 
if you did not make the  request'''
    mail.send(msg)

def save_picture(form_picture):
    '''save the file picture of the user. we will randomize 
    the name of the file

    returns picture file name so that it can be stored in the database
    '''
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext # the new name of the picture
    picture_path = os.path.join(current_app.root_path, 'static/img', picture_fn)
    # resize the picture before saving it
    output_size = (128, 128)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(picture_path)
    return picture_fn
