#!/usr/bin/env python3
"""Inject rich content into all topic pages to reach 700+ words."""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "public_html"))

def sec(sid, title, body):
    return f'<div class="content-section" id="{sid}"><h2>{title}</h2>{body}</div>'

def p(*texts):
    return "".join(f"<p>{t}</p>" for t in texts)

# topic slug -> list of extra HTML sections to inject before </main>
EXTRA = {}

# ── CALCULUS ──────────────────────────────────────────────────────────────────
EXTRA["calculus/limit"] = [
    sec("background","Background & Motivation", p(
        "The concept of a limit is the cornerstone of modern calculus. Before the 17th century, mathematicians struggled to give rigorous meaning to instantaneous velocity and the area under a curve. Newton and Leibniz independently developed calculus, but it was Cauchy and Weierstrass in the 19th century who gave limits their precise ε–δ definition, finally placing calculus on a firm logical foundation.",
        "Informally, \\(\\lim_{x\\to a}f(x)=L\\) means we can make \\(f(x)\\) as close to \\(L\\) as we wish by taking \\(x\\) sufficiently close to \\(a\\) — without ever requiring \\(x=a\\). This subtlety is crucial: the limit describes the <em>approach</em>, not the value at the point.",
        "One-sided limits extend this idea: the left-hand limit \\(\\lim_{x\\to a^-}f(x)\\) considers only \\(x<a\\), and the right-hand limit \\(\\lim_{x\\to a^+}f(x)\\) considers only \\(x>a\\). A two-sided limit exists if and only if both one-sided limits exist and are equal."
    )),
    sec("techniques","Evaluation Techniques", p(
        "Direct substitution works whenever \\(f\\) is continuous at \\(a\\): simply compute \\(f(a)\\). When this yields an indeterminate form such as \\(0/0\\) or \\(\\infty/\\infty\\), other techniques are needed.",
        "Factoring and cancellation: if \\(f(x)=(x^2-1)/(x-1)\\), factor the numerator to get \\((x+1)(x-1)/(x-1)\\), cancel, and substitute to obtain \\(\\lim_{x\\to1}f(x)=2\\).",
        "L'Hôpital's Rule: for \\(0/0\\) or \\(\\infty/\\infty\\) forms, \\(\\lim f/g = \\lim f'/g'\\) (provided the latter limit exists). This powerful tool converts many hard limits into straightforward derivatives.",
        "The Squeeze Theorem is indispensable for oscillating functions: if \\(g(x)\\leq f(x)\\leq h(x)\\) near \\(a\\) and \\(\\lim g=\\lim h=L\\), then \\(\\lim f=L\\). The classic application is \\(\\lim_{x\\to0}(\\sin x)/x=1\\)."
    )),
    sec("applications","Applications", p(
        "Limits underpin every major concept in calculus. The derivative is defined as a limit of a difference quotient; the definite integral is a limit of Riemann sums; continuity is defined in terms of limits. In analysis, limits of sequences and series determine convergence. In physics, instantaneous velocity, acceleration, and electric field intensity all rely on limiting processes.",
        "In numerical analysis, understanding limits helps predict the behavior of algorithms as step sizes shrink. In probability theory, the Central Limit Theorem — one of the most important results in all of mathematics — is itself a statement about the limit of a sequence of distributions."
    )),
]

EXTRA["calculus/derivative"] = [
    sec("background","Background & Motivation", p(
        "The derivative measures the instantaneous rate of change of a function. Historically, the problem of finding the tangent line to a curve motivated its development. If we draw a secant line through \\((x, f(x))\\) and \\((x+h, f(x+h))\\), its slope is the difference quotient \\([f(x+h)-f(x)]/h\\). As \\(h\\to0\\), this slope approaches the slope of the tangent — the derivative \\(f'(x)\\).",
        "The notation \\(dy/dx\\) introduced by Leibniz emphasizes the derivative as a ratio of infinitesimal changes, while Newton's dot notation \\(\\dot{y}\\) is still used in physics for time derivatives. Both notations capture the same idea: the derivative is the best linear approximation to \\(f\\) near a point."
    )),
    sec("deeper","Deeper Properties", p(
        "A function is differentiable at \\(a\\) only if it is continuous there, but continuity does not imply differentiability — the absolute value function \\(|x|\\) is continuous but not differentiable at \\(x=0\\). Weierstrass constructed a function that is continuous everywhere but differentiable nowhere, shocking 19th-century mathematicians.",
        "Higher-order derivatives \\(f'', f''', \\ldots\\) describe how the rate of change itself changes. The second derivative \\(f''(x)\\) determines concavity: \\(f''>0\\) means the graph is concave up (like a bowl), \\(f''<0\\) means concave down. Inflection points occur where concavity changes.",
        "The Mean Value Theorem guarantees that for a differentiable function on \\([a,b]\\), there exists \\(c\\in(a,b)\\) with \\(f'(c)=(f(b)-f(a))/(b-a)\\). Geometrically, some tangent line is parallel to the secant. This theorem is the engine behind many results in analysis and optimization."
    )),
    sec("applications","Real-World Applications", p(
        "Derivatives appear throughout science and engineering. In physics, velocity is the derivative of position and acceleration is the derivative of velocity. In economics, marginal cost and marginal revenue are derivatives of total cost and revenue functions. In machine learning, gradient descent minimizes a loss function by repeatedly moving in the direction of the negative gradient — a vector of partial derivatives.",
        "In medicine, pharmacokinetics models how drug concentration changes over time using differential equations built from derivatives. In finance, the Black–Scholes equation for option pricing is a partial differential equation whose solution requires understanding derivatives of functions of multiple variables."
    )),
]

EXTRA["calculus/continuity"] = [
    sec("background","Background & Motivation", p(
        "Continuity formalizes the intuitive idea that a function has no sudden jumps or breaks. A function \\(f\\) is continuous at \\(a\\) if three conditions hold: \\(f(a)\\) is defined, \\(\\lim_{x\\to a}f(x)\\) exists, and the limit equals \\(f(a)\\). Failing any one condition produces a discontinuity.",
        "The Intermediate Value Theorem (IVT) is one of the most powerful consequences of continuity: if \\(f\\) is continuous on \\([a,b]\\) and \\(k\\) is any value between \\(f(a)\\) and \\(f(b)\\), then there exists \\(c\\in(a,b)\\) with \\(f(c)=k\\). This guarantees, for example, that every polynomial of odd degree has at least one real root."
    )),
    sec("types_detail","Classifying Discontinuities", p(
        "A <strong>removable discontinuity</strong> occurs when \\(\\lim_{x\\to a}f(x)\\) exists but either \\(f(a)\\) is undefined or \\(f(a)\\neq L\\). It can be 'removed' by redefining \\(f(a)=L\\). Example: \\(f(x)=\\sin(x)/x\\) at \\(x=0\\).",
        "A <strong>jump discontinuity</strong> occurs when the left and right limits both exist but differ. The floor function \\(\\lfloor x\\rfloor\\) has jump discontinuities at every integer.",
        "An <strong>infinite discontinuity</strong> occurs when the function grows without bound near \\(a\\). Example: \\(f(x)=1/x\\) at \\(x=0\\). These cannot be removed by redefining a single point.",
        "Uniform continuity is a stronger condition: \\(f\\) is uniformly continuous on a set if the same \\(\\delta\\) works for every point simultaneously. Every continuous function on a closed bounded interval is uniformly continuous (Heine–Cantor theorem)."
    )),
    sec("applications","Applications", p(
        "Continuity is a prerequisite for integration: the Riemann integral is guaranteed to exist for continuous functions on closed intervals. In numerical methods, continuity ensures that small changes in input produce small changes in output, which is essential for stable algorithms. In topology, continuous functions preserve connectedness and compactness — properties that generalize geometric intuition to abstract spaces."
    )),
]

EXTRA["calculus/differentiation-rules"] = [
    sec("background","Why These Rules Matter", p(
        "Computing derivatives from the limit definition is tedious. The differentiation rules — power, product, quotient, chain — allow us to differentiate any elementary function algebraically, without returning to limits. These rules are derived once from the definition and then applied mechanically.",
        "The <strong>chain rule</strong> \\((f\\circ g)'=(f'\\circ g)\\cdot g'\\) is arguably the most important: it handles compositions, which appear everywhere. In neural networks, backpropagation is simply the chain rule applied repeatedly through layers of composed functions.",
        "The <strong>product rule</strong> \\((fg)'=f'g+fg'\\) reflects the fact that when two quantities both change, the total change has two contributions. Integration by parts is the integral analogue of the product rule."
    )),
    sec("implicit","Implicit and Logarithmic Differentiation", p(
        "When a function is defined implicitly by an equation like \\(x^2+y^2=r^2\\), we differentiate both sides with respect to \\(x\\), treating \\(y\\) as a function of \\(x\\) and applying the chain rule to \\(y\\)-terms. This gives \\(2x+2y(dy/dx)=0\\), so \\(dy/dx=-x/y\\).",
        "Logarithmic differentiation simplifies products and powers: take \\(\\ln\\) of both sides, differentiate, then multiply through by the original function. For \\(y=x^x\\), \\(\\ln y=x\\ln x\\), so \\(y'/y=\\ln x+1\\), giving \\(y'=x^x(\\ln x+1)\\)."
    )),
    sec("applications","Applications", p(
        "Differentiation rules are used in every quantitative field. In physics, deriving equations of motion from energy functions requires the chain rule. In economics, elasticity of demand is computed using the quotient rule. In computer graphics, ray tracing and surface normal computation rely on differentiating implicit surface equations."
    )),
]

