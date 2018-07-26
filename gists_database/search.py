from .models import Gist
from datetime import datetime

def search_gists(db_connection, github_id=None, created_at=None):
    query_params = {
        "github_id": github_id,
        "created_at": created_at
    }
    query_string = "SELECT * FROM gists"
    if github_id or created_at:
        query_string +=  " WHERE"
        if github_id:
            query_string += " github_id = :github_id"
        if created_at:
            print(created_at)
            query_string += " datetime(created_at) = :created_at"
    
    cur = db_connection.cursor()
    cur.execute(query_string, query_params)
    gist_rows = cur.fetchall()
    gist_objects = [Gist(row) for row in gist_rows]
    
    return gist_objects
    