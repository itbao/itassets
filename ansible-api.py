#!/bin/env python
#coding: utf-8
#write by xuchangbao

"""
ansible==1.9.2
"""

import ansible.runner
import sys
import yaml

try :
        import pymysql as mysql
except :
        import MySQLdb as mysql

#获取Ansibel setup module info
results = ansible.runner.Runner(pattern='*', forks=10, module_name='setup').run()

#获取不到Ansible即退出
if results is None:
    print "No hosts found"
    sys.exit(1)

#连接MySQL，如需要插入数据下一个id
def nextid(table,id):
    conn=mysql.connect(
            host='127.0.0.1',
            database='itassets',
            user='xcb',
            password='xcb',
            use_unicode=True
            )
    cursor=conn.cursor()
    cursor.execute('Select max(%s) From itassets_%s;' % (id,table))
    value = cursor.fetchall()
    cursor.close()
    conn.close()

    if value[0][0] is None:
        return 1
    else:
        return value[0][0]+1

def exesql(sql):
    conn=mysql.connect(
            host='127.0.0.1',
            database='itassets',
            user='xcb',
            password='xcb',
            use_unicode=True
            )
    cursor=conn.cursor()
    cursor.execute(sql)
    result=cursor.fetchall()
    cursor.close()
    conn.close()
    return result

#同步MySQL   
for hostname,result in  results['contacted'].items():
    #invocation=result['invocation']  #module_args,module_name
    #verbose_override=result['verbose_override']
    #changed=result['changed']
    facts=result['ansible_facts']
    
    #-------------------- 获取CPU信息并更新Mysql --------------------------------------------------
    cpus={
        'cpu_id':nextid('cpus','cpuid'),
        'vcpus':facts['ansible_processor_vcpus'],
        #'vcps':facts['ansible_processor_count'],
        'cpu_name':facts['ansible_processor'][1]
        }

    sql=exesql('select cpuid,cpuname,vcpus From itassets_cpus group by cpuname,vcpus;')
    for record in sql:
        if cpus['cpu_name'] == record[1] and cpus['vcpus'] == record[2]:
            cpu_id=record[0]
        
    if 'cpu_id' not in locals().keys():
        sql='insert into itassets_%s (cpuid,cpuname,vcpus) values (%d,"%s",%d);' \
        % ('cpus',cpus['cpu_id'],cpus['cpu_name'],cpus['vcpus'])
        exesql(sql)
        cpu_id = cpus['cpu_id']
    #---------------------------------------------------------------------------------------------


    mems={
        'memid': nextid('memory','memid'),
        'capacity':facts['ansible_memtotal_mb']/1000
    }
    #print mems

    hosts={
        'hostid':nextid('hosts','hostid'),
        'hostname':facts['ansible_fqdn'],
        'sn':facts['ansible_product_serial'],
        'brand':facts['ansible_product_name'],
        'updatedate':facts['ansible_date_time']['date']
        }
    #print hosts
    
 
