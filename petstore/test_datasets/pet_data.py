from petstore.domain.domain_types import PetStatus

pet_add = [
    ('{"id":9910,"name":"dog9910","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"available"}', 200),
    ('{"id":9911,"name":"dog9911","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"pending"}', 200),
    ('{"id":9912,"name":"dog9912","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"sold"}', 200),
]
pet_add_ids = [f"Data=[{item[0]}], expected code={item[1]}" for item in pet_add]

pet_update = [
    ('{"id":9910,"name":"new-dog9910","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"sold"}', 200),
    ('{"id":9911,"name":"new-dog9911","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"available"}', 200),
    ('{"id":9912,"name":"new-dog9912","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"pending"}', 200),
]
pet_update_ids = [f"Data=[{item[0]}], expected code={item[1]}" for item in pet_update]

pet_id = [
    (9910, '{"id":9910,"name":"new-dog9910","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"sold"}', 200),
    (9911, '{"id":9911,"name":"new-dog9911","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"available"}', 200),
    (9912, '{"id":9912,"name":"new-dog9912","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"pending"}', 200),
    (999999, 'Pet not found', 404),
]
pet_id_ids = [f"Pet ID=[{item[0]}], expected code={item[2]}" for item in pet_id]

pet_status = [
    (PetStatus.available, 200),
    (PetStatus.pending, 200),
    (PetStatus.sold, 200),
]
pet_status_ids = [f"Pet status=[{item[0].value}], expected code={item[1]}" for item in pet_status]

pet_tag = [
    (['{"id":0,"name":"Tag1"}'], 200),
    (['{"id":0,"name":"Tag1"}', '{"id":22,"name":"tag2"}'], 200),
    (['{"id":10,"name":"tag11"}'], 200),
]
pet_tag_ids = [f"Pet tags=[{item[0]}], expected code={item[1]}" for item in pet_tag]

pet_update_by_form = [
    ('{"id":9910,"name":"newdog9910","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"pending"}', "newdog9910", PetStatus.pending, 200),
    ('{"id":9911,"name":"newdog9911","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"sold"}', "newdog9911", PetStatus.sold, 200),
    ('{"id":9912,"name":"newdog9912","category":{"id":1,"name":"Dogs"},"photoUrls":["string"],"tags":[{"id":0,'
     '"name":"string"}],"status":"available"}', "newdog9912", PetStatus.available, 200),
]
pet_update_by_form_ids = [f"New Pet Name=[{item[1]}], expected code={item[3]}" for item in pet_update_by_form]

pet_upload = [
    (9910, "metadata_9910", b"binary data for upload 9910", 200),
    (9911, "metadata_9911", b"binary data for upload 9911", 200),
    (9912, "metadata_9912", b"binary data for upload 9912", 200),
]
pet_upload_ids = [f"Pet ID=[{item[0]}], expected code={item[3]}" for item in pet_upload]

pet_delete = [
    (9910, "API_KEY", 200), (9911, "API_KEY", 200), (9912, "API_KEY", 200),
]
pet_delete_ids = [f"Pet ID=[{item[0]}], expected code={item[2]}" for item in pet_delete]
