data_api_solo = {}
data_api_duo = {}
data_api_squad = {}
data_api_overall = {}
df_solo = pd.DataFrame()
df_duo = pd.DataFrame()
df_squad = pd.DataFrame()
df_overall = pd.DataFrame()
current_timestamp = datetime.datetime.now()
formatted_current_timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

for x in datasetnames:
    try:
        
        data_api_solo['name'] = x['displayName']
        data_api_solo['rank'] = x['rank']
         
        call = api.stats.fetch_by_name(x['displayName'])
        if call.stats.all.solo.score is not None:
            data_api_solo['solo_score'] = call.stats.all.solo.score
            data_api_solo['solo_score_per_min'] = call.stats.all.solo.score_per_min
            data_api_solo['solo_score_per_match'] = call.stats.all.solo.scorePerMatch
            data_api_solo['solo_top5'] = call.stats.all.solo.top5
            data_api_solo['solo_top12'] = call.stats.all.solo.top12
            data_api_solo['solo_kills'] =  call.stats.all.solo.kills
            data_api_solo['solo_kills_per_min'] =  call.stats.all.solo.kills_per_min
            data_api_solo['solo_kills_per_match'] =  call.stats.all.solo.kills_per_match
            data_api_solo['solo_deaths'] =  call.stats.all.solo.deaths
            data_api_solo['solo_kd'] = call.stats.all.solo.kd
            data_api_solo['solo_matchs'] = call.stats.all.solo.matches
            data_api_solo['solo_win_rate'] = call.stats.all.solo.win_rate
            data_api_solo['solo_minutes_played'] =  call.stats.all.solo.minutes_played
            data_api_solo['solo_players_outlived'] =   call.stats.all.solo.players_outlived
            last_modified = call.stats.all.solo.last_modified
            formatted_last_modified = last_modified.strftime('%Y-%m-%d %H:%M:%S')
            data_api_solo['solo_last_modified'] = formatted_last_modified
            data_api_solo['solo_ingest_timestamp'] = formatted_current_timestamp
            
            df_solo = df_solo.append(data_api_solo, ignore_index=True)
            
        
        data_api_duo['name'] = x['displayName']
        data_api_duo['rank'] = x['rank']
        if call.stats.all.duo.score is not None:
            data_api_duo['duo_score'] = call.stats.all.duo.score
            data_api_duo['duo_score_per_min'] = call.stats.all.duo.score_per_min
            data_api_duo['duo_score_per_match'] = call.stats.all.duo.scorePerMatch
            data_api_duo['duo_top5'] = call.stats.all.duo.top5
            data_api_duo['duo_top12'] = call.stats.all.duo.top12
            data_api_duo['duo_kills'] =  call.stats.all.duo.kills
            data_api_duo['duo_kills_per_min'] =  call.stats.all.duo.kills_per_min
            data_api_duo['duo_kills_per_match'] =  call.stats.all.duo.kills_per_match
            data_api_duo['duo_deaths'] =  call.stats.all.duo.deaths
            data_api_duo['duo_kd'] = call.stats.all.duo.kd
            data_api_duo['duo_matchs'] = call.stats.all.duo.matches
            data_api_duo['duo_win_rate'] = call.stats.all.duo.win_rate
            data_api_duo['duo_minutes_played'] =  call.stats.all.duo.minutes_played
            data_api_duo['duo_players_outlived'] =   call.stats.all.duo.players_outlived
            last_modified = call.stats.all.duo.last_modified
            formatted_last_modified = last_modified.strftime('%Y-%m-%d %H:%M:%S')
            data_api_duo['duo_last_modified'] = formatted_last_modified
            data_api_duo['duo_ingest_timestamp']  = formatted_current_timestamp
            df_duo = df_duo.append(data_api_duo, ignore_index=True)
        
        data_api_squad['name'] = x['displayName']
        data_api_squad['rank'] = x['rank']
        if call.stats.all.squad.kills is not None:
            data_api_squad['squad_score'] = call.stats.all.squad.score
            data_api_squad['squad_score_per_min'] = call.stats.all.squad.score_per_min
            data_api_squad['squad_score_per_match'] = call.stats.all.squad.scorePerMatch
            data_api_squad['squad_top5'] = call.stats.all.squad.top5
            data_api_squad['squad_top12'] = call.stats.all.squad.top12
            data_api_squad['squad_kills'] =  call.stats.all.squad.kills
            data_api_squad['squad_kills_per_min'] =  call.stats.all.squad.kills_per_min
            data_api_squad['squad_kills_per_match'] =  call.stats.all.squad.kills_per_match
            data_api_squad['squad_deaths'] =  call.stats.all.squad.deaths
            data_api_squad['squad_kd'] = call.stats.all.squad.kd
            data_api_squad['squad_matchs'] = call.stats.all.squad.matches
            data_api_squad['squad_win_rate'] = call.stats.all.squad.win_rate
            data_api_squad['squad_minutes_played'] =  call.stats.all.squad.minutes_played
            data_api_squad['squad_players_outlived'] =   call.stats.all.squad.players_outlived
            last_modified = call.stats.all.squad.last_modified
            formatted_last_modified = last_modified.strftime('%Y-%m-%d %H:%M:%S')
            data_api_squad['squad_last_modified'] = formatted_last_modified
            data_api_squad['squad_ingest_timestamp'] =  formatted_current_timestamp
            df_squad = df_squad.append(data_api_squad, ignore_index=True)
            
            
        data_api_overall['name'] = x['displayName']
        data_api_overall['rank'] = x['rank']
        if call.stats.all.squad.kills is not None:
            data_api_overall['overall_score'] = call.stats.all.overall.score
            data_api_overall['overall_score_per_min'] = call.stats.all.overall.score_per_min
            data_api_overall['overall_score_per_match'] = call.stats.all.overall.scorePerMatch
            data_api_overall['overall_top5'] = call.stats.all.overall.top5
            data_api_overall['overall_top12'] = call.stats.all.overall.top12
            data_api_overall['overall_kills'] =  call.stats.all.overall.kills
            data_api_overall['overall_kills_per_min'] =  call.stats.all.overall.kills_per_min
            data_api_overall['overall_kills_per_match'] =  call.stats.all.overall.kills_per_match
            data_api_overall['overall_deaths'] =  call.stats.all.overall.deaths
            data_api_overall['overall_kd'] = call.stats.all.overall.kd
            data_api_overall['overall_matchs'] = call.stats.all.overall.matches
            data_api_overall['overall_win_rate'] = call.stats.all.overall.win_rate
            data_api_overall['overall_minutes_played'] =  call.stats.all.overall.minutes_played
            data_api_overall['overall_players_outlived'] =   call.stats.all.overall.players_outlived
            last_modified = call.stats.all.overall.last_modified
            formatted_last_modified = last_modified.strftime('%Y-%m-%d %H:%M:%S')
            data_api_overall['overall_last_modified'] = formatted_last_modified
            data_api_overall['overall_ingest_timestamp'] =  formatted_current_timestamp
            df_overall = df_overall.append(data_api_overall, ignore_index=True)
    except Exception as e:
        if e.args[0] == "Forbidden":
            pass


