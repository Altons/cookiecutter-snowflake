import os
from os.path import join, dirname, abspath
import snowflake.snowpark as snowpark

# Get the absolute path of the current script
current_dir = dirname(abspath(__file__))

# Navigate two directories above
two_directories_up = join(current_dir, '..', '..')

# Combine with the .env file path
dotenv_path = join(two_directories_up, '.env')

# Load the .env file
from dotenv import load_dotenv
load_dotenv(dotenv_path)

# Create conn params from credentials in .env

connection_parameters = {
        "account": os.getenv('SF_ACCOUNT'),
        "user": os.getenv('SF_USER'),    
        "role": os.getenv('SF_ROLE'),
        "warehouse": os.getenv('SF_WAREHOUSE'),
        "database": os.getenv('SF_DATABASE'),
        "schema": os.getenv('SF_SCHEMA')
    }


{% if cookiecutter.snowflake_connection=='Auth0' %}
connection_parameters["authenticator"]="externalbrowser"
{% else %}
connection_parameters["password"]=os.getenv('SF_PASSWORD')
{% endif %}


def create_snowflake_session(connection_parameters: dict):
    """Create a connection/session to Snowflake

    Args:
        connection_parameters (dict): connection parameters

    Returns:
        Session: Snowflake Session or None if err
    """
    try:
        session = snowpark.Session.builder.configs(connection_parameters).create()
        return session
    except Exception as e:
        print(f"Error creating Snowflake session: {str(e)}")
        return None