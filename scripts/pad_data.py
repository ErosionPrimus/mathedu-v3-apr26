"""Second-pass: inject a generic 'Key Properties & Applications' section
into every page still under 700 words, using topic-specific content."""
import os, re, sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "public_html")

def p(*texts):
    return "".join(f"<p>{t}</p>" for t in texts)

def sec(body):
    return f'<div class="content-section" id="applications"><h2>Key Properties &amp; Applications</h2>{body}</div>'

# slug -> extra HTML to append
PADS = {}

# ── CALCULUS ──────────────────────────────────────────────────────────────────
PADS["calculus/integral"] = sec(p(
    "Integration has three major computational techniques: substitution (reversing the chain rule), integration by parts \\(\\int u\\,dv=uv-\\int v\\,du\\) (reversing the product rule), and partial fractions (decomposing rational functions). Trigonometric substitution handles integrands involving \\(\\sqrt{a^2-x^2}\\), \\(\\sqrt{a^2+x^2}\\), and \\(\\sqrt{x^2-a^2}\\).",
    "Numerical integration methods — the trapezoidal rule, Simpson's rule, and Gaussian quadrature — approximate definite integrals when antiderivatives are unavailable. Simpson's rule achieves \\(O(h^4)\\) accuracy; Gaussian quadrature with \\(n\\) points is exact for polynomials of degree \\(\\leq2n-1\\).",
    "Applications span every quantitative field: computing areas, volumes, arc lengths, surface areas, work, fluid pressure, probability (CDF from PDF), expected values, and Fourier coefficients. The integral is the fundamental tool for converting local (differential) information into global (cumulative) quantities."
))

PADS["calculus/gradient"] = sec(p(
    "The gradient is central to optimization. At a local minimum or maximum of \\(f\\), \\(\\nabla f=\\mathbf{0}\\) (necessary condition). The second-derivative test uses the Hessian matrix \\(H_{ij}=\\partial^2f/\\partial x_i\\partial x_j\\): if \\(\\nabla f=0\\) and \\(H\\) is positive definite, the point is a local minimum.",
    "Lagrange multipliers use the gradient to optimize \\(f\\) subject to constraints \\(g=0\\): at a constrained extremum, \\(\\nabla f=\\lambda\\nabla g\\). This says the gradient of \\(f\\) is parallel to the gradient of the constraint — the level curves of \\(f\\) and \\(g\\) are tangent.",
    "In physics, the gradient of a scalar potential gives a force field: \\(\\mathbf{F}=-\\nabla V\\) (conservative force). The electric field is \\(\\mathbf{E}=-\\nabla\\phi\\); gravity is \\(\\mathbf{g}=-\\nabla\\Phi\\). The negative sign means forces point toward lower potential energy."
))

PADS["calculus/infinite-limits"] = sec(p(
    "Infinite limits describe vertical asymptotes: \\(\\lim_{x\\to a}f(x)=\\infty\\) means \\(f(x)\\) grows without bound as \\(x\\to a\\). Limits at infinity describe horizontal asymptotes: \\(\\lim_{x\\to\\infty}f(x)=L\\) means \\(f(x)\\to L\\). Rational functions have horizontal asymptotes determined by the ratio of leading coefficients.",
    "L'Hôpital's rule resolves indeterminate forms \\(0/0\\) and \\(\\infty/\\infty\\): if \\(\\lim f/g\\) is indeterminate, then \\(\\lim f/g=\\lim f'/g'\\) (under regularity conditions). Other indeterminate forms (\\(0\\cdot\\infty\\), \\(\\infty-\\infty\\), \\(0^0\\), \\(1^\\infty\\), \\(\\infty^0\\)) are reduced to \\(0/0\\) or \\(\\infty/\\infty\\) by algebraic manipulation.",
    "Infinite limits are essential in asymptotic analysis: big-O notation, little-o notation, and asymptotic equivalence (\\(f\\sim g\\) means \\(f/g\\to1\\)) describe the growth rates of functions and algorithms. The prime number theorem \\(\\pi(x)\\sim x/\\ln x\\) is an asymptotic statement."
))

PADS["calculus/power-series"] = sec(p(
    "A power series \\(\\sum_{n=0}^\\infty a_n(x-c)^n\\) converges absolutely for \\(|x-c|<R\\) (radius of convergence) and diverges for \\(|x-c|>R\\). The radius is \\(R=1/\\limsup|a_n|^{1/n}\\) (Cauchy–Hadamard formula). Behavior at \\(|x-c|=R\\) requires separate analysis.",
    "Within the radius of convergence, power series can be differentiated and integrated term by term. This makes them powerful: the Taylor series of \\(e^x\\), \\(\\sin x\\), \\(\\cos x\\), and \\(\\ln(1+x)\\) are computed by differentiating and evaluating at \\(x=0\\).",
    "Power series are used to define functions (\\(e^z=\\sum z^n/n!\\) for complex \\(z\\)), solve differential equations (Frobenius method), and compute values numerically. The error in truncating at degree \\(N\\) is bounded by the first omitted term (for alternating series) or by Taylor's remainder theorem."
))

PADS["calculus/convergence-tests"] = sec(p(
    "The comparison test: if \\(0\\leq a_n\\leq b_n\\) and \\(\\sum b_n\\) converges, so does \\(\\sum a_n\\). The limit comparison test: if \\(a_n/b_n\\to L>0\\), then \\(\\sum a_n\\) and \\(\\sum b_n\\) converge or diverge together. These reduce unknown series to known benchmarks like \\(\\sum 1/n^p\\).",
    "The ratio test: if \\(|a_{n+1}/a_n|\\to L\\), the series converges absolutely if \\(L<1\\), diverges if \\(L>1\\), and is inconclusive if \\(L=1\\). The root test uses \\(|a_n|^{1/n}\\to L\\) with the same criteria. Both tests work well for series involving factorials or exponentials.",
    "The alternating series test (Leibniz): \\(\\sum(-1)^n b_n\\) converges if \\(b_n\\) decreases to 0. The error in truncating at \\(N\\) terms is at most \\(b_{N+1}\\). Absolute convergence (\\(\\sum|a_n|<\\infty\\)) implies convergence; the converse fails (conditional convergence, e.g., \\(\\sum(-1)^n/n\\))."
))

PADS["calculus/vector-calculus"] = sec(p(
    "The three fundamental theorems of vector calculus generalize the Fundamental Theorem of Calculus to higher dimensions. Green's theorem relates a line integral around a closed curve to a double integral over the enclosed region. Stokes' theorem generalizes this to surfaces in 3D. The Divergence theorem (Gauss) relates a surface integral to a volume integral.",
    "The curl \\(\\nabla\\times\\mathbf{F}\\) measures the rotation of a vector field; a field with zero curl is irrotational (conservative). The divergence \\(\\nabla\\cdot\\mathbf{F}\\) measures the net outflow; a field with zero divergence is solenoidal (incompressible). These operators appear in Maxwell's equations of electromagnetism.",
    "Conservative vector fields satisfy \\(\\mathbf{F}=\\nabla f\\) for some potential \\(f\\). Line integrals of conservative fields are path-independent: \\(\\int_C\\mathbf{F}\\cdot d\\mathbf{r}=f(B)-f(A)\\). Testing for conservatism: \\(\\mathbf{F}\\) is conservative on a simply connected domain iff \\(\\nabla\\times\\mathbf{F}=\\mathbf{0}\\)."
))

PADS["calculus/higher-order-derivatives"] = sec(p(
    "The \\(n\\)-th derivative \\(f^{(n)}\\) is computed by differentiating \\(n\\) times. Leibniz's rule generalizes the product rule: \\((fg)^{(n)}=\\sum_{k=0}^n\\binom{n}{k}f^{(k)}g^{(n-k)}\\). For \\(f(x)=x^m\\), \\(f^{(n)}=m(m-1)\\cdots(m-n+1)x^{m-n}\\) (falling factorial).",
    "Taylor's theorem with remainder: \\(f(x)=\\sum_{k=0}^n f^{(k)}(a)(x-a)^k/k!+R_n(x)\\) where the Lagrange remainder \\(R_n(x)=f^{(n+1)}(c)(x-a)^{n+1}/(n+1)!\\) for some \\(c\\) between \\(a\\) and \\(x\\). This bounds the error in polynomial approximation.",
    "Higher derivatives appear in physics (jerk = third derivative of position, snap = fourth), in the classification of inflection points (\\(f''=0\\) is necessary but not sufficient; check sign change), and in the Euler–Bernoulli beam equation \\(EI\\,d^4w/dx^4=q(x)\\) governing beam deflection."
))

