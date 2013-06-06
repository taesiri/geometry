u, v = var('u,v')
fx = cos(u)*sin(v)
fy = sin(u)*sin(v)
fz = (cos(v)+log(tan(v/2))) + 0.2*u
parametric_plot3d([fx, fy, fz], (u, 0, 12.4), (v, 0.1, 2),frame=False, color="red")