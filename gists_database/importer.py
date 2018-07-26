import requests
import sqlite3

def import_gists_to_database(db, username, commit=True):
    api_url = "https://api.github.com/users/{}/gists".format(username)
    response = requests.get(api_url)
    
    if response.status_code == 404:
        raise requests.exceptions.HTTPError
        
    gists = response.json()
    
    # gists_for_db = ({
    #     "github_id": gist['id'],
    #     "html_url": gist['html_url'],
    #     'commits_url': gist['commits_url'],
    #     "git_pull_url": gist['git_pull_url'],
    #     "git_push_url": gist['git_push_url'],
    #     "forks_url": gist['forks_url'],
    #     "public": int(gist['public']),
    #     "created_at": gist["created_at"],
    #     "updated_at": gist["updated_at"],
    #     "comments": gist["comments"],
    #     "comments_url": gist["comments_url"]} for gist in gists)
    
    gists_for_db = ((
                gist['id'],
                gist['html_url'],
                gist['git_pull_url'],
                gist['git_push_url'],
                gist['commits_url'],
                gist['forks_url'],
                int(gist['public']),
                gist["created_at"],
                gist["updated_at"],
                gist["comments"],
                gist["comments_url"]) for gist in gists)
    
    curs = db.cursor()
    
    for gist in gists_for_db:
        
        # '''create paired iters to ensure that
        # keys and values are in the same order'''
        # pairs = gist.items()
        # keys = tuple(pair[0] for pair in pairs)
        # values = tuple(pair[1] for pair in pairs)
        # insert_string = '''
        #         INSERT INTO gists
        #             {keys}
        #         VALUES
        #             {values}
        #     '''.format(keys=keys, values=values)
        # 
        # curs.execute(insert_string)
        
        # insert_string = '''
        #         INSERT INTO gists
        #             (github_id, html_url, git_pull_url, git_push_url,
        #             commits_url, forks_url, public, created_at, updated_at,
        #             comments, comments_url)
        #         VALUES
        #             {gist}
        #     '''.format(gist=gist)
        # curs.execute(insert_string)
        
        insert_string = '''
                INSERT INTO gists
                    (github_id, html_url, git_pull_url, git_push_url,
                    commits_url, forks_url, public, created_at, updated_at,
                    comments, comments_url)
                VALUES
                    (?,?,?,?,?,?,?,?,?,?,?)
            '''
        curs.execute(insert_string, gist)
        
        
        
    if commit == True:
        db.commit()
    else:
        db.rollback()
        
    
    