fortnite_solo_table_create = ("""CREATE TABLE IF NOT EXISTS fortnite_solo(
                        name VARCHAR PRIMARY KEY,
                        rank INTEGER,
                        solo_score INTEGER,
                        solo_score_per_min REAL,
                        solo_score_per_match REAL,
                        solo_top5 INTEGER,
                        solo_top12 INTEGER,
                        solo_kills INTEGER,
                        solo_kills_per_min REAL,
                        solo_kills_per_match REAL,
                        solo_deaths INTEGER,
                        solo_kd REAL,
                        solo_matchs INTEGER,
                        solo_win_rate REAL,
                        solo_minutes_played INTEGER,
                        solo_players_outlived INTEGER,
                        solo_last_modified  TIMESTAMP,
                        solo_ingest_timestamp TIMESTAMP 
                        )
                        """)

#The cur.execute(fortnite_solo_table_create) statement executes the SQL query using a cursor object named cur.
#Finally, conn.commit() is called to commit the changes made to the database, ensuring the table creation is finalized.
cur.execute(fortnite_solo_table_create)
conn.commit()

#Reorders the dataframe to match inserted data
ordered_df_solo = df_solo[['name',
                           'rank',
                        'solo_score' ,
                        'solo_score_per_min' ,
                        'solo_score_per_match' ,
                        'solo_top5' ,
                        'solo_top12' ,
                        'solo_kills' ,
                        'solo_kills_per_min' ,
                        'solo_kills_per_match' ,
                        'solo_deaths' ,
                        'solo_kd' ,
                        'solo_matchs' ,
                        'solo_win_rate' ,
                        'solo_minutes_played' ,
                        'solo_players_outlived',
                        'solo_last_modified',
                        'solo_ingest_timestamp' ]]


