import init_like

if __name__ == "__main__":
	t = init_like.useDBHDFS('lala','yongqian')
#	t.create()
	t.drop()
	print 'OK'
