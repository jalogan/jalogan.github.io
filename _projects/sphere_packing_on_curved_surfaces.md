---
layout:      project
title:       "Sphere packing on curved 2D manifolds"
published:   true

#date:        2 Jan 2014
order: 1
#image:
#  path:      /assets/img/spheres_on_curved_surfaces/spheres_on_sphere_cover_image.png
#  srcset:
#    1920w:   /assets/img/spheres_on_curved_surfaces/spheres_on_sphere_cover_image.png
#    960w:    /assets/img/spheres_on_curved_surfaces/spheres_on_sphere_cover_image.png
#    480w:    /assets/img/spheres_on_curved_surfaces/spheres_on_sphere_cover_image.png
video:
  path: /assets/videos/spheres_on_curved_surfaces/spheres_moving_on_sphere.mp4
  poster: /assets/img/spheres_on_curved_surfaces/spheres_on_sphere_cover_image.png
caption:     Sphere packings on curved surfaces
#description: >
#  Hyde is a brazen two-column [Jekyll](http://jekyllrb.com) theme.
#  It's based on [Poole](http://getpoole.com), the Jekyll butler.
#links:
#  - title:   Publication
#    url:     https://arxiv.org/pdf/2501.02424
featured:    false
#related_posts: 
---

* this unordered seed list will be replaced by the toc
{:toc}


# **In Progress!**


In this work we use constrained molecular dynamics (MD) to simulate the interactions of soft polydisperse spheres on curved 2D manifolds. Specifically we implement the constrained MD algorithm RATTLE in C++ to study interaction and jamming of spheres on curved manifolds. 



## **Why This Work Matters**


## **Modifying the Equations of Motion**

Standard MD solves Newton's equations of motion

$$
m\ddot{q} = F(q),
$$

where $$q$$ is a generalized position.

Constrained MD solves Newton's equations of motion modified by constraints $$g(q)=0$$

$$
m\ddot{q} = F(q) + \lambda \nabla g(q).
$$

Standard MD velocity verlet algorithm follows a kick-drift-kick form: 

$$
\begin{align*}
\text{Kick:} \quad & v\left(t+\frac{1}{2}\right) = v(t) + \frac{\Delta t}{2m} F(t)\\
\text{Drift:} \quad & q(t+1) = q(t) + \Delta t\, v\left(t+\frac{1}{2}\right)\\
\text{Update Force:} \quad & F(t+1) = F\big(q(t+1)\big)\\
\text{Kick:} \quad & v(t+1) = v\left(t+\frac{1}{2}\right) + \frac{\Delta t}{2m} F(t+1)
\end{align*}
$$

It is time-reversible, symplectic, second-order integrator, which means it preserves temporal symmetry, phase space volume, and has local error (single step) $$\mathcal{O}(\Delta t^3)$$ and global error over many steps $$\mathcal{O}(\Delta t^2)$$.

However, standard velocity verlet doesn't guarantee that the particle positions will stay on a surface or that the velocities will remain tangent to a surface.<br>

RATTLE is effectively constrained velocity verlet. It was introudced by by Hans C. Andersen in his 1983 paper "Rattle: A “velocity” version of the shake algorithm for molecular dynamics calculations." It is still time-reversible, symplectic, and a second-order integrator. It's the perfect choice for simulating the dynamics of systems with constraints.

It has a kick-drift-kick form, but must correct positions and velocities to respect the constraints and keep the particles stuck to the constraint surface and the velocities tangent to that surface. To do this there must be a position constraint and a velocity constraint

$$
\begin{align*}
\text{Position Constraint:} \quad & g\left(q(t)\right) = 0 \\ 
\text{Velocity Constraint:} \quad & \nabla g\left( q(t) \right) \cdot v\left( t \right) = 0. 
\end{align*}
$$

The position constraint in our simulations keeps the particles on the constraint surface (our manifold). The velocity constraint says that the normal vector to the constraint surface at the position of the particle ($$\nabla g\left( q(t+1) \right)$$) must be orthogonal to the velocity vectors--the velocity must lie entirely in the tangent space of the manifold. Really there is only one constraint $$g\left(q(t)\right) = 0$$. The second constraint is really just saying that the position constraint can't change with time 

$$
\begin{align*}
\frac{d}{dt} g\left(q(t)\right) &= 0 \\ 
\nabla g\left( q(t) \right) \cdot v\left( t \right) &= 0.
\end{align*}
$$

This means there is one constraint per particle, but two lagrange multipliers per particle per time step.<br>

The standard form of RATTLE as a modified velocity verlet:

$$
\begin{align*}
\text{Kick:} \quad & v\left(t+\frac{1}{2}\right) = v(t) + \frac{\Delta t}{2m} F(t)\\
\text{Drift:} \quad & q(t+1) = q(t) + \Delta t\, v\left(t+\frac{1}{2}\right)\\
\text{Update Force:} \quad & F(t+1) = F\big(q(t+1)\big)\\
\text{Kick:} \quad & v(t+1) = v\left(t+\frac{1}{2}\right) + \frac{\Delta t}{2m} F(t+1)
\end{align*}
$$