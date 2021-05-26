from figures import GeometricObject, Circle, ResizableCircle, Resizable, Rectangle, ResizableRectangle

def print_figure(gf):
    print(f'{gf}, perimeter = {gf.perimeter():.3f}, area = {gf.area():.3f}')

def double_size(gf):
    if isinstance(gf,Resizable):
        gf.resize(200)
    else:
      print('Figure cannot be enlarged!')

print('Testing figures')
print('****************')
c = Circle()
print_figure(c)
r = Rectangle(10, 20)
print_figure(r)

rc = ResizableCircle(5)
print_figure(rc)
rr = ResizableRectangle(5, 10)
print_figure(rr)

print('\nResizing')
print('****************')
print('Before')
print(rc)
print(rr)
print('After')
rc.resize(10)
rr.resize(150)
print(rc)
print(rr)

print('\nTesting double_size')
print('****************')
double_size(c)
double_size(r)
double_size(rc)
print(rc)
double_size(rr)
print(rr)