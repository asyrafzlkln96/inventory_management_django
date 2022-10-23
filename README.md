## Inventory management system developed in Django Framework
Author: Asyraf Zulkalnain

## Pre-requisites :

* Step 1: Make sure you have Django installed. This project uses Django==3.2 . Run pip install -r requirements.txt if you dont have Django installed.
* Step 2: Run python manage.py runserver in local. 
* Step 3: Open browser and browse to http://localhost:8000/api/inventory
to see all inventories (see endpoint below for more info)

## Endpoints
* /inventory - To list all inventories in view.
![image](https://user-images.githubusercontent.com/53460015/197374845-e6b44dc0-972d-40f4-ab2f-77b54bcae866.png)


* /api/inventory - To list all inventories
![image](https://user-images.githubusercontent.com/53460015/197374857-4afad67d-42aa-427c-8ea4-2d6fa65eb530.png)

* /api/inventory/?=name - To query inventory by name. E.g : vans shoes
![image](https://user-images.githubusercontent.com/53460015/197407602-f356023a-6316-40f4-b419-13f3ba3392e2.png)


* /inventory/id - To get inventory based on id
![image](https://user-images.githubusercontent.com/53460015/197405592-83649384-dc1e-45b4-8348-4313f7ea3572.png)



 * /admin - To access admin panel and view Inventory and Supplier models (CRUD management)
 ![image](https://user-images.githubusercontent.com/53460015/197374953-910d33af-99a8-4def-962b-f64a03f00515.png)

  
 ## Tests
 Run python manage.py test in order to test the endpoints.
 ![image](https://user-images.githubusercontent.com/53460015/197375170-9f72ef7b-7b08-421f-9f66-632ecff17873.png)

 
 
  ## Admin
  Admin user: asyraf
  Password: admin123