EXTRA["calculus/applications-of-derivatives"] = [
    sec("background","Overview", p(
        "Once we can compute derivatives, we can use them to analyze function behavior in detail. The first derivative test classifies critical points: if \\(f'\\) changes from positive to negative at \\(c\\), then \\(f(c)\\) is a local maximum; if from negative to positive, a local minimum.",
        "The second derivative test provides an alternative: if \\(f'(c)=0\\) and \\(f''(c)>0\\), then \\(c\\) is a local minimum; if \\(f''(c)<0\\), a local maximum. If \\(f''(c)=0\\), the test is inconclusive.",
        "Curve sketching combines all this information: find domain, intercepts, symmetry, asymptotes, intervals of increase/decrease (from \\(f'\\)), and concavity (from \\(f''\\)) to produce an accurate graph without plotting many points."
    )),
    sec("optimization","Optimization", p(
        "Applied optimization problems ask for the maximum or minimum of a quantity subject to constraints. The procedure: (1) identify the objective function and any constraints, (2) use constraints to reduce to one variable, (3) find critical points, (4) check endpoints and second derivative to confirm the nature of each critical point.",
        "Classic examples include minimizing the surface area of a can for a fixed volume, maximizing the area of a rectangle inscribed in a circle, and finding the dimensions of the cheapest box. In machine learning, training a model is an optimization problem: minimize the loss function over millions of parameters.",
        "Related rates problems use implicit differentiation with respect to time. If a ladder slides down a wall, the rates at which the base moves out and the top slides down are related by differentiating the Pythagorean constraint \\(x^2+y^2=L^2\\) with respect to \\(t\\)."
    )),
]

EXTRA["calculus/indefinite-integral"] = [
    sec("background","Antiderivatives & the Indefinite Integral", p(
        "An antiderivative of \\(f\\) is any function \\(F\\) with \\(F'=f\\). The indefinite integral \\(\\int f(x)\\,dx=F(x)+C\\) represents the entire family of antiderivatives, differing only by the constant \\(C\\). This constant reflects the fact that differentiation destroys constant information.",
        "The Fundamental Theorem of Calculus Part 1 connects antiderivatives to definite integrals: \\(\\frac{d}{dx}\\int_a^x f(t)\\,dt=f(x)\\). This means every continuous function has an antiderivative, even if it cannot be expressed in closed form (e.g., \\(e^{-x^2}\\)).",
        "Standard antiderivatives to memorize: \\(\\int x^n\\,dx=x^{n+1}/(n+1)+C\\) (\\(n\\neq-1\\)), \\(\\int e^x\\,dx=e^x+C\\), \\(\\int \\sin x\\,dx=-\\cos x+C\\), \\(\\int 1/x\\,dx=\\ln|x|+C\\), \\(\\int \\sec^2 x\\,dx=\\tan x+C\\)."
    )),
    sec("techniques_indef","Key Techniques", p(
        "U-substitution reverses the chain rule. Let \\(u=g(x)\\); then \\(\\int f(g(x))g'(x)\\,dx=\\int f(u)\\,du\\). Choose \\(u\\) to simplify the integrand — typically the inner function of a composition.",
        "Completing the square and trigonometric substitution handle integrals involving \\(\\sqrt{a^2-x^2}\\), \\(\\sqrt{a^2+x^2}\\), and \\(\\sqrt{x^2-a^2}\\). These arise in geometry (arc length, surface area) and physics (gravitational and electric potentials).",
        "Recognizing patterns is a skill built through practice. The integral \\(\\int f'(x)/f(x)\\,dx=\\ln|f(x)|+C\\) appears constantly in differential equations and probability."
    )),
]

EXTRA["calculus/definite-integral"] = [
    sec("background","Riemann Sums & the FTC", p(
        "The definite integral \\(\\int_a^b f(x)\\,dx\\) is defined as the limit of Riemann sums: partition \\([a,b]\\) into \\(n\\) subintervals, pick a sample point \\(x_i^*\\) in each, form \\(\\sum f(x_i^*)\\Delta x_i\\), and take \\(n\\to\\infty\\). For continuous \\(f\\), this limit always exists.",
        "The Fundamental Theorem of Calculus Part 2 gives the practical computation rule: \\(\\int_a^b f(x)\\,dx=F(b)-F(a)\\) where \\(F'=f\\). This remarkable result connects the geometric concept of area with the algebraic concept of antidifferentiation.",
        "Geometrically, \\(\\int_a^b f(x)\\,dx\\) equals the signed area between the graph of \\(f\\) and the \\(x\\)-axis: area above the axis counts positive, area below counts negative."
    )),
    sec("properties_detail","Properties in Practice", p(
        "Linearity: \\(\\int_a^b(\\alpha f+\\beta g)=\\alpha\\int_a^b f+\\beta\\int_a^b g\\). This allows us to integrate term by term.",
        "Symmetry shortcuts: if \\(f\\) is even, \\(\\int_{-a}^a f=2\\int_0^a f\\); if \\(f\\) is odd, \\(\\int_{-a}^a f=0\\). These can dramatically simplify calculations.",
        "Comparison: if \\(f\\leq g\\) on \\([a,b]\\), then \\(\\int_a^b f\\leq\\int_a^b g\\). The triangle inequality for integrals states \\(|\\int_a^b f|\\leq\\int_a^b|f|\\)."
    )),
    sec("applications_defint","Applications", p(
        "Definite integrals compute area, volume, arc length, surface area, work, center of mass, and probability. In statistics, the probability that a continuous random variable falls in \\([a,b]\\) is \\(\\int_a^b f(x)\\,dx\\) where \\(f\\) is the probability density function. In physics, work done by a variable force \\(F(x)\\) over displacement \\([a,b]\\) is \\(\\int_a^b F(x)\\,dx\\)."
    )),
]

EXTRA["calculus/integration-techniques"] = [
    sec("background","Why Techniques Are Needed", p(
        "Most integrals cannot be evaluated by direct lookup of standard forms. Integration techniques are systematic methods for transforming a hard integral into a recognizable one. Unlike differentiation, integration has no universal algorithm — choosing the right technique requires pattern recognition and experience.",
        "The three most important techniques are substitution (reversing the chain rule), integration by parts (reversing the product rule), and partial fractions (decomposing rational functions). Trigonometric substitution and trigonometric identities handle integrals involving square roots of quadratics."
    )),
    sec("parts_detail","Integration by Parts in Depth", p(
        "The formula \\(\\int u\\,dv=uv-\\int v\\,du\\) is derived from the product rule. The LIATE mnemonic guides the choice of \\(u\\): Logarithms, Inverse trig, Algebraic, Trigonometric, Exponential — choose \\(u\\) from the earliest category present.",
        "Sometimes integration by parts must be applied twice, or the original integral reappears on the right side (allowing it to be solved algebraically). For example, \\(\\int e^x\\sin x\\,dx\\) requires two applications and then solving for the integral."
    )),
    sec("partial_detail","Partial Fractions in Depth", p(
        "Any proper rational function \\(P(x)/Q(x)\\) (degree of \\(P\\) less than degree of \\(Q\\)) can be decomposed into partial fractions. Factor \\(Q(x)\\) completely over the reals: linear factors give terms \\(A/(x-r)\\), repeated linear factors give \\(A/(x-r)+B/(x-r)^2+\\ldots\\), and irreducible quadratic factors give \\((Ax+B)/(x^2+bx+c)\\). Determine coefficients by equating numerators."
    )),
]

EXTRA["calculus/applications-of-integrals"] = [
    sec("background","Overview", p(
        "The definite integral is a versatile tool for computing geometric and physical quantities. The key idea is always the same: slice the quantity into infinitesimal pieces, express each piece as \\(f(x)\\,dx\\), and integrate.",
        "Area between curves: if \\(f(x)\\geq g(x)\\) on \\([a,b]\\), the area between them is \\(\\int_a^b[f(x)-g(x)]\\,dx\\). When the curves cross, split the interval at intersection points and integrate each piece separately.",
        "Arc length of \\(y=f(x)\\) on \\([a,b]\\): \\(L=\\int_a^b\\sqrt{1+[f'(x)]^2}\\,dx\\). This formula comes from approximating the curve by tiny straight segments using the Pythagorean theorem."
    )),
    sec("volumes","Volumes of Revolution", p(
        "The <strong>disk method</strong> rotates a region about the \\(x\\)-axis: \\(V=\\pi\\int_a^b[f(x)]^2\\,dx\\). Each cross-section is a disk of radius \\(f(x)\\).",
        "The <strong>washer method</strong> handles regions between two curves: \\(V=\\pi\\int_a^b([f(x)]^2-[g(x)]^2)\\,dx\\).",
        "The <strong>shell method</strong> integrates cylindrical shells: \\(V=2\\pi\\int_a^b x\\,f(x)\\,dx\\). It is often easier when the axis of rotation is vertical.",
        "In physics, these techniques compute moments of inertia and centers of mass. In engineering, they determine the volume of machine parts with rotational symmetry."
    )),
]

