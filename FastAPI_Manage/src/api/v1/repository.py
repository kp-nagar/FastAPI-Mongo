def insert_user(session, db, username, email, password, lastname=None):
    user_data = {
        'username': username,
        'email': email,
        'password': password,
        'lastname': lastname
    }
    user_collection = session.client.db.UserInformation

    # Add new user data to 'UserInformation' collection
    user_collection.insert_one(user_data, session=session)
    print("Add user successful")
    return True