#!/usr/local/bin python3
# -*- coding: utf8 -*-

__author__ = 'vincen'

import json
import psycopg2
from psycopg2.extras import execute_batch
from psycopg2.extras import execute_values
from psycopg2.pool import SimpleConnectionPool
import time

pgpool = SimpleConnectionPool(2, 3, host='localhost', port='5432', user='phileas', password='fogg', database='bb2')


def read(path):
    """读取文件，获得数据节点"""
    with open(path, 'r') as f:
        data = json.load(f)
    return data['data']['data']


def parse(data):
    """解析数据，提取关键字段"""
    cursor = 1
    result = list()
    for values1 in data.values():
        values2_code = values1.get('code')
        values2_name = values1.get('name')
        values2_typename = values1.get('typename')
        values2_type = values1.get('type')
        values2_orgid = values1.get('orgid')
        values2_clrq = values1.get('clrq')
        if not values2_clrq.strip():
            values2_clrq = None
        # values2 = {
        #     'code': values2_code,
        #     'name': values2_name,
        #     'typename': values2_typename,
        #     'type': values2_type,
        #     'clrq': values2_clrq,
        #     'orgid': values2_orgid
        # }
        values2 = (values2_code, values2_name, values2_typename, values2_type, values2_clrq, values2_orgid)
        result.append(values2)
        if cursor % 100 == 0 :
            batch_insert4(data=result)
            result.clear()
        cursor += 1
    else:
        batch_insert4(data=result)


def batch_insert(data):
    """批量存储节点，速度就像自行车"""
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        user='phileas',
        password='fogg',
        database='bb2')
    cur = conn.cursor()
    try:
        cur.executemany('''INSERT INTO t_fund_info (fcode, fname, type1, type2, created_at, orgid) VALUES (%(code)s, %(name)s, %(typename)s, %(type)s, %(clrq)s, %(orgid)s)''', data)
        conn.commit()
    except psycopg2.ProgrammingError as e:
        conn.rollback()
        print("Error at : " + data)
    finally:
        conn.close()


def batch_insert2(data):
    """批量存储节点，速度就像电动车"""
    SQL = '''INSERT INTO t_fund_info (fcode, fname, type1, type2, created_at, orgid) VALUES (%(code)s, %(name)s, %(typename)s, %(type)s, %(clrq)s, %(orgid)s)'''
    with psycopg2.connect(host='localhost', port='5432', user='phileas', password='fogg', database='bb2') as conn:
        with conn.cursor() as cur:
            execute_batch(cur=cur, sql=SQL, argslist=data)


def batch_insert3(data):
    """批量存储节点，速度就像小汽车"""
    SQL = '''INSERT INTO t_fund_info (fcode, fname, type1, type2, created_at, orgid) VALUES %s'''
    with psycopg2.connect(host='localhost', port='5432', user='phileas', password='fogg', database='bb2') as conn:
        with conn.cursor() as cur:
            execute_values(cur=cur, sql=SQL, argslist=data)


def batch_insert4(data):
    """批量存储节点，速度就像跑车"""
    SQL = '''INSERT INTO t_fund_info (fcode, fname, type1, type2, created_at, orgid) VALUES %s'''
    with pgpool.getconn() as conn:
        with conn.cursor() as cur:
            print('a', pgpool.__dict__)
            execute_values(cur=cur, sql=SQL, argslist=data)
    pgpool.putconn(conn)
    print('b', pgpool.__dict__)


def main():
    # start = time.process_time()
    start = time.perf_counter()
    path = 'result-test.json'
    data = read(path)
    parse(data)
    end = time.perf_counter()
    # end = time.process_time()

    duration = end - start
    print("198 rows cost %10.7f s " % duration)

    print('c', pgpool.__dict__)
    pgpool.closeall()
    print('d', pgpool.__dict__)



main()
