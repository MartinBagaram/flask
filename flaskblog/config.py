class Config:
    
    SECRET_KEY = '044c16e09c56ad89a1e136f98ebd0fcc'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # should be in environment variable
    MAIL_SERVER = 'stmtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '*****@gmail.com' # needs to fill in real email or set up environment variables
    MAIL_PASSWORD = '*********'  # needs to fill in real email or set up environment variables