EXTRA["calculus/sequences-and-series"] = [
    sec("background","Sequences", p(
        "A sequence \\(\\{a_n\\}\\) is a function from the positive integers to the reals. It converges to \\(L\\) if for every \\(\\varepsilon>0\\) there exists \\(N\\) such that \\(|a_n-L|<\\varepsilon\\) for all \\(n>N\\). Monotone bounded sequences always converge — a fact used constantly in analysis.",
        "Important sequences: \\(a_n=1/n\\to0\\), \\(a_n=r^n\\to0\\) for \\(|r|<1\\), \\(a_n=(1+1/n)^n\\to e\\). The last limit defines Euler's number \\(e\\approx2.71828\\)."
    )),
    sec("series_detail","Series", p(
        "An infinite series \\(\\sum_{n=1}^\\infty a_n\\) converges if its partial sums \\(S_N=\\sum_{n=1}^N a_n\\) converge. The geometric series \\(\\sum_{n=0}^\\infty ar^n=a/(1-r)\\) for \\(|r|<1\\) is the most important example.",
        "The harmonic series \\(\\sum 1/n\\) diverges despite \\(1/n\\to0\\) — a famous counterexample showing that \\(a_n\\to0\\) is necessary but not sufficient for convergence.",
        "Absolute convergence (\\(\\sum|a_n|\\) converges) implies convergence and allows rearrangement of terms. Conditional convergence (convergent but not absolutely) is more delicate: the Riemann rearrangement theorem says the terms can be rearranged to sum to any value."
    )),
    sec("tests_detail","Convergence Tests", p(
        "The <strong>ratio test</strong> \\(L=\\lim|a_{n+1}/a_n|\\) is best for factorials and exponentials. The <strong>root test</strong> \\(L=\\lim|a_n|^{1/n}\\) works well for \\(n\\)th powers. The <strong>integral test</strong> compares \\(\\sum f(n)\\) to \\(\\int f\\). The <strong>comparison test</strong> and <strong>limit comparison test</strong> relate an unknown series to a known one. The <strong>alternating series test</strong> (Leibniz) handles series with alternating signs."
    )),
]

EXTRA["calculus/taylor-series"] = [
    sec("background","Motivation", p(
        "A Taylor series represents a smooth function as an infinite polynomial. This is powerful because polynomials are easy to differentiate, integrate, and evaluate numerically. The Taylor series of \\(f\\) centered at \\(a\\) is \\(\\sum_{n=0}^\\infty f^{(n)}(a)(x-a)^n/n!\\). When \\(a=0\\), it is called a Maclaurin series.",
        "The partial sums are Taylor polynomials \\(T_n(x)\\), which approximate \\(f\\) near \\(a\\). The error is bounded by the remainder term \\(R_n(x)=f^{(n+1)}(c)(x-a)^{n+1}/(n+1)!\\) for some \\(c\\) between \\(x\\) and \\(a\\) (Taylor's theorem with Lagrange remainder)."
    )),
    sec("convergence_taylor","Radius of Convergence", p(
        "A power series \\(\\sum c_n(x-a)^n\\) converges absolutely for \\(|x-a|<R\\) and diverges for \\(|x-a|>R\\), where \\(R=1/\\limsup|c_n|^{1/n}\\) is the radius of convergence. At the endpoints \\(x=a\\pm R\\), convergence must be checked separately.",
        "For \\(e^x\\), \\(\\sin x\\), and \\(\\cos x\\), the radius of convergence is infinite — these series converge for all \\(x\\). For \\(\\ln(1+x)\\), \\(R=1\\), and the series converges on \\((-1,1]\\)."
    )),
    sec("applications_taylor","Applications", p(
        "Taylor series are used to compute limits (replace functions by their series and simplify), to approximate integrals that have no closed form (e.g., \\(\\int e^{-x^2}\\,dx\\)), and to solve differential equations (power series method). In physics, small-angle approximations \\(\\sin\\theta\\approx\\theta\\) and \\(\\cos\\theta\\approx1-\\theta^2/2\\) are first-order Taylor approximations. In computer science, Taylor series underlie fast algorithms for computing transcendental functions."
    )),
]

EXTRA["calculus/partial-derivatives"] = [
    sec("background","Functions of Several Variables", p(
        "When a quantity depends on more than one variable — temperature depending on position \\((x,y,z)\\), profit depending on price and quantity — we need calculus for multivariable functions. The partial derivative \\(\\partial f/\\partial x\\) measures the rate of change of \\(f\\) with respect to \\(x\\) while all other variables are held fixed.",
        "Geometrically, for \\(z=f(x,y)\\), the partial derivative \\(\\partial f/\\partial x\\) at a point is the slope of the curve obtained by intersecting the surface with a plane parallel to the \\(xz\\)-plane."
    )),
    sec("gradient_detail","Gradient & Directional Derivatives", p(
        "The gradient \\(\\nabla f=(\\partial f/\\partial x,\\partial f/\\partial y,\\partial f/\\partial z)\\) is a vector that points in the direction of steepest ascent of \\(f\\). Its magnitude \\(|\\nabla f|\\) is the maximum rate of change.",
        "The directional derivative in direction \\(\\mathbf{u}\\) (unit vector) is \\(D_{\\mathbf{u}}f=\\nabla f\\cdot\\mathbf{u}\\). This generalizes the ordinary derivative to arbitrary directions.",
        "Critical points of \\(f(x,y)\\) occur where \\(\\nabla f=\\mathbf{0}\\). The second derivative test uses the Hessian matrix \\(H\\) of second partial derivatives: if \\(\\det H>0\\) and \\(f_{xx}>0\\), the point is a local minimum; if \\(\\det H>0\\) and \\(f_{xx}<0\\), a local maximum; if \\(\\det H<0\\), a saddle point."
    )),
    sec("applications_partial","Applications", p(
        "Partial derivatives are fundamental in physics (heat equation, wave equation, Maxwell's equations), economics (marginal utility, Lagrange multipliers for constrained optimization), and machine learning (gradient of the loss function with respect to model parameters). The method of Lagrange multipliers uses gradients to optimize a function subject to equality constraints."
    )),
]

EXTRA["calculus/differential-equation"] = [
    sec("background","What Are Differential Equations?", p(
        "A differential equation (DE) is an equation relating a function to its derivatives. Ordinary differential equations (ODEs) involve functions of one variable; partial differential equations (PDEs) involve functions of several variables. DEs are the language of science: Newton's second law \\(F=ma\\) is an ODE, the heat equation and wave equation are PDEs.",
        "The <strong>order</strong> of a DE is the highest derivative present. A <strong>solution</strong> is a function satisfying the equation on some interval. The general solution of an \\(n\\)th-order ODE contains \\(n\\) arbitrary constants; initial conditions or boundary conditions determine specific solutions."
    )),
    sec("classification","Classification & Solution Methods", p(
        "First-order ODEs: separable equations (\\(dy/dx=f(x)g(y)\\)) are solved by separating variables and integrating. Linear first-order equations (\\(y'+P(x)y=Q(x)\\)) are solved using an integrating factor \\(\\mu=e^{\\int P\\,dx}\\).",
        "Second-order linear ODEs with constant coefficients (\\(ay''+by'+cy=0\\)) are solved via the characteristic equation \\(ar^2+br+c=0\\). The nature of the roots (real distinct, repeated, complex) determines the form of the general solution.",
        "Nonlinear DEs are generally much harder. Qualitative methods (phase plane analysis, stability theory) and numerical methods (Euler's method, Runge–Kutta) are used when closed-form solutions are unavailable."
    )),
    sec("applications_de","Applications", p(
        "DEs model exponential growth and decay (population, radioactive decay), oscillations (springs, circuits), heat transfer, fluid flow, and quantum mechanics. The logistic equation \\(dP/dt=rP(1-P/K)\\) models population growth with a carrying capacity. The SIR model for infectious disease spread is a system of three coupled ODEs."
    )),
]

