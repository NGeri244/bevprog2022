bekert = str(input("Adj meg egy egy mondatot/szót: "))
if str(bekert) == bekert[::-1]:
    print("{0} == {1}".format(bekert,bekert[::-1]))
else:
    print("{0} != {1}".format(bekert, bekert[::-1]))