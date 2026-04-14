"""Extra content part 1: calculus new topics + top-up for existing calculus."""

def sec(sid, title, body):
    return f'<div class="content-section" id="{sid}"><h2>{title}</h2>{body}</div>'

def p(*texts):
    return "".join(f"<p>{t}</p>" for t in texts)

EXTRA2 = {}

# ── CALCULUS category hub ─────────────────────────────────────────────────────
EXTRA2["calculus"] = [sec("overview","Branches of Calculus", p(
    "Calculus divides into differential calculus (rates of change, derivatives, optimization) and integral calculus (accumulation, areas, volumes). The Fundamental Theorem of Calculus unifies them: differentiation and integration are inverse operations.",
    "Multivariable calculus extends both branches to functions of several variables. Partial derivatives, gradients, and directional derivatives generalize the derivative; double and triple integrals generalize the definite integral. Vector calculus adds line integrals, surface integrals, and the theorems of Green, Stokes, and Gauss.",
    "Differential equations — ordinary and partial — apply calculus to model dynamic systems. From Newton's laws of motion to Maxwell's equations of electromagnetism, the language of science is differential equations built from calculus.",
    "Numerical analysis provides algorithms for computing derivatives and integrals when closed forms are unavailable. Finite difference methods approximate derivatives; quadrature rules (Simpson's, Gaussian) approximate integrals; Runge–Kutta methods solve differential equations numerically."
))]

# ── CALCULUS new topics ───────────────────────────────────────────────────────
EXTRA2["calculus/integral"] = [sec("indepth","In Depth", p(
    "The integral is the central concept of integral calculus, capturing the idea of continuous summation. The indefinite integral (antiderivative) reverses differentiation; the definite integral computes signed area. The Fundamental Theorem of Calculus connects them: \\(\\int_a^b f(x)\\,dx = F(b)-F(a)\\) where \\(F'=f\\).",
    "Riemann integration defines \\(\\int_a^b f\\,dx\\) as the limit of Riemann sums. Lebesgue integration, developed in the early 20th century, extends this to a much larger class of functions and has better convergence properties — the dominated convergence theorem allows limits and integrals to be exchanged under mild conditions.",
    "Improper integrals handle unbounded intervals or unbounded integrands: \\(\\int_1^\\infty x^{-p}\\,dx\\) converges for \\(p>1\\) and diverges for \\(p\\leq1\\). The comparison test, limit comparison test, and Dirichlet's test determine convergence without computing the integral explicitly.",
    "Multiple integrals extend integration to functions of several variables. Fubini's theorem allows a double integral to be computed as iterated single integrals. Change of variables (substitution in multiple dimensions) uses the Jacobian determinant: \\(\\iint_R f\\,dA = \\iint_S f(\\mathbf{g}(u,v))|J|\\,du\\,dv\\)."
))]

EXTRA2["calculus/gradient"] = [sec("indepth","In Depth", p(
    "The gradient \\(\\nabla f = (\\partial f/\\partial x_1, \\ldots, \\partial f/\\partial x_n)\\) is the multivariable generalization of the derivative. It is a vector field that points in the direction of steepest ascent of \\(f\\), with magnitude equal to the maximum rate of change.",
    "The directional derivative \\(D_{\\mathbf{u}}f = \\nabla f \\cdot \\mathbf{u}\\) gives the rate of change in any direction \\(\\mathbf{u}\\). The gradient is perpendicular to level curves (in 2D) and level surfaces (in 3D) — a fact used in implicit differentiation and in defining surface normals.",
    "Gradient descent is the workhorse optimization algorithm in machine learning. Starting from an initial point, it iteratively moves in the direction \\(-\\nabla f\\) (steepest descent) to minimize \\(f\\). Variants include stochastic gradient descent (SGD), momentum, Adam, and RMSProp, each addressing different challenges in high-dimensional optimization.",
    "The gradient theorem (fundamental theorem for line integrals): \\(\\int_C \\nabla f \\cdot d\\mathbf{r} = f(\\mathbf{b}) - f(\\mathbf{a})\\). A vector field is conservative (path-independent) if and only if it is the gradient of some scalar potential function."
))]

