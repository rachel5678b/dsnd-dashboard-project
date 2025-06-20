# Import the QueryBase class
from employee_events import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module
# from employee_events.sql_execution import QueryMixin
# QueryMixin is not used since QueryMixin is inherited through QueryBase

# Define a subclass of QueryBase
# called Employee


class Employee(QueryBase):
    """
    Employee a subclass of QueryBase

    Attributes:
        name (str): name of employee

    Methods:
        names()
            Returns list of tuples of employee full name and ID
        username(ID: int)
            Returns a list of tuples of employee full name name
        model_data(id: int)
            Return the sums of all postive and negative events
            for an employee_id
    """

    # Set the class attribute `name`
    # to the string "employee"
    name = "employee"

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution

    def names(self):
        """
        Return a list of tuples of employee full name and ID

        Returns:
            A list of tuples that includes columns full_name
             and employee_id
        """

        # Query 3
        # Write an SQL query
        # that selects two columns
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        sql_query = """SELECT first_name || ' ' || last_name
                       AS full_name, employee_id
                       FROM employee;
                    """

        return self.query(sql_query)

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    def username(self, ID):
        """
        Return a list of tuples of employee full name

        Args:
            ID (int): The employee_id to retrieve full name.

        Returns:
            A list of tuples with column full_name
        """
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        sql_query = f"""
            SELECT first_name || ' ' || last_name AS full_name
                FROM employee
                WHERE employee.employee_ID = {ID};
            """

        return self.query(sql_query)

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query

    def model_data(self, id):
        """
        Return the sums of all postive and negative events
         for an employee_id

        Args:
            id (int): The employee_id to retrieve events for

        Returns:
            A pandas DataFrame with columns of positive_events,
             negative_events
        """
        return self.pandas_query(f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """)
