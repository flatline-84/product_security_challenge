class Config:
    # hostname = 'localhost'
    # Need to bind to all addresses as WSL doesn't like localhost >:(
    # Just WSL sucks. Why bind to the wrong interface WSL, why
    hostname = '0.0.0.0'
    port = '8080'
    debug = True
    secret_key = 'sdiu0qioje2019j1pmdn*&%&%&^%@987098@)(80' #TODO: fix this
    salt = '29830970sdu0osidu'
    db_conn_string = 'sqlite:///zenchair.sqlite3'

    # For IP filtering
    allowed_subnet = '0.0.0.0/0'