# ── STATISTICS ────────────────────────────────────────────────────────────────
EXTRA["statistics/descriptive-statistics"] = [
    sec("background","Why Descriptive Statistics?", p(
        "Before drawing any conclusions from data, we must understand what the data look like. Descriptive statistics provide a concise numerical and visual summary of a dataset, revealing its center, spread, and shape without making inferences beyond the observed values.",
        "A dataset's <strong>distribution</strong> describes how values are spread across the range. Histograms, box plots, and stem-and-leaf plots are graphical tools that complement numerical summaries. Together they reveal features like skewness, outliers, and multimodality that single numbers can miss."
    )),
    sec("measures_detail","Measures in Depth", p(
        "The <strong>mean</strong> is sensitive to outliers because every value contributes equally. A single extreme value can pull the mean far from the bulk of the data. The <strong>median</strong> is resistant to outliers — it depends only on the middle value(s). For skewed distributions, the median is often a better measure of center.",
        "The <strong>standard deviation</strong> \\(s\\) measures typical distance from the mean. Chebyshev's inequality guarantees that at least \\(1-1/k^2\\) of any dataset lies within \\(k\\) standard deviations of the mean, regardless of distribution shape. For bell-shaped distributions, the empirical rule (68-95-99.7) gives tighter bounds.",
        "The <strong>interquartile range</strong> (IQR = Q3 − Q1) is a robust measure of spread. The box plot displays the five-number summary (min, Q1, median, Q3, max) and flags outliers as points beyond \\(Q1-1.5\\cdot\\text{IQR}\\) or \\(Q3+1.5\\cdot\\text{IQR}\\)."
    )),
    sec("shape_detail","Shape & Skewness", p(
        "Skewness quantifies asymmetry. A right-skewed (positively skewed) distribution has a long right tail; the mean exceeds the median. Income distributions are typically right-skewed. A left-skewed distribution has a long left tail; the mean is below the median.",
        "Kurtosis measures tail heaviness relative to a normal distribution. High kurtosis (leptokurtic) means heavy tails and a sharp peak — more extreme values than expected. Low kurtosis (platykurtic) means light tails. Financial return distributions often exhibit excess kurtosis, making extreme events more likely than a normal model predicts."
    )),
]

EXTRA["statistics/probability"] = [
    sec("background","Foundations of Probability", p(
        "Probability theory provides a mathematical framework for reasoning about uncertainty. The sample space \\(\\Omega\\) is the set of all possible outcomes; an event \\(A\\) is a subset of \\(\\Omega\\). The probability function \\(P\\) assigns a number in \\([0,1]\\) to each event, satisfying Kolmogorov's axioms: \\(P(\\Omega)=1\\) and countable additivity.",
        "There are three interpretations of probability: <strong>classical</strong> (equally likely outcomes), <strong>frequentist</strong> (long-run relative frequency), and <strong>Bayesian</strong> (degree of belief). Each has its domain of applicability and philosophical implications."
    )),
    sec("independence","Independence & Conditional Probability", p(
        "Events \\(A\\) and \\(B\\) are independent if \\(P(A\\cap B)=P(A)P(B)\\). Independence means knowing \\(B\\) occurred gives no information about \\(A\\). This is a mathematical definition — it must be verified, not assumed.",
        "The law of total probability: \\(P(B)=\\sum_i P(B|A_i)P(A_i)\\) for a partition \\(\\{A_i\\}\\) of \\(\\Omega\\). Combined with Bayes' theorem, this allows updating probabilities as new evidence arrives — the foundation of Bayesian inference.",
        "Common pitfalls: the <strong>prosecutor's fallacy</strong> confuses \\(P(\\text{evidence}|\\text{innocent})\\) with \\(P(\\text{innocent}|\\text{evidence})\\). The <strong>birthday problem</strong> shows that in a group of 23 people, the probability of a shared birthday exceeds 50% — far higher than intuition suggests."
    )),
    sec("applications_prob","Applications", p(
        "Probability underpins statistics, information theory, quantum mechanics, and finance. In machine learning, probabilistic models (Naive Bayes, Gaussian processes, variational autoencoders) use probability to quantify uncertainty. In finance, option pricing models treat asset prices as random processes. In cryptography, probabilistic algorithms provide security guarantees."
    )),
]

EXTRA["statistics/hypothesis-testing"] = [
    sec("background","The Logic of Hypothesis Testing", p(
        "Hypothesis testing is a formal procedure for deciding whether data provide sufficient evidence against a null hypothesis \\(H_0\\). The logic is indirect: assume \\(H_0\\) is true, compute the probability of observing data at least as extreme as what was observed (the p-value), and reject \\(H_0\\) if this probability is small.",
        "The significance level \\(\\alpha\\) (typically 0.05 or 0.01) is the threshold for rejection. It represents the maximum acceptable probability of a Type I error (rejecting a true \\(H_0\\)). Choosing \\(\\alpha\\) before seeing the data is essential to avoid p-hacking."
    )),
    sec("pvalue","P-values & Effect Size", p(
        "A p-value is not the probability that \\(H_0\\) is true. It is the probability of the observed (or more extreme) data given that \\(H_0\\) is true. A small p-value means the data are unlikely under \\(H_0\\), not that \\(H_0\\) is false.",
        "Statistical significance does not imply practical significance. With a large enough sample, even a trivially small effect can yield \\(p<0.05\\). Always report effect sizes (Cohen's \\(d\\), \\(r^2\\), odds ratio) alongside p-values.",
        "The <strong>power</strong> of a test (\\(1-\\beta\\)) is the probability of correctly rejecting a false \\(H_0\\). Power increases with sample size, effect size, and significance level. Power analysis before data collection determines the sample size needed to detect a meaningful effect."
    )),
    sec("multiple","Multiple Testing", p(
        "When many hypotheses are tested simultaneously, the probability of at least one false positive grows rapidly. With 20 independent tests at \\(\\alpha=0.05\\), the expected number of false positives is 1. The Bonferroni correction controls the family-wise error rate by using \\(\\alpha/m\\) for each of \\(m\\) tests. The Benjamini–Hochberg procedure controls the false discovery rate, which is less conservative and more appropriate for exploratory research."
    )),
]

EXTRA["statistics/normal-distribution"] = [
    sec("background","Why the Normal Distribution?", p(
        "The normal distribution \\(N(\\mu,\\sigma^2)\\) is the most important distribution in statistics, for both theoretical and practical reasons. Theoretically, the Central Limit Theorem guarantees that the sum (or mean) of many independent random variables converges to a normal distribution, regardless of the original distribution. Practically, many natural measurements — heights, weights, measurement errors — are approximately normally distributed.",
        "The standard normal \\(N(0,1)\\) has mean 0 and variance 1. Any normal variable can be standardized: \\(Z=(X-\\mu)/\\sigma\\sim N(0,1)\\). Tables or software give \\(P(Z\\leq z)=\\Phi(z)\\), the cumulative distribution function."
    )),
    sec("properties_norm","Properties in Depth", p(
        "The normal PDF is symmetric about \\(\\mu\\), bell-shaped, and has inflection points at \\(\\mu\\pm\\sigma\\). The tails decrease faster than any polynomial but slower than a step function — there is always some probability in the tails.",
        "Linear combinations of independent normals are normal: if \\(X\\sim N(\\mu_1,\\sigma_1^2)\\) and \\(Y\\sim N(\\mu_2,\\sigma_2^2)\\) independently, then \\(aX+bY\\sim N(a\\mu_1+b\\mu_2, a^2\\sigma_1^2+b^2\\sigma_2^2)\\). This closure property makes the normal distribution especially tractable.",
        "The lognormal distribution: if \\(\\ln X\\sim N(\\mu,\\sigma^2)\\), then \\(X\\) is lognormal. Stock prices and income are often modeled as lognormal because they are positive and right-skewed."
    )),
    sec("applications_norm","Applications", p(
        "The normal distribution is used in quality control (Six Sigma), finance (Black–Scholes model), psychometrics (IQ scores), and natural sciences. In Bayesian statistics, the normal distribution is its own conjugate prior for the mean when the variance is known, making posterior calculations tractable."
    )),
]

EXTRA["statistics/regression-analysis"] = [
    sec("background","Regression Overview", p(
        "Regression analysis models the relationship between a response variable \\(Y\\) and one or more predictor variables \\(X_1,\\ldots,X_p\\). Simple linear regression (one predictor) fits a line \\(\\hat{y}=\\hat{\\beta}_0+\\hat{\\beta}_1 x\\) that minimizes the sum of squared residuals \\(\\sum(y_i-\\hat{y}_i)^2\\) — the ordinary least squares (OLS) criterion.",
        "The OLS estimators are unbiased and, under the Gauss–Markov assumptions (linearity, independence, homoscedasticity, zero-mean errors), have the smallest variance among all linear unbiased estimators (BLUE property)."
    )),
    sec("inference_reg","Inference in Regression", p(
        "After fitting, we test whether the slope \\(\\beta_1\\) is significantly different from zero using a t-test: \\(t=\\hat{\\beta}_1/\\text{SE}(\\hat{\\beta}_1)\\) with \\(n-2\\) degrees of freedom. A significant slope means \\(X\\) is a useful linear predictor of \\(Y\\).",
        "The coefficient of determination \\(R^2=1-\\text{SSE}/\\text{SST}\\) measures the proportion of variance in \\(Y\\) explained by the model. \\(R^2\\) ranges from 0 (no fit) to 1 (perfect fit). In multiple regression, adjusted \\(R^2\\) penalizes for adding predictors that do not improve fit.",
        "Residual diagnostics check model assumptions: a residual plot (residuals vs. fitted values) should show no pattern; a Q–Q plot checks normality of residuals; Cook's distance identifies influential observations."
    )),
    sec("applications_reg","Applications", p(
        "Regression is used in economics (demand forecasting), medicine (dose-response relationships), social sciences (predicting outcomes from demographics), and machine learning (linear regression as a baseline model). Multiple regression extends to many predictors; logistic regression handles binary outcomes; polynomial regression fits curves."
    )),
]

