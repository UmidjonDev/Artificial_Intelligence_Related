"""import numpy as np
def one_dim(n):
    #Function which creates one dimensional array
    newArrayModel=np.random.rand(n)*n
    newArray=np.array(newArrayModel)
    return newArray"""

"""import numpy as np
def two_dim(r, c):
    newArrayModel=np.random.rand(r, c)*100
    newArray=np.array(newArrayModel)
    return newArray
"""
"""import numpy as np
def nd_array():
  newArrayModel=np.array([np.arange(0, 3, 1), np.arange(3, 6, 1), np.arange(6, 9, 1)],subok=True)
  return newArrayModel
def sliced_array_2d():
    array = nd_array() 
    return array[2, :2]
"""
"""import numpy as np
def nd_array():
    newArrayModel=np.array(np.arange(0, 27, 1).reshape(3, 3, 3), subok=True)
    return newArrayModel
def sliced_array_3d():
    array = nd_array()
    return np.array([array[1, 1:][0, :2]]+[array[1, 1:][1, :2]])
"""
import numpy as np
testArray=np.array(['Hasan', 'Husan', 'Javohir', 'Elyor', 'Hasan', 'Javohir', 'Elyor'])
booleanArray=((testArray=='Javohir')|(testArray=='Elyor'))
dataArray= np.array([[5, 6, 1, 1],
            [9, 1, 1, 1],
            [7, 7, 4, 2],
            [1, 5, 1, 9],
            [9, 9, 4, 5],
            [7, 5, 9, 6],
            [5, 3, 7, 4]])
resultingArray=dataArray[booleanArray]
print(resultingArray)