EXTRA2["calculus/infinite-limits"] = [sec("indepth","In Depth", p(
    "Infinite limits describe the behavior of functions as the input grows without bound (limits at infinity) or as the function value grows without bound (infinite limits at a point). Both are essential for understanding asymptotic behavior and vertical/horizontal asymptotes.",
    "Horizontal asymptotes: \\(\\lim_{x\\to\\infty} f(x) = L\\) means the graph approaches the horizontal line \\(y=L\\). For rational functions, compare degrees: if degree of numerator < denominator, limit is 0; if equal, limit is the ratio of leading coefficients; if numerator degree is greater, the limit is \\(\\pm\\infty\\).",
    "Vertical asymptotes occur where \\(\\lim_{x\\to a} f(x) = \\pm\\infty\\). For rational functions, these occur at zeros of the denominator that are not canceled by the numerator. The sign of the limit (\\(+\\infty\\) or \\(-\\infty\\)) depends on the sign of the function near \\(a\\).",
    "L'Hôpital's Rule handles indeterminate forms \\(0/0\\) and \\(\\infty/\\infty\\) at infinity: \\(\\lim_{x\\to\\infty} f(x)/g(x) = \\lim_{x\\to\\infty} f'(x)/g'(x)\\). Other indeterminate forms (\\(0\\cdot\\infty\\), \\(\\infty-\\infty\\), \\(0^0\\), \\(1^\\infty\\), \\(\\infty^0\\)) are converted to \\(0/0\\) or \\(\\infty/\\infty\\) by algebraic manipulation."
))]

EXTRA2["calculus/power-series"] = [sec("indepth","In Depth", p(
    "A power series \\(\\sum_{n=0}^\\infty c_n(x-a)^n\\) is an infinite polynomial centered at \\(a\\). Within its radius of convergence \\(R\\), it converges absolutely and defines a smooth (infinitely differentiable) function. Outside \\(|x-a|>R\\), it diverges.",
    "The radius of convergence is determined by the Cauchy–Hadamard formula: \\(1/R = \\limsup_{n\\to\\infty} |c_n|^{1/n}\\). Equivalently, the ratio test gives \\(R = \\lim |c_n/c_{n+1}|\\) when this limit exists.",
    "Power series can be differentiated and integrated term by term within the radius of convergence. This makes them powerful tools for solving differential equations (the power series method) and for computing integrals without closed forms.",
    "Key power series: \\(e^x = \\sum x^n/n!\\) (\\(R=\\infty\\)), \\(\\sin x = \\sum (-1)^n x^{2n+1}/(2n+1)!\\) (\\(R=\\infty\\)), \\(\\cos x = \\sum (-1)^n x^{2n}/(2n)!\\) (\\(R=\\infty\\)), \\(1/(1-x) = \\sum x^n\\) (\\(R=1\\)), \\(\\ln(1+x) = \\sum (-1)^{n+1} x^n/n\\) (\\(R=1\\))."
))]

EXTRA2["calculus/convergence-tests"] = [sec("indepth","In Depth", p(
    "Determining whether an infinite series converges is a central problem in analysis. No single test works for all series; choosing the right test requires recognizing the structure of the terms.",
    "The <strong>divergence test</strong> (necessary condition): if \\(\\sum a_n\\) converges, then \\(a_n\\to0\\). Contrapositive: if \\(a_n\\not\\to0\\), the series diverges. This test can only prove divergence, never convergence.",
    "The <strong>integral test</strong>: if \\(f\\) is positive, continuous, and decreasing on \\([1,\\infty)\\) with \\(f(n)=a_n\\), then \\(\\sum a_n\\) and \\(\\int_1^\\infty f\\,dx\\) either both converge or both diverge. This gives the p-series result: \\(\\sum 1/n^p\\) converges iff \\(p>1\\).",
    "The <strong>ratio test</strong> \\(L=\\lim|a_{n+1}/a_n|\\): converges absolutely if \\(L<1\\), diverges if \\(L>1\\), inconclusive if \\(L=1\\). Best for series with factorials or exponentials. The <strong>root test</strong> \\(L=\\lim|a_n|^{1/n}\\): same conclusion rules. Best for series with \\(n\\)th powers.",
    "The <strong>alternating series test</strong> (Leibniz): \\(\\sum(-1)^n b_n\\) converges if \\(b_n\\) is decreasing and \\(b_n\\to0\\). The error in truncating at \\(N\\) terms is bounded by \\(b_{N+1}\\). This gives a simple error estimate for alternating series approximations."
))]

EXTRA2["calculus/vector-calculus"] = [sec("indepth","In Depth", p(
    "Vector calculus studies differentiation and integration of vector fields — functions that assign a vector to each point in space. The three fundamental operations are the gradient (of a scalar field), divergence (of a vector field), and curl (of a vector field in 3D).",
    "The <strong>divergence</strong> \\(\\nabla\\cdot\\mathbf{F} = \\partial F_1/\\partial x + \\partial F_2/\\partial y + \\partial F_3/\\partial z\\) measures the net outward flux per unit volume at a point. Positive divergence means the field is a source; negative means a sink. The divergence theorem (Gauss): \\(\\oiint_S \\mathbf{F}\\cdot d\\mathbf{S} = \\iiint_V \\nabla\\cdot\\mathbf{F}\\,dV\\).",
    "The <strong>curl</strong> \\(\\nabla\\times\\mathbf{F}\\) measures the rotation of a vector field. A field with zero curl everywhere is irrotational (conservative). Stokes' theorem: \\(\\oint_C \\mathbf{F}\\cdot d\\mathbf{r} = \\iint_S (\\nabla\\times\\mathbf{F})\\cdot d\\mathbf{S}\\), relating a line integral around a closed curve to a surface integral over any surface bounded by that curve.",
    "Maxwell's equations of electromagnetism are elegantly expressed in vector calculus notation. The four equations relate the divergence and curl of the electric and magnetic fields to charge and current densities, predicting electromagnetic waves traveling at the speed of light."
))]

