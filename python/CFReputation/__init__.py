import os.path
import sqlite3

import Crossfire

_dict_name = 'CFReputationConnection'

def _init_schema(con, version, *schema_files):
    con.execute("PRAGMA journal_mode=WAL;");
    con.execute("PRAGMA synchronous=NORMAL;");
    con.execute("CREATE TABLE IF NOT EXISTS schema(version INT);");
    result = con.execute("SELECT version FROM schema").fetchall();
    curr = len(result)
    if curr < version:
        Crossfire.Log(Crossfire.LogInfo,
                "Initializing factions schema %d->%d" % (curr, version))
        for f in schema_files:
            with open(f) as initfile:
                con.executescript(initfile.read())
        con.commit()

def _get_sql_path(f):
    return os.path.join(Crossfire.DataDirectory(), Crossfire.MapDirectory(),
            "python/CFReputation/sql", f)

def _init_db():
    schema_files = map(_get_sql_path, ["schema.sql"])
    init_files = map(_get_sql_path, ["init.sql", "gods.sql"])
    db_path = os.path.join(Crossfire.LocalDirectory(), "factions.db")
    con = sqlite3.connect(':memory:')
    _init_schema(con, 1, *schema_files)
    for f in init_files:
        with open(f) as initfile:
            con.executescript(initfile.read())
    Crossfire.GetSharedDictionary()[_dict_name] = con

def _get_db():
    d = Crossfire.GetSharedDictionary()
    if _dict_name not in d:
        _init_db()
    return d[_dict_name]

def reputation(player, faction=None):
    """
    Return tuple with the name and reputation of the player with the given
    faction. If faction is None, return all known reputations.
    """
    con = _get_db()
    if faction is None:
        query="""
SELECT faction, CAST(ROUND(reputation*100) as integer) as rep
FROM reputations
WHERE name=? AND ABS(rep) > 0;
        """
        result = con.execute(query, (player,)).fetchall()
    else:
        query="""
SELECT faction, CAST(ROUND(reputation*100) as integer) as rep
FROM reputations
WHERE name=? AND faction=? AND ABS(rep) > 0;
        """
        result = con.execute(query, (player, faction)).fetchall()
    return result

def record_kill(race, region, player, fraction=0.0001, limit=0.4):
    con = _get_db()
    query = """
WITH updates AS (
    SELECT faction, -attitude*? AS change
    FROM regions
    NATURAL JOIN relations
    WHERE race=? AND (region=? OR region='ALL'))
REPLACE INTO reputations
SELECT ? AS player, updates.faction,
    COALESCE(reputation, 0) + change AS new_rep
FROM updates
LEFT JOIN reputations
    ON updates.faction=reputations.faction AND player=reputations.name
WHERE ABS(new_rep) <= ?;
    """
    con.execute(query, (fraction, race, region, player, limit))
    con.commit()