fortnite_solo_table_insert = ("""INSERT INTO fortnite_solo (
                        name,
                        rank,
                        solo_score ,
                        solo_score_per_min ,
                        solo_score_per_match ,
                        solo_top5 ,
                        solo_top12 ,
                        solo_kills ,
                        solo_kills_per_min ,
                        solo_kills_per_match ,
                        solo_deaths ,
                        solo_kd ,
                        solo_matchs ,
                        solo_win_rate ,
                        solo_minutes_played ,
                        solo_players_outlived,
                        solo_last_modified,
                        solo_ingest_timestamp )
                        VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)
""")

for i, row in ordered_df_solo.iterrows():
    cur.execute(fortnite_solo_table_insert,list(row))
    
conn.commit()


ordered_df_duo = df_duo[['name'   ,
                         'rank',
                        'duo_score',
                        'duo_score_per_min' ,
                        'duo_score_per_match' ,
                        'duo_top5' ,
                        'duo_top12' ,
                        'duo_kills' ,
                        'duo_kills_per_min' ,
                        'duo_kills_per_match' ,
                        'duo_deaths' ,
                        'duo_kd' ,
                        'duo_matchs' ,
                        'duo_win_rate' ,
                        'duo_minutes_played' ,
                        'duo_players_outlived',
                        'duo_last_modified',
                        'duo_ingest_timestamp'
                        ]]


fortnite_duo_table_create = ("""CREATE TABLE IF NOT EXISTS fortnite_duo(
                        name VARCHAR PRIMARY KEY,
                        rank INTEGER,
                        duo_score INTEGER,
                        duo_score_per_min REAL,
                        duo_score_per_match REAL,
                        duo_top5 INTEGER,
                        duo_top12 INTEGER,
                        duo_kills INTEGER,
                        duo_kills_per_min REAL,
                        duo_kills_per_match REAL,
                        duo_deaths INTEGER,
                        duo_kd REAL,
                        duo_matchs INTEGER,
                        duo_win_rate REAL,
                        duo_minutes_played INTEGER,
                        duo_players_outlived INTEGER,
                        duo_last_modified  TIMESTAMP,
                        duo_ingest_timestamp TIMESTAMP 

                        )
                        """)
cur.execute(fortnite_duo_table_create)
conn.commit()


fortnite_duo_table_insert = ("""INSERT INTO fortnite_duo (
                        name ,
                        rank,
                        duo_score ,
                        duo_score_per_min ,
                        duo_score_per_match ,
                        duo_top5 ,
                        duo_top12 ,
                        duo_kills ,
                        duo_kills_per_min ,
                        duo_kills_per_match ,
                        duo_deaths ,
                        duo_kd ,
                        duo_matchs ,
                        duo_win_rate ,
                        duo_minutes_played ,
                        duo_players_outlived,
                        duo_last_modified,
                        duo_ingest_timestamp
 )
                        VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)
""")


for i, row in ordered_df_duo.iterrows():
    cur.execute(fortnite_duo_table_insert,list(row))
    
conn.commit()


ordered_df_squad = df_squad[['name'   ,
                        'rank',
                        'squad_score',
                        'squad_score_per_min' ,
                        'squad_score_per_match' ,
                        'squad_top5' ,
                        'squad_top12' ,
                        'squad_kills' ,
                        'squad_kills_per_min' ,
                        'squad_kills_per_match' ,
                        'squad_deaths' ,
                        'squad_kd' ,
                        'squad_matchs' ,
                        'squad_win_rate' ,
                        'squad_minutes_played' ,
                        'squad_players_outlived',
                        'squad_last_modified',
                        'squad_ingest_timestamp'  ]]