PADS["calculus/implicit-differentiation"] = sec(p(
    "Implicit differentiation applies the chain rule to equations \\(F(x,y)=0\\) without solving for \\(y\\) explicitly. Differentiating both sides with respect to \\(x\\) and treating \\(y\\) as a function of \\(x\\) gives \\(dy/dx=-F_x/F_y\\) (implicit function theorem formula).",
    "The implicit function theorem guarantees that \\(F(x,y)=0\\) defines \\(y\\) as a smooth function of \\(x\\) near a point \\((x_0,y_0)\\) where \\(F_y\\neq0\\). In higher dimensions, \\(F(\\mathbf{x},\\mathbf{y})=\\mathbf{0}\\) defines \\(\\mathbf{y}\\) as a function of \\(\\mathbf{x}\\) when the Jacobian \\(\\partial F/\\partial\\mathbf{y}\\) is invertible.",
    "Applications: finding tangent lines to curves defined implicitly (circles, ellipses, folium of Descartes); related rates problems (how fast is the area of a circle changing as the radius changes?); and computing derivatives of inverse functions (\\(d/dx[\\arcsin x]=1/\\sqrt{1-x^2}\\) via implicit differentiation of \\(\\sin y=x\\))."
))

PADS["calculus/separable-equations"] = sec(p(
    "A separable ODE \\(dy/dx=f(x)g(y)\\) is solved by separating variables: \\(dy/g(y)=f(x)\\,dx\\), then integrating both sides. This gives an implicit solution \\(G(y)=F(x)+C\\) where \\(G'=1/g\\) and \\(F'=f\\). Solving for \\(y\\) (if possible) gives the explicit solution.",
    "Equilibrium solutions occur where \\(g(y)=0\\) — the function \\(y=y_0\\) (constant) satisfies the ODE. Stability analysis determines whether nearby solutions approach or diverge from equilibrium: if \\(g'(y_0)<0\\) (in the autonomous case \\(dy/dx=g(y)\\)), the equilibrium is stable.",
    "Classic separable equations: exponential growth/decay \\(dy/dt=ky\\) (solution \\(y=Ce^{kt}\\)); logistic growth \\(dy/dt=ky(1-y/K)\\) (solution via partial fractions); Newton's law of cooling \\(dT/dt=-k(T-T_\\infty)\\). These model population dynamics, radioactive decay, and heat transfer."
))

PADS["calculus/linear-differential-equations"] = sec(p(
    "A first-order linear ODE \\(y'+P(x)y=Q(x)\\) is solved by the integrating factor \\(\\mu=e^{\\int P\\,dx}\\): multiply both sides by \\(\\mu\\) to get \\((\\mu y)'=\\mu Q\\), then integrate. This always works when \\(P\\) and \\(Q\\) are continuous.",
    "Second-order linear ODEs \\(y''+py'+qy=f(x)\\) have general solution = complementary solution (solving the homogeneous equation) + particular solution. The complementary solution depends on the roots of the characteristic equation \\(r^2+pr+q=0\\): real distinct roots give \\(e^{r_1x},e^{r_2x}\\); repeated root gives \\(e^{rx},xe^{rx}\\); complex roots \\(\\alpha\\pm\\beta i\\) give \\(e^{\\alpha x}\\cos\\beta x,e^{\\alpha x}\\sin\\beta x\\).",
    "The method of undetermined coefficients finds particular solutions when \\(f(x)\\) is a polynomial, exponential, sine, or cosine (or products thereof). Variation of parameters works for any continuous \\(f(x)\\) and uses the Wronskian of the complementary solutions."
))

PADS["calculus/second-order-equations"] = sec(p(
    "The characteristic equation \\(ar^2+br+c=0\\) determines the behavior of solutions to \\(ay''+by'+cy=0\\). The discriminant \\(\\Delta=b^2-4ac\\) classifies: \\(\\Delta>0\\) (overdamped, two real roots), \\(\\Delta=0\\) (critically damped, repeated root), \\(\\Delta<0\\) (underdamped, complex roots with oscillation).",
    "Resonance occurs in the forced equation \\(y''+\\omega_0^2y=F\\cos(\\omega t)\\) when the driving frequency \\(\\omega\\) equals the natural frequency \\(\\omega_0\\). The particular solution grows like \\(t\\sin(\\omega_0 t)\\) — unbounded oscillation. Damping prevents true resonance but produces a maximum response near \\(\\omega_0\\).",
    "The Laplace transform converts a linear ODE with constant coefficients into an algebraic equation: \\(\\mathcal{L}\\{y'\\}=sY-y(0)\\), \\(\\mathcal{L}\\{y''\\}=s^2Y-sy(0)-y'(0)\\). This handles initial conditions automatically and is especially useful for piecewise or impulsive forcing functions."
))

PADS["calculus/multiple-integrals"] = sec(p(
    "Double integrals \\(\\iint_R f(x,y)\\,dA\\) compute volumes, masses, and averages over 2D regions. Fubini's theorem allows evaluation as iterated integrals: \\(\\iint_R f\\,dA=\\int_a^b\\int_{g_1(x)}^{g_2(x)}f(x,y)\\,dy\\,dx\\). The order of integration can be switched (with adjusted limits) to simplify computation.",
    "Change of variables uses the Jacobian: \\(\\iint_R f(x,y)\\,dA=\\iint_S f(x(u,v),y(u,v))|J|\\,du\\,dv\\) where \\(J=\\partial(x,y)/\\partial(u,v)\\). Polar coordinates (\\(J=r\\)), cylindrical (\\(J=r\\)), and spherical (\\(J=\\rho^2\\sin\\phi\\)) are the most common transformations.",
    "Triple integrals extend to 3D: \\(\\iiint_V f\\,dV\\) computes mass, charge, or probability over a 3D region. Applications include computing moments of inertia, centers of mass, and gravitational potentials. The divergence theorem converts volume integrals to surface integrals, often simplifying computation."
))

# ── GEOMETRY ──────────────────────────────────────────────────────────────────
PADS["geometry/surface-area"] = sec(p(
    "Surface area calculations are essential in engineering and science. Heat exchangers maximize surface area to improve thermal transfer. Catalysts use porous materials with enormous surface areas (activated carbon: up to 3000 m²/g). Drug delivery systems use surface area to control dissolution rates.",
    "For parametric surfaces \\(\\mathbf{r}(u,v)\\), the surface area element is \\(dS=|\\mathbf{r}_u\\times\\mathbf{r}_v|\\,du\\,dv\\). The cross product of the partial derivatives gives the normal vector; its magnitude is the area scaling factor. This formula unifies all surface area calculations.",
    "The isoperimetric inequality in 3D: \\(SA^3\\geq36\\pi V^2\\), with equality only for the sphere. This means the sphere is the most efficient shape for enclosing volume — a fact exploited by cells, bubbles, and pressure vessels."
))

PADS["geometry/angle"] = sec(p(
    "Directed angles (signed angles) distinguish clockwise from counterclockwise rotation, essential in navigation, robotics, and complex number arithmetic. The argument of a complex number \\(z=re^{i\\theta}\\) is a directed angle. Multiplying complex numbers adds their arguments.",
    "Solid angles measure the 2D angle subtended by a surface at a point in 3D, measured in steradians. A full sphere subtends \\(4\\pi\\) steradians. Solid angles appear in radiometry (measuring light intensity), gravitational physics, and the inverse-square law.",
    "In non-Euclidean geometry, angle sums differ from 180°. On a sphere, the angle sum of a triangle exceeds 180° by an amount proportional to the triangle's area (spherical excess). In hyperbolic geometry, the angle sum is less than 180°."
))

PADS["geometry/distance-formula"] = sec(p(
    "The distance formula generalizes to non-Euclidean settings. On a sphere of radius \\(R\\), the great-circle distance between points with latitudes/longitudes is given by the haversine formula, used in GPS and aviation. In special relativity, the spacetime interval \\(ds^2=c^2dt^2-dx^2-dy^2-dz^2\\) replaces Euclidean distance.",
    "Signed distance functions (SDFs) assign to each point the signed distance to a surface (positive outside, negative inside). They are used in computer graphics for ray marching, collision detection, and smooth blending of shapes. The gradient of an SDF has unit magnitude everywhere (the Eikonal equation).",
    "In machine learning, distance metrics define similarity. The choice of metric profoundly affects clustering and classification. The Mahalanobis distance \\(d=\\sqrt{(\\mathbf{x}-\\boldsymbol{\\mu})^T\\Sigma^{-1}(\\mathbf{x}-\\boldsymbol{\\mu})}\\) accounts for correlations between features and is scale-invariant."
))

