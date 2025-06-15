# Import any dependencies needed to execute sql queries
from employee_events.sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.


class QueryBase(QueryMixin):
    """
    QueryBase a subclass of QueryMixin

    Attributes:
        name (str): name of employee or team

    Methods:
        names()
            Returns an empty list
        event_counts(id: int)
            Returns a pandas DataFrame of event_counts
        notes(id: int)
            Returns a pandas DataFrame of notes
    """
    # Create a class attribute called `name`
    # set the attribute to an empty string
    name = ""

    # Define a `names` method that receives
    # no passed arguments
    def names(self):
        """
        Return an empty list.

        Returns:
            list: An empty list.
        """
        # Return an empty list
        return []

    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe

    def event_counts(self, id):
        """
        Create a DataFrame of daily event counts for an ID.

        Args:
            id (int): The ID of the entity (employee or team) for which to count events.

        Returns:
            events_df (DataFrame): A DataFrame with columns for event_date,
                            total_positive_events, and total_negative_events
                            ordered by event date.
        """
        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        sql_query = f"""
            SELECT event_date,
                   SUM(positive_events) AS total_positive_events,
                   SUM(negative_events) AS total_negative_events
            FROM {self.name}
            JOIN employee_events
                USING ({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
            GROUP BY event_date
            ORDER BY event_date;
        """
        events_df = self.pandas_query(sql_query)

        return events_df

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe

    def notes(self, id):
        """
        Create a DataFrame of notes for an ID.

        Args:
            id (int): The ID of the entity (employee or team) to retrive notes for.

        Returns:
            notes_df (DataFrame): A DataFrame with columns for note_date,
                            and note.
        """
        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        sql_query = f"""
            SELECT note_date, note
            FROM notes
            JOIN {self.name}
                USING ({self.name}_id)
            WHERE notes.{self.name}_id = {id};
        """
        notes_df = self.pandas_query(sql_query)

        return notes_df
