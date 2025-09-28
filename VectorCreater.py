vectx1 = []
vectx2 = []
vecty1 = []
vecty2 = []
def clear():
    vectx1.clear()
    vectx2.clear()
    vecty1.clear()
    vecty2.clear()

class Vector():
    def plotVector(x1, x2, y1, y2):
        global plotx1, plotx2, ploty1, ploty2
        plotx1 = x1
        plotx2 = x2
        ploty1 = y1
        ploty2 = y2
        print('Vector plotted')
    def storeVector():
        vectx1.append(plotx1)
        vectx2.append(plotx2)
        vecty1.append(ploty1)
        vecty2.append(ploty2)
        print('Succesfully stored vector at position <{}>'.format(len(vectx1)))
    def accessVector():
        for i in range(0, len(vectx1)):
            print('Currently accessing vector {}: <{}, {}> to <{}, {}>'.format(i + 1, vectx1, vecty1, vectx2, vecty2))
while True:
    try:
        print('Enter graphing function:')
        func = input()
        exec(func)
    except:
        print('There was an error while running this function. [{}]'.format(func))
