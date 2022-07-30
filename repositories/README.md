# The outline of the repository pattern

1. Unique repository directory for every unique data type (Inventory and Orders)

2. Abstract class within each repository (interfaces) that acts as a contract on how every repository class should behave

3. Individual repository classes (Adapters) that inherit the abstract class and return the same data from different sources (API, SQL, NOSQL, etc)

# NOTE
Generally it is recommended that you have some form of dependency injection to ease the management of the repository pattern, but for the sake of time in rest_api/handlers/orderhandler you can see how I initalize a OrderService object and a InventoryService Object by just passing in a repository object into each. 