EXTRA["statistics/confidence-intervals"] = [
    sec("background","Confidence Intervals Explained", p(
        "A confidence interval (CI) provides a range of plausible values for an unknown population parameter, based on sample data. A 95% CI means: if we repeated the sampling procedure many times and constructed a CI each time, 95% of those intervals would contain the true parameter. It does not mean there is a 95% probability that the true value lies in this particular interval — the true value is fixed, not random.",
        "The width of a CI reflects precision: narrower intervals indicate more precise estimates. Width decreases as sample size \\(n\\) increases (proportional to \\(1/\\sqrt{n}\\)) and increases with confidence level (a 99% CI is wider than a 95% CI for the same data)."
    )),
    sec("construction","Constructing CIs", p(
        "For a population mean with known \\(\\sigma\\): \\(\\bar{x}\\pm z_{\\alpha/2}\\sigma/\\sqrt{n}\\). For unknown \\(\\sigma\\) (the usual case): \\(\\bar{x}\\pm t_{\\alpha/2,n-1}\\cdot s/\\sqrt{n}\\), using the t-distribution with \\(n-1\\) degrees of freedom.",
        "For a proportion \\(p\\): \\(\\hat{p}\\pm z_{\\alpha/2}\\sqrt{\\hat{p}(1-\\hat{p})/n}\\) (Wald interval). The Wilson interval has better coverage for small \\(n\\) or extreme \\(p\\).",
        "Bootstrap CIs make no distributional assumptions: resample the data with replacement many times, compute the statistic each time, and use the empirical distribution of the statistic to construct the interval."
    )),
    sec("applications_ci","Applications", p(
        "CIs are reported in clinical trials (treatment effect with uncertainty), opinion polls (margin of error), and scientific publications. Reporting a CI alongside a p-value gives a more complete picture: the CI shows the magnitude and precision of the effect, while the p-value indicates statistical significance."
    )),
]

EXTRA["statistics/correlation"] = [
    sec("bg","Background", p(
        "Correlation measures the strength and direction of a linear relationship between two variables. The Pearson correlation coefficient \\(r\\) ranges from −1 (perfect negative linear relationship) to +1 (perfect positive linear relationship), with 0 indicating no linear association. It is dimensionless and unaffected by linear rescaling of either variable.",
        "A crucial warning: correlation does not imply causation. Two variables can be strongly correlated because one causes the other, because both are caused by a third variable (confounding), or purely by chance (spurious correlation). Always consider the data-generating process before interpreting \\(r\\).",
        "The Spearman rank correlation \\(\\rho\\) replaces values with their ranks before computing Pearson's \\(r\\). It detects any monotone relationship (not just linear) and is robust to outliers. Kendall's \\(\\tau\\) is another rank-based measure, preferred for small samples or many ties.",
        "Testing whether \\(r\\) is significantly different from zero uses the t-statistic \\(t=r\\sqrt{n-2}/\\sqrt{1-r^2}\\) with \\(n-2\\) degrees of freedom. A significant result means the linear association is unlikely to be due to chance alone, but the effect size (\\(r^2\\), the proportion of shared variance) determines practical importance."
    )),
]

EXTRA["statistics/inferential-statistics"] = [
    sec("bg","Background", p(
        "Inferential statistics uses sample data to draw conclusions about a larger population, always acknowledging sampling variability. The fundamental challenge is that different samples from the same population yield different statistics — the sampling distribution of a statistic describes this variability.",
        "The standard error (SE) of a statistic measures its typical variability across samples. For the sample mean, \\(\\text{SE}=\\sigma/\\sqrt{n}\\). As \\(n\\) increases, the SE decreases, meaning larger samples give more precise estimates.",
        "The Central Limit Theorem guarantees that for large \\(n\\), the sampling distribution of \\(\\bar{X}\\) is approximately normal regardless of the population distribution. This justifies using z- and t-tests broadly.",
        "Parametric methods (t-tests, ANOVA, regression) assume specific distributional forms and are powerful when assumptions hold. Nonparametric methods (Mann–Whitney, Kruskal–Wallis, permutation tests) make fewer assumptions and are more robust, at the cost of some power."
    )),
]

EXTRA["statistics/random-variables"] = [
    sec("bg","Background", p(
        "A random variable (RV) is a function that assigns a numerical value to each outcome in a sample space. It transforms qualitative outcomes into numbers amenable to mathematical analysis. Discrete RVs take countable values; continuous RVs take values in an interval.",
        "The cumulative distribution function (CDF) \\(F(x)=P(X\\leq x)\\) is defined for all RVs and completely characterizes the distribution. For discrete RVs, the probability mass function (PMF) gives \\(P(X=x)\\); for continuous RVs, the probability density function (PDF) \\(f(x)\\) satisfies \\(P(a\\leq X\\leq b)=\\int_a^b f(x)\\,dx\\).",
        "Key properties: \\(E[g(X)]=\\sum g(x)P(X=x)\\) or \\(\\int g(x)f(x)\\,dx\\). The variance \\(\\text{Var}(X)=E[(X-\\mu)^2]=E[X^2]-\\mu^2\\). For independent RVs, \\(\\text{Var}(X+Y)=\\text{Var}(X)+\\text{Var}(Y)\\).",
        "Moment generating functions (MGFs) \\(M_X(t)=E[e^{tX}]\\) uniquely determine distributions and simplify computing moments: \\(E[X^n]=M_X^{(n)}(0)\\). The MGF of a sum of independent RVs is the product of their MGFs."
    )),
]

EXTRA["statistics/statistical-distributions"] = [
    sec("bg","Background", p(
        "Statistical distributions are mathematical models for random phenomena. Choosing the right distribution for a problem requires understanding the data-generating process: count data suggest Poisson or binomial; waiting times suggest exponential or gamma; proportions suggest beta; extreme values suggest Gumbel or Pareto.",
        "The <strong>binomial distribution</strong> \\(B(n,p)\\) models the number of successes in \\(n\\) independent Bernoulli trials. Mean \\(np\\), variance \\(np(1-p)\\). For large \\(n\\) and moderate \\(p\\), it is approximated by \\(N(np, np(1-p))\\); for large \\(n\\) and small \\(p\\), by Poisson(\\(np\\)).",
        "The <strong>Poisson distribution</strong> models rare events in a fixed interval of time or space. If events occur at rate \\(\\lambda\\), the number in a unit interval is Poisson(\\(\\lambda\\)). The exponential distribution models the waiting time between Poisson events.",
        "The <strong>t-distribution</strong> with \\(\\nu\\) degrees of freedom has heavier tails than the normal. As \\(\\nu\\to\\infty\\), it converges to \\(N(0,1)\\). The chi-squared distribution \\(\\chi^2(\\nu)\\) is the sum of \\(\\nu\\) squared standard normals; it arises in variance estimation and goodness-of-fit tests. The F-distribution is the ratio of two chi-squared variables divided by their degrees of freedom; it appears in ANOVA and regression."
    )),
]

EXTRA["statistics/sampling-methods"] = [
    sec("bg","Background", p(
        "A sample is a subset of a population selected to make inferences about the whole. The quality of inference depends critically on how the sample is drawn. A biased sampling method — one that systematically over- or under-represents certain groups — produces misleading conclusions regardless of sample size.",
        "Simple random sampling (SRS) gives every subset of size \\(n\\) an equal chance of selection. It is the gold standard for unbiasedness but may be impractical for large or geographically dispersed populations.",
        "Stratified sampling divides the population into homogeneous subgroups (strata) and samples from each. It reduces variance compared to SRS when strata differ in their means. Proportional allocation samples each stratum in proportion to its size; optimal allocation (Neyman) allocates more to strata with higher variability.",
        "Cluster sampling randomly selects clusters (e.g., schools, cities) and surveys all members within selected clusters. It is cost-effective but less precise than SRS. Two-stage cluster sampling surveys a random sample within each selected cluster, balancing cost and precision. Systematic sampling (every \\(k\\)th element) is simple to implement but can be biased if the population has periodic structure."
    )),
]

EXTRA["statistics/bayesian-statistics"] = [
    sec("bg","Background", p(
        "Bayesian statistics treats probability as a degree of belief and updates beliefs as evidence accumulates. The prior distribution \\(P(\\theta)\\) encodes knowledge about the parameter \\(\\theta\\) before seeing data. The likelihood \\(P(x|\\theta)\\) describes how probable the observed data are for each value of \\(\\theta\\). Bayes' theorem combines them: \\(P(\\theta|x)\\propto P(x|\\theta)P(\\theta)\\).",
        "The posterior distribution \\(P(\\theta|x)\\) is the complete Bayesian answer — it is a full probability distribution over \\(\\theta\\), not just a point estimate. Point summaries include the posterior mean, median, and mode (MAP estimate). Credible intervals (e.g., the central 95% of the posterior) have a direct probability interpretation: there is a 95% probability that \\(\\theta\\) lies in the interval, given the data.",
        "Conjugate priors simplify computation: when the prior and posterior belong to the same family, the posterior has a closed form. Beta–Binomial, Normal–Normal, and Gamma–Poisson are classic conjugate pairs.",
        "Markov Chain Monte Carlo (MCMC) methods — Metropolis–Hastings, Gibbs sampling, Hamiltonian Monte Carlo — enable Bayesian inference for complex models where the posterior has no closed form. Modern probabilistic programming languages (Stan, PyMC) automate MCMC, making Bayesian methods accessible for practical data analysis."
    )),
]

