class Query:
    CREATE_TABLE="""
    CREATE TABLE IF NOT EXISTS User(
        username TEXT,
        password TEXT
        phone_number TEXT,
        email TEXT,
        role TEXT
        adhaar_card_number TEXT
        
        )
    """
    CREATE_USER = """
              INSERT INTO User(
                username,
                password,
                phone_number,
                email,
                role,
                adhaar_card_number 
            ) VALUES(?,?, ?, ?, ?,?,?)
        """

    CREATE_TABLE_RIDE = """
        CREATE TABLE IF NOT EXISTS Ride(
            ride_id TEXT,
            departure TEXT,
            destination TEXT,
            date  TEXT,
            vehicle_registration_number TEXT
            )
        """
    CREATE_RIDE = """
            INSERT INTO Ride(
                ride_id,
                station,
                date,
                distance,
                total_distance,
                vehicle_registration_number,
                time,
                sequence_number
            ) VALUES(?,?,?,?,?,?,?,?)
    """

    CREATE_VEHICLE = """
                INSERT INTO Vehicle(
                    vehicle_registration_number,
                    vehicle_brand,
                    vehicle_name,
                    sitting_capacity
                ) VALUES(?,?,?,?)
        """

    CREATE_RIDE_MAPPING="""
    INSERT INTO UserRideMapping(
        id,
        rider_name,
        ride_id1,
        ride_id2
    ) VALUES(?,?,?,?)
    """
    CREATE_VEHICLE_MAPPING = """
       INSERT INTO UserVehicleMapping(
           id,
           publisher_name,
           vehicle_registration_number
       ) VALUES(?,?,?)
       """

    PRAGMA_QUERY="""
    PRAGMA foreign_keys=on
    """
    GET_ALL_USERS="""
    SELECT * FROM user
    """

    GET_USER_CREDENTIALS="""
    SELECT * FROM User WHERE username = ? AND password = ?
    """

    GET_VEHICLE="""
    SELECT * FROM Vehicle where vehicle_name=?
    """

    GET_VEHICLE_BY_REGISTRATION_NO = """
        SELECT * FROM Vehicle where vehicle_registration_number=?
        """

    GET_RIDE_BY_RIDE_NO="""
    SELECT station,date,time FROM Ride where ride_id=?
    """

    GET_RIDE_DETAILS_FROM_RIDE_TABLE="""
    SELECT * FROM Ride where vehicle_registration_number=? and date=?
    """

    GET_VEHICLES = """
        SELECT * FROM Vehicle
        """

    GET_USER_VEHICLE_MAPPING="""
    SELECT vehicle_registration_number FROM UserVehicleMapping where publisher_name = ?
    """

    GET_AVAILABLE_RIDES="""
    SELECT station,date,distance,vehicle_registration_number,time,sequence_number from Ride where station = ? and date=?  
    """
    SEARCH_RIDES = """SELECT r1.ride_id, r2.ride_id, r1.station,r2.station, r1.date, r1.distance,r2.distance,r1.total_distance, r1.time, r2.time FROM Ride r1
     JOIN Ride r2 ON r1.vehicle_registration_number = r2.vehicle_registration_number AND 
     r1.station = ? AND r2.station = ? AND r1.sequence_number < r2.sequence_number"""

    GET_USER_RIDE_MAPPING = """
    SELECT * FROM UserRideMapping where rider_name = ?
    """
    GET_RIDE_BY_RIDE_ID="""
    SELECT * FROM UserRideMapping where id=?
    """
    DELETE_VEHICLE="""
    DELETE FROM UserVehicleMapping where publisher_name = ? and vehicle_registration_number = ? 
    """
    DELETE_VEHICLE_FROM_VEHICLE = """
        DELETE FROM Vehicle where vehicle_registration_number = ? 
        """

    DELETE_RIDE_FROM_MAPPING = """
        DELETE FROM UserRideMapping where id = ? 
        """
    DELETE_RIDE_FROM_RIDE = """
            DELETE FROM Ride where ride_id = ? 
            """

