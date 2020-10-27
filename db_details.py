# -*- coding: utf-8 -*-
from pymongo import MongoClient


def db_info(url,hostname,port):
    instance=hostname+":"+port
    #client = MongoClient("mongodb+srv://m001-student:vemara@sandbox.m8irx.mongodb.net/sandbox?retryWrites=true&w=majority") # defaults to port 27017
    client = MongoClient(url)
    db_list=["DB NAME"]
    col_count=["COLL COUNT"]
    db_size=[]
    db_size.append(0)
    idx_count=["INDEX COUNT"]
    doc_count=["DOC COUNT"]
    col_list=["COLLECTIONS"]

    final_list=[]

    for db in client.list_databases():
        db_list.append(db["name"])
        db_size.append(round(db["sizeOnDisk"]/1024/1024/1024,2))
             
        col_count.append(client[db["name"]].command("dbstats")["collections"])
        idx_count.append(client[db["name"]].command("dbstats")["indexes"])
        doc_count.append(client[db["name"]].command("dbstats")["objects"]) 
        col_list.append(list(client[db["name"]].list_collection_names()))

    

    tot_size= (sum(db_size)) 
    db_size[0]="DB SIZE (GB)"
    final_list.append(db_list)
    final_list.append(db_size)
    final_list.append(col_count)
    final_list.append(idx_count)
    final_list.append(doc_count)
    final_list.append(col_list)

    return final_list,tot_size,instance

