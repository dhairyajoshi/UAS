### 1. User registration
#### /rest-auth/registration/ [POST]

- password1 (string)
- password2 (string)
- username (string)
- email (string)
- first_name (string)
- middle_name (char)
- last_name (string)
- date_of_birth (dd/mm/yyyy)
- gender (string)
- category (string)
- religion (string)
- blood_groups (string)
- father_name (string)
- mother_name (string)
- phone_number (string)
- image (blob)
- group_id (int)

### 2. Designation list
#### /employee/designation-list/ [GET,POST]
 - name (string)
 - short_name (string)
 - pay (int)

 ### 3. Designation detail
 #### /employee/designation-detail/<int:pk> [GET]
  - id (int)
  - name (string)
  - short_name (string)
  -pay (int)