PADS["geometry/solid-geometry"] = sec(p(
    "Cavalieri's principle: two solids with equal cross-sectional areas at every height have equal volumes. This elegant principle derives the volume of a sphere from that of a cylinder minus a cone, without integration. It was used by Archimedes and later formalized by Cavalieri.",
    "The method of shells and disks computes volumes of revolution. The disk method integrates \\(\\pi[f(x)]^2\\) along the axis; the shell method integrates \\(2\\pi x f(x)\\). Choosing the right method depends on the axis of revolution and the shape of the region.",
    "In architecture and engineering, solid geometry underlies structural analysis. The moment of inertia of a cross-section determines beam stiffness. The centroid of a solid determines its balance point. Finite element methods discretize solids into tetrahedral or hexahedral elements for stress analysis."
))

PADS["geometry/sphere"] = sec(p(
    "Packing spheres efficiently is a classical problem. Kepler's conjecture (1611) — that face-centered cubic packing achieves the maximum density of \\(\\pi/(3\\sqrt{2})\\approx74\\%\\) — was proved by Hales in 1998 using computer-assisted proof. The 2D analogue (circle packing) was proved by Thue in 1910.",
    "The \\(n\\)-sphere \\(S^n\\) is the set of unit vectors in \\(\\mathbb{R}^{n+1}\\). Its volume (surface area) is \\(2\\pi^{(n+1)/2}/\\Gamma((n+1)/2)\\). Interestingly, the volume of the unit ball in \\(\\mathbb{R}^n\\) peaks at \\(n=5\\) and then decreases to 0 — high-dimensional spheres are 'thin'.",
    "Spherical harmonics \\(Y_l^m(\\theta,\\phi)\\) are the eigenfunctions of the Laplacian on the sphere. They form an orthonormal basis for \\(L^2(S^2)\\) and are used in quantum mechanics (atomic orbitals), geophysics (modeling Earth's gravitational field), and computer graphics (environment lighting)."
))

PADS["geometry/polyhedron"] = sec(p(
    "The four-color theorem (proved 1976) states that any planar map can be colored with 4 colors so adjacent regions have different colors. Via the duality between planar graphs and polyhedra, this is equivalent to a statement about coloring the faces of polyhedra.",
    "Geodesic domes (Buckminster Fuller) approximate spheres with triangulated polyhedra. The icosahedron is the starting point; subdividing its faces and projecting onto the sphere gives geodesic polyhedra with high symmetry and structural efficiency.",
    "In virology, many virus capsids have icosahedral symmetry — the most efficient way to build a closed shell from identical protein subunits. The Caspar–Klug theory classifies viral capsids by their triangulation number \\(T=h^2+hk+k^2\\)."
))

PADS["geometry/similarity"] = sec(p(
    "The side-splitter theorem: a line parallel to one side of a triangle divides the other two sides proportionally. This is the key tool for proving similar triangles and for constructions involving proportional division of segments.",
    "Scale models and maps use similarity. A 1:50000 map means distances on the map are 1/50000 of real distances; areas are scaled by \\((1/50000)^2\\). Engineering drawings specify scale factors; architectural models use similarity to represent buildings.",
    "Fractal geometry studies self-similar objects — shapes that are similar to parts of themselves at all scales. The Sierpiński triangle, Koch snowflake, and Mandelbrot set are self-similar. Their fractal dimension (between 1 and 2 for planar fractals) measures their complexity."
))

PADS["geometry/congruence"] = sec(p(
    "The triangle congruence criteria (SSS, SAS, ASA, AAS) are used in engineering to ensure structural rigidity. A triangulated truss is rigid because triangles are the only rigid polygon — adding a diagonal to a quadrilateral creates two triangles and rigidifies it.",
    "In manufacturing, congruence (dimensional tolerance) ensures interchangeable parts. Two parts are 'congruent' within tolerance if their dimensions agree within specified limits. Statistical process control monitors whether manufactured parts remain within tolerance.",
    "Congruence transformations (isometries) form the Euclidean group E(n). In 2D, every isometry is a translation, rotation, reflection, or glide reflection. The classification of wallpaper patterns (17 groups) and frieze patterns (7 groups) uses the theory of isometry groups."
))

PADS["geometry/plane-geometry"] = sec(p(
    "The nine-point circle of a triangle passes through the midpoints of the sides, the feet of the altitudes, and the midpoints of the segments from vertices to the orthocenter. Its radius is half the circumradius. The nine-point center lies on the Euler line.",
    "Projective geometry extends the Euclidean plane by adding a 'line at infinity' where parallel lines meet. In projective geometry, any two lines intersect (in exactly one point), and duality exchanges points and lines. Projective transformations (homographies) are used in computer vision.",
    "Inversive geometry studies transformations that map circles and lines to circles and lines. Inversion in a circle maps a point \\(P\\) to \\(P'\\) on the same ray with \\(OP\\cdot OP'=r^2\\). It is conformal (angle-preserving) and is used in solving Apollonius circle problems."
))

PADS["geometry/euclidean-geometry"] = sec(p(
    "Euclid's Elements is organized as a deductive system: definitions, postulates (axioms), and propositions (theorems). Book I covers basic plane geometry; Books II–IV cover geometric algebra and circles; Book V covers proportion; Books VII–IX cover number theory; Book X covers irrationals; Books XI–XIII cover solid geometry.",
    "The discovery of non-Euclidean geometry in the 19th century was revolutionary. It showed that mathematics need not describe physical reality — geometry is a formal system, and different axiom systems give different geometries. Einstein's general relativity uses Riemannian geometry (curved spacetime) to describe gravity.",
    "Tarski's axioms (1959) give a complete, decidable axiomatization of Euclidean geometry — every statement in the language of Euclidean geometry is either provable or disprovable. This contrasts with arithmetic (Gödel's incompleteness theorems) and shows Euclidean geometry is simpler than arithmetic."
))

PADS["geometry/analytic-geometry"] = sec(p(
    "Vectors in the plane and space provide a powerful language for analytic geometry. The dot product gives angles; the cross product gives areas and normals. Vector equations of lines (\\(\\mathbf{r}=\\mathbf{a}+t\\mathbf{b}\\)) and planes (\\(\\mathbf{n}\\cdot(\\mathbf{r}-\\mathbf{a})=0\\)) are more flexible than Cartesian equations.",
    "Parametric curves \\((x(t),y(t))\\) describe paths that cannot be expressed as \\(y=f(x)\\). Arc length: \\(L=\\int_a^b\\sqrt{(dx/dt)^2+(dy/dt)^2}\\,dt\\). Curvature: \\(\\kappa=|x'y''-y'x''|/(x'^2+y'^2)^{3/2}\\). These formulas apply to any smooth parametric curve.",
    "Polar coordinates \\((r,\\theta)\\) simplify curves with rotational symmetry. The cardioid \\(r=1+\\cos\\theta\\), rose curves \\(r=\\cos(n\\theta)\\), and Archimedean spiral \\(r=a\\theta\\) are naturally expressed in polar form. Area in polar coordinates: \\(A=\\frac{1}{2}\\int_\\alpha^\\beta r^2\\,d\\theta\\)."
))

PADS["geometry/differential-geometry"] = sec(p(
    "Geodesics are the 'straightest possible' curves on a surface — they generalize straight lines. On a sphere, geodesics are great circles. On a cylinder, they are helices. Geodesics satisfy the geodesic equation, a second-order ODE derived from the metric.",
    "Minimal surfaces have zero mean curvature (\\(H=(\\kappa_1+\\kappa_2)/2=0\\)) and locally minimize area. Soap films spanning a wire frame form minimal surfaces. Examples: the catenoid (surface of revolution of a catenary), the helicoid, and Scherk's surface.",
    "The Ricci flow, introduced by Hamilton and used by Perelman to prove the Poincaré conjecture (2003), evolves a Riemannian metric by \\(\\partial g/\\partial t=-2\\text{Ric}\\). It smooths out irregularities in the metric, eventually producing a metric of constant curvature."
))

