def edades():
    l = [input("Edad %d" % (i)) for i in range(1,11)]
    print "Menor: %d" % (min(l))
    print "Mayor: %d" % (max(l))
    print "Media: %d" % (sum(l)/len(l))
edades()
