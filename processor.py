import pandas as pd
import json

filepath = 'Spotify_Youtube.csv'


def open_youtube():
    """This func check which song has a YouTube video and return json"""

    global filepath
    df = pd.read_csv(filepath)
    filtered = df[df[['Url_youtube']].notnull().all(1)]
    filtered_to_json = filtered.to_json()
    return filtered_to_json


def sort():
    """This func return json, which sorted by LIKES, COMMENTS AND VIEWS"""

    global filepath
    df = pd.read_csv(filepath, usecols=['Artist', 'Likes', 'Comments', 'Views'])
    sorted_df = df.sort_values(by=['Likes', 'Comments', 'Views'], ascending=[False, False, False])
    print(sorted_df.to_dict()['Artist'][9348])
    return sorted_df.to_json()


def search():
    """"This func return json, which has individually columns"""

    global filepath
    df = pd.read_csv(filepath)
    json_object = (df[['Artist', 'Danceability', 'Energy', 'Key', 'Loudness', 'Speechiness', 'Acousticness', 'Instrumentalness', 'Liveness', 'Valence', 'Tempo']]).to_json()
    json_formatted = json.dumps(json_object, indent=2)
    print(json_formatted)
    return json_formatted


def test_pretty():
    """"This func is test route"""

    global filepath
    df = pd.read_csv(filepath)
    json_data = df[['Artist', 'Energy', 'Key']].to_json(orient='records')
    parsed = json.loads(json_data)
    pretty_json = json.dumps(parsed)
    return pretty_json


if __name__ == '__main__':
    search()