PADS["geometry/conic-sections"] = sec(p(
    "Kepler's first law: planetary orbits are ellipses with the Sun at one focus. The eccentricity of Earth's orbit is 0.017 (nearly circular); Pluto's is 0.25. Comets often have highly eccentric elliptical or parabolic orbits.",
    "Parabolic reflectors focus parallel rays to a point (the focus): satellite dishes, telescope mirrors, and car headlights use parabolic shapes. The reflective property — a ray from the focus reflects parallel to the axis — follows from the equal-angle reflection law and the focus-directrix definition.",
    "Hyperbolas appear in navigation (LORAN uses hyperbolic position lines), in the Bohr model of atomic scattering (Rutherford scattering), and in the shape of cooling towers. The asymptotes of a hyperbola \\(x^2/a^2-y^2/b^2=1\\) are \\(y=\\pm(b/a)x\\)."
))

PADS["geometry/geometric-constructions"] = sec(p(
    "Origami (paper folding) is more powerful than compass-and-straightedge: it can trisect angles and double the cube. Huzita–Hatori axioms formalize origami constructions. Origami can solve cubic and quartic equations, making it strictly more powerful than classical constructions.",
    "Neusis constructions (using a marked straightedge) can also trisect angles and double the cube. Archimedes described a neusis trisection. The additional power comes from the ability to set a specific length on the straightedge.",
    "In computer-aided design, geometric constructions are replaced by constraint-based modeling: specify geometric relationships (parallel, perpendicular, tangent, equal length) and the software solves the constraint system. This is the modern analogue of classical construction."
))

PADS["geometry/quadrilateral"] = sec(p(
    "The area of a general quadrilateral with diagonals \\(d_1,d_2\\) meeting at angle \\(\\theta\\) is \\(A=\\frac{1}{2}d_1d_2\\sin\\theta\\). For a parallelogram, the diagonals bisect each other, so this simplifies. For a rhombus (\\(\\theta=90°\\)): \\(A=\\frac{1}{2}d_1d_2\\).",
    "Tangential quadrilaterals (with an inscribed circle) satisfy \\(AB+CD=BC+DA\\) (sum of opposite sides are equal). Bicentric quadrilaterals are both cyclic and tangential; they satisfy both Brahmagupta's formula and the tangential condition.",
    "In computer graphics, quadrilaterals (quads) are the preferred polygon for mesh modeling because they subdivide cleanly (Catmull–Clark subdivision) and align naturally with surface curvature. Triangle meshes are used for rendering; quad meshes for modeling."
))

PADS["geometry/line-geometry"] = sec(p(
    "Pencils of lines (all lines through a point) and pencils of planes (all planes through a line) are fundamental in projective geometry. Cross-ratio, a projective invariant, measures the relative position of four collinear points and is preserved by all projective transformations.",
    "In computational geometry, line segment intersection is a fundamental problem. The Bentley–Ottmann algorithm finds all \\(k\\) intersections among \\(n\\) segments in \\(O((n+k)\\log n)\\) time using a sweep line. This is used in GIS, VLSI design, and computational topology.",
    "Duality in projective geometry exchanges points and lines: every theorem about points and lines has a dual theorem obtained by swapping the words 'point' and 'line'. Desargues' theorem and its converse are dual to each other."
))

PADS["geometry/transformation-geometry"] = sec(p(
    "Affine transformations preserve parallelism and ratios of lengths along parallel lines. They include linear transformations (represented by matrices) plus translations. Every affine transformation of \\(\\mathbb{R}^n\\) has the form \\(\\mathbf{x}\\mapsto A\\mathbf{x}+\\mathbf{b}\\) with \\(A\\) invertible.",
    "Möbius transformations \\(f(z)=(az+b)/(cz+d)\\) (\\(ad-bc\\neq0\\)) are the conformal automorphisms of the Riemann sphere. They map circles and lines to circles and lines, and are used in complex analysis, hyperbolic geometry, and electrical engineering (Smith chart).",
    "In computer graphics, the model-view-projection pipeline applies a sequence of transformations: model (object to world coordinates), view (world to camera), projection (3D to 2D). Each is a matrix multiplication; the pipeline is a composition of affine and projective transformations."
))

PADS["geometry/point-geometry"] = sec(p(
    "The Euler line of a triangle passes through the circumcenter \\(O\\), centroid \\(G\\), and orthocenter \\(H\\), with \\(OG:GH=1:2\\). The nine-point center \\(N\\) also lies on the Euler line, midway between \\(O\\) and \\(H\\). This collinearity holds for all non-equilateral triangles.",
    "Voronoi diagrams partition the plane into regions based on proximity to a set of seed points. Each region contains all points closer to its seed than to any other. Voronoi diagrams are dual to Delaunay triangulations and are used in GIS, robotics, and computational biology.",
    "In topology, fixed-point theorems are fundamental. The Brouwer fixed-point theorem: any continuous map from a closed ball to itself has a fixed point. The Lefschetz fixed-point theorem counts fixed points using algebraic topology. These have applications in economics, game theory, and differential equations."
))

# ── NUMBER THEORY ─────────────────────────────────────────────────────────────
PADS["number-theory/composite-number"] = sec(p(
    "Smooth numbers (numbers with only small prime factors) are important in factoring algorithms. The quadratic sieve and number field sieve collect relations involving smooth numbers to factor large composites. A number is \\(B\\)-smooth if all its prime factors are \\(\\leq B\\).",
    "The Carmichael numbers are composite numbers \\(n\\) satisfying \\(a^{n-1}\\equiv1\\pmod{n}\\) for all \\(a\\) with \\(\\gcd(a,n)=1\\) — they fool Fermat's primality test. The smallest is 561=3×11×17. The Miller–Rabin test is not fooled by Carmichael numbers.",
    "Semiprime numbers (products of exactly two primes) are the basis of RSA cryptography. The difficulty of factoring a semiprime \\(n=pq\\) into its prime factors \\(p\\) and \\(q\\) is the computational hardness assumption underlying RSA security."
))

PADS["number-theory/congruence"] = sec(p(
    "Wilson's theorem: \\(p\\) is prime iff \\((p-1)!\\equiv-1\\pmod{p}\\). While impractical for primality testing (computing \\((p-1)!\\) is expensive), it is theoretically elegant and has applications in combinatorics.",
    "The structure of \\(\\mathbb{Z}/n\\mathbb{Z}\\): it is a field iff \\(n\\) is prime. The group of units \\((\\mathbb{Z}/n\\mathbb{Z})^*\\) has order \\(\\phi(n)\\) and is cyclic iff \\(n=1,2,4,p^k,2p^k\\). Understanding this group structure is essential for cryptographic applications.",
    "Congruences modulo prime powers: Hensel's lemma lifts solutions of \\(f(x)\\equiv0\\pmod{p}\\) to solutions modulo \\(p^k\\), provided \\(f'(x)\\not\\equiv0\\pmod{p}\\). This is the \\(p\\)-adic analogue of Newton's method and is used in solving polynomial congruences."
))

PADS["number-theory/least-common-multiple"] = sec(p(
    "The lcm appears in the analysis of the Euclidean algorithm: the number of steps to compute \\(\\gcd(a,b)\\) is related to the size of \\(a\\) and \\(b\\) relative to their gcd. Fibonacci numbers are the worst case.",
    "In ring theory, the lcm of two ideals \\(I\\) and \\(J\\) in a PID is their intersection \\(I\\cap J\\). For principal ideals \\((a)\\) and \\((b)\\), \\((a)\\cap(b)=(\\text{lcm}(a,b))\\). This generalizes the integer lcm to polynomial rings and other PIDs.",
    "The Chebyshev function \\(\\psi(n)=\\ln\\text{lcm}(1,2,\\ldots,n)\\) is closely related to the prime counting function. The prime number theorem is equivalent to \\(\\psi(n)\\sim n\\). This connection makes the lcm of consecutive integers a tool in analytic number theory."
))

PADS["number-theory/continued-fractions"] = sec(p(
    "The Euclidean algorithm and continued fractions are intimately connected: the quotients in the Euclidean algorithm are exactly the partial quotients of the continued fraction. The number of steps equals the number of partial quotients.",
    "Diophantine approximation: Hurwitz's theorem states that for any irrational \\(\\alpha\\), there are infinitely many rationals \\(p/q\\) with \\(|\\alpha-p/q|<1/(\\sqrt{5}q^2)\\). The constant \\(\\sqrt{5}\\) is best possible (achieved by the golden ratio). The convergents of the continued fraction provide these approximations.",
    "Continued fractions are used in the PSLQ algorithm (integer relation detection), in the analysis of hash functions and pseudorandom number generators, and in the theory of dynamical systems (rotation numbers of circle maps are continued fractions)."
))

