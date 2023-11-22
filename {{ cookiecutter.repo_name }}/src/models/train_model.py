from common.snowflake_connector import connection_parameters, create_snowflake_session
import snowflake.snowpark as snowpark


snowflake_session = create_snowflake_session(connection_parameters)

def main(session:snowpark.Session):
    ...