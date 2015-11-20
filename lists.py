#coding=utf-8
import threading
import urllib2
import re
import Queue
from content import getpapaer
count=0
class getpage(threading.Thread):
	def __init__(self,queue,inqueue):
		threading.Thread.__init__(self)
		self.queue=queue
		self.inqueue=inqueue
		
	def get(self,num):
		try:
			url=urllib2.urlopen("http://wooyun.org/bugs/page/%s"%(str(num))).read()
			x=re.findall('<td><a href="(.*)">(.*)</a>',url)
			for i in x:
				self.inqueue.put("%s<c>%s"%(i[0],i[1]))
				getpapaer(i[0])
				#print "%s<c>%s"%(i[0],i[1])
				print "[!]Size: ",self.inqueue.qsize()
		except:
			pass
	def run(self):
		while True:
			try:
				line=self.queue.get(block=False,timeout=1)
				if line:
					self.get(line)
			except:
				break

th=Queue.Queue()
res=Queue.Queue()
for i in xrange(3832):
	th.put(i)
x=[]	
for t in xrange(25):
	f=getpage(th,res)
	x.append(f)
for q in x:
	q.start()
for q in x:
	q.join()

	
	
	

		