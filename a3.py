import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        self.A = A
        self.x_lst = []
        self.y_lst = []
        for i in range(len(self.A)):
            self.x_lst.append(self.A[i][0])
            self.y_lst.append(self.A[i][1])

        self.x_lst_copy = self.x_lst.copy()
        self.y_lst_copy = self.y_lst.copy()
 
    
    def translate(self, dx, dy):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        self.x_lst_copy = self.x_lst.copy()
        self.y_lst_copy = self.y_lst.copy()
        self.x_lst = []
        self.y_lst = []

        Shape.translate(self,dx,dy)
        for i in range(len(self.A)):
            self.A[i] = np.matmul(self.T_t, self.A[i])
        for i in range(len(self.A)):
            self.x_lst.append(round(self.A[i][0],2))
            self.y_lst.append(round(self.A[i][1],2))

        return self.x_lst, self.y_lst

    
    def scale(self, sx, sy):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''

        self.x_lst_copy = self.x_lst.copy()
        self.y_lst_copy = self.y_lst.copy()


        Shape.scale(self,sx,sy)
        center_x = sum(self.x_lst)/len(self.x_lst)
        center_y = sum(self.y_lst)/len(self.y_lst)
        Shape.translate(self, -center_x, -center_y)
        for i in range(len(self.A)):
            self.A[i] = np.matmul(self.T_t,self.A[i])
        for i in range(len(self.A)):
            self.A[i] = np.matmul(self.T_s,self.A[i])
        Shape.translate(self,center_x,center_y)
        for i in range(len(self.A)):
            self.A[i] = np.matmul(self.T_t, self.A[i])

        self.x_lst = []
        self.y_lst = []

        for i in range(len(self.A)):
            self.x_lst.append(round(self.A[i][0],2))
            self.y_lst.append(round(self.A[i][1],2))

        return self.x_lst, self.y_lst



    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        self.x_lst_copy = self.x_lst.copy()
        self.y_lst_copy = self.y_lst.copy()

        Shape.rotate(self,deg)
        Shape.translate(self, -rx, -ry)
        for i in range(len(self.A)):
            self.A[i] = np.matmul(self.T_t, self.A[i])
        for i in range(len(self.A)):
            self.A[i] = np.matmul(self.T_r, self.A[i])
        Shape.translate(self, rx, ry)
        for i in range(len(self.A)):
            self.A[i] = np.matmul(self.T_t, self.A[i])

        self.x_lst = []
        self.y_lst = []

        for i in range(len(self.A)):
            self.x_lst.append(round(self.A[i][0],2))
            self.y_lst.append(round(self.A[i][1],2))

        return self.x_lst, self.y_lst


    

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        x_coord = self.x_lst
        x_coord.append(self.x_lst[0])
        y_coord = self.y_lst
        y_coord.append(self.y_lst[0])
        plt.plot(x_coord, y_coord, linestyle="solid")
        x_coord_copy = self.x_lst_copy
        x_coord_copy.append(self.x_lst_copy[0])
        y_coord_copy = self.y_lst_copy
        y_coord_copy.append(self.y_lst_copy[0])
        plt.plot(x_coord_copy, y_coord_copy, linestyle="dashed")
        Shape.plot(self, max(max(max(self.x_lst),max(self.x_lst_copy)),max(max(self.y_lst),max(self.y_lst_copy))), max(max(max(self.x_lst),max(self.x_lst_copy)),max(max(self.y_lst),max(self.y_lst_copy))))

