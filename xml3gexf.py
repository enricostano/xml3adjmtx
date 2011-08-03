#!/usr/bin/python
  
import networkx as nx
import xml.etree.ElementTree as etree
import sys
print ('xml3gexf.py')
print ('transform XML nodes and ties in Gexf format')
if len(sys.argv) < 2:
	print ('')
	print ("Usage: python xml3matrix.py nodes.xml ties.xml")
	print ("")
	sys.exit()
xmlNodesPath = sys.argv[1]
xmlTiesPath = sys.argv[2]

nodesTree = etree.parse(xmlNodesPath)
tiesTree = etree.parse(xmlTiesPath)

G = nx.DiGraph()
node_order = []

#crea i nodi e prende nota dell'ordine
nodesRoot = nodesTree.getroot()
for node in nodesRoot:
	G.add_node(node[4].text)
	node_order.append(node[4].text)
print("nodes: ", G.number_of_nodes())

#crea le relazioni
tiesRoot = tiesTree.getroot()
for tie in tiesRoot:
	G.add_edge(tie[7].text, tie[8].text)
print("ties: ", G.number_of_edges())

#scrive il file GEFX
#nx.write_gexf(G, '/home/enrico/Sviluppo/xarxaStBoi/19julio2011/xarxaStBoi.gexf')

#matrice