EXTRA2["calculus/higher-order-derivatives"] = [sec("indepth","In Depth", p(
    "The \\(n\\)th derivative \\(f^{(n)}\\) is obtained by differentiating \\(f\\) a total of \\(n\\) times. Higher-order derivatives describe how lower-order rates of change themselves change. In physics, the first three derivatives of position with respect to time are velocity, acceleration, and jerk.",
    "The second derivative \\(f''\\) determines concavity: \\(f''>0\\) means concave up (the graph curves upward like a bowl); \\(f''<0\\) means concave down. Inflection points occur where \\(f''\\) changes sign. The second derivative test for local extrema: if \\(f'(c)=0\\) and \\(f''(c)>0\\), then \\(c\\) is a local minimum.",
    "Taylor's theorem with remainder: \\(f(x) = \\sum_{k=0}^n f^{(k)}(a)(x-a)^k/k! + R_n(x)\\). The Lagrange remainder \\(R_n(x) = f^{(n+1)}(c)(x-a)^{n+1}/(n+1)!\\) for some \\(c\\) between \\(x\\) and \\(a\\). This gives explicit error bounds for polynomial approximations.",
    "Leibniz's rule for the \\(n\\)th derivative of a product: \\((fg)^{(n)} = \\sum_{k=0}^n \\binom{n}{k} f^{(k)} g^{(n-k)}\\). This generalizes the product rule and is analogous to the binomial theorem. It is useful for computing derivatives of products without repeated application of the product rule."
))]

EXTRA2["calculus/implicit-differentiation"] = [sec("indepth","In Depth", p(
    "Implicit differentiation finds \\(dy/dx\\) when \\(y\\) is defined implicitly by an equation \\(F(x,y)=0\\), without solving for \\(y\\) explicitly. Differentiate both sides with respect to \\(x\\), treating \\(y\\) as a function of \\(x\\) and applying the chain rule to every \\(y\\)-term.",
    "The implicit function theorem gives conditions under which an equation \\(F(x,y)=0\\) defines \\(y\\) as a function of \\(x\\) near a point: if \\(F\\) is continuously differentiable and \\(\\partial F/\\partial y \\neq 0\\) at the point, then \\(y\\) is locally a function of \\(x\\) with \\(dy/dx = -(\\partial F/\\partial x)/(\\partial F/\\partial y)\\).",
    "In multivariable calculus, implicit differentiation extends to surfaces \\(F(x,y,z)=0\\): the gradient \\(\\nabla F\\) is normal to the surface, and partial derivatives of \\(z\\) with respect to \\(x\\) and \\(y\\) are \\(\\partial z/\\partial x = -(F_x/F_z)\\) and \\(\\partial z/\\partial y = -(F_y/F_z)\\).",
    "Applications: finding tangent lines to curves defined by polynomial equations (algebraic curves), computing derivatives of inverse functions (\\(d/dx[\\arcsin x] = 1/\\sqrt{1-x^2}\\) is derived by implicit differentiation of \\(\\sin y = x\\)), and analyzing level curves in optimization."
))]

EXTRA2["calculus/separable-equations"] = [sec("indepth","In Depth", p(
    "A separable ODE has the form \\(dy/dx = f(x)g(y)\\). The solution method: separate variables to get \\(dy/g(y) = f(x)\\,dx\\), then integrate both sides. This works whenever \\(g(y)\\neq0\\); solutions where \\(g(y)=0\\) are equilibrium (constant) solutions.",
    "Exponential growth and decay \\(dy/dt = ky\\) is the simplest separable equation. Separating: \\(dy/y = k\\,dt\\), integrating: \\(\\ln|y| = kt+C\\), so \\(y = Ae^{kt}\\). For \\(k>0\\): exponential growth (population, compound interest). For \\(k<0\\): exponential decay (radioactive decay, drug elimination).",
    "The logistic equation \\(dy/dt = ry(1-y/K)\\) is separable. Partial fractions give the solution \\(y(t) = K/(1+Ae^{-rt})\\), an S-shaped curve approaching the carrying capacity \\(K\\). This models population growth with resource limits, epidemic spread, and technology adoption.",
    "Newton's law of cooling \\(dT/dt = -k(T-T_\\infty)\\) is separable: \\(T(t) = T_\\infty + (T_0-T_\\infty)e^{-kt}\\). It models the temperature of an object cooling toward ambient temperature \\(T_\\infty\\), with applications in forensics (estimating time of death) and engineering (thermal management)."
))]

