import sympy as sp

# Set sympy matrix display
sp.init_printing(use_latex='mathjax') 
from IPython.display import display

# Define 3d Vector function
def identiteit():
    return sp.Matrix([[1,0,0],[0,1,0],[0,0,1]])

def schalen(x,y):
    return sp.Matrix([[x,o,0],[0,y,0],[0,0,1]])

def roteren(theta):
    theta = theta/180*np.pi
    return sp.Matrix([[np.cos(theta), -np.sin(theta),0],[np.sin(theta), np.cos(theta),0],[0,0,1]])

def verplaatsen(x,y):
    return sp.Matrix([[1, 0, x], [0, 1, y], [0, 0, 1]])

def horizontaal_uitrekken(x):
    return sp.Matrix([[1,x,0],[0,1,0],[0,0,1]])

def verticaal_uitrekken(y):
    return sp.Matrix([[1,0,0],[y,1,0],[0,0,1]])

def spiegelx():
    return sp.Matrix([[-1,0,0],[0,1,0],[0,0,1]])

def spiegely():
    return sp.Matrix([[1,0,0],[0,-1,0],[0,0,1]])

def projecterenx():
    return sp.Matrix([[1,0,0],[0,0,0],[0,0,1]])

def projectereny():
    return sp.Matrix([[0,0,0],[0,1,0],[0,0,1]])

# Define optica matrixes
def translatie(L):
    return sp.Matrix([[1,L],[0,1]])

def refractie(n,na,R):
    return sp.Matrix([[1,0],[(n-na)/(R*na), n/na]])

def sferische_spiegel(R):
    return sp.Matrix([[1,0],[2/R,1]])

def dunne_lens(f):
    return sp.Matrix([[1,0],[-1/f,1]])
