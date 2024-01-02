#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Optional, Any
from urllib.parse import quote
from urllib.parse import quote_plus as urlquote
from dbgpt.datasource.rdbms.base import RDBMSDatabase


class GBaseConnect(RDBMSDatabase):
    """Connect GBase Database fetch MetaData
    Args:
    Usage:
    """

    db_type: str = "gbase"
    db_dialect: str = "gbase"
    driver: str = "odbc"

    default_db = ["information_schema", "performance_schema", "gbase", "gclusterdb", "gctmpdb"]
    
   @classmethod
    def from_uri_db(
        cls,
        host: str,
        port: int,
        user: str,
        pwd: str,
        db_name: str,
        engine_args: Optional[dict] = None,
        **kwargs: Any,
    ) -> RDBMSDatabase:
        db_url: str = (
            f"{cls.driver}://{quote(user)}:{urlquote(pwd)}@{host}:{str(port)}/{db_name}"
        )
        return cls.from_uri(db_url, engine_args, **kwargs)