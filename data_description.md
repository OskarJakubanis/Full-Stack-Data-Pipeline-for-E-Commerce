# Data Description

## support_tickets.csv
- **ticket_id** – unique identifier of the support ticket  
- **issue_type** – type/category of the issue reported  
- **created_date** – date when the ticket was created  
- **resolved_date** – date when the ticket was resolved  
- **status** – current status of the ticket  
- **channel** – communication channel used (email, chat, phone)  

## customers.csv
- **customer_id** – unique identifier of the customer  
- **first_name** – customer first name  
- **last_name** – customer last name  
- **email** – customer email  
- **signup_date** – date of account creation  
- **region** – geographic region  
- **segment** – customer segment (e.g., premium, standard)  

## orders.csv
- **order_id** – unique identifier of the order  
- **order_date** – date when the order was placed  
- **product_id** – identifier of the product ordered  
- **quantity** – number of units ordered  
- **price** – price per unit  
- **status** – current order status  

## products.csv
- **product_id** – unique identifier of the product  
- **product_name** – name of the product  
- **category** – product category  
- **price** – price of the product  

## returns.csv
- **return_id** – unique identifier of the return  
- **order_id** – related order identifier  
- **return_date** – date of the return  
- **reason** – reason for return  
- **status** – return status  

## sessions.csv
- **session_id** – unique identifier of the session  
- **user_id** – identifier of the customer/user  
- **start_time** – session start timestamp  
- **end_time** – session end timestamp  
- **page_views** – number of pages viewed  
- **bounce** – whether the session was a bounce (yes/no)  