PADS["number-theory/euler-totient"] = sec(p(
    "Carmichael's function \\(\\lambda(n)\\) is the smallest \\(m\\) such that \\(a^m\\equiv1\\pmod{n}\\) for all \\(\\gcd(a,n)=1\\). It divides \\(\\phi(n)\\) and equals \\(\\phi(n)\\) when \\((\\mathbb{Z}/n\\mathbb{Z})^*\\) is cyclic. Using \\(\\lambda(n)\\) instead of \\(\\phi(n)\\) in RSA gives smaller exponents.",
    "The totient function satisfies \\(\\phi(n)=n\\prod_{p|n}(1-1/p)\\). For \\(n=p_1^{a_1}\\cdots p_k^{a_k}\\), this is \\(\\phi(n)=p_1^{a_1-1}(p_1-1)\\cdots p_k^{a_k-1}(p_k-1)\\). The totient is even for all \\(n>2\\).",
    "Euler's product formula \\(\\zeta(s)\\prod_p(1-p^{-s})=1\\) (where the product is over all primes) is equivalent to the Fundamental Theorem of Arithmetic. It connects the totient function (via the Euler product for \\(\\phi\\)) to the Riemann zeta function."
))

PADS["number-theory/diophantine-equations"] = sec(p(
    "The Pythagorean triples \\((a,b,c)\\) with \\(a^2+b^2=c^2\\) are parameterized by \\(a=m^2-n^2\\), \\(b=2mn\\), \\(c=m^2+n^2\\) for integers \\(m>n>0\\) with \\(\\gcd(m,n)=1\\) and \\(m\\not\\equiv n\\pmod2\\). This gives all primitive triples.",
    "Waring's problem: every positive integer is a sum of at most \\(g(k)\\) perfect \\(k\\)-th powers. Lagrange's four-square theorem (\\(g(2)=4\\)) states every positive integer is a sum of four squares. Hilbert proved \\(g(k)\\) is finite for all \\(k\\); the exact values are known for small \\(k\\).",
    "The ABC conjecture (Masser–Oesterlé, 1985) states that for coprime \\(a+b=c\\), the product of distinct prime factors of \\(abc\\) (the 'radical') is usually large relative to \\(c\\). It implies Fermat's Last Theorem and many other results. Mochizuki claimed a proof in 2012; the mathematical community has not reached consensus."
))

PADS["number-theory/euclidean-algorithm"] = sec(p(
    "The Euclidean algorithm is the oldest non-trivial algorithm still in widespread use. Its time complexity is \\(O(\\log\\min(a,b))\\) divisions, or \\(O(\\log^2 n)\\) bit operations. For large integers, fast multiplication (Karatsuba, FFT-based) reduces this to \\(O(M(n)\\log n)\\) where \\(M(n)\\) is the multiplication cost.",
    "The subresultant algorithm extends the Euclidean algorithm to polynomials, computing GCDs without coefficient explosion. It is used in computer algebra systems (Mathematica, Maple, SageMath) for symbolic computation.",
    "The Euclidean algorithm has a beautiful connection to the Stern–Brocot tree: the sequence of quotients in the algorithm traces a path in the tree from the root to the fraction \\(a/b\\). This gives a bijection between positive rationals and finite binary strings."
))

PADS["number-theory/p-adic-numbers"] = sec(p(
    "The \\(p\\)-adic integers \\(\\mathbb{Z}_p\\) are the completion of \\(\\mathbb{Z}\\) under the \\(p\\)-adic metric. They form a compact ring containing \\(\\mathbb{Z}\\) as a dense subring. Every \\(p\\)-adic integer has a unique expansion \\(\\sum_{k=0}^\\infty a_k p^k\\) with \\(0\\leq a_k<p\\).",
    "The \\(p\\)-adic exponential and logarithm converge on appropriate domains in \\(\\mathbb{Z}_p\\), enabling \\(p\\)-adic analysis. The \\(p\\)-adic gamma function and \\(p\\)-adic \\(L\\)-functions are analytic functions on \\(\\mathbb{Z}_p\\) that interpolate classical number-theoretic functions.",
    "In the Langlands program, \\(p\\)-adic representations of Galois groups are central objects. The \\(p\\)-adic Langlands correspondence (proved for \\(GL_2(\\mathbb{Q}_p)\\) by Colmez and Kisin) relates \\(p\\)-adic Galois representations to \\(p\\)-adic representations of \\(GL_2(\\mathbb{Q}_p)\\)."
))

PADS["number-theory/sieve-of-eratosthenes"] = sec(p(
    "The sieve of Eratosthenes has time complexity \\(O(N\\log\\log N)\\) due to the harmonic series of prime reciprocals: \\(\\sum_{p\\leq N}1/p\\sim\\ln\\ln N\\). The segmented sieve processes the range \\([L,R]\\) using only primes up to \\(\\sqrt{R}\\), requiring \\(O(\\sqrt{R})\\) space.",
    "Wheel factorization pre-eliminates multiples of small primes (2, 3, 5, …) before sieving, reducing the work by a constant factor. A wheel of circumference 30 (= 2×3×5) reduces candidates by 73%, giving a practical speedup.",
    "The prime number theorem implies the average gap between consecutive primes near \\(N\\) is \\(\\ln N\\). Cramér's conjecture predicts the maximum gap is \\(O((\\ln N)^2)\\). The largest known prime gaps are consistent with this but the conjecture is unproved."
))

PADS["number-theory/perfect-numbers"] = sec(p(
    "The abundancy index \\(\\sigma(n)/n\\) classifies numbers: deficient (\\(<2\\)), perfect (\\(=2\\)), abundant (\\(>2\\)). The natural density of abundant numbers is about 24.76%. Every multiple of an abundant number is abundant; every divisor of a deficient number is deficient.",
    "Sociable numbers generalize amicable pairs: a cycle \\(n_1\\to n_2\\to\\cdots\\to n_k\\to n_1\\) where each number is the sum of proper divisors of the previous. Amicable pairs are 2-cycles. The smallest known 4-cycle starts at 1264460.",
    "The Riemann hypothesis is equivalent to a statement about the sum of divisors: \\(\\sigma(n)<e^\\gamma n\\ln\\ln n\\) for all \\(n>5040\\) (Robin's inequality). This connects the ancient study of perfect numbers to the deepest unsolved problem in mathematics."
))

PADS["number-theory/arithmetic-functions"] = sec(p(
    "The Ramanujan sum \\(c_q(n)=\\sum_{\\gcd(k,q)=1}e^{2\\pi ikn/q}\\) is a multiplicative arithmetic function that appears in the Fourier analysis of arithmetic functions. It satisfies \\(c_q(n)=\\mu(q/\\gcd(n,q))\\phi(q)/\\phi(q/\\gcd(n,q))\\).",
    "Selberg's formula \\(\\sum_{p\\leq x}(\\ln p)^2+\\sum_{pq\\leq x}\\ln p\\ln q=2x\\ln x+O(x)\\) is the starting point for the elementary proof of the prime number theorem. It shows that primes are 'almost' uniformly distributed without using complex analysis.",
    "The Dirichlet hyperbola method computes \\(\\sum_{n\\leq x}(f*g)(n)\\) efficiently by splitting the sum at \\(\\sqrt{x}\\). Applied to \\(d=1*1\\), it gives \\(\\sum_{n\\leq x}d(n)=x\\ln x+(2\\gamma-1)x+O(\\sqrt{x})\\) — the Dirichlet divisor problem."
))

PADS["number-theory/mersenne-primes"] = sec(p(
    "The Lucas–Lehmer test is highly efficient: it requires only \\(p-2\\) squarings modulo \\(M_p\\), each taking \\(O(p^2)\\) bit operations naively or \\(O(p\\log p\\log\\log p)\\) with FFT-based multiplication. This makes testing 100-million-digit Mersenne numbers feasible.",
    "Mersenne numbers \\(M_p=2^p-1\\) have a special factorization structure: any prime factor \\(q\\) of \\(M_p\\) satisfies \\(q\\equiv1\\pmod{p}\\) and \\(q\\equiv\\pm1\\pmod{8}\\). This restricts the possible factors and speeds up trial division.",
    "The New Mersenne conjecture (Bateman, Selfridge, Wagstaff): if two of the three conditions hold — (1) \\(p=2^k\\pm1\\) or \\(p=4^k\\pm3\\), (2) \\(2^p-1\\) is prime, (3) \\((2^p+1)/3\\) is prime — then the third also holds. This is verified for all known cases but unproved."
))