EXTRA2["calculus/linear-differential-equations"] = [sec("indepth","In Depth", p(
    "A first-order linear ODE has the form \\(y' + P(x)y = Q(x)\\). The integrating factor method multiplies both sides by \\(\\mu(x) = e^{\\int P\\,dx}\\), making the left side the derivative of \\(\\mu y\\): \\((\\mu y)' = \\mu Q\\). Integrating gives \\(y = (1/\\mu)\\int \\mu Q\\,dx + C/\\mu\\).",
    "Second-order linear ODEs with constant coefficients \\(ay''+by'+cy=0\\) are solved via the characteristic equation \\(ar^2+br+c=0\\). Three cases: (1) two distinct real roots \\(r_1,r_2\\): \\(y=C_1e^{r_1x}+C_2e^{r_2x}\\); (2) repeated root \\(r\\): \\(y=(C_1+C_2x)e^{rx}\\); (3) complex roots \\(\\alpha\\pm\\beta i\\): \\(y=e^{\\alpha x}(C_1\\cos\\beta x+C_2\\sin\\beta x)\\).",
    "For nonhomogeneous equations \\(ay''+by'+cy=f(x)\\), the general solution is \\(y=y_h+y_p\\) where \\(y_h\\) is the homogeneous solution and \\(y_p\\) is any particular solution. Methods for finding \\(y_p\\): undetermined coefficients (for polynomial, exponential, sinusoidal \\(f\\)) and variation of parameters (general method).",
    "Linear ODEs model spring-mass systems (\\(mx''+bx'+kx=F(t)\\)), RLC circuits (\\(LQ''+RQ'+Q/C=V(t)\\)), and beam deflection. The resonance phenomenon — when the forcing frequency matches the natural frequency — leads to unbounded oscillations in the undamped case, with critical engineering implications."
))]

EXTRA2["calculus/second-order-equations"] = [sec("indepth","In Depth", p(
    "Second-order ODEs \\(F(x,y,y',y'')=0\\) arise naturally in mechanics (Newton's second law), circuit theory, and wave propagation. The general solution of a second-order linear ODE contains two arbitrary constants, determined by two initial conditions (initial value problem) or two boundary conditions (boundary value problem).",
    "The Wronskian \\(W(y_1,y_2) = y_1y_2'-y_2y_1'\\) tests linear independence of two solutions: if \\(W\\neq0\\) on an interval, \\(y_1\\) and \\(y_2\\) form a fundamental set of solutions. Abel's theorem gives \\(W(x) = W(x_0)e^{-\\int_{x_0}^x P(t)\\,dt}\\) for \\(y''+P(x)y'+Q(x)y=0\\).",
    "Boundary value problems (BVPs) specify conditions at two different points. Unlike IVPs, BVPs may have no solution, a unique solution, or infinitely many solutions. Sturm–Liouville theory studies a class of BVPs whose solutions form orthogonal bases — the foundation of Fourier series and spectral methods.",
    "Euler–Cauchy equations \\(x^2y''+axy'+by=0\\) have solutions of the form \\(y=x^r\\). The substitution \\(x=e^t\\) converts them to constant-coefficient equations. They arise in problems with spherical or cylindrical symmetry."
))]

EXTRA2["calculus/multiple-integrals"] = [sec("indepth","In Depth", p(
    "Multiple integrals extend the definite integral to functions of several variables. The double integral \\(\\iint_R f(x,y)\\,dA\\) computes the signed volume under the surface \\(z=f(x,y)\\) over the region \\(R\\). Fubini's theorem: for continuous \\(f\\) on a rectangle, \\(\\iint_R f\\,dA = \\int_a^b\\int_c^d f(x,y)\\,dy\\,dx\\).",
    "For non-rectangular regions, the limits of the inner integral depend on the outer variable. Choosing the order of integration wisely can simplify the computation dramatically. Switching order requires re-describing the region.",
    "Change of variables in double integrals: \\(\\iint_R f(x,y)\\,dA = \\iint_S f(x(u,v),y(u,v))|J|\\,du\\,dv\\) where \\(J = \\partial(x,y)/\\partial(u,v)\\) is the Jacobian determinant. Polar coordinates (\\(x=r\\cos\\theta\\), \\(y=r\\sin\\theta\\), \\(|J|=r\\)) simplify integrals over circular regions.",
    "Triple integrals \\(\\iiint_V f\\,dV\\) compute mass, charge, and other quantities distributed in 3D space. Cylindrical coordinates (\\(|J|=r\\)) suit problems with axial symmetry; spherical coordinates (\\(|J|=\\rho^2\\sin\\phi\\)) suit problems with spherical symmetry."
))]