# ── GEOMETRY ──────────────────────────────────────────────────────────────────
_geo_extra = {
"triangle": p(
    "Triangles are the simplest polygons and the building blocks of all polygonal geometry. Every polygon can be triangulated — divided into triangles — making triangles fundamental to computational geometry, finite element analysis, and computer graphics.",
    "The <strong>law of sines</strong> \\(a/\\sin A=b/\\sin B=c/\\sin C=2R\\) (where \\(R\\) is the circumradius) and the <strong>law of cosines</strong> \\(c^2=a^2+b^2-2ab\\cos C\\) solve any triangle given sufficient information. The law of cosines generalizes the Pythagorean theorem to non-right triangles.",
    "Special points: the <strong>centroid</strong> (intersection of medians) divides each median 2:1 from vertex. The <strong>circumcenter</strong> (intersection of perpendicular bisectors) is equidistant from all vertices. The <strong>incenter</strong> (intersection of angle bisectors) is equidistant from all sides. The <strong>orthocenter</strong> (intersection of altitudes) completes the Euler line with the centroid and circumcenter.",
    "Heron's formula computes area from side lengths alone: \\(A=\\sqrt{s(s-a)(s-b)(s-c)}\\) where \\(s=(a+b+c)/2\\) is the semi-perimeter. This is useful when the height is unknown."
),
"circle": p(
    "The circle is defined as the set of all points equidistant from a center. Its perfect symmetry makes it appear throughout mathematics, physics, and engineering. The ratio of circumference to diameter is \\(\\pi\\approx3.14159\\), one of the most important constants in mathematics.",
    "Key theorems: the <strong>inscribed angle theorem</strong> states that an inscribed angle is half the central angle subtending the same arc. The <strong>tangent-radius theorem</strong> states that a tangent to a circle is perpendicular to the radius at the point of tangency. Two tangents from an external point have equal length.",
    "The equation of a circle with center \\((h,k)\\) and radius \\(r\\) is \\((x-h)^2+(y-k)^2=r^2\\). Expanding gives the general form \\(x^2+y^2+Dx+Ey+F=0\\), where the center is \\((-D/2,-E/2)\\) and radius \\(\\sqrt{D^2/4+E^2/4-F}\\).",
    "In trigonometry, the unit circle (\\(r=1\\), centered at origin) defines \\(\\sin\\theta\\) and \\(\\cos\\theta\\) as the \\(y\\)- and \\(x\\)-coordinates of the point at angle \\(\\theta\\). This connects circular geometry to periodic functions and complex numbers via Euler's formula \\(e^{i\\theta}=\\cos\\theta+i\\sin\\theta\\)."
),
"pythagorean-theorem": p(
    "The Pythagorean theorem \\(a^2+b^2=c^2\\) is one of the oldest and most proved theorems in mathematics — over 370 distinct proofs are known. It is the foundation of Euclidean distance in any number of dimensions: in \\(\\mathbb{R}^n\\), the distance between points \\(\\mathbf{u}\\) and \\(\\mathbf{v}\\) is \\(\\|\\mathbf{u}-\\mathbf{v}\\|=\\sqrt{\\sum(u_i-v_i)^2}\\).",
    "Pythagorean triples are integer solutions: (3,4,5), (5,12,13), (8,15,17), (7,24,25). The general formula generates all primitive triples: \\(a=m^2-n^2\\), \\(b=2mn\\), \\(c=m^2+n^2\\) for integers \\(m>n>0\\) with \\(\\gcd(m,n)=1\\) and \\(m-n\\) odd.",
    "The converse is equally important: if \\(a^2+b^2=c^2\\), the triangle is right-angled. This is used in construction to verify right angles (the 3-4-5 check). In non-Euclidean geometry, the Pythagorean theorem fails: on a sphere, \\(\\cos c=\\cos a\\cos b\\) (spherical law of cosines).",
    "Fermat's Last Theorem, proved by Andrew Wiles in 1995, states that \\(a^n+b^n=c^n\\) has no positive integer solutions for \\(n>2\\) — a profound generalization of the Pythagorean equation."
),
"trigonometry": p(
    "Trigonometry studies the relationships between angles and side lengths in triangles, then extends these to periodic functions defined on the entire real line. The six trig functions — sin, cos, tan, csc, sec, cot — are defined via the unit circle and satisfy a rich web of identities.",
    "The <strong>angle addition formulas</strong> \\(\\sin(A+B)=\\sin A\\cos B+\\cos A\\sin B\\) and \\(\\cos(A+B)=\\cos A\\cos B-\\sin A\\sin B\\) are the source of all other identities. From them derive double-angle, half-angle, product-to-sum, and sum-to-product formulas.",
    "Inverse trig functions (arcsin, arccos, arctan) recover angles from ratios. Their derivatives — \\(d/dx[\\arcsin x]=1/\\sqrt{1-x^2}\\), \\(d/dx[\\arctan x]=1/(1+x^2)\\) — appear in integration formulas for expressions involving \\(\\sqrt{a^2-x^2}\\) and \\(a^2+x^2\\).",
    "Applications span navigation (bearing and distance), physics (wave motion, oscillations, AC circuits), signal processing (Fourier series decomposes any periodic signal into sines and cosines), and computer graphics (rotation matrices use trig functions)."
),
"polygon": p(
    "A polygon is a closed plane figure bounded by straight line segments. Regular polygons — all sides and angles equal — have been studied since antiquity. The ancient Greeks knew how to construct regular polygons with 3, 4, 5, 6, and 15 sides using compass and straightedge. Gauss proved at age 18 that a regular 17-gon is constructible, and characterized all constructible regular polygons.",
    "The interior angle sum of an \\(n\\)-gon is \\((n-2)\\cdot180°\\). For a regular \\(n\\)-gon, each interior angle is \\((n-2)\\cdot180°/n\\). As \\(n\\to\\infty\\), the regular \\(n\\)-gon approaches a circle and each interior angle approaches 180°.",
    "The area of a regular \\(n\\)-gon with side length \\(s\\) is \\(A=\\frac{ns^2}{4}\\cot(\\pi/n)\\). Polygons tile the plane only for \\(n=3,4,6\\) (triangles, squares, hexagons) — a fact with implications for crystallography and architecture.",
    "In computational geometry, polygon algorithms (convex hull, point-in-polygon, polygon clipping) are fundamental to GIS, robotics, and computer graphics. The shoelace formula computes the area of any polygon from its vertex coordinates: \\(A=\\frac{1}{2}|\\sum_{i}(x_iy_{i+1}-x_{i+1}y_i)|\\)."
),
}

for slug, extra_html in _geo_extra.items():
    EXTRA[f"geometry/{slug}"] = [sec("indepth","In Depth", extra_html)]

