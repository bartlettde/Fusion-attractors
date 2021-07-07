import adsk.core, adsk.fusion, adsk.cam, traceback
import math

# ----------------------------- Colour Selection of line ---------------------------
def colour_selector(selected):

    effect = adsk.fusion.CustomGraphicsSolidColorEffect

    if selected == 'Orange':
        orange = effect.create(adsk.core.Color.create(255,165,0,255))
        return orange
    elif selected == 'Yellow':
        yellow = effect.create(adsk.core.Color.create(255,255,0,255))
        return yellow
    elif selected == 'Green':
        green = effect.create(adsk.core.Color.create(0,128,0,255))
        return green
    elif selected == 'Blue':
        blue = effect.create(adsk.core.Color.create(0,0,255,255))
        return blue
    elif selected == 'Violet':
        violet = effect.create(adsk.core.Color.create(238,130,238,255))
        return violet
    elif selected == 'Red':
        red = effect.create(adsk.core.Color.create(255,0,0,255))
        return red

# ----------------------------- Lorenz Calculations ---------------------------
def lorenz(num_steps, xs, ys, zs):

        # Initial Values
    xs.append(0.0)
    ys.append(1.0)
    zs.append(1.05)

    dt = 0.01

    for i in range(num_steps):
        x_dot, y_dot, z_dot = calc_lorenz(xs[i], ys[i], zs[i])
        xs.append(xs[i] + (x_dot * dt))
        ys.append(ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))
    
    return xs, ys, zs

def calc_lorenz(x, y, z, s = 10, r = 28, b = 2.0667):

    x_dot = s*(y-x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

# ----------------------------- Thomas Calculations ---------------------------
def thomas(num_steps, xs, ys, zs):

    # Initial Values
    xs.append(1.1)
    ys.append(1.1)
    zs.append(-0.01)

    dt = 0.05

    for i in range(num_steps):
        x_dot, y_dot, z_dot = calc_thomas(xs[i], ys[i], zs[i])
        xs.append(xs[i] + (x_dot * dt))
        ys.append(ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))

    return xs, ys, zs

def calc_thomas(x, y, z, b = 0.208186):

    x_dot = math.sin(y) - (b * x)
    y_dot = math.sin(z) - (b * y)
    z_dot = math.sin(x) - (b * z)
    return x_dot, y_dot, z_dot

# ----------------------------- Aizawa Calculations ---------------------------
def aizawa(num_steps, xs, ys, zs):

        # Initial Values
        xs.append(0.1)
        ys.append(1.0)
        zs.append(0.01)

        dt = 0.01

        for i in range(num_steps):
            x_dot, y_dot, z_dot = calc_aizawa(xs[i], ys[i], zs[i])
            xs.append(xs[i] + (x_dot * dt))
            ys.append(ys[i] + (y_dot * dt))
            zs.append(zs[i] + (z_dot * dt))

        return xs, ys, zs

def calc_aizawa(x, y, z, a = 0.95, b = 0.7, c = 0.6, d = 3.5, e = 0.25, f = 0.1):

    x_dot = (z-b)* x-d*y
    y_dot = d*x+(z-b)*y
    z_dot = c+a*z-(pow(z, 3)/3)-(x*x+y*y)*(1+e*z)+f*z*pow(x, 3)
    return x_dot, y_dot, z_dot

# ----------------------------- Dadras Calculations ---------------------------
def dadras(num_steps, xs, ys, zs):
    # Initial Values
    xs.append(0.0)
    ys.append(1.0)
    zs.append(1.05)

    dt = 0.01

    for i in range(num_steps):
        x_dot, y_dot, z_dot = calc_dadras(xs[i], ys[i], zs[i])
        xs.append(xs[i] + (x_dot * dt))
        ys.append(ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))

    return xs, ys, zs

def calc_dadras(x, y, z, a = 3, b = 2.7, c = 1.7, d = 2, e = 9):

    x_dot = y-a*x+b*y*z
    y_dot = c*y-x*z+z
    z_dot = d*x*y-e*z
    return x_dot, y_dot, z_dot

# ----------------------------- Chen Calculations ---------------------------
def chen(num_steps, xs, ys, zs):
    # Initial Values
    xs.append(5.0)
    ys.append(10.0)
    zs.append(10.0)

    dt = 0.0025

    for i in range(num_steps):
        x_dot, y_dot, z_dot = calc_chen(xs[i], ys[i], zs[i])
        xs.append(xs[i] + (x_dot * dt))
        ys.append(ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))

    return xs, ys, zs

def calc_chen(x, y, z, a = 5, b = -10, c = -0.38):

    x_dot = a*x-y*z
    y_dot = b*y+x*z
    z_dot = c*z+x*y/3
    return x_dot, y_dot, z_dot

# ----------------------------- Lorenz84 Calculations ---------------------------
def lorenz84(num_steps, xs, ys, zs):
    # Initial Values
    xs.append(-0.2)
    ys.append(-2.82)
    zs.append(2.71)

    dt = 0.01

    for i in range(num_steps):
        x_dot, y_dot, z_dot = calc_lorenz84(xs[i], ys[i], zs[i])
        xs.append(xs[i] + (x_dot * dt))
        ys.append(ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))

    return xs, ys, zs

