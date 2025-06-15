# Import the QueryBase class
from employee_events import QueryBase

# Import dependencies for sql execution
# from employee_events.sql_execution import QueryMixin
# QueryMixin is not used since QueryMixin is inherited through QueryBase

# Create a subclass of QueryBase
# called  `Team`


class Team(QueryBase):
    """
    Team a subclass of QueryBase

    Attributes:
        name (str): name of team

    Methods:
        names()
            Returns list of tuples of team name and ID
        username(ID: int)
            Returns a list of tuples of team name
        model_data(id: int)
             Return the sums of all postive and negative events for a team_id
    """
    # Set the class attribute `name`
    # to the string "team"
    name = "team"

    # Define a `names` method
    # that receives no arguments
    # This method should return
    # a list of tuples from an sql execution
    def names(self):
        """
        Return a list of tuples of team name and ID

        Returns:
            A list of tuples that includes columns team_name and team_id
        """
        # Query 5
        # Write an SQL query that selects
        # the team_name and team_id columns
        # from the team table for all teams
        # in the database
        sql_query = "SELECT team_name, team_id FROM team;"

        # Execute the query using the inherited query method and return the
        # result as a list of tuples
        return self.query(sql_query)

    # Define a `username` method
    # that receives an ID argument
    # This method should return
    # a list of tuples from an sql execution

    def username(self, ID):
        """
        Return a list of tuples of team name

        Args:
            ID (int): The team_id to retrieve team name.

        Returns:
            A list of tuples with column team_name
        """
        # Query 6
        # Write an SQL query
        # that selects the team_name column
        # Use f-string formatting and a WHERE filter
        # to only return the team name related to
        # the ID argument
        sql_query = f"SELECT team_name FROM team WHERE team.team_id = {ID}"

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
        Return the sums of all postive and negative events for a team_id

        Args:
            id (int): The team_id used to retrieve events.

        Returns:
            A pandas DataFrame with columns of positive_events, negative_events
        """
        return self.pandas_query(f"""
            SELECT positive_events, negative_events FROM (
                    SELECT employee_id
                         , SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                    GROUP BY employee_id
                   )
                """)
