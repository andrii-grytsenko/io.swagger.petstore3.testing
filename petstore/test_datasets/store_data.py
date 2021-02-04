order_place = [
    ('{"id":9910,"petId":99101,"quantity":7,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"approved",'
     '"complete":true}', 200),
    ('{"id":9911,"petId":99111,"quantity":5,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"placed",'
     '"complete":true}', 200),
    ('{"id":9912,"petId":99121,"quantity":6,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"delivered",'
     '"complete":true}', 200),
]
order_place_ids = [f"Place order [Data: {item[0]}], expected code={item[1]}" for item in order_place]

order_find = [
    ('{"id":9910,"petId":99101,"quantity":7,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"approved",'
     '"complete":true}', 200),
    ('{"id":9911,"petId":99111,"quantity":5,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"placed",'
     '"complete":true}', 200),
    ('{"id":9912,"petId":99121,"quantity":6,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"delivered",'
     '"complete":true}', 200),
    ('{"id":121212,"petId":99121,"quantity":6,"shipDate":"2021-02-03T19:43:55.849+00:00","status":"delivered",'
     '"complete":true}', 404),
]
order_find_ids = [f"Find order [Data: {item[0]}], expected code={item[1]}" for item in order_find]

order_delete = [(9910, 200), (9911, 200), (9912, 200), (12121212, 404)]
order_delete_ids = [f"Delete order [Data: {item[0]}], expected code={item[1]}" for item in order_delete]