PADS["number-theory/quadratic-residue"] = sec(p(
    "The Tonelli–Shanks algorithm computes \\(\\sqrt{a}\\bmod p\\) in \\(O(\\log^2 p)\\) time. It factors \\(p-1=2^s\\cdot q\\) (\\(q\\) odd) and uses the structure of the 2-Sylow subgroup of \\((\\mathbb{Z}/p\\mathbb{Z})^*\\). The Cipolla algorithm is an alternative with similar complexity.",
    "Gauss sums \\(g(\\chi)=\\sum_{a=0}^{p-1}\\chi(a)e^{2\\pi ia/p}\\) for the Legendre symbol \\(\\chi=(\\cdot/p)\\) satisfy \\(|g(\\chi)|^2=p\\). They are used to prove quadratic reciprocity and appear in the functional equation of Dirichlet \\(L\\)-functions.",
    "Quadratic residues are used in the construction of Paley graphs: vertices are elements of \\(\\mathbb{F}_p\\), with edges between \\(x\\) and \\(y\\) iff \\(x-y\\) is a nonzero QR. Paley graphs are self-complementary and have strong pseudorandom properties, making them useful in combinatorics and coding theory."
))

PADS["number-theory/mobius-function"] = sec(p(
    "The Möbius function is the key to the inclusion-exclusion principle in number theory. The number of integers in \\([1,n]\\) coprime to \\(m\\) is \\(\\sum_{d|m}\\mu(d)\\lfloor n/d\\rfloor\\). This is used to count lattice points, compute Euler's totient, and analyze the distribution of squarefree numbers.",
    "The Mertens function \\(M(x)=\\sum_{n\\leq x}\\mu(n)\\) oscillates around 0. The prime number theorem is equivalent to \\(M(x)=o(x)\\). The Riemann hypothesis is equivalent to \\(M(x)=O(x^{1/2+\\epsilon})\\). The disproved Mertens conjecture \\(|M(x)|<\\sqrt{x}\\) would have implied RH.",
    "In combinatorics, the Möbius function of a poset \\(P\\) is defined by \\(\\mu(x,x)=1\\) and \\(\\sum_{x\\leq z\\leq y}\\mu(x,z)=0\\) for \\(x<y\\). Möbius inversion on posets generalizes the number-theoretic version and is used in the theory of lattices, matroids, and the chromatic polynomial."
))

PADS["number-theory/analytic-number-theory"] = sec(p(
    "The explicit formula for \\(\\pi(x)\\): \\(\\pi(x)=\\text{Li}(x)-\\sum_\\rho\\text{Li}(x^\\rho)-\\ln2+\\int_x^\\infty\\frac{dt}{t(t^2-1)\\ln t}\\) where the sum is over non-trivial zeros \\(\\rho\\) of \\(\\zeta\\). Each zero contributes an oscillation to \\(\\pi(x)\\); the Riemann hypothesis controls the size of these oscillations.",
    "The large sieve inequality bounds exponential sums over primes and is a key tool in analytic number theory. It implies the Bombieri–Vinogradov theorem: primes are equidistributed in arithmetic progressions on average, with an error as good as GRH would give for individual progressions.",
    "Exponential sums \\(\\sum_{n\\leq N}e^{2\\pi i f(n)}\\) (Weyl sums) measure the equidistribution of sequences modulo 1. Weyl's theorem: \\(\\{n^k\\alpha\\}\\) is equidistributed for irrational \\(\\alpha\\). Van der Corput's method bounds these sums using repeated differencing."
))

PADS["number-theory/primitive-root"] = sec(p(
    "The index (discrete logarithm) of \\(a\\) with respect to primitive root \\(g\\) modulo \\(p\\) is the unique \\(k\\in\\{0,\\ldots,p-2\\}\\) with \\(g^k\\equiv a\\pmod{p}\\). Index arithmetic: \\(\\text{ind}(ab)\\equiv\\text{ind}(a)+\\text{ind}(b)\\pmod{p-1}\\), analogous to logarithm laws.",
    "Baby-step giant-step computes discrete logs in \\(O(\\sqrt{p})\\) time and space. The index calculus method achieves subexponential time \\(L_p[1/2]\\) for prime fields. For elliptic curves, no subexponential algorithm is known, making ECC more efficient than RSA for equivalent security.",
    "Primitive roots modulo prime powers: if \\(g\\) is a primitive root mod \\(p\\), then either \\(g\\) or \\(g+p\\) is a primitive root mod \\(p^k\\) for all \\(k\\geq1\\). This lifts primitive roots from \\(\\mathbb{Z}/p\\mathbb{Z}\\) to \\(\\mathbb{Z}/p^k\\mathbb{Z}\\) using Hensel's lemma."
))

PADS["number-theory/twin-primes"] = sec(p(
    "The Elliott–Halberstam conjecture (EH) is a strong form of the Bombieri–Vinogradov theorem. Assuming EH, Goldston–Pintz–Yıldırım (2005) proved \\(\\liminf(p_{n+1}-p_n)/\\ln p_n=0\\) — prime gaps are infinitely often much smaller than average. Zhang's 2013 result built on their method.",
    "Polignac's conjecture: for every even \\(k\\), there are infinitely many prime pairs \\((p,p+k)\\). Twin primes correspond to \\(k=2\\). The Polymath8 project, following Zhang, proved infinitely many pairs with gap \\(\\leq246\\), which would follow from Polignac's conjecture for some \\(k\\leq246\\).",
    "The Green–Tao theorem (2004): the primes contain arithmetic progressions of arbitrary length. The proof uses Szemerédi's theorem (dense sets contain long APs) and a transference principle showing primes are 'pseudorandom' enough for Szemerédi to apply."
))

PADS["number-theory/algebraic-number-theory"] = sec(p(
    "The Dedekind zeta function \\(\\zeta_K(s)=\\sum_{\\mathfrak{a}}N(\\mathfrak{a})^{-s}\\) (sum over nonzero ideals of \\(\\mathcal{O}_K\\)) generalizes the Riemann zeta function. The analytic class number formula expresses the residue at \\(s=1\\) in terms of the class number, regulator, discriminant, and number of roots of unity.",
    "Ramification describes how primes of \\(\\mathbb{Z}\\) split in \\(\\mathcal{O}_K\\): a prime \\(p\\) can split (\\(e=1\\), \\(f=1\\)), remain inert (\\(e=1\\), \\(f=[K:\\mathbb{Q}]\\)), or ramify (\\(e>1\\)). Ramification is controlled by the discriminant: \\(p\\) ramifies iff \\(p\\mid\\text{disc}(K/\\mathbb{Q})\\).",
    "The Langlands program, formulated in 1967, proposes a vast web of correspondences between automorphic forms (generalizing modular forms) and Galois representations. Wiles' proof of Fermat's Last Theorem established a special case (modularity of elliptic curves over \\(\\mathbb{Q}\\))."
))

PADS["number-theory/goldbach-conjecture"] = sec(p(
    "Numerical verification: Goldbach's conjecture has been verified for all even integers up to \\(4\\times10^{18}\\) by Oliveira e Silva et al. (2013). The verification uses a segmented sieve and took years of distributed computation.",
    "The Goldbach comet: plotting the number of ways to write \\(2n\\) as a sum of two primes shows a comet-like pattern. The 'tail' corresponds to even numbers with few representations; the 'head' to those with many. The Hardy–Littlewood conjecture predicts the average number of representations.",
    "Schnirelmann's theorem (1930): every integer \\(\\geq2\\) is a sum of at most \\(C\\) primes for some absolute constant \\(C\\). This was the first unconditional result toward Goldbach. The current best unconditional result (Helfgott, 2013) gives \\(C=3\\) for odd integers \\(>5\\)."
))

