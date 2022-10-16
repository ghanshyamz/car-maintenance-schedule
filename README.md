# car-maintenance-schedule
Flask-RESTful API
```
API:
All POST APIs to be receive and send JSON data
1. /user/create [POST]
  a. Desc: Create new user
  b. Parameters:
    i. "name": string
    ii. "phone_no" : "10 digit numeric string"
  c. Returns:
    i. {
      ‘error’: 0 if no error, 1 if error,
      ‘error-message’: error message if error, “” if no error
      }
      
2. /user/getall [GET]
  a. Desc: get list of all users
  b. Parameters: 
  c. Returns:
    i. {
      ‘error’: 0 if no error, 1 if error,
      ‘error-message’: error message if error, “” if no error”,
      ‘Users’: [
        {‘id’: 1, ‘name’: ‘abc’, ‘phone-number’: 1231231234}
        ]
      }


3. /user/get/<id> [GET]
a. Desc: get user with id: <id>
b. Parameters:
c. Returns:
  i. {
      ‘error’: 0 if no error, 1 if error,
      ‘error-message’: error message if error, “” if no error”,
      ‘User’: {
       ‘id’: <id>, 
       ‘name’: ‘abc’, 
       ‘phone-number’: 123123,
        ‘Cars’: [
        {‘Id’: 1, ‘Model’: ‘Maruti 800’, ‘Color’: ‘Green’, ‘Purchase-date’: 2019/12/23}
          ]
      }
    }


4. /car/create [POST]
a. Desc: Create new car
b. Parameters:
  i. model : string
  ii. color : string
  iii. ownerid : int (userid)
  iv. purchase_date : string in YYYY/MM/DD format
c. Returns:
    i. {
      ‘error’: 0 if no error, 1 if error,
      ‘error-message’: error message if error, “” if no error”
    }
    
5. /car/getall [POST]
a. Desc: get list of all cars for a user
b. Parameters:
  i. userid : int (User id)
c. Returns:
  i. {
    ‘error’: 0 if no error, 1 if error,
    ‘error-message’: error message if error, “” if no error”,
    ‘Cars’: [
      {
        ‘Id’: 1,
        ‘Model’: ‘Maruti 800’,
        ‘Color’: ‘Green’,
        ‘Purchase-date’: 2019/10/23
      }
    ]
   }


6. /car/get/<id> [GET]
a. Desc: get car with id: <id>
b. Parameters:
c. Returns:
  i. {
    ‘error’: 0 if no error, 1 if error,
    ‘error-message’: error message if error, “” if no error”,
    ‘Car’: {
      ‘id’: <id>, 
      ‘model’: 
      ‘Maruti 800’, 
      ‘purchase-date’: 2019/10/23,
      ‘Servicing’: [
      { ‘Id’: 1, servicing-date’: 2019/12/30, ‘Status’: ‘Finished’}
        ]
   }
  }
  
  
7. /servicing/create [POST]
a. Desc: Create new servicing entry
b. Parameters:
  i. carid : integer
  ii. servicing_date : string in YYYY/MM/DD format
  iii. Status : string
c. Returns:
  i. {
    ‘error’: 0 if no error, 1 if error,
    ‘error-message’: error message if error, “” if no error”
  }

8. /servicing/getall [POST]
a. Desc: get list of all servicings for a car
b. Parameters:
  i. carid : int (Car id)
c. Returns:
  i. {
    ‘error’: 0 if no error, 1 if error,
    ‘error-message’: error message if error, “” if no error”,
    ‘servicings’: [
        {
          ‘Id’: 1,
          ‘servicing-date’:2019/12/30,
          ‘Status’: ‘Finished’
        }
      ]
  }
```
