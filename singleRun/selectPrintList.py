import pymel.core as pm

sels = pm.selected()

print '['
for sel in sels:
    print "'" + sel + "',"
print ']'