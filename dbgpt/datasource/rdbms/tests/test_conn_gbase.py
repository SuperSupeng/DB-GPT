"""
    Run unit test with command: pytest dbgpt/datasource/rdbms/tests/test_conn_gbase.py
    docker run -it --name gbase8a --hostname=gbase8a --privileged=true -p5258:5258 shihd/gbase8a:1.0
    docker exec -it gbase8a /bin/base 
    gbase -uroot -p
    Enter password:

    GBase client Free Edition 8.6.2.43-R7-free.110605. Copyright (c) 2004-2024, GBase.  All Rights Reserved.

    create database test;
    
"""

import pytest
from dbgpt.datasource.rdbms.conn_gbase import GBaseConnect

_create_table_sql = """
            CREATE TABLE IF NOT EXISTS `test` (
                `id` int
                );
            """


@pytest.fixture
def db():
    config = {'host':'localhost','port':5258,'database':'test', 'user':'root','root':'root'}
    conn = GBaseConnect.from_uri_db(
        "localhost",
        5258,
        "root",
        "root",
        "test",
    )
    yield conn

def test_get_table_info_with_table(db):
    db.run(_create_table_sql)
    print(db._sync_tables_from_db())
    table_info = db.get_table_info()
    assert "CREATE TABLE test" in table_info