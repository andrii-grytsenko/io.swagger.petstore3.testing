user_add = [
    ('{"id":9910,"username":"user9910","firstName":"John","lastName":"James","email":"john@email.com",'
     '"password":"9910","phone":"9910","userStatus":1}', 200),
    ('{"id":9910,"username":"user9910","firstName":"John","lastName":"James","email":"john@email.com",'
     '"password":"9910","phone":"9910","userStatus":1}', 400),
    ('{"id":9911,"username":"user9911","firstName":"John","lastName":"James","email":"john@email.com",'
     '"password":"9911","phone":"9911","userStatus":2}', 200),
    ('{"id":9911,"username":"user9911","firstName":"John","lastName":"James","email":"john@email.com",'
     '"password":"9911","phone":"9911","userStatus":2}', 400),
    ('{"id":9912,"username":"user9912","firstName":"John","lastName":"James","email":"john@email.com",'
     '"password":"9912","phone":"9912","userStatus":3}', 200),
    ('{"id":9912,"username":"user9912","firstName":"John","lastName":"James","email":"john@email.com",'
     '"password":"9912","phone":"9912","userStatus":3}', 400),
]
user_add_ids = [f"Create user [Data: {item[0]}], expected code={item[1]}" for item in user_add]

user_login = [("user9910", "9910", 200), ("user9911", "9911", 200), ("user9912", "9912", 200),
              ("user9910", "", 400), ("user9911", "", 400), ("user9912", "", 400),
              ]
user_login_ids = [f"Login with user name [{item[0]}] and password [{item[1]}], expected code={item[2]}" for item in
                  user_login]

user_delete = [
    ('user9910', 200), ('user9910', 400),
    ('user9911', 200), ('user9911', 400),
    ('user9912', 200), ('user9912', 400),
]
user_delete_ids = [f"Delete user {item[0]}], expected code={item[1]}" for item in user_delete]

user_find = [
    ('{"id":9910,"username":"user9910","firstName":"John","lastName":"James","email":"john@email.com",'
     '"password":"9910","phone":"9910","userStatus":1}', 200),
    ('{"id":9911,"username":"user9911","firstName":"John","lastName":"James","email":"john@email.com",'
     '"password":"9911","phone":"9911","userStatus":2}', 200),
    ('{"id":9912,"username":"user9912","firstName":"John","lastName":"James","email":"john@email.com",'
     '"password":"9912","phone":"9912","userStatus":3}', 200),
    ('{"id":10,"username":"theUser","firstName":"John","lastName":"James","email":"john@email.com",'
     '"password":"9910","phone":"9910","userStatus":1}', 200),
]
user_find_ids = [f"Create user [Data: {item[0]}], expected code={item[1]}" for item in user_find]

user_update = [
    ("user9910", '{"id":9910,"username":"user9910new","firstName":"John","lastName":"James",'
                 '"email":"john@email.com","password":"9910","phone":"99100099","userStatus":1}', 200),
    ("user9911", '{"id":9911,"username":"user9911new","firstName":"John","lastName":"James",'
                 '"email":"john@email.com","password":"9911","phone":"99110099","userStatus":2}', 200),
    ("user9912", '{"id":9912,"username":"user9912new","firstName":"John","lastName":"James",'
                 '"email":"john@email.com","password":"9912","phone":"99120099","userStatus":3}', 200),
]
user_update_ids = [f"Update user {item[0]}], expected code={item[2]}" for item in user_update]

user_add_list = [
    (['{"id":19910,"username":"user9910","firstName":"John","lastName":"James","email":"john@email.com",'
      '"password":"9910","phone":"9910","userStatus":1}',
      '{"id":19911,"username":"user9911","firstName":"John","lastName":"James","email":"john@email.com",'
      '"password":"9911","phone":"9911","userStatus":2}',
      '{"id":19912,"username":"user9912","firstName":"John","lastName":"James","email":"john@email.com",'
      '"password":"9912","phone":"9912","userStatus":3}'], 200),
]
user_add_list_ids = [f"Create user [Data: {item[0]}], expected code={item[1]}" for item in user_add_list]