fortnite_squad_table_create = ("""CREATE TABLE IF NOT EXISTS fortnite_squad(
                        name VARCHAR PRIMARY KEY,
                        rank INTEGER,
                        squad_score INTEGER,
                        squad_score_per_min REAL,
                        squad_score_per_match REAL,
                        squad_top5 INTEGER,
                        squad_top12 INTEGER,
                        squad_kills INTEGER,
                        squad_kills_per_min REAL,
                        squad_kills_per_match REAL,
                        squad_deaths INTEGER,
                        squad_kd REAL,
                        squad_matchs INTEGER,
                        squad_win_rate REAL,
                        squad_minutes_played INTEGER,
                        squad_players_outlived INTEGER,
                        squad_last_modified  TIMESTAMP,
                        squad_ingest_timestamp TIMESTAMP 
                        )
                        """)
cur.execute(fortnite_squad_table_create)
conn.commit()


fortnite_squad_table_insert = ("""INSERT INTO fortnite_squad (
                        name ,
                        rank,
                        squad_score ,
                        squad_score_per_min ,
                        squad_score_per_match ,
                        squad_top5 ,
                        squad_top12 ,
                        squad_kills ,
                        squad_kills_per_min ,
                        squad_kills_per_match ,
                        squad_deaths ,
                        squad_kd ,
                        squad_matchs ,
                        squad_win_rate ,
                        squad_minutes_played ,
                        squad_players_outlived,
                        squad_last_modified,
                        squad_ingest_timestamp
 )
                        VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s , %s)
""")

for i, row in ordered_df_squad.iterrows():
    cur.execute(fortnite_squad_table_insert,list(row))
    
conn.commit()

ordered_df_overall= df_overall[['name'   ,
                        'rank',
                        'overall_score',
                        'overall_score_per_min' ,
                        'overall_score_per_match' ,
                        'overall_top5' ,
                        'overall_top12' ,
                        'overall_kills' ,
                        'overall_kills_per_min' ,
                        'overall_kills_per_match' ,
                        'overall_deaths' ,
                        'overall_kd' ,
                        'overall_matchs' ,
                        'overall_win_rate' ,
                        'overall_minutes_played' ,
                        'overall_players_outlived',
                        'overall_last_modified',
                        'overall_ingest_timestamp']]

fortnite_overall_table_create = ("""CREATE TABLE IF NOT EXISTS fortnite_overall(
                        name VARCHAR PRIMARY KEY,
                        rank INTEGER,
                        overall_score INTEGER,
                        overall_score_per_min REAL,
                        overall_score_per_match REAL,
                        overall_top5 INTEGER,
                        overall_top12 INTEGER,
                        overall_kills INTEGER,
                        overall_kills_per_min REAL,
                        overall_kills_per_match REAL,
                        overall_deaths INTEGER,
                        overall_kd REAL,
                        overall_matchs INTEGER,
                        overall_win_rate REAL,
                        overall_minutes_played INTEGER,
                        overall_players_outlived INTEGER,
                        overall_last_modified  TIMESTAMP,
                        overall_ingest_timestamp TIMESTAMP 


                        )
                        """)
cur.execute(fortnite_overall_table_create)
conn.commit()

fortnite_overall_table_insert = ("""INSERT INTO fortnite_overall (
                        name ,
                        rank,
                        overall_score ,
                        overall_score_per_min ,
                        overall_score_per_match ,
                        overall_top5 ,
                        overall_top12 ,
                        overall_kills ,
                        overall_kills_per_min ,
                        overall_kills_per_match ,
                        overall_deaths ,
                        overall_kd ,
                        overall_matchs ,
                        overall_win_rate ,
                        overall_minutes_played ,
                        overall_players_outlived,
                        overall_last_modified,
                        overall_ingest_timestamp

 )
                        VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s , %s)
""")


for i, row in ordered_df_overall.iterrows():
    cur.execute(fortnite_overall_table_insert,list(row))
    
conn.commit()