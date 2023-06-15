MODEL/DB FIELDS

### LISTING
* id: INT<br>
* realtor: INT (FOREIGN KEY [realtor])<br>
* title: STR<br>
* address: STR<br>
* city: STR<br>
* state: STR<br>
* zipcode: STR<br>
* description: TEXT (longer)<br>
* price: INT<br>
* bedrooms: INT<br>
* bathrooms: INT<br>
* garage: INT [0]<br>
* sqft: INT<br>
* lot_price: FLOAT<br>
* is_published: BOOL [true]<br>
* list_date: DATE<br>
* photo_main: SRT<br>
* photo_1: SRT<br>
* photo_2: SRT<br>
* photo_3: SRT<br>
* photo_4: SRT<br>
* photo_5: SRT<br>
* photo_6: SRT<br>


### REALTOR
id: INT<br>
name: SRT<br>
photo: SRT<br>
description: SRT<br>
email: SRT<br>
phone: SRT<br>
is_mvp: BOOL [0]<br>
hire_date: DATE<br>


### CONTACT
id: INT <br>
user_id: INT <br>
listing: INT <br>
listing_id: INT <br>
name: STR <br>
email: STR <br>
phone: STR <br>
message: TEXT <br>
contact_date: DATE <br>
