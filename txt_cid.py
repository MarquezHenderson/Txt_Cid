import random
import glob
import os


 # finds all text files that reside in folder
h = glob.glob('*.txt')
cid = glob.glob('*.cid')
#print h
stocks ={}
layouts = {}

item_list = open("itemlist.ini","r")

#print item_list.readlines()
for item in item_list:
	#print 'this is to split' + str(item.split(","))
	x = item.split(",")
	#print item
	sideA = x[0]
	sideB = x[1]
	sideC = len(sideB)-1
	sideB = sideB[0:sideC]
	stocks[sideA]=sideB
	layouts[sideA]=sideB

def loaddic():
	pass



#opens each text file seperates lines into list  
def findpagefiles(h):
 	for pagefiles in range(len(h)):
 		textfile=h[pagefiles]
 		pagedna = open(textfile)
 		#print pagedna.readlines()
 		o = pagedna.readlines()
 		orders = o[1:] #reading everything but the header of the file
 		print orders
 		#saving to temp file
 		for items in range(len(orders)):
 			temp = open('temp.tmp' , 'a')
 			orders[items]
 			lines = orders[items]
 			temp.write(lines)
			temp = open('temp.tmp', 'r')
			item2 = temp.readlines()
			print len(item2)
			order_count = len(item2)
			ordernum = 1
			while order_count >= 1:
				for lines in item2:
					x = lines.split(',')
					layout_code = str(x[2])
					print layout_code
					stock_code = str(x[2])
					sets = x[4]
					qty = x[5]
					if sets == '':
						sets = 1
					if qty.startswith('Box(s) of '):
						qty = qty[len('Box[s] of '):]
					elif qty.startswith('Pack(s) of'):
						qty = qty[len('Pack[s] of '):]
					elif qty.startswith('Each'):
						qty = 1
					elif qty.startswith(''):
						qty = 1
					print qty
					qty = int(sets) * int(qty)
					newfile = open(str(x[1])+str(ordernum)+'.cid','w')
					newfile.write('[ORDER]\n')
					newfile.write('1='+str(x[11])+'\n')
					newfile.write('BCT#=3048\n')
					newfile.write('CUSTOMER=794\n')
					newfile.write('COMPANY NAME=Umpqua\n')
					newfile.write('SUBACCT=sb\n')
					newfile.write('ORDER#='+str(x[1])+str(ordernum)+'\n')
					newfile.write('MEMO='+str(x[3].strip('Item # '))+'\n')
					newfile.write('LAYOUT='+layouts[str(layout_code.upper())]+'\n')
					newfile.write('QUANTITY='+str(qty)+'\n')
					newfile.write('STOCK='+stocks[str(stock_code.upper())]+'\n')
					newfile.write('INK=BLK\n')
					newfile.write('FINISH=S\n')
					newfile.write('\n')
					newfile.write('[SHIP]\n')
					newfile.write('NAME='+str(x[11])+'\n')
					newfile.write('ADDRESS='+str(x[13])+str(x[14])+'\n')
					newfile.write('CITY='+str(x[15])+'\n')
					newfile.write('STATE='+str(x[16])+'\n')
					newfile.write('ZIP='+str(x[17])+'\n')
					newfile.write('COUNTRY=UNITED STATES\n')
					newfile.write('PO='+str(x[20])+'\n')
					newfile.write('METHOD=DRP\n')
					newfile.write('SHIPCODE=\n')
					newfile.write('\n')
					newfile.write('[LINE]\n')
					newfile.write('LOGO1='+str(x[1])+str(ordernum)+'.EPS'+'[,BLK,]'+'\n')
					newfile.write('\n')
					newfile.write('[CUSTOM]\n')
					newfile.write('\n')
					newfile.write('[USER_DATA]\n')
					order_count -= 1
					ordernum += 1
					#print order_count
					print ordernum
		temp.close()
		os.remove('temp.tmp')

findpagefiles(h)
