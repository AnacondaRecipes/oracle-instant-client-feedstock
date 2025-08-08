import os
import platform

import oracledb

def test_instant_client_enable_thick_mode():
    print("Initializing client thick mode")
    oracledb.init_oracle_client()
    print("Client initialized successfully")