PADS["number-theory/divisibility"] = sec(p(
    "The Fundamental Theorem of Arithmetic: every integer \\(n>1\\) factors uniquely as \\(n=p_1^{a_1}\\cdots p_k^{a_k}\\) (up to order). This is equivalent to \\(\\mathbb{Z}\\) being a unique factorization domain (UFD). The proof uses Euclid's lemma: if \\(p\\mid ab\\) and \\(p\\) is prime, then \\(p\\mid a\\) or \\(p\\mid b\\).",
    "Divisibility in polynomial rings: \\(f(x)\\mid g(x)\\) in \\(F[x]\\) (\\(F\\) a field) iff \\(g(x)=f(x)q(x)\\) for some polynomial \\(q\\). The Euclidean algorithm works in \\(F[x]\\), making it a Euclidean domain and hence a PID and UFD. The GCD of polynomials is computed by the polynomial Euclidean algorithm.",
    "Divisibility tests for large numbers use modular arithmetic. To test if \\(n\\) is divisible by 7: double the last digit, subtract from the rest, repeat. This works because \\(10\\equiv3\\pmod7\\) and \\(10^6\\equiv1\\pmod7\\), giving a period-6 pattern."
))

PADS["number-theory/number-theory-cryptography"] = sec(p(
    "The security of RSA depends on the integer factorization problem. The best known classical algorithm, the general number field sieve (GNFS), factors an \\(n\\)-bit number in \\(L[1/3,(64/9)^{1/3}]\\) time (subexponential but superpolynomial). For 2048-bit RSA, this is computationally infeasible with current hardware.",
    "Elliptic curve Diffie–Hellman (ECDH) and ECDSA are the elliptic curve analogues of DH and DSA. A 256-bit ECC key provides security equivalent to a 3072-bit RSA key. ECC is preferred for constrained devices (IoT, smart cards) due to smaller key sizes and faster operations.",
    "Post-quantum cryptography (PQC) designs systems secure against quantum computers. NIST standardized CRYSTALS-Kyber (key encapsulation, lattice-based) and CRYSTALS-Dilithium (signatures, lattice-based) in 2024. These rely on the hardness of the Learning With Errors (LWE) problem."
))

# ── LINEAR ALGEBRA ────────────────────────────────────────────────────────────
PADS["linear-algebra/null-space"] = sec(p(
    "The null space is used in data compression: if \\(A\\mathbf{x}=\\mathbf{b}\\) has many solutions, the null space parameterizes the degrees of freedom. In control theory, the null space of the controllability matrix determines which states are unreachable.",
    "Sparse null spaces arise in network analysis: the null space of the incidence matrix of a graph encodes the cycle space. Each basis vector of the null space corresponds to a fundamental cycle. The dimension of the null space equals the circuit rank (cyclomatic number) of the graph.",
    "In machine learning, the null space of the feature matrix \\(X\\) contains directions in feature space that have no effect on predictions. Regularization (ridge regression) effectively shrinks components in the null space direction, improving generalization."
))

PADS["linear-algebra/dimension"] = sec(p(
    "The dimension of the solution space of a homogeneous linear system \\(A\\mathbf{x}=\\mathbf{0}\\) equals \\(n-\\text{rank}(A)\\) (rank-nullity theorem). This tells us immediately how many free parameters the solution has, without solving the system.",
    "Dimension counting is a powerful heuristic: two subspaces of dimensions \\(d_1\\) and \\(d_2\\) in \\(\\mathbb{R}^n\\) generically intersect in a subspace of dimension \\(\\max(0,d_1+d_2-n)\\). This is used in algebraic geometry (Bézout's theorem) and in the analysis of constraint systems.",
    "The Grassmannian \\(\\text{Gr}(k,n)\\) is the space of all \\(k\\)-dimensional subspaces of \\(\\mathbb{R}^n\\). It is a smooth manifold of dimension \\(k(n-k)\\) and is fundamental in algebraic geometry, topology, and the theory of vector bundles."
))

PADS["linear-algebra/least-squares"] = sec(p(
    "The pseudoinverse \\(A^+=V\\Sigma^+U^T\\) (where \\(\\Sigma^+\\) inverts nonzero singular values) gives the minimum-norm least-squares solution: \\(\\hat{\\mathbf{x}}=A^+\\mathbf{b}\\) minimizes \\(\\|\\mathbf{x}\\|\\) among all minimizers of \\(\\|A\\mathbf{x}-\\mathbf{b}\\|\\).",
    "Weighted least squares minimizes \\(\\|W^{1/2}(A\\mathbf{x}-\\mathbf{b})\\|^2\\) where \\(W\\) is a diagonal weight matrix. It is used when observations have different reliabilities. The solution is \\(\\hat{\\mathbf{x}}=(A^TWA)^{-1}A^TW\\mathbf{b}\\).",
    "Total least squares (TLS) minimizes errors in both \\(A\\) and \\(\\mathbf{b}\\), appropriate when both are measured with noise. The TLS solution is given by the right singular vector of \\([A|\\mathbf{b}]\\) corresponding to the smallest singular value."
))

PADS["linear-algebra/eigenvector"] = sec(p(
    "The spectral theorem for symmetric matrices: every real symmetric matrix \\(A\\) has an orthonormal eigenbasis and real eigenvalues. This means \\(A=Q\\Lambda Q^T\\) with orthogonal \\(Q\\) and diagonal \\(\\Lambda\\). Symmetric matrices represent self-adjoint operators in quantum mechanics (observables).",
    "Perron–Frobenius theorem: a matrix with all positive entries has a unique largest real eigenvalue (the Perron root) with a corresponding eigenvector of all positive entries. This is the basis of Google's PageRank algorithm and Markov chain analysis.",
    "Eigenvalue perturbation theory (Weyl's inequalities, Bauer–Fike theorem) bounds how much eigenvalues change when a matrix is perturbed. This is crucial for numerical stability analysis and for understanding the sensitivity of physical systems to parameter changes."
))

PADS["linear-algebra/inner-product"] = sec(p(
    "The polarization identity recovers the inner product from the norm: \\(\\langle u,v\\rangle=\\frac{1}{4}(\\|u+v\\|^2-\\|u-v\\|^2)\\). This shows that in an inner product space, the norm determines the inner product. Not every norm comes from an inner product (the parallelogram law \\(\\|u+v\\|^2+\\|u-v\\|^2=2\\|u\\|^2+2\\|v\\|^2\\) must hold).",
    "Reproducing kernel Hilbert spaces (RKHS) are inner product spaces of functions where evaluation is a continuous linear functional. The kernel \\(K(x,y)=\\langle\\phi(x),\\phi(y)\\rangle\\) computes inner products in a (possibly infinite-dimensional) feature space. This is the 'kernel trick' in machine learning.",
    "The spectral theorem for compact self-adjoint operators on a Hilbert space: every such operator has a countable orthonormal eigenbasis with eigenvalues converging to 0. This generalizes the finite-dimensional spectral theorem and underlies Fourier analysis and quantum mechanics."
))

PADS["linear-algebra/orthogonality"] = sec(p(
    "The projection matrix \\(P=A(A^TA)^{-1}A^T\\) projects onto the column space of \\(A\\). It satisfies \\(P^2=P\\) (idempotent) and \\(P^T=P\\) (symmetric). The complementary projection \\(I-P\\) projects onto the orthogonal complement (the left null space of \\(A\\)).",
    "Orthogonal polynomials (Legendre, Chebyshev, Hermite, Laguerre) are orthogonal with respect to specific inner products on function spaces. They are used in numerical integration (Gaussian quadrature), approximation theory, and quantum mechanics (Hermite polynomials for the harmonic oscillator).",
    "The discrete Fourier transform (DFT) matrix \\(F_{jk}=\\omega^{jk}/\\sqrt{n}\\) (\\(\\omega=e^{2\\pi i/n}\\)) is unitary: \\(F^*F=I\\). Its columns are orthonormal vectors. The FFT computes the DFT in \\(O(n\\log n)\\) operations by exploiting the recursive structure of the DFT matrix."
))

PADS["linear-algebra/lu-decomposition"] = sec(p(
    "The LU decomposition is used to compute determinants efficiently: \\(\\det(A)=\\det(L)\\det(U)=\\prod u_{ii}\\) (since \\(\\det(L)=1\\) for unit lower triangular \\(L\\)). With partial pivoting, \\(\\det(A)=\\pm\\prod u_{ii}\\) (sign depends on the permutation).",
    "Sparse LU decomposition is used for large sparse systems arising in finite element analysis, circuit simulation, and computational fluid dynamics. Fill-reducing orderings (AMD, METIS) minimize the number of nonzeros introduced during factorization.",
    "The LDL\\(^T\\) decomposition factors a symmetric matrix as \\(A=LDL^T\\) with unit lower triangular \\(L\\) and diagonal \\(D\\). It is more efficient than Cholesky for indefinite matrices and is used in interior-point optimization methods."
))