# remaining geometry topics — shared deep-dive template
_geo_remaining = {
"slope": p("Slope is the fundamental measure of steepness of a line, defined as rise over run: \\(m=(y_2-y_1)/(x_2-x_1)\\). It is the derivative of a linear function and the simplest case of a derivative. Parallel lines have equal slopes; perpendicular lines have slopes that are negative reciprocals (\\(m_1 m_2=-1\\)).", "In calculus, the slope of the tangent line to a curve at a point is the derivative at that point. In statistics, the slope of the regression line equals \\(r\\cdot(s_y/s_x)\\), connecting correlation to linear prediction. In physics, slope on a position-time graph is velocity; slope on a velocity-time graph is acceleration.", "The slope-intercept form \\(y=mx+b\\) is convenient for graphing. The point-slope form \\(y-y_1=m(x-x_1)\\) is convenient for writing the equation given a point and slope. The standard form \\(Ax+By=C\\) is useful for finding intercepts and for systems of equations."),
"area": p("Surface area measures the total area of the outer surface of a 3D solid. It is essential in engineering (heat transfer is proportional to surface area), biology (cell surface-to-volume ratio limits cell size), and packaging design (minimizing material for a given volume).", "For curved surfaces, surface area is computed by integration: \\(SA=\\iint_S dA\\). For a surface of revolution \\(y=f(x)\\) rotated about the \\(x\\)-axis: \\(SA=2\\pi\\int_a^b f(x)\\sqrt{1+[f'(x)]^2}\\,dx\\).", "The isoperimetric inequality states that among all closed curves of a given perimeter, the circle encloses the maximum area. In 3D, among all surfaces enclosing a given volume, the sphere has the minimum surface area — explaining why soap bubbles are spherical."),
"volume": p("Volume measures the amount of 3D space enclosed by a surface. Cavalieri's principle: if two solids have equal cross-sectional areas at every height, they have equal volumes. This principle, used by Archimedes, allows computing volumes of irregular solids by comparing them to known ones.", "For solids of revolution, the disk/washer and shell methods (from integral calculus) compute volumes exactly. For irregular solids, numerical integration or the divergence theorem (Gauss's theorem) \\(V=\\frac{1}{3}\\oiint_S \\mathbf{r}\\cdot d\\mathbf{S}\\) can be used.", "Packing problems ask how efficiently identical objects fill space. Spheres can fill at most \\(\\pi/(3\\sqrt{2})\\approx74.05\\%\\) of space (Kepler conjecture, proved by Hales in 1998). This has applications in coding theory and materials science."),
"coordinate-system": p("The Cartesian coordinate system, introduced by Descartes in 1637, unified algebra and geometry. Every geometric object can be described by an equation, and every equation describes a geometric object. This duality is the foundation of analytic geometry and all of modern mathematics.", "Beyond 2D and 3D Cartesian coordinates, other systems are often more natural: polar coordinates \\((r,\\theta)\\) for circular symmetry, cylindrical coordinates \\((r,\\theta,z)\\) for axial symmetry, and spherical coordinates \\((\\rho,\\theta,\\phi)\\) for full 3D symmetry. Changing coordinates can simplify integrals dramatically.", "In linear algebra, a coordinate system is a choice of basis. The same vector has different coordinates in different bases. Change-of-basis matrices transform coordinates between systems, a concept central to eigenvalue problems and principal component analysis."),
"ellipse": p("The ellipse is the set of points whose sum of distances from two fixed points (foci) is constant. It is one of the four conic sections obtained by intersecting a cone with a plane. Kepler's first law states that planetary orbits are ellipses with the Sun at one focus — a profound connection between geometry and celestial mechanics.", "The eccentricity \\(e=c/a\\) (where \\(c^2=a^2-b^2\\)) measures how elongated the ellipse is: \\(e=0\\) gives a circle, \\(e\\to1\\) gives a very elongated ellipse. Earth's orbit has \\(e\\approx0.017\\) (nearly circular); Halley's comet has \\(e\\approx0.967\\).", "The reflective property: a ray from one focus reflects off the ellipse and passes through the other focus. This is used in whispering galleries (elliptical rooms where a whisper at one focus is heard clearly at the other) and in medical lithotripsy (focusing shock waves to break kidney stones)."),
"parabola": p("The parabola is the set of points equidistant from a fixed point (focus) and a fixed line (directrix). It is the trajectory of a projectile under constant gravity (ignoring air resistance) and the shape of satellite dishes, car headlights, and telescope mirrors.", "The reflective property: rays parallel to the axis of symmetry reflect through the focus. This concentrates incoming parallel rays (sunlight, radio waves) at the focus, making parabolic reflectors ideal for antennas and solar collectors. Conversely, a light source at the focus produces a parallel beam.", "In algebra, every quadratic function \\(y=ax^2+bx+c\\) has a parabolic graph. The vertex form \\(y=a(x-h)^2+k\\) reveals the vertex \\((h,k)\\) directly. The discriminant \\(b^2-4ac\\) determines the number of real roots (x-intercepts): positive means two, zero means one (tangent to x-axis), negative means none."),
"hyperbola": p("The hyperbola is the set of points whose difference of distances from two foci is constant. It appears in navigation (LORAN system uses hyperbolic position lines), physics (Rutherford scattering of alpha particles follows hyperbolic paths), and optics (some telescope designs use hyperbolic mirrors).", "The asymptotes \\(y=\\pm(b/a)x\\) are lines the hyperbola approaches but never reaches. The eccentricity \\(e=c/a>1\\) (since \\(c^2=a^2+b^2>a^2\\)). A rectangular hyperbola (\\(a=b\\)) has perpendicular asymptotes and the equation \\(xy=k\\) — the graph of an inverse proportion.", "The conjugate hyperbola \\(y^2/b^2-x^2/a^2=1\\) shares the same asymptotes. Together, a hyperbola and its conjugate form a pair that appears in the study of indefinite quadratic forms and Lorentzian geometry (special relativity uses a hyperbolic metric)."),
}

for slug, extra_html in _geo_remaining.items():
    EXTRA[f"geometry/{slug}"] = [sec("indepth","In Depth", extra_html)]

# ── NUMBER THEORY ─────────────────────────────────────────────────────────────
_nt_extra = {
"prime-number": p("Prime numbers are the atoms of arithmetic — every integer greater than 1 is either prime or a unique product of primes. The Prime Number Theorem (PNT), proved independently by Hadamard and de la Vallée Poussin in 1896, gives the asymptotic density: \\(\\pi(x)\\sim x/\\ln x\\), meaning primes thin out logarithmically.", "The distribution of primes is deeply connected to the Riemann zeta function. The Riemann Hypothesis — that all non-trivial zeros of \\(\\zeta(s)\\) lie on the line \\(\\text{Re}(s)=1/2\\) — would give the sharpest known error term in the PNT. It remains unproved and is one of the Millennium Prize Problems.", "Primality testing is computationally easy: the AKS algorithm (2002) runs in polynomial time. Factoring, however, is believed to be hard — the security of RSA encryption rests on this asymmetry. The largest known prime (as of 2024) is a Mersenne prime with over 41 million digits."),
"modular-arithmetic": p("Modular arithmetic is arithmetic on a 'clock' — numbers wrap around after reaching the modulus \\(m\\). It is the foundation of number theory and modern cryptography. The integers mod \\(m\\), written \\(\\mathbb{Z}/m\\mathbb{Z}\\), form a ring; when \\(m\\) is prime, they form a field.", "The multiplicative group \\((\\mathbb{Z}/m\\mathbb{Z})^*\\) consists of residues coprime to \\(m\\) and has order \\(\\varphi(m)\\). Fermat's little theorem and Euler's theorem describe the structure of this group. Discrete logarithms in this group — finding \\(x\\) such that \\(g^x\\equiv a\\pmod{m}\\) — are computationally hard, forming the basis of Diffie–Hellman key exchange.", "The Chinese Remainder Theorem shows that \\(\\mathbb{Z}/mn\\mathbb{Z}\\cong\\mathbb{Z}/m\\mathbb{Z}\\times\\mathbb{Z}/n\\mathbb{Z}\\) when \\(\\gcd(m,n)=1\\). This isomorphism is used in fast arithmetic (splitting large computations into smaller ones) and in the RSA algorithm."),
"prime-factorization": p("The Fundamental Theorem of Arithmetic guarantees unique prime factorization. This uniqueness is not automatic — in some rings (e.g., \\(\\mathbb{Z}[\\sqrt{-5}]\\)), factorization is not unique, motivating the theory of ideals in algebraic number theory.", "Computing the prime factorization of a large integer is believed to be computationally hard (no polynomial-time algorithm is known). The best general-purpose algorithm, the General Number Field Sieve, runs in sub-exponential time \\(\\exp(O(n^{1/3}(\\ln n)^{2/3}))\\). This hardness is the security foundation of RSA.", "Applications: GCD and LCM are easily computed from prime factorizations. The number of divisors \\(\\tau(n)=\\prod(a_i+1)\\) and sum of divisors \\(\\sigma(n)=\\prod(p_i^{a_i+1}-1)/(p_i-1)\\) are multiplicative functions of the factorization."),
"greatest-common-divisor": p("The Euclidean algorithm is one of the oldest algorithms in mathematics, appearing in Euclid's Elements (c. 300 BCE). It runs in \\(O(\\log\\min(a,b))\\) steps — the number of steps is bounded by the number of digits. The extended Euclidean algorithm also finds integers \\(x,y\\) such that \\(ax+by=\\gcd(a,b)\\) (Bézout's identity).", "GCD has a beautiful lattice structure: \\(\\gcd(a,b)\\) is the largest element dividing both \\(a\\) and \\(b\\), while \\(\\text{lcm}(a,b)\\) is the smallest multiple of both. The identity \\(\\gcd(a,b)\\cdot\\text{lcm}(a,b)=|ab|\\) reflects this duality.", "In abstract algebra, the GCD generalizes to principal ideal domains (PIDs): \\(\\gcd(a,b)\\) generates the ideal \\((a)+(b)=\\{ax+by:x,y\\in\\mathbb{Z}\\}\\). This perspective unifies integer GCDs with polynomial GCDs and other algebraic structures."),
"fermats-little-theorem": p("Fermat's little theorem is a cornerstone of number theory with direct applications to primality testing and cryptography. The Miller–Rabin primality test is a probabilistic algorithm based on a strengthening of Fermat's theorem: if \\(n\\) is prime, then for any \\(a\\) coprime to \\(n\\), either \\(a^d\\equiv1\\) or \\(a^{2^r d}\\equiv-1\\pmod{n}\\) for some \\(r\\).", "Carmichael numbers are composite integers \\(n\\) satisfying \\(a^{n-1}\\equiv1\\pmod{n}\\) for all \\(a\\) coprime to \\(n\\) — they fool the naive Fermat primality test. The smallest is 561=3·11·17. The Miller–Rabin test is not fooled by Carmichael numbers.", "Euler's generalization: \\(a^{\\varphi(n)}\\equiv1\\pmod{n}\\) for \\(\\gcd(a,n)=1\\). This is the mathematical basis of RSA decryption: the decryption exponent \\(d\\) satisfies \\(ed\\equiv1\\pmod{\\varphi(n)}\\), so \\((m^e)^d=m^{ed}\\equiv m\\pmod{n}\\)."),
"chinese-remainder-theorem": p("The Chinese Remainder Theorem (CRT) has been known in China since the 3rd century CE (Sun Tzu's Mathematical Classic). It states that a system of simultaneous congruences with pairwise coprime moduli has a unique solution modulo the product of the moduli.", "The CRT has a constructive proof: the solution is \\(x=\\sum_i a_i M_i y_i\\pmod{M}\\) where \\(M=\\prod m_i\\), \\(M_i=M/m_i\\), and \\(y_i=M_i^{-1}\\pmod{m_i}\\). This construction is used in fast multi-precision arithmetic and in the RSA algorithm (CRT form of RSA is about 4× faster).", "In abstract algebra, CRT is the statement \\(\\mathbb{Z}/M\\mathbb{Z}\\cong\\prod_i\\mathbb{Z}/m_i\\mathbb{Z}\\) as rings. This ring isomorphism generalizes to any principal ideal domain and is a special case of the structure theorem for modules over PIDs."),
"riemann-hypothesis": p("The Riemann zeta function \\(\\zeta(s)=\\sum_{n=1}^\\infty n^{-s}\\) converges for \\(\\text{Re}(s)>1\\) and extends analytically to the entire complex plane (except a simple pole at \\(s=1\\)). Its zeros control the distribution of primes: the explicit formula \\(\\pi(x)=\\text{Li}(x)-\\sum_\\rho\\text{Li}(x^\\rho)+\\ldots\\) sums over the non-trivial zeros \\(\\rho\\).", "The Riemann Hypothesis (RH), stated in 1859, asserts all non-trivial zeros satisfy \\(\\text{Re}(\\rho)=1/2\\). It has been verified for the first \\(10^{13}\\) zeros. If true, RH implies the sharpest possible error bound in the PNT: \\(|\\pi(x)-\\text{Li}(x)|=O(\\sqrt{x}\\ln x)\\).", "RH is one of the seven Millennium Prize Problems (\\$1 million prize). It has hundreds of equivalent formulations and conditional results — many theorems in analytic number theory are proved 'assuming RH'. Its resolution would have profound implications for cryptography, since the distribution of primes affects the security of many cryptographic systems."),
}

