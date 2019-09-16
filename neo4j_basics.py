from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client


url = 'http://localhost:7474'
user = 'neo4j'
pwd = 'test'

def main():

    try:
        gdb = GraphDatabase(url, username=user, password=pwd)
    except Exception as e:
        print('GraphDatabase() raised exception => '+str(e))
        return 1

    # gdb.nodes.create(name="p1.exe").labels.add("process")
    # gdb.nodes.create(name="p2.exe").labels.add("process")
    # gdb.nodes.create(name="p3.exe").labels.add("process")
    # gdb.nodes.create(name="p4.exe").labels.add("process")
    # gdb.nodes.create(name="p5.exe").labels.add("process")

    process = gdb.labels.get("process")

    # gdb.relationships.create(process.get(name='p2.exe')[0], "parent", process.get(name='p1.exe')[0])
    # gdb.relationships.create(process.get(name='p1.exe')[0], "children", process.get(name='p2.exe')[0])
    #
    # gdb.relationships.create(process.get(name='p3.exe')[0], "parent", process.get(name='p2.exe')[0])
    # gdb.relationships.create(process.get(name='p2.exe')[0], "children", process.get(name='p3.exe')[0])
    #
    # gdb.relationships.create(process.get(name='p4.exe')[0], "parent", process.get(name='p3.exe')[0])
    # gdb.relationships.create(process.get(name='p3.exe')[0], "children", process.get(name='p4.exe')[0])
    #
    # gdb.relationships.create(process.get(name='p5.exe')[0], "parent", process.get(name='p4.exe')[0])
    # gdb.relationships.create(process.get(name='p4.exe')[0], "children", process.get(name='p5.exe')[0])

    n1 = process.get(name='p1.exe')[0]

    # q = 'MATCH (n)-[r]->(m) RETURN n, r, m'
    #
    # ret = gdb.query(q=q)
    # for r in ret:
    #     print(r[0]['data'],r[1]['type'],r[2]['data'])

    return 0

if __name__  == "__main__":
    main()