def calc_lorenz84(x, y, z, a = 0.95, b = 7.91, f = 4.83, g = 4.66):

    x_dot = -a*x-(y*y)-(z*z)+a*f
    y_dot = -y+x*y-b*x*z+g
    z_dot = -z+b*x*y+x*z
    return x_dot, y_dot, z_dot

# ----------------------------- Rossler Calculations ---------------------------
def rossler(num_steps, xs, ys, zs):

    # Initial Values
    xs.append(10.0)
    ys.append(0.0)
    zs.append(10.0)

    dt = 0.01

    for i in range(num_steps):
        x_dot, y_dot, z_dot = calc_rossler(xs[i], ys[i], zs[i])
        xs.append(xs[i] + (x_dot * dt))
        ys.append(ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))

    return xs, ys, zs

def calc_rossler(x, y, z, a = 0.2, b = 0.2, c = 5.7):

    x_dot = -(y+z)
    y_dot = x+a*y
    z_dot = b+z*(x-c)
    return x_dot, y_dot, z_dot

# ----------------------------- Halvorsen Calculations ---------------------------
def halvorsen(num_steps, xs, ys, zs):
    # Initial Values
    xs.append(-1.48)
    ys.append(-1.51)
    zs.append(2.04)

    dt = 0.01

    for i in range(num_steps):
        x_dot, y_dot, z_dot = calc_halvorsen(xs[i], ys[i], zs[i])
        xs.append(xs[i] + (x_dot * dt))
        ys.append(ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))

    return xs, ys, zs

def calc_halvorsen(x, y, z, a = 1.89):

    x_dot = -a*x-4*y-4*z-(y*y)
    y_dot = -a*y-4*z-4*x-(z*z)
    z_dot = -a*z-4*x-4*y-(x*x)
    return x_dot, y_dot, z_dot

# ----------------------------- Rabinovich-Fabrikant Calculations ---------------------------
def rf(num_steps, xs, ys, zs):
    # Initial Values
    xs.append(0.0)
    ys.append(1.0)
    zs.append(1.05)

    dt = 0.01

    for i in range(num_steps):
        x_dot, y_dot, z_dot = calc_rf(xs[i], ys[i], zs[i])
        xs.append(xs[i] + (x_dot * dt))
        ys.append(ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))

    return xs, ys, zs

def calc_rf(x, y, z, a = 0.14, b = 0.1):

    x_dot = y*(z-1+(x*x))+b*x
    y_dot = x*(3*z+1-(x*x))+b*y
    z_dot = -2*z*(a+x*y)
    return x_dot, y_dot, z_dot

# ----------------------------- Three Scroll Calculations ---------------------------
def three_scroll(num_steps, xs, ys, zs):

    # Initial Values
    xs.append(-0.29)
    ys.append(-0.25)
    zs.append(-0.59)

    dt = 0.01

    for i in range(num_steps):
        x_dot, y_dot, z_dot = calc_three_scroll(xs[i], ys[i], zs[i])
        xs.append(xs[i] + (x_dot * dt))
        ys.append(ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))

    return xs, ys, zs

def calc_three_scroll(x, y, z, a = 0.03248, b = 0.04584, c = 0.00118, d = 0.00013, e = 0.00057, f = 0.0147):

    x_dot = a*(y-x)+d*x*y
    y_dot = b*x-x*z+f*y
    z_dot = c*z+x*y-e*(x*x)
    return x_dot, y_dot, z_dot

# ----------------------------- Sprott Calculations ---------------------------
def sprott(num_steps, xs, ys, zs):
    # Initial Values
    xs.append(0.63)
    ys.append(0.47)
    zs.append(-0.54)

    dt = 0.01

    for i in range(num_steps):
        x_dot, y_dot, z_dot = calc_sprott(xs[i], ys[i], zs[i])
        xs.append(xs[i] + (x_dot * dt))
        ys.append(ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))

    return xs, ys, zs
    
def calc_sprott(x, y, z, a = 2.07, b = 1.79):

    x_dot = y+a*x*y+x*z
    y_dot = 1-b*(x*x)+y*z
    z_dot = x-(x*x)-(y*y)
    return x_dot, y_dot, z_dot

# ----------------------------- Four wing Calculations ---------------------------
def four_wing(num_steps, xs, ys, zs):

    # Initial Values
    xs.append(1.3)
    ys.append(-0.18)
    zs.append(0.01)

    dt = 0.05

    for i in range(num_steps):
        x_dot, y_dot, z_dot = calc_four_wing(xs[i], ys[i], zs[i])
        xs.append(xs[i] + (x_dot * dt))
        ys.append(ys[i] + (y_dot * dt))
        zs.append(zs[i] + (z_dot * dt))

    return xs, ys, zs
    
def calc_four_wing(x, y, z, a = 0.2, b = 0.01, c = -0.4):

    x_dot = a*x+y*z
    y_dot = b*x+c*y-x*z
    z_dot = -z-x*y
    return x_dot, y_dot, z_dot
    