import pandas as pd
import mysql.connector

def subgroup (conn, classgroup):
    """   Create a list with all parents that have the common ancestor specified"""
    query_getid = "SELECT node_id FROM classyfire_classification_dictionary WHERE node_name = %s"
    node_idDB = pd.read_sql(query_getid, conn, params=[classgroup])

    query_descendants = "select node_id from classyfire_classification where super_class = %s"
    descendt = pd.read_sql(query_descendants, conn, params=[node_idDB.loc[0, 'node_id']])

    node_id_listDesc = descendt['node_id'].tolist()
    node_name_listDesc = []

    for d in node_id_listDesc:
        query_name = "SELECT node_name FROM classyfire_classification_dictionary WHERE node_id = %s"
        comp_name = pd.read_sql(query_name, conn, params=[d])
        node_name_listDesc.append(comp_name.loc[0, 'node_name'])
    return node_name_listDesc

