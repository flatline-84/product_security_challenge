import os

class Config:
    # hostname = 'localhost'
    # Need to bind to all addresses as WSL doesn't like localhost >:(
    # Just WSL sucks. Why bind to the wrong interface WSL, why
    hostname = os.getenv('HOST') or 'localhost'
    port = os.getenv('PORT') or '8080'
    debug = os.getenv('DEBUG') or True
    secret_key = os.getenv('SECRET_KEY') or 'sdiu0qioje2019j1pmdn*&%&%&^%@987098@)(80'
    # BCrypt automatically does this for us now
    # salt = os.getenv('SALT') or '29830970sdu0osidu'
    db_conn_string = 'sqlite:///zenchair.sqlite3'

    # Log file
    log_file = 'zenchair.log'

    # For IP filtering
    allowed_subnet = '0.0.0.0/0'

    # Naughty counter (for login locking)
    naughty_counter = 5