PADS["linear-algebra/vectors-in-rn"] = sec(p(
    "The \\(\\ell^p\\) norms \\(\\|\\mathbf{v}\\|_p=(\\sum|v_i|^p)^{1/p}\\) generalize the Euclidean norm (\\(p=2\\)). The \\(\\ell^1\\) norm (Manhattan distance) promotes sparsity in optimization (LASSO). The \\(\\ell^\\infty\\) norm \\(\\max|v_i|\\) measures the largest component. All \\(\\ell^p\\) norms on \\(\\mathbb{R}^n\\) are equivalent.",
    "The outer product \\(\\mathbf{u}\\mathbf{v}^T\\) is an \\(m\\times n\\) rank-1 matrix. Every matrix is a sum of rank-1 matrices (its SVD). The outer product is used in neural networks (weight updates in gradient descent are outer products of activations and error signals).",
    "Concentration of measure: in high dimensions, most of the volume of a unit ball is near its surface, and most points on the surface are near the equator. Random vectors in \\(\\mathbb{R}^n\\) are nearly orthogonal with high probability. This 'curse of dimensionality' affects nearest-neighbor search and density estimation."
))

PADS["linear-algebra/rank"] = sec(p(
    "Matrix rank is computed numerically using the SVD: the rank equals the number of singular values above a threshold (accounting for floating-point errors). The numerical rank (rank with tolerance \\(\\epsilon\\)) is more practically useful than the exact rank for noisy data.",
    "The rank of a matrix product: \\(\\text{rank}(AB)\\leq\\min(\\text{rank}(A),\\text{rank}(B))\\). For square invertible \\(C\\): \\(\\text{rank}(CA)=\\text{rank}(A)\\). The rank of \\(A^TA\\) equals the rank of \\(A\\) (since \\(\\text{Null}(A^TA)=\\text{Null}(A)\\)).",
    "Low-rank structure is ubiquitous in applications. Recommendation systems model user-item interactions as a low-rank matrix (collaborative filtering). Image compression uses low-rank approximations. Quantum state tomography reconstructs low-rank density matrices from measurements."
))

PADS["linear-algebra/linear-systems"] = sec(p(
    "Direct methods (LU, Cholesky, QR) solve \\(A\\mathbf{x}=\\mathbf{b}\\) exactly in \\(O(n^3)\\) operations. Iterative methods (CG, GMRES, BiCGSTAB) are preferred for large sparse systems: they exploit sparsity and can achieve high accuracy in far fewer than \\(n\\) iterations with good preconditioning.",
    "The conjugate gradient method minimizes the quadratic \\(\\frac{1}{2}\\mathbf{x}^TA\\mathbf{x}-\\mathbf{b}^T\\mathbf{x}\\) over Krylov subspaces \\(\\mathcal{K}_k=\\text{span}\\{\\mathbf{r}_0,A\\mathbf{r}_0,\\ldots,A^{k-1}\\mathbf{r}_0\\}\\). It converges in at most \\(n\\) steps and faster when eigenvalues are clustered.",
    "Overdetermined systems (more equations than unknowns) are solved by least squares. Underdetermined systems (fewer equations than unknowns) have infinitely many solutions; the minimum-norm solution is \\(\\mathbf{x}=A^T(AA^T)^{-1}\\mathbf{b}\\) (right pseudoinverse)."
))

PADS["linear-algebra/qr-decomposition"] = sec(p(
    "Householder reflections \\(H=I-2\\mathbf{v}\\mathbf{v}^T/\\|\\mathbf{v}\\|^2\\) are orthogonal matrices that reflect across the hyperplane perpendicular to \\(\\mathbf{v}\\). Applying \\(n-1\\) Householder reflections to \\(A\\) produces the QR decomposition. This is backward stable and is the standard method in LAPACK.",
    "Givens rotations \\(G(i,j,\\theta)\\) zero out a single element by rotating in the \\((i,j)\\) plane. They are used for sparse QR (where Householder would destroy sparsity) and for updating QR when a row is added or deleted.",
    "The QR algorithm with shifts converges to Schur form \\(A=QTQ^T\\) (\\(T\\) upper triangular, \\(Q\\) orthogonal). The eigenvalues are the diagonal entries of \\(T\\). With Francis double-shift, convergence is typically cubic. This is the algorithm used in MATLAB's \\texttt{eig} and NumPy's \\texttt{linalg.eig}."
))

PADS["linear-algebra/subspace"] = sec(p(
    "Krylov subspaces \\(\\mathcal{K}_k(A,\\mathbf{b})=\\text{span}\\{\\mathbf{b},A\\mathbf{b},A^2\\mathbf{b},\\ldots,A^{k-1}\\mathbf{b}\\}\\) are the basis of iterative methods for linear systems and eigenvalue problems. The Arnoldi process builds an orthonormal basis for \\(\\mathcal{K}_k\\) and is the foundation of GMRES and the Lanczos algorithm.",
    "Invariant subspaces: a subspace \\(W\\) is invariant under \\(A\\) if \\(AW\\subseteq W\\). Eigenspaces are invariant. The Schur decomposition \\(A=QTQ^*\\) reveals a nested sequence of invariant subspaces (the columns of \\(Q\\) span invariant subspaces of increasing dimension).",
    "In quantum mechanics, the state space is a Hilbert space and physical observables correspond to self-adjoint operators. Measurement collapses the state to an eigenspace of the observable. Superposition is a linear combination of states in different eigenspaces."
))

PADS["linear-algebra/basis"] = sec(p(
    "The Gram–Schmidt process converts any linearly independent set \\(\\{\\mathbf{v}_1,\\ldots,\\mathbf{v}_k\\}\\) to an orthonormal set \\(\\{\\mathbf{q}_1,\\ldots,\\mathbf{q}_k\\}\\) spanning the same subspace. Modified Gram–Schmidt is numerically more stable and is equivalent to computing the thin QR decomposition.",
    "Dual bases: for a basis \\(B=\\{\\mathbf{b}_1,\\ldots,\\mathbf{b}_n\\}\\), the dual basis \\(B^*=\\{\\mathbf{b}_1^*,\\ldots,\\mathbf{b}_n^*\\}\\) satisfies \\(\\langle\\mathbf{b}_i^*,\\mathbf{b}_j\\rangle=\\delta_{ij}\\). For orthonormal bases, the dual basis equals the original. Dual bases are used in tensor analysis and finite element methods.",
    "Lattice bases in cryptography: a lattice is a discrete subgroup of \\(\\mathbb{R}^n\\), equivalently the set of integer linear combinations of basis vectors. The shortest vector problem (SVP) and closest vector problem (CVP) are hard lattice problems that underpin post-quantum cryptographic schemes."
))

# ── STATISTICS HUB ────────────────────────────────────────────────────────────
PADS["statistics"] = sec(p(
    "The law of large numbers (LLN) and central limit theorem (CLT) are the two pillars of classical statistics. The LLN guarantees that sample means converge to population means. The CLT explains why the normal distribution is ubiquitous: sums of independent random variables are approximately normal, regardless of the original distribution.",
    "Bayesian statistics treats parameters as random variables with prior distributions. Bayes' theorem updates the prior to a posterior given data: \\(p(\\theta|x)\\propto p(x|\\theta)p(\\theta)\\). The posterior summarizes all information about \\(\\theta\\) after observing \\(x\\). Bayesian methods naturally quantify uncertainty and incorporate prior knowledge.",
    "Nonparametric statistics makes fewer distributional assumptions. The Wilcoxon rank-sum test, Kruskal–Wallis test, and Spearman correlation use ranks rather than raw values. The Kolmogorov–Smirnov test compares empirical distribution functions. These methods are robust to outliers and non-normality."
))

# ── RUNNER ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import re
    enriched = skipped = already = 0
    for slug, html_block in PADS.items():
        path = os.path.join(ROOT, slug, "index.html")
        if not os.path.exists(path):
            print(f"SKIP: {slug}"); skipped += 1; continue
        with open(path, encoding="utf-8") as f:
            html = f.read()
        if 'id="applications"' in html:
            already += 1; continue
        words = len(re.sub(r'<[^>]+>', ' ', html).split())
        if words >= 700:
            already += 1; continue
        new_html = html.replace("</main>", html_block + "\n</main>", 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"padded: {slug}"); enriched += 1
    print(f"\nDone: {enriched} padded, {already} already ok, {skipped} skipped")