for slug, extra_html in _nt_extra.items():
    EXTRA[f"number-theory/{slug}"] = [sec("indepth","In Depth", extra_html)]

# ── LINEAR ALGEBRA ────────────────────────────────────────────────────────────
_la_extra = {
"eigenvalue": p("Eigenvalues and eigenvectors reveal the intrinsic geometry of a linear transformation. The characteristic polynomial \\(\\det(A-\\lambda I)=0\\) has degree \\(n\\) for an \\(n\\times n\\) matrix, so there are exactly \\(n\\) eigenvalues (counting multiplicity) over \\(\\mathbb{C}\\).", "The spectral theorem states that every real symmetric matrix has real eigenvalues and an orthonormal basis of eigenvectors. This means symmetric matrices are diagonalizable: \\(A=Q\\Lambda Q^T\\) where \\(Q\\) is orthogonal and \\(\\Lambda\\) is diagonal. Symmetric matrices arise naturally as covariance matrices, Hessians, and graph Laplacians.", "Applications: Google's PageRank algorithm finds the dominant eigenvector of a web link matrix. Principal Component Analysis (PCA) computes eigenvectors of the data covariance matrix to find directions of maximum variance. Quantum mechanics represents observable quantities as Hermitian operators whose eigenvalues are the possible measurement outcomes."),
"singular-value-decomposition": p("SVD is the most important matrix factorization in applied mathematics. Every \\(m\\times n\\) matrix \\(A\\) has an SVD \\(A=U\\Sigma V^T\\) where \\(U\\) (\\(m\\times m\\)) and \\(V\\) (\\(n\\times n\\)) are orthogonal and \\(\\Sigma\\) (\\(m\\times n\\)) is diagonal with non-negative entries \\(\\sigma_1\\geq\\sigma_2\\geq\\ldots\\geq0\\).", "The rank-\\(k\\) truncated SVD \\(A_k=U_k\\Sigma_k V_k^T\\) is the best rank-\\(k\\) approximation to \\(A\\) in both the 2-norm and Frobenius norm (Eckart–Young theorem). This is the mathematical basis of image compression, latent semantic analysis, and collaborative filtering (Netflix-style recommendation).", "The condition number \\(\\kappa(A)=\\sigma_1/\\sigma_n\\) measures sensitivity of the linear system \\(Ax=b\\) to perturbations. A large condition number means the system is ill-conditioned — small errors in \\(b\\) can cause large errors in \\(x\\). SVD-based solvers (pseudoinverse) handle rank-deficient and ill-conditioned systems robustly."),
"linear-transformation": p("Linear transformations are the morphisms of vector spaces — the structure-preserving maps. Every linear map \\(T:\\mathbb{R}^n\\to\\mathbb{R}^m\\) is represented by an \\(m\\times n\\) matrix \\(A\\) via \\(T(\\mathbf{x})=A\\mathbf{x}\\). The matrix depends on the choice of bases; changing bases changes the matrix by a similarity transformation \\(A\\mapsto P^{-1}AP\\).", "The kernel (null space) and image (column space) of \\(T\\) are subspaces satisfying the rank-nullity theorem: \\(\\dim(\\ker T)+\\dim(\\text{im}\\,T)=\\dim(\\text{domain})\\). Injective maps have trivial kernel; surjective maps have image equal to the codomain; bijective maps are invertible.", "Geometric transformations — rotations, reflections, projections, shears — are all linear. Rotation by \\(\\theta\\) in \\(\\mathbb{R}^2\\) has matrix \\([[\\cos\\theta,-\\sin\\theta],[\\sin\\theta,\\cos\\theta]]\\). Composition of transformations corresponds to matrix multiplication, which is why matrix multiplication is defined the way it is."),
"determinant": p("The determinant of an \\(n\\times n\\) matrix is a scalar that encodes the signed volume scaling factor of the corresponding linear transformation. If \\(|\\det A|>1\\), the transformation expands volumes; if \\(|\\det A|<1\\), it contracts them; if \\(\\det A=0\\), the transformation collapses the space to lower dimension (the matrix is singular).", "The sign of \\(\\det A\\) indicates orientation: positive means the transformation preserves orientation (like a rotation); negative means it reverses orientation (like a reflection). This is why \\(\\det(AB)=\\det A\\cdot\\det B\\) — composing transformations multiplies their volume scaling factors.", "Cramer's rule expresses the solution of \\(Ax=b\\) as \\(x_i=\\det(A_i)/\\det(A)\\) where \\(A_i\\) replaces the \\(i\\)th column of \\(A\\) with \\(b\\). While theoretically elegant, it is computationally inefficient for large systems — Gaussian elimination is far faster in practice."),
"gram-schmidt": p("The Gram–Schmidt process converts any linearly independent set into an orthonormal basis. Orthonormal bases simplify nearly every computation: projections become dot products, the matrix of a linear map in an orthonormal basis is easier to analyze, and numerical algorithms are more stable.", "Numerically, the classical Gram–Schmidt process can lose orthogonality due to floating-point errors. The modified Gram–Schmidt algorithm reorders the computation to maintain orthogonality more robustly. Householder reflections and Givens rotations are even more numerically stable alternatives used in production QR decomposition algorithms.", "The Gram–Schmidt process is the constructive proof that every finite-dimensional inner product space has an orthonormal basis. In function spaces (Hilbert spaces), the analogous process produces orthogonal polynomials — Legendre, Chebyshev, Hermite — which are fundamental in approximation theory and numerical integration."),
}

for slug, extra_html in _la_extra.items():
    EXTRA[f"linear-algebra/{slug}"] = [sec("indepth","In Depth", extra_html)]

# ── INJECTION LOGIC ───────────────────────────────────────────────────────────
def inject(html: str, sections: list) -> str:
    """Insert extra sections before </main>."""
    extra_html = "\n".join(sections)
    return html.replace("</main>", extra_html + "\n</main>", 1)

def run():
    for rel_slug, sections in EXTRA.items():
        path = os.path.join(ROOT, rel_slug, "index.html")
        if not os.path.exists(path):
            print(f"SKIP (not found): {path}")
            continue
        with open(path, encoding="utf-8") as f:
            html = f.read()
        # Skip if already enriched
        if 'id="indepth"' in html or 'id="bg"' in html or 'id="background"' in html:
            print(f"already enriched: {rel_slug}")
            continue
        new_html = inject(html, sections)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        print(f"enriched: {rel_slug}")

if __name__ == "__main__":
    run()
