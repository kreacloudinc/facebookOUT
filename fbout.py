import requests

# Imposta qui il tuo token di accesso valido
access_token = 'YOUR_ACCESS_TOKEN_HERE'

# Specifica la versione dell'API Graph di Facebook
api_version = 'v11.0'
base_api_url = f'https://graph.facebook.com/{api_version}/me/posts/'

# Imposta i timestamp di inizio e fine (Unix timestamp)
since_timestamp = 'UNIX_TIMESTAMP_START'
until_timestamp = 'UNIX_TIMESTAMP_END'

# Numero massimo di post da recuperare per richiesta (fino a 100 è generalmente supportato)
limit = 100

params = {
    'access_token': access_token,
    'since': since_timestamp,
    'until': until_timestamp,
    'limit': limit,
}

def delete_facebook_posts():
    posts_response = requests.get(base_api_url, params=params)

    if posts_response.status_code == 200:
        posts_data = posts_response.json()['data']
        print(f"Total posts found: {len(posts_data)}")

        for post in posts_data:
            post_id = post['id']
            delete_response = requests.delete(f'https://graph.facebook.com/{api_version}/{post_id}', params={'access_token': access_token})

            if delete_response.status_code == 200:
                print(f"Deleted post {post_id}")
            else:
                print(f"Failed to delete post {post_id}: {delete_response.json().get('error').get('message')}")
    else:
        print(f"Failed to retrieve posts: {posts_response.json().get('error').get('message')}")

if __name__ == "__main__":
    delete_facebook_posts()
    