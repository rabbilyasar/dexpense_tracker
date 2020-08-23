# dexpense_tracker

## Initial Setup
step 1. Install packages from requirements.txt <br/>
step 2. Make a superuser. <br/>
step 3. Make groups ["employee", "manager", "auditor"] from django admin dashboard or from shell<br/>
step 4. Create users either from the registration page or from the django admin panel and assign them to the necessary groups. A USER CAN BELONG TO ONLY ONE GROUP. <br/>
step 5. Create categories ["travel", "misc", "food", "accommodation", "training", "certification", "software purchase"] <br/>

## Roles
1. Manager ["can submit expenses", "approve/reject expenses", "can edit/del their own expenses before being approved"] <br/> 
2. Employee ["can submit expenses","can edit/del their own expenses before being approved"] <br/>
3. Auditor ["can view approved expenses filtered by month"] <br/>

## Tracker app functionality
Home page: It can be accesible by the employee and manager. It shows all the pending expenses and rejected expenses. Status can be changed which can only be done by a manager.<br/>
Approved expenses page: It can be viewed by everyone it shows the expenses which has been approved.
Create expenses page: Expenses can be created only by the admins and by the employees. Status is automatically set to pending and submitted by is set to backend automatically.