class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.x = x
        self.y = y
        self.radius = radius
        self.x_copy = x
        self.y_copy = y
        self.radius_copy = radius

        self.lst = np.array([self.x, self.y, 1])

    
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''

        self.x_copy = self.x
        self.y_copy = self.y
        self.radius_copy = self.radius

        Shape.translate(self, dx, dy)
        self.lst = np.matmul(self.T_t, self.lst)
        self.x = self.lst[0]
        self.y = self.lst[1]

        return round(self.x,2), round(self.y,2), round(self.radius,2)

 
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''

        self.x_copy = self.x
        self.y_copy = self.y
        self.radius_copy = self.radius

        Shape.scale(self,sx,sx)
        radius_lst = np.array([self.radius, 0, 0])

        self.radius_lst = np.matmul(self.T_s, radius_lst)
        self.radius = self.radius_lst[0]

        return round(self.x,2), round(self.y,2), round(self.radius,2)
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''


        self.x_copy = self.x
        self.y_copy = self.y
        self.radius_copy = self.radius

        Shape.translate(self, -rx, -ry)

        self.lst = np.matmul(self.T_t, self.lst)
        Shape.rotate(self, deg)
        self.lst = np.matmul(self.T_r, self.lst)
        Shape.translate(self, rx, ry)
        self.lst = np.matmul(self.T_t, self.lst)

        self.x = self.lst[0]
        self.y = self.lst[1]


        return round(self.lst[0],2), round(self.lst[1],2), round(self.radius,2)


    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        circle_1 = plt.Circle((self.x, self.y), self.radius, fill=False, linestyle="solid")
        circle_2 = plt.Circle((self.x_copy, self.y_copy), self.radius_copy, fill=False, linestyle="dashed")
        plt.gca().add_patch(circle_1)
        plt.gca().add_patch(circle_2)
        Shape.plot(self,(max(self.x,self.x_copy)+max(self.y,self.y_copy)+max(self.radius,self.radius_copy)),(max(self.x,self.x_copy)+max(self.y,self.y_copy)+max(self.radius,self.radius_copy)))

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    val = int(input("Enter (Verbose): 1 -> Plot, result and 0 -> result only "))
    n = int(input("Enter number of test cases "))
    for i in range(n):
        fig = int(input("Enter 0 for Polygon , 1 for Circle "))
        if fig == 1:
            A = list(map(float, input("Enter x coordinate, y coordinate, radius ").split()))
            if len(A) == 0:
                x = 0
                y = 0
                radius = 5
            else:
                x = A[0]
                y = A[1]
                radius = A[2]

            cir = Circle(x, y, radius)
            query = int(input("Enter Number of Query: "))
            for i in range(query):
                print("*"*30)
                print("""
1) Translate T dx dy
2) scale S sx
3) rotate R deg rx ry
4) plot P """)
                print("*"*30)
                B = list(map(str, input("Enter Query: ").split()))
                if B[0] == "T":
                    if len(B) == 2:
                        dx = float(B[1])
                        dy = dx
                    else:
                        dx = float(B[1])
                        dy = float(B[2])
                    print(cir.translate(dx, dy))
                elif B[0] == "S":
                    sx = float(B[1])
                    print(cir.scale(sx))
                elif B[0] == "R":
                    if len(B) == 2:
                        deg = float(B[1])
                        rx = 0
                        ry = 0
                    elif len(B) == 3:
                        deg = float(B[1])
                        rx = float(B[2])
                        ry = rx
                    else:
                        deg = B[1]
                        rx = float(B[2])
                        ry = float(B[3])
                    print(cir.rotate(deg, rx, ry))
                elif B[0] == "P":
                    cir.plot()
                if val == 1:
                    cir.plot()


        elif fig == 0:
            n_2 = int(input("Enter number of sides: "))
            A = []
            for k in range(n_2):
                B = list(map(str, input("Enter (x{},y{}): ".format(k+1, k+1)).split()))
                A.append([float(B[0]),float(B[1]),float(1)])
            pol = Polygon(A)
            query = int(input("Enter Number of Query: "))
            for j in range(query):
                print("*" * 30)
                print("""
1) Translate T dx dy
2) scale S sx sy
3) rotate R deg rx ry
4) plot P """)
                print("*" * 30)
                B = list(map(str, input("Enter Query: ").split()))
                if B[0] == "T":
                    if len(B) == 2:
                        dx = float(B[1])
                        dy = dx
                    else:
                        dx = float(B[1])
                        dy = float(B[2])
                    print(pol.translate(dx, dy))
                elif B[0] == "S":
                    if len(B) == 2:
                        sx = float(B[1])
                        sy = sx
                    else:
                        sx = float(B[1])
                        sy = float(B[2])
                    print(pol.scale(sx, sy))

                elif B[0] == "R":
                    if len(B) == 2:
                        deg = float(B[1])
                        rx = 0
                        ry = 0
                    elif len(B) == 3:
                        deg = float(B[1])
                        rx = float(B[2])
                        ry = rx
                    else:
                        deg = B[1]
                        rx = float(B[2])
                        ry = float(B[3])
                    print(pol.rotate(deg, rx, ry))

                elif B[0] == "P":
                    pol.plot()
                if val == 1:
                    pol.plot()

