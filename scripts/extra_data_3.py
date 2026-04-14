"""Extra content part 3: number-theory, linear-algebra, statistics hub."""

def sec(sid, title, body):
    return f'<div class="content-section" id="{sid}"><h2>{title}</h2>{body}</div>'

def p(*texts):
    return "".join(f"<p>{t}</p>" for t in texts)

EXTRA3 = {}

EXTRA3["number-theory/composite-number"] = [sec("indepth","In Depth", p(
    "A composite number is a positive integer greater than 1 that has at least one positive divisor other than 1 and itself. Every composite number can be written as a product of primes — this is the content of the Fundamental Theorem of Arithmetic. The smallest composite is 4 = 2×2.",
    "Composite numbers are detected by trial division: test divisibility by all primes up to \\(\\sqrt{n}\\). If none divide \\(n\\), it is prime; otherwise it is composite. For large numbers, probabilistic primality tests (Miller–Rabin) are far faster and are used in cryptographic libraries.",
    "Highly composite numbers (Ramanujan's term) have more divisors than any smaller positive integer: 1, 2, 4, 6, 12, 24, 60, 120, … They arise naturally in problems involving divisibility and are related to the divisor function \\(d(n)\\).",
    "The density of composites grows: by the prime number theorem, the fraction of integers up to \\(N\\) that are prime is approximately \\(1/\\ln N\\), so almost all large integers are composite. Consecutive composites can be arbitrarily long — the sequence \\(n!+2, n!+3, \\ldots, n!+n\\) gives \\(n-1\\) consecutive composites.",
    "In cryptography, the difficulty of factoring large composites (products of two large primes) underpins RSA encryption. The security relies on the fact that while multiplying two primes is fast, reversing the process — finding the factors of a large composite — is computationally infeasible with current algorithms."
))]

EXTRA3["number-theory/congruence"] = [sec("indepth","In Depth", p(
    "Two integers \\(a\\) and \\(b\\) are congruent modulo \\(n\\) (written \\(a\\equiv b\\pmod{n}\\)) if \\(n\\mid(a-b)\\). Congruence is an equivalence relation that partitions the integers into \\(n\\) residue classes \\(\\{0,1,\\ldots,n-1\\}\\). Arithmetic on residue classes forms the ring \\(\\mathbb{Z}/n\\mathbb{Z}\\).",
    "Congruences can be added and multiplied: if \\(a\\equiv b\\) and \\(c\\equiv d\\pmod{n}\\), then \\(a+c\\equiv b+d\\) and \\(ac\\equiv bd\\pmod{n}\\). Division requires care: \\(ac\\equiv bc\\pmod{n}\\) implies \\(a\\equiv b\\pmod{n/\\gcd(c,n)}\\), not necessarily \\(\\pmod{n}\\).",
    "Fermat's little theorem: if \\(p\\) is prime and \\(\\gcd(a,p)=1\\), then \\(a^{p-1}\\equiv 1\\pmod{p}\\). Euler's generalization: \\(a^{\\phi(n)}\\equiv 1\\pmod{n}\\) when \\(\\gcd(a,n)=1\\). These are the basis of RSA and other public-key cryptosystems.",
    "The Chinese Remainder Theorem (CRT) reconstructs an integer from its residues modulo pairwise coprime moduli. If \\(n=p_1p_2\\cdots p_k\\) with distinct primes, then \\(\\mathbb{Z}/n\\mathbb{Z}\\cong\\mathbb{Z}/p_1\\mathbb{Z}\\times\\cdots\\times\\mathbb{Z}/p_k\\mathbb{Z}\\). CRT is used in fast arithmetic and in cryptographic protocols.",
    "Quadratic congruences \\(x^2\\equiv a\\pmod{p}\\) are solvable iff \\(a\\) is a quadratic residue mod \\(p\\), determined by the Legendre symbol \\((a/p)=a^{(p-1)/2}\\bmod p\\). The law of quadratic reciprocity relates \\((p/q)\\) and \\((q/p)\\) for odd primes \\(p,q\\) and is one of the most celebrated theorems in number theory."
))]

EXTRA3["number-theory/least-common-multiple"] = [sec("indepth","In Depth", p(
    "The least common multiple \\(\\text{lcm}(a,b)\\) is the smallest positive integer divisible by both \\(a\\) and \\(b\\). The fundamental identity \\(\\text{lcm}(a,b)\\cdot\\gcd(a,b)=ab\\) connects lcm and gcd, allowing lcm to be computed efficiently via the Euclidean algorithm.",
    "Using prime factorizations: \\(\\text{lcm}(a,b)\\) takes the maximum exponent of each prime, while \\(\\gcd(a,b)\\) takes the minimum. For example, \\(\\text{lcm}(12,18)=\\text{lcm}(2^2\\cdot3, 2\\cdot3^2)=2^2\\cdot3^2=36\\).",
    "The lcm of more than two numbers is computed iteratively: \\(\\text{lcm}(a,b,c)=\\text{lcm}(\\text{lcm}(a,b),c)\\). This is associative and commutative. The lcm of \\(1,2,\\ldots,n\\) grows like \\(e^n\\) by the prime number theorem.",
    "In algebra, the lcm of polynomials is the lowest-degree polynomial divisible by each, used when adding rational expressions. In modular arithmetic, the period of a combined system of congruences is the lcm of the individual periods.",
    "Applications: scheduling problems (when do two periodic events coincide?) reduce to lcm. Gear ratios, musical rhythms, and clock synchronization all involve lcm. In abstract algebra, the lcm generalizes to the least common multiple of ideals in a ring."
))]

EXTRA3["number-theory/continued-fractions"] = [sec("indepth","In Depth", p(
    "A continued fraction expresses a number as \\(a_0+\\cfrac{1}{a_1+\\cfrac{1}{a_2+\\cdots}}\\), written \\([a_0;a_1,a_2,\\ldots]\\). Every rational number has a finite continued fraction; every irrational has an infinite one. The convergents \\(p_k/q_k\\) are the best rational approximations to the number.",
    "The Euclidean algorithm produces the continued fraction expansion: repeatedly take the integer part and invert the remainder. For \\(\\sqrt{2}=[1;2,2,2,\\ldots]\\), the convergents \\(1/1, 3/2, 7/5, 17/12,\\ldots\\) are the best rational approximations and satisfy \\(p_k^2-2q_k^2=\\pm1\\) (Pell's equation).",
    "Periodic continued fractions characterize quadratic irrationals (Lagrange's theorem): \\(\\alpha\\) has a periodic continued fraction iff \\(\\alpha\\) satisfies a quadratic equation with integer coefficients. The period length is related to the class number of the associated quadratic field.",
    "The golden ratio \\(\\phi=[1;1,1,1,\\ldots]\\) has the simplest possible continued fraction and is the 'most irrational' number — its convergents are ratios of consecutive Fibonacci numbers, and it is hardest to approximate by rationals (Hurwitz's theorem).",
    "Continued fractions are used in the PSLQ algorithm for finding integer relations, in the Stern–Brocot tree for enumerating rationals, and in solving Pell's equation \\(x^2-Dy^2=1\\). They also appear in the analysis of the Euclidean algorithm's worst-case complexity (Fibonacci inputs)."
))]

EXTRA3["number-theory/euler-totient"] = [sec("indepth","In Depth", p(
    "Euler's totient function \\(\\phi(n)\\) counts the integers in \\(\\{1,\\ldots,n\\}\\) coprime to \\(n\\). For prime \\(p\\): \\(\\phi(p)=p-1\\). For prime power: \\(\\phi(p^k)=p^{k-1}(p-1)\\). Multiplicativity: \\(\\phi(mn)=\\phi(m)\\phi(n)\\) when \\(\\gcd(m,n)=1\\). General formula: \\(\\phi(n)=n\\prod_{p\\mid n}(1-1/p)\\).",
    "Euler's theorem: \\(a^{\\phi(n)}\\equiv1\\pmod{n}\\) for \\(\\gcd(a,n)=1\\). This generalizes Fermat's little theorem (\\(n=p\\) prime, \\(\\phi(p)=p-1\\)). The multiplicative order of \\(a\\) modulo \\(n\\) divides \\(\\phi(n)\\).",
    "RSA key generation uses \\(\\phi(n)\\): with \\(n=pq\\), \\(\\phi(n)=(p-1)(q-1)\\). The public exponent \\(e\\) satisfies \\(\\gcd(e,\\phi(n))=1\\); the private exponent \\(d\\) satisfies \\(ed\\equiv1\\pmod{\\phi(n)}\\). Decryption works because \\(m^{ed}\\equiv m\\pmod{n}\\) by Euler's theorem.",
    "The sum formula: \\(\\sum_{d\\mid n}\\phi(d)=n\\). This identity, proved by grouping fractions \\(k/n\\) by their reduced denominator, is a key tool in number theory. It shows \\(\\phi\\) is the Möbius inversion of the identity function.",
    "The average order of \\(\\phi(n)\\) is \\(3n/\\pi^2\\): \\(\\frac{1}{N}\\sum_{n=1}^N\\phi(n)\\sim\\frac{3N}{\\pi^2}\\). The constant \\(3/\\pi^2=6/\\pi^2\\cdot1/2\\) is related to the probability that two random integers are coprime, which equals \\(6/\\pi^2\\)."
))]

EXTRA3["number-theory/diophantine-equations"] = [sec("indepth","In Depth", p(
    "A Diophantine equation requires integer (or rational) solutions. The simplest is the linear equation \\(ax+by=c\\), which has integer solutions iff \\(\\gcd(a,b)\\mid c\\); the general solution is \\(x=x_0+bt/d\\), \\(y=y_0-at/d\\) for integer \\(t\\).",
    "Pell's equation \\(x^2-Dy^2=1\\) (\\(D\\) not a perfect square) always has infinitely many solutions, generated from the fundamental solution via the continued fraction expansion of \\(\\sqrt{D}\\). It was studied by Brahmagupta and Fermat long before Pell.",
    "Fermat's Last Theorem: \\(x^n+y^n=z^n\\) has no positive integer solutions for \\(n\\geq3\\). Stated by Fermat in 1637, proved by Wiles in 1995 using elliptic curves and modular forms — one of the greatest achievements in 20th-century mathematics.",
    "The Hasse–Minkowski theorem classifies which quadratic Diophantine equations have rational solutions: a quadratic form represents zero over \\(\\mathbb{Q}\\) iff it does so over \\(\\mathbb{R}\\) and over all \\(p\\)-adic fields \\(\\mathbb{Q}_p\\). This 'local-global principle' fails for higher-degree equations.",
    "Hilbert's tenth problem asked for an algorithm to decide whether any Diophantine equation has integer solutions. Matiyasevich (1970) proved no such algorithm exists — the problem is undecidable. This connects number theory to computability theory."
))]

EXTRA3["number-theory/euclidean-algorithm"] = [sec("indepth","In Depth", p(
    "The Euclidean algorithm computes \\(\\gcd(a,b)\\) by repeated division: \\(\\gcd(a,b)=\\gcd(b,a\\bmod b)\\), terminating when the remainder is 0. It is one of the oldest algorithms, appearing in Euclid's Elements (c. 300 BCE), and runs in \\(O(\\log\\min(a,b))\\) steps.",
    "The extended Euclidean algorithm also finds integers \\(x,y\\) such that \\(ax+by=\\gcd(a,b)\\) (Bézout's identity). These coefficients are used to compute modular inverses: if \\(\\gcd(a,n)=1\\), then \\(a^{-1}\\bmod n\\) is the \\(x\\) from \\(ax+ny=1\\).",
    "Worst-case inputs are consecutive Fibonacci numbers: \\(\\gcd(F_{n+1},F_n)\\) requires exactly \\(n\\) steps. This proves the algorithm's \\(O(\\log n)\\) bound is tight. The Fibonacci numbers are the 'most difficult' inputs for the Euclidean algorithm.",
    "The binary GCD algorithm replaces division with subtraction and halving, using only bit shifts and subtraction — faster on hardware where division is expensive. It achieves the same \\(O(\\log n)\\) complexity.",
    "The Euclidean algorithm generalizes to any Euclidean domain: a ring with a 'size' function where division with remainder is possible. Examples include the Gaussian integers \\(\\mathbb{Z}[i]\\) and polynomial rings \\(F[x]\\) over a field. In these settings, the algorithm computes GCDs of complex numbers or polynomials."
))]

EXTRA3["number-theory/p-adic-numbers"] = [sec("indepth","In Depth", p(
    "The \\(p\\)-adic numbers \\(\\mathbb{Q}_p\\) are a completion of \\(\\mathbb{Q}\\) using the \\(p\\)-adic absolute value \\(|p^k m/n|_p=p^{-k}\\) (with \\(p\\nmid m,n\\)). Unlike the real completion, \\(p\\)-adic numbers measure divisibility by \\(p\\): numbers highly divisible by \\(p\\) are 'small'.",
    "Every nonzero rational has a unique \\(p\\)-adic expansion \\(\\sum_{k=v}^\\infty a_k p^k\\) with \\(0\\leq a_k<p\\) and \\(v\\in\\mathbb{Z}\\). Unlike decimal expansions, these extend infinitely to the left. For example, in \\(\\mathbb{Q}_5\\): \\(-1=4+4\\cdot5+4\\cdot5^2+\\cdots\\).",
    "Hensel's lemma: if \\(f(a)\\equiv0\\pmod{p}\\) and \\(f'(a)\\not\\equiv0\\pmod{p}\\), then \\(a\\) lifts uniquely to a root of \\(f\\) in \\(\\mathbb{Z}_p\\). This is the \\(p\\)-adic analogue of Newton's method and is used to solve congruences modulo prime powers.",
    "Ostrowski's theorem: every non-trivial absolute value on \\(\\mathbb{Q}\\) is equivalent to either the usual absolute value or a \\(p\\)-adic absolute value. So the reals and the \\(p\\)-adic fields are the only completions of \\(\\mathbb{Q}\\) — they capture all possible notions of 'closeness' for rationals.",
    "\\(p\\)-adic numbers are central to modern number theory: the Hasse–Minkowski theorem uses all \\(p\\)-adic fields simultaneously; \\(p\\)-adic \\(L\\)-functions interpolate classical \\(L\\)-functions; and \\(p\\)-adic Hodge theory connects \\(p\\)-adic representations to differential forms."
))]

EXTRA3["number-theory/sieve-of-eratosthenes"] = [sec("indepth","In Depth", p(
    "The Sieve of Eratosthenes finds all primes up to \\(N\\) by iteratively marking multiples of each prime as composite. Start with all integers from 2 to \\(N\\); mark multiples of 2, then 3, then 5, and so on up to \\(\\sqrt{N}\\). Unmarked numbers are prime.",
    "Time complexity: \\(O(N\\log\\log N)\\) — nearly linear. Space: \\(O(N)\\). The segmented sieve reduces space to \\(O(\\sqrt{N})\\) by processing the range in blocks, enabling sieving of very large ranges. The linear sieve achieves \\(O(N)\\) time by ensuring each composite is crossed off exactly once.",
    "The prime counting function \\(\\pi(N)\\) (number of primes \\(\\leq N\\)) is computed exactly by the sieve. The prime number theorem gives the asymptotic \\(\\pi(N)\\sim N/\\ln N\\). More precise estimates use the logarithmic integral \\(\\text{Li}(N)=\\int_2^N dt/\\ln t\\).",
    "Generalizations: the Sieve of Sundaram finds odd primes; the Sieve of Atkin is faster in practice for large \\(N\\). Analytic sieves (Brun, Selberg, large sieve) are theoretical tools that estimate the count of primes in arithmetic progressions and twin prime pairs.",
    "The sieve principle extends beyond primes: inclusion-exclusion sieves count integers in a range satisfying various divisibility conditions. Brun's theorem (proved using his sieve) shows the sum of reciprocals of twin primes converges, unlike the divergent sum of prime reciprocals."
))]

EXTRA3["number-theory/perfect-numbers"] = [sec("indepth","In Depth", p(
    "A perfect number equals the sum of its proper divisors. The first four are 6, 28, 496, 8128. Euclid proved that \\(2^{p-1}(2^p-1)\\) is perfect whenever \\(2^p-1\\) is prime (a Mersenne prime). Euler proved the converse: every even perfect number has this form.",
    "Whether any odd perfect number exists is one of the oldest open problems in mathematics. If one exists, it must be greater than \\(10^{1500}\\), have at least 9 distinct prime factors, and satisfy many other constraints — yet none has been found or ruled out.",
    "Related concepts: abundant numbers (sum of proper divisors exceeds the number), deficient numbers (sum is less), and amicable pairs (each equals the sum of the other's proper divisors). The pair (220, 284) was known to the ancient Greeks.",
    "The sum-of-divisors function \\(\\sigma(n)=\\sum_{d\\mid n}d\\) satisfies \\(\\sigma(n)=2n\\) for perfect \\(n\\). It is multiplicative: \\(\\sigma(mn)=\\sigma(m)\\sigma(n)\\) for \\(\\gcd(m,n)=1\\). For prime powers: \\(\\sigma(p^k)=(p^{k+1}-1)/(p-1)\\).",
    "Mersenne primes \\(M_p=2^p-1\\) are required for even perfect numbers. As of 2024, only 51 Mersenne primes are known, the largest being \\(2^{136279841}-1\\). The Great Internet Mersenne Prime Search (GIMPS) uses distributed computing to search for new ones."
))]

EXTRA3["number-theory/arithmetic-functions"] = [sec("indepth","In Depth", p(
    "An arithmetic function maps positive integers to complex numbers. Key examples: \\(d(n)\\) (number of divisors), \\(\\sigma(n)\\) (sum of divisors), \\(\\phi(n)\\) (Euler's totient), \\(\\mu(n)\\) (Möbius function), \\(\\Lambda(n)\\) (von Mangoldt function). These encode deep properties of the integers.",
    "Multiplicative functions satisfy \\(f(mn)=f(m)f(n)\\) when \\(\\gcd(m,n)=1\\). Completely multiplicative functions satisfy this for all \\(m,n\\). The Dirichlet series \\(\\sum_{n=1}^\\infty f(n)/n^s\\) encodes a multiplicative function as an Euler product \\(\\prod_p(1+f(p)/p^s+f(p^2)/p^{2s}+\\cdots)\\).",
    "Dirichlet convolution: \\((f*g)(n)=\\sum_{d\\mid n}f(d)g(n/d)\\). Arithmetic functions form a ring under pointwise addition and Dirichlet convolution. The identity element is \\(\\epsilon(n)=[n=1]\\). The Möbius function is the inverse of the constant function 1: \\(\\mu*1=\\epsilon\\).",
    "Möbius inversion: if \\(g(n)=\\sum_{d\\mid n}f(d)\\), then \\(f(n)=\\sum_{d\\mid n}\\mu(n/d)g(d)\\). This is used to invert summatory formulas — for example, recovering \\(\\phi\\) from the identity \\(\\sum_{d\\mid n}\\phi(d)=n\\).",
    "The Riemann zeta function \\(\\zeta(s)=\\sum_{n=1}^\\infty n^{-s}=\\prod_p(1-p^{-s})^{-1}\\) is the Dirichlet series of the constant function 1. The distribution of its zeros controls the error term in the prime number theorem, connecting arithmetic functions to complex analysis."
))]

EXTRA3["number-theory/mersenne-primes"] = [sec("indepth","In Depth", p(
    "A Mersenne prime has the form \\(M_p=2^p-1\\) where \\(p\\) itself is prime (a necessary but not sufficient condition). The first few are \\(M_2=3\\), \\(M_3=7\\), \\(M_5=31\\), \\(M_7=127\\). Not all prime \\(p\\) give prime \\(M_p\\): \\(M_{11}=2047=23\\times89\\).",
    "The Lucas–Lehmer test efficiently checks whether \\(M_p\\) is prime: define \\(s_0=4\\), \\(s_{k+1}=s_k^2-2\\pmod{M_p}\\); then \\(M_p\\) is prime iff \\(s_{p-2}\\equiv0\\pmod{M_p}\\). This deterministic test runs in \\(O(p^3)\\) bit operations and is the basis of GIMPS.",
    "Every even perfect number corresponds to a Mersenne prime via Euclid's formula \\(2^{p-1}(2^p-1)\\). So the search for Mersenne primes is equivalent to the search for even perfect numbers. As of 2024, 51 Mersenne primes are known.",
    "Mersenne primes are rare: heuristically, the probability that \\(2^p-1\\) is prime is approximately \\(e^\\gamma\\ln 2/p\\approx1.13/p\\) (Wagstaff's conjecture), so the expected number of Mersenne primes with exponent up to \\(N\\) grows like \\(e^\\gamma\\ln 2\\cdot\\ln N\\).",
    "Mersenne numbers \\(M_p\\) have special structure that makes them useful in computing: fast modular reduction modulo \\(M_p\\) uses only shifts and additions. This is exploited in cryptographic implementations and in the Fast Fourier Transform over finite fields."
))]

EXTRA3["number-theory/quadratic-residue"] = [sec("indepth","In Depth", p(
    "An integer \\(a\\) is a quadratic residue modulo \\(p\\) (odd prime, \\(p\\nmid a\\)) if \\(x^2\\equiv a\\pmod{p}\\) has a solution. There are exactly \\((p-1)/2\\) quadratic residues and \\((p-1)/2\\) non-residues among \\(\\{1,\\ldots,p-1\\}\\).",
    "The Legendre symbol \\(\\left(\\frac{a}{p}\\right)=a^{(p-1)/2}\\bmod p\\) equals \\(+1\\) if \\(a\\) is a QR, \\(-1\\) if a non-residue, and \\(0\\) if \\(p\\mid a\\). It is completely multiplicative in \\(a\\) and is computed efficiently using Euler's criterion.",
    "The law of quadratic reciprocity (Gauss): for distinct odd primes \\(p,q\\), \\(\\left(\\frac{p}{q}\\right)\\left(\\frac{q}{p}\\right)=(-1)^{\\frac{p-1}{2}\\cdot\\frac{q-1}{2}}\\). This means the two Legendre symbols agree unless both \\(p\\equiv q\\equiv3\\pmod4\\). Gauss gave eight proofs; over 200 proofs are now known.",
    "The Jacobi symbol \\(\\left(\\frac{a}{n}\\right)\\) extends the Legendre symbol to composite \\(n\\) as a product of Legendre symbols over prime factors. It satisfies the same reciprocity law but \\(\\left(\\frac{a}{n}\\right)=1\\) does not guarantee \\(a\\) is a QR mod \\(n\\).",
    "Quadratic residues appear in: the Tonelli–Shanks algorithm for computing square roots mod \\(p\\); the quadratic sieve factoring algorithm; and the construction of Paley graphs and Hadamard matrices in combinatorics."
))]

EXTRA3["number-theory/mobius-function"] = [sec("indepth","In Depth", p(
    "The Möbius function \\(\\mu(n)\\) is defined as: \\(\\mu(1)=1\\); \\(\\mu(n)=(-1)^k\\) if \\(n\\) is a product of \\(k\\) distinct primes; \\(\\mu(n)=0\\) if \\(n\\) has a squared prime factor. It is multiplicative and encodes the inclusion-exclusion principle for divisors.",
    "The key identity: \\(\\sum_{d\\mid n}\\mu(d)=[n=1]\\) (equals 1 if \\(n=1\\), else 0). This is the basis of Möbius inversion: if \\(g=f*1\\) (Dirichlet convolution with the constant 1), then \\(f=g*\\mu\\). It is the number-theoretic analogue of the inclusion-exclusion principle.",
    "The Mertens function \\(M(x)=\\sum_{n\\leq x}\\mu(n)\\) is conjectured to satisfy \\(|M(x)|<\\sqrt{x}\\) (the Mertens conjecture, disproved in 1985 — a counterexample exists but is astronomically large). The Riemann hypothesis is equivalent to \\(M(x)=O(x^{1/2+\\epsilon})\\) for all \\(\\epsilon>0\\).",
    "The Dirichlet series of \\(\\mu\\) is \\(\\sum\\mu(n)/n^s=1/\\zeta(s)\\), the reciprocal of the Riemann zeta function. This connects \\(\\mu\\) directly to the distribution of primes via the zeros of \\(\\zeta\\).",
    "In combinatorics, the Möbius function generalizes to partially ordered sets (posets). The Möbius function of a poset encodes inclusion-exclusion over the poset's structure and is used in the theory of lattices, matroids, and the chromatic polynomial of graphs."
))]

EXTRA3["number-theory/analytic-number-theory"] = [sec("indepth","In Depth", p(
    "Analytic number theory uses tools from complex analysis and real analysis to study the distribution of primes and arithmetic functions. Its central object is the Riemann zeta function \\(\\zeta(s)=\\sum_{n=1}^\\infty n^{-s}\\), which encodes prime distribution via the Euler product \\(\\prod_p(1-p^{-s})^{-1}\\).",
    "The prime number theorem (PNT): \\(\\pi(x)\\sim x/\\ln x\\) as \\(x\\to\\infty\\). Proved independently by Hadamard and de la Vallée Poussin in 1896 using the fact that \\(\\zeta(s)\\neq0\\) on the line \\(\\text{Re}(s)=1\\). An elementary proof (without complex analysis) was found by Selberg and Erdős in 1949.",
    "Dirichlet's theorem on primes in arithmetic progressions: if \\(\\gcd(a,q)=1\\), there are infinitely many primes \\(p\\equiv a\\pmod{q}\\). The proof uses Dirichlet \\(L\\)-functions \\(L(s,\\chi)=\\sum_{n=1}^\\infty\\chi(n)/n^s\\) for Dirichlet characters \\(\\chi\\) modulo \\(q\\).",
    "The Riemann hypothesis (RH): all non-trivial zeros of \\(\\zeta(s)\\) lie on the critical line \\(\\text{Re}(s)=1/2\\). RH implies the sharpest known error term in the PNT: \\(\\pi(x)=\\text{Li}(x)+O(\\sqrt{x}\\ln x)\\). It remains unproved and is one of the Millennium Prize Problems.",
    "The circle method (Hardy–Littlewood–Ramanujan) uses Fourier analysis on \\(\\mathbb{Z}/N\\mathbb{Z}\\) to count representations of integers as sums of primes or powers. It proved Vinogradov's theorem: every sufficiently large odd integer is a sum of three primes."
))]

EXTRA3["number-theory/primitive-root"] = [sec("indepth","In Depth", p(
    "A primitive root modulo \\(n\\) is an integer \\(g\\) whose powers generate all units: \\(\\{g^1,g^2,\\ldots,g^{\\phi(n)}\\}=\\{a:\\gcd(a,n)=1\\}\\). Primitive roots exist modulo \\(n\\) iff \\(n=1,2,4,p^k,2p^k\\) for odd prime \\(p\\). When they exist, the group \\((\\mathbb{Z}/n\\mathbb{Z})^*\\) is cyclic.",
    "Finding a primitive root: test candidates \\(g\\) by checking \\(g^{\\phi(n)/q}\\not\\equiv1\\pmod{n}\\) for each prime \\(q\\mid\\phi(n)\\). The smallest primitive root modulo \\(p\\) is usually small (often less than \\(\\ln^2 p\\) under GRH), but no deterministic polynomial-time algorithm is known unconditionally.",
    "Discrete logarithm: given \\(g^x\\equiv h\\pmod{p}\\), find \\(x\\). This is believed to be hard (no polynomial-time classical algorithm), and its hardness underpins Diffie–Hellman key exchange and ElGamal encryption. The best algorithms (index calculus, number field sieve) run in subexponential time.",
    "The number of primitive roots modulo \\(p\\) is \\(\\phi(p-1)\\). For example, modulo 7 (\\(p-1=6\\), \\(\\phi(6)=2\\)), there are 2 primitive roots: 3 and 5. The primitive roots are the generators of the cyclic group \\((\\mathbb{Z}/p\\mathbb{Z})^*\\).",
    "Artin's conjecture: every integer \\(a\\neq-1\\) that is not a perfect square is a primitive root for infinitely many primes. Hooley proved this conditionally under GRH. Heath-Brown proved unconditionally that at most two of any three candidates fail to be primitive roots for infinitely many primes."
))]

EXTRA3["number-theory/twin-primes"] = [sec("indepth","In Depth", p(
    "Twin primes are pairs of primes differing by 2: (3,5), (5,7), (11,13), (17,19), (29,31), … The twin prime conjecture asserts there are infinitely many such pairs. Despite being one of the oldest open problems, it remains unproved.",
    "Brun's theorem (1919): the sum of reciprocals of twin primes \\(\\sum(1/p+1/(p+2))\\) converges to Brun's constant \\(B_2\\approx1.902\\). This contrasts with the divergent sum of all prime reciprocals and was the first quantitative result on twin primes.",
    "Zhang's breakthrough (2013): there are infinitely many prime pairs with gap at most 70,000,000. The Polymath project reduced this to 246. Under the Elliott–Halberstam conjecture, the bound reduces to 6. The goal is to reach 2 (twin primes).",
    "The Hardy–Littlewood conjecture gives an asymptotic for the number of twin prime pairs up to \\(x\\): \\(\\pi_2(x)\\sim 2C_2 x/(\\ln x)^2\\) where \\(C_2=\\prod_{p>2}\\frac{p(p-2)}{(p-1)^2}\\approx0.6601\\) is the twin prime constant. This is consistent with numerical evidence but unproved.",
    "Cousin primes differ by 4, sexy primes by 6. Prime constellations are patterns of primes with fixed differences; the admissibility condition (no prime divides all differences) is necessary for infinitely many occurrences. The Green–Tao theorem (2004) proves primes contain arbitrarily long arithmetic progressions."
))]

EXTRA3["number-theory/algebraic-number-theory"] = [sec("indepth","In Depth", p(
    "Algebraic number theory studies number fields — finite extensions \\(K/\\mathbb{Q}\\) — and their rings of integers \\(\\mathcal{O}_K\\). The ring \\(\\mathcal{O}_K\\) generalizes \\(\\mathbb{Z}\\) but may fail unique factorization. The class group \\(\\text{Cl}(K)\\) measures this failure; its order is the class number \\(h_K\\).",
    "Dedekind's ideal theory restores unique factorization at the level of ideals: every nonzero ideal in \\(\\mathcal{O}_K\\) factors uniquely as a product of prime ideals. This is the fundamental theorem of algebraic number theory.",
    "The Minkowski bound \\(M_K\\) guarantees every ideal class contains an ideal of norm \\(\\leq M_K\\). Since there are finitely many ideals of bounded norm, the class group is finite. Computing \\(h_K\\) is a central problem; for imaginary quadratic fields, Gauss's class number problem asked which have \\(h_K=1\\) (answer: exactly 9 fields).",
    "The Dirichlet unit theorem describes the group of units \\(\\mathcal{O}_K^*\\): it is isomorphic to \\(\\mu_K\\times\\mathbb{Z}^{r_1+r_2-1}\\) where \\(\\mu_K\\) is the finite group of roots of unity, \\(r_1\\) is the number of real embeddings, and \\(r_2\\) is the number of pairs of complex embeddings.",
    "Class field theory describes all abelian extensions of a number field in terms of the arithmetic of the field itself (via idèles and the Artin map). It is the culmination of 19th-century number theory and the starting point for the Langlands program, which seeks to unify number theory and representation theory."
))]

EXTRA3["number-theory/goldbach-conjecture"] = [sec("indepth","In Depth", p(
    "Goldbach's conjecture (1742): every even integer greater than 2 is the sum of two primes. Verified computationally up to \\(4\\times10^{18}\\), it remains unproved. It is one of the oldest and most famous unsolved problems in mathematics.",
    "The weak Goldbach conjecture (every odd integer \\(>5\\) is the sum of three primes) was proved by Helfgott in 2013 using the Hardy–Littlewood circle method with extensive numerical verification for small cases.",
    "Vinogradov's theorem (1937): every sufficiently large odd integer is the sum of three primes. 'Sufficiently large' originally meant \\(>e^{e^{11.503}}\\), a number with about \\(10^{6846}\\) digits. Helfgott's work reduced this to \\(>5\\), completing the proof for all odd integers \\(>5\\).",
    "The Hardy–Littlewood conjecture gives an asymptotic for the number of representations of \\(2n\\) as a sum of two primes: \\(r(2n)\\sim 2C_2\\prod_{p\\mid n,p>2}\\frac{p-1}{p-2}\\cdot\\frac{2n}{(\\ln 2n)^2}\\). This is consistent with numerical data but far from proved.",
    "Chen's theorem (1966): every sufficiently large even integer is the sum of a prime and a number with at most two prime factors (a 'P2 number'). This is the closest proved result to Goldbach's conjecture and uses the large sieve and Brun's sieve."
))]

EXTRA3["number-theory/divisibility"] = [sec("indepth","In Depth", p(
    "An integer \\(a\\) divides \\(b\\) (written \\(a\\mid b\\)) if \\(b=ka\\) for some integer \\(k\\). Divisibility is reflexive (\\(a\\mid a\\)), transitive (\\(a\\mid b\\) and \\(b\\mid c\\) implies \\(a\\mid c\\)), and antisymmetric on positive integers. The divisors of \\(n\\) form a lattice under divisibility.",
    "The division algorithm: for any integers \\(a\\) and \\(b>0\\), there exist unique \\(q,r\\) with \\(a=qb+r\\) and \\(0\\leq r<b\\). This is the foundation of the Euclidean algorithm and modular arithmetic.",
    "Divisibility rules provide shortcuts: \\(2\\mid n\\) iff the last digit is even; \\(3\\mid n\\) iff the digit sum is divisible by 3; \\(9\\mid n\\) iff the digit sum is divisible by 9; \\(11\\mid n\\) iff the alternating digit sum is divisible by 11. These follow from the fact that \\(10\\equiv1\\pmod9\\) and \\(10\\equiv-1\\pmod{11}\\).",
    "The number of divisors \\(d(n)=\\prod(e_i+1)\\) where \\(n=\\prod p_i^{e_i}\\). The average value of \\(d(n)\\) is \\(\\ln n\\): \\(\\frac{1}{N}\\sum_{n=1}^N d(n)\\sim\\ln N\\). The maximum of \\(d(n)\\) for \\(n\\leq N\\) grows like \\(N^{c/\\ln\\ln N}\\) for a constant \\(c\\).",
    "In abstract algebra, divisibility generalizes to any integral domain. An element \\(a\\) divides \\(b\\) if \\(b=ac\\) for some \\(c\\). Unique factorization domains (UFDs) are rings where every element factors uniquely into irreducibles — the algebraic abstraction of the Fundamental Theorem of Arithmetic."
))]

EXTRA3["number-theory/number-theory-cryptography"] = [sec("indepth","In Depth", p(
    "Modern cryptography relies heavily on number theory. RSA encryption uses the difficulty of factoring large semiprimes \\(n=pq\\). Diffie–Hellman key exchange relies on the discrete logarithm problem in \\((\\mathbb{Z}/p\\mathbb{Z})^*\\). Elliptic curve cryptography (ECC) uses the discrete log on elliptic curve groups, achieving equivalent security with smaller keys.",
    "The RSA algorithm: choose primes \\(p,q\\), set \\(n=pq\\), pick \\(e\\) with \\(\\gcd(e,\\phi(n))=1\\), compute \\(d=e^{-1}\\bmod\\phi(n)\\). Public key: \\((n,e)\\). Encryption: \\(c=m^e\\bmod n\\). Decryption: \\(m=c^d\\bmod n\\). Security: factoring \\(n\\) is believed hard for 2048-bit \\(n\\).",
    "Elliptic curves over finite fields \\(\\mathbb{F}_p\\) form groups under a geometric addition law. The group order is approximately \\(p\\) (Hasse's theorem: \\(|\\#E(\\mathbb{F}_p)-p-1|\\leq2\\sqrt{p}\\)). The discrete log on these groups has no known subexponential algorithm, making ECC very efficient.",
    "Hash functions, digital signatures, and zero-knowledge proofs also use number-theoretic hardness assumptions. The Schnorr signature scheme uses discrete logs; the Fiat–Shamir transform converts interactive proofs to non-interactive ones; lattice-based cryptography (post-quantum) uses the hardness of the shortest vector problem.",
    "Quantum computers threaten RSA and ECC: Shor's algorithm factors integers and computes discrete logs in polynomial time on a quantum computer. Post-quantum cryptography (NIST standardization ongoing) uses lattices, codes, and hash functions whose hardness is believed to resist quantum attacks."
))]

# ── LINEAR ALGEBRA ────────────────────────────────────────────────────────────
EXTRA3["linear-algebra/null-space"] = [sec("indepth","In Depth", p(
    "The null space (kernel) of a matrix \\(A\\) is \\(\\text{Null}(A)=\\{\\mathbf{x}:A\\mathbf{x}=\\mathbf{0}\\}\\). It is a subspace of the domain. The rank-nullity theorem: \\(\\text{rank}(A)+\\text{nullity}(A)=n\\) (number of columns). The null space captures all solutions to the homogeneous system.",
    "The null space is computed by row-reducing \\(A\\) to reduced row echelon form (RREF). Free variables (columns without pivots) parameterize the null space. Each free variable contributes one basis vector to the null space.",
    "The null space of \\(A^T\\) is the left null space of \\(A\\). The four fundamental subspaces of \\(A\\) (column space, null space, row space, left null space) are orthogonally complementary in pairs: \\(\\text{Col}(A)\\perp\\text{Null}(A^T)\\) and \\(\\text{Row}(A)\\perp\\text{Null}(A)\\).",
    "A matrix has trivial null space (only \\(\\mathbf{0}\\)) iff it has full column rank iff its columns are linearly independent iff \\(A\\mathbf{x}=\\mathbf{b}\\) has at most one solution for any \\(\\mathbf{b}\\). Square matrices with trivial null space are invertible.",
    "In differential equations, the null space of a linear differential operator \\(L\\) is the solution space of \\(Lu=0\\). For \\(L=d^2/dx^2+1\\), the null space is \\(\\{c_1\\cos x+c_2\\sin x\\}\\), a 2-dimensional space. The dimension of the null space equals the order of the ODE."
))]

EXTRA3["linear-algebra/dimension"] = [sec("indepth","In Depth", p(
    "The dimension of a vector space is the number of vectors in any basis — the minimum number of vectors needed to span the space. All bases of a finite-dimensional space have the same cardinality (the dimension theorem). \\(\\mathbb{R}^n\\) has dimension \\(n\\); the space of \\(m\\times n\\) matrices has dimension \\(mn\\).",
    "The rank-nullity theorem: for a linear map \\(T:V\\to W\\), \\(\\dim(\\ker T)+\\dim(\\text{im}\\,T)=\\dim V\\). This is one of the most useful results in linear algebra, relating the dimensions of the kernel (null space) and image (column space) to the domain dimension.",
    "Subspace dimensions: if \\(U,W\\) are subspaces of \\(V\\), then \\(\\dim(U+W)=\\dim U+\\dim W-\\dim(U\\cap W)\\) (inclusion-exclusion for dimensions). A direct sum \\(V=U\\oplus W\\) requires \\(U\\cap W=\\{0\\}\\) and \\(U+W=V\\), giving \\(\\dim V=\\dim U+\\dim W\\).",
    "Infinite-dimensional spaces arise in functional analysis: \\(L^2[0,1]\\) (square-integrable functions) has a countably infinite orthonormal basis (Fourier series). Hilbert spaces generalize finite-dimensional inner product spaces to infinite dimensions, preserving most geometric intuition.",
    "Dimension is a topological invariant: homeomorphic spaces have the same topological dimension. The Brouwer invariance of domain theorem proves that \\(\\mathbb{R}^m\\) and \\(\\mathbb{R}^n\\) are not homeomorphic for \\(m\\neq n\\), confirming that dimension is well-defined topologically."
))]

EXTRA3["linear-algebra/least-squares"] = [sec("indepth","In Depth", p(
    "The least-squares problem minimizes \\(\\|A\\mathbf{x}-\\mathbf{b}\\|^2\\) over all \\(\\mathbf{x}\\). When \\(A\\mathbf{x}=\\mathbf{b}\\) is overdetermined (more equations than unknowns), the least-squares solution \\(\\hat{\\mathbf{x}}=(A^TA)^{-1}A^T\\mathbf{b}\\) minimizes the sum of squared residuals.",
    "The normal equations \\(A^TA\\hat{\\mathbf{x}}=A^T\\mathbf{b}\\) characterize the least-squares solution. Geometrically, \\(A\\hat{\\mathbf{x}}\\) is the orthogonal projection of \\(\\mathbf{b}\\) onto the column space of \\(A\\). The residual \\(\\mathbf{b}-A\\hat{\\mathbf{x}}\\) is orthogonal to every column of \\(A\\).",
    "When \\(A^TA\\) is ill-conditioned, direct solution of the normal equations is numerically unstable. The QR decomposition \\(A=QR\\) gives a stable algorithm: \\(\\hat{\\mathbf{x}}=R^{-1}Q^T\\mathbf{b}\\). The SVD-based pseudoinverse \\(A^+=V\\Sigma^+U^T\\) handles rank-deficient cases.",
    "Regularization adds a penalty term: ridge regression minimizes \\(\\|A\\mathbf{x}-\\mathbf{b}\\|^2+\\lambda\\|\\mathbf{x}\\|^2\\), giving \\(\\hat{\\mathbf{x}}=(A^TA+\\lambda I)^{-1}A^T\\mathbf{b}\\). This shrinks coefficients toward zero and stabilizes ill-conditioned problems. LASSO uses an \\(\\ell^1\\) penalty, promoting sparsity.",
    "Least squares is the foundation of linear regression in statistics, curve fitting in engineering, and parameter estimation in science. The Gauss–Markov theorem states that the least-squares estimator is the best linear unbiased estimator (BLUE) when errors are uncorrelated with equal variance."
))]

EXTRA3["linear-algebra/eigenvector"] = [sec("indepth","In Depth", p(
    "An eigenvector of a matrix \\(A\\) is a nonzero vector \\(\\mathbf{v}\\) satisfying \\(A\\mathbf{v}=\\lambda\\mathbf{v}\\) for some scalar \\(\\lambda\\) (the eigenvalue). Eigenvectors point in directions that are only scaled, not rotated, by \\(A\\). They reveal the intrinsic geometry of the linear transformation.",
    "Eigenvalues are roots of the characteristic polynomial \\(\\det(A-\\lambda I)=0\\). An \\(n\\times n\\) matrix has \\(n\\) eigenvalues (counting multiplicity) over \\(\\mathbb{C}\\). The trace equals the sum of eigenvalues; the determinant equals their product.",
    "The eigenspace for eigenvalue \\(\\lambda\\) is \\(\\ker(A-\\lambda I)\\), the null space of \\(A-\\lambda I\\). Its dimension (geometric multiplicity) may be less than the algebraic multiplicity (multiplicity as a root of the characteristic polynomial). When they are equal for all eigenvalues, \\(A\\) is diagonalizable.",
    "Symmetric matrices (\\(A=A^T\\)) have real eigenvalues and orthogonal eigenvectors (spectral theorem). This makes them especially well-behaved: they are always diagonalizable as \\(A=Q\\Lambda Q^T\\) with orthogonal \\(Q\\). Positive definite matrices have all positive eigenvalues.",
    "Power iteration finds the dominant eigenvector by repeatedly multiplying by \\(A\\) and normalizing. The QR algorithm computes all eigenvalues efficiently. In data science, PCA finds the eigenvectors of the covariance matrix; Google's PageRank is the dominant eigenvector of the web's link matrix."
))]

EXTRA3["linear-algebra/inner-product"] = [sec("indepth","In Depth", p(
    "An inner product on a vector space \\(V\\) over \\(\\mathbb{R}\\) (or \\(\\mathbb{C}\\)) is a map \\(\\langle\\cdot,\\cdot\\rangle:V\\times V\\to\\mathbb{R}\\) satisfying linearity in the first argument, symmetry (\\(\\langle u,v\\rangle=\\langle v,u\\rangle\\)), and positive definiteness (\\(\\langle v,v\\rangle>0\\) for \\(v\\neq0\\)). It generalizes the dot product.",
    "The standard inner product on \\(\\mathbb{R}^n\\) is \\(\\langle\\mathbf{u},\\mathbf{v}\\rangle=\\mathbf{u}^T\\mathbf{v}=\\sum u_iv_i\\). On \\(L^2[a,b]\\): \\(\\langle f,g\\rangle=\\int_a^b f(x)g(x)\\,dx\\). The induced norm is \\(\\|v\\|=\\sqrt{\\langle v,v\\rangle}\\).",
    "The Cauchy–Schwarz inequality: \\(|\\langle u,v\\rangle|\\leq\\|u\\|\\|v\\|\\), with equality iff \\(u\\) and \\(v\\) are proportional. This implies the triangle inequality \\(\\|u+v\\|\\leq\\|u\\|+\\|v\\|\\) and is one of the most widely used inequalities in mathematics.",
    "The angle between vectors: \\(\\cos\\theta=\\langle u,v\\rangle/(\\|u\\|\\|v\\|)\\). Vectors are orthogonal iff \\(\\langle u,v\\rangle=0\\). The Gram–Schmidt process converts any basis to an orthonormal one by successive orthogonalization and normalization.",
    "Inner product spaces (Hilbert spaces when complete) are the natural setting for quantum mechanics (states are unit vectors, observables are self-adjoint operators), signal processing (Fourier analysis uses the \\(L^2\\) inner product), and machine learning (kernel methods implicitly compute inner products in high-dimensional feature spaces)."
))]

EXTRA3["linear-algebra/orthogonality"] = [sec("indepth","In Depth", p(
    "Two vectors are orthogonal if their inner product is zero. A set of vectors is orthogonal if every pair is orthogonal; orthonormal if additionally each vector has unit norm. Orthonormal bases simplify computations enormously: coordinates are inner products, and the matrix of an orthonormal basis is orthogonal (\\(Q^TQ=I\\)).",
    "The orthogonal complement of a subspace \\(W\\) is \\(W^\\perp=\\{v:\\langle v,w\\rangle=0\\text{ for all }w\\in W\\}\\). Every vector decomposes uniquely as \\(v=w+w^\\perp\\) with \\(w\\in W\\) and \\(w^\\perp\\in W^\\perp\\). This orthogonal decomposition is the basis of projection and least squares.",
    "Orthogonal matrices (\\(Q^TQ=QQ^T=I\\)) preserve lengths and angles: \\(\\|Q\\mathbf{v}\\|=\\|\\mathbf{v}\\|\\) and \\(\\langle Q\\mathbf{u},Q\\mathbf{v}\\rangle=\\langle\\mathbf{u},\\mathbf{v}\\rangle\\). They represent rotations and reflections. Their eigenvalues lie on the unit circle in \\(\\mathbb{C}\\).",
    "The QR decomposition \\(A=QR\\) (\\(Q\\) orthogonal, \\(R\\) upper triangular) is computed by Gram–Schmidt or Householder reflections. It is numerically stable and used for solving least-squares problems, computing eigenvalues (QR algorithm), and solving linear systems.",
    "Fourier series express a function as an infinite sum of orthogonal sinusoids: \\(f(x)=\\sum_{n=-\\infty}^\\infty c_n e^{inx}\\) where \\(c_n=\\frac{1}{2\\pi}\\int_{-\\pi}^\\pi f(x)e^{-inx}dx\\). The exponentials \\(e^{inx}\\) form an orthonormal basis of \\(L^2[-\\pi,\\pi]\\), making Fourier analysis a special case of orthogonal decomposition."
))]

EXTRA3["linear-algebra/lu-decomposition"] = [sec("indepth","In Depth", p(
    "LU decomposition factors a matrix as \\(A=LU\\) where \\(L\\) is lower triangular (with 1s on the diagonal) and \\(U\\) is upper triangular. It is essentially Gaussian elimination recorded in matrix form. Solving \\(A\\mathbf{x}=\\mathbf{b}\\) reduces to two triangular solves: \\(L\\mathbf{y}=\\mathbf{b}\\) then \\(U\\mathbf{x}=\\mathbf{y}\\).",
    "Partial pivoting (PA=LU) permutes rows to place the largest element in the pivot position, improving numerical stability. Complete pivoting (PAQ=LU) also permutes columns. In practice, partial pivoting is almost always sufficient and is the default in LAPACK and NumPy.",
    "LU decomposition costs \\(O(n^3/3)\\) flops — the same as Gaussian elimination. Once computed, each solve costs only \\(O(n^2)\\). This makes LU ideal when solving \\(A\\mathbf{x}=\\mathbf{b}\\) for many right-hand sides \\(\\mathbf{b}\\) with the same \\(A\\).",
    "The Cholesky decomposition \\(A=LL^T\\) applies when \\(A\\) is symmetric positive definite. It is twice as fast as LU and numerically more stable. It is used in statistics (sampling from multivariate normals), optimization (Newton's method), and finite element analysis.",
    "Block LU decomposition handles structured matrices efficiently. The Schur complement \\(S=D-CA^{-1}B\\) appears in the block factorization of \\([[A,B],[C,D]]\\) and is fundamental in control theory, statistics (conditional distributions), and the analysis of bordered systems."
))]

EXTRA3["linear-algebra/vectors-in-rn"] = [sec("indepth","In Depth", p(
    "Vectors in \\(\\mathbb{R}^n\\) are ordered \\(n\\)-tuples of real numbers. They support addition (componentwise) and scalar multiplication, making \\(\\mathbb{R}^n\\) a vector space. The standard basis vectors \\(\\mathbf{e}_1,\\ldots,\\mathbf{e}_n\\) (with a 1 in position \\(i\\) and 0s elsewhere) span \\(\\mathbb{R}^n\\).",
    "The Euclidean norm \\(\\|\\mathbf{v}\\|=\\sqrt{\\sum v_i^2}\\) measures length. The dot product \\(\\mathbf{u}\\cdot\\mathbf{v}=\\sum u_iv_i=\\|\\mathbf{u}\\|\\|\\mathbf{v}\\|\\cos\\theta\\) encodes both length and angle. The cross product in \\(\\mathbb{R}^3\\) gives a vector perpendicular to both inputs with magnitude equal to the parallelogram area.",
    "Linear combinations \\(c_1\\mathbf{v}_1+\\cdots+c_k\\mathbf{v}_k\\) and their spans are the building blocks of linear algebra. A set of vectors is linearly independent if no vector is a linear combination of the others — equivalently, \\(\\sum c_i\\mathbf{v}_i=\\mathbf{0}\\) implies all \\(c_i=0\\).",
    "Projections: the projection of \\(\\mathbf{b}\\) onto \\(\\mathbf{a}\\) is \\(\\text{proj}_{\\mathbf{a}}\\mathbf{b}=(\\mathbf{a}\\cdot\\mathbf{b}/\\|\\mathbf{a}\\|^2)\\mathbf{a}\\). The projection onto a subspace spanned by columns of \\(A\\) is \\(P=A(A^TA)^{-1}A^T\\). Projections satisfy \\(P^2=P\\) (idempotent) and \\(P^T=P\\) (symmetric).",
    "In machine learning, data points are vectors in \\(\\mathbb{R}^n\\) (feature vectors). Distance metrics (Euclidean, cosine similarity) measure similarity. Dimensionality reduction (PCA, t-SNE) projects high-dimensional vectors to lower-dimensional spaces while preserving structure."
))]

EXTRA3["linear-algebra/rank"] = [sec("indepth","In Depth", p(
    "The rank of a matrix \\(A\\) is the dimension of its column space (equivalently, row space). It equals the number of pivots in the row echelon form. The rank-nullity theorem: \\(\\text{rank}(A)+\\text{nullity}(A)=n\\) (number of columns). Row rank equals column rank — a non-obvious fact.",
    "A matrix has full column rank if its columns are linearly independent (rank = number of columns); full row rank if its rows are linearly independent (rank = number of rows). A square matrix is invertible iff it has full rank iff its determinant is nonzero.",
    "Rank and linear systems: \\(A\\mathbf{x}=\\mathbf{b}\\) is consistent iff \\(\\text{rank}(A)=\\text{rank}([A|\\mathbf{b}])\\). If consistent, the solution is unique iff \\(A\\) has full column rank; otherwise there are infinitely many solutions parameterized by the null space.",
    "The rank of a product: \\(\\text{rank}(AB)\\leq\\min(\\text{rank}(A),\\text{rank}(B))\\). Multiplying by an invertible matrix preserves rank. The rank of \\(A+B\\) satisfies \\(|\\text{rank}(A)-\\text{rank}(B)|\\leq\\text{rank}(A+B)\\leq\\text{rank}(A)+\\text{rank}(B)\\).",
    "Low-rank approximation: the best rank-\\(k\\) approximation to \\(A\\) (in Frobenius or spectral norm) is given by the truncated SVD \\(A_k=\\sum_{i=1}^k\\sigma_i\\mathbf{u}_i\\mathbf{v}_i^T\\). This is the mathematical basis of image compression, collaborative filtering, and latent semantic analysis."
))]

EXTRA3["linear-algebra/linear-systems"] = [sec("indepth","In Depth", p(
    "A linear system \\(A\\mathbf{x}=\\mathbf{b}\\) has three possible outcomes: no solution (inconsistent), exactly one solution (unique), or infinitely many solutions. The augmented matrix \\([A|\\mathbf{b}]\\) row-reduced to echelon form reveals which case applies and gives the solution(s).",
    "Gaussian elimination transforms \\(A\\) to upper triangular form using row operations (swap, scale, add multiple of one row to another). Back substitution then solves the triangular system. With partial pivoting, this is numerically stable and costs \\(O(n^3/3)\\) flops.",
    "Cramer's rule expresses each solution component as a ratio of determinants: \\(x_i=\\det(A_i)/\\det(A)\\) where \\(A_i\\) replaces column \\(i\\) of \\(A\\) with \\(\\mathbf{b}\\). While theoretically elegant, it is computationally impractical for large systems (\\(O(n!)\\) vs \\(O(n^3)\\) for Gaussian elimination).",
    "Iterative methods (Jacobi, Gauss–Seidel, conjugate gradient) solve large sparse systems without forming \\(A^{-1}\\). The conjugate gradient method solves symmetric positive definite systems in at most \\(n\\) steps and converges faster when eigenvalues are clustered. Preconditioning improves convergence.",
    "Condition number \\(\\kappa(A)=\\|A\\|\\|A^{-1}\\|\\) measures sensitivity: a relative perturbation \\(\\delta\\mathbf{b}/\\|\\mathbf{b}\\|\\) in the right-hand side causes a relative error \\(\\leq\\kappa(A)\\cdot\\delta\\mathbf{b}/\\|\\mathbf{b}\\|\\) in the solution. Ill-conditioned systems (large \\(\\kappa\\)) require careful numerical treatment."
))]

EXTRA3["linear-algebra/qr-decomposition"] = [sec("indepth","In Depth", p(
    "The QR decomposition factors \\(A\\) (\\(m\\times n\\), \\(m\\geq n\\)) as \\(A=QR\\) where \\(Q\\) is \\(m\\times m\\) orthogonal and \\(R\\) is \\(m\\times n\\) upper triangular. The 'thin' QR has \\(Q\\) as \\(m\\times n\\) with orthonormal columns and \\(R\\) as \\(n\\times n\\) upper triangular.",
    "Gram–Schmidt orthogonalization computes QR by successively orthogonalizing columns of \\(A\\). Modified Gram–Schmidt is numerically more stable. Householder reflections and Givens rotations are the preferred numerical methods, achieving backward stability.",
    "Least squares via QR: \\(\\min\\|A\\mathbf{x}-\\mathbf{b}\\|\\) reduces to \\(\\min\\|R\\mathbf{x}-Q^T\\mathbf{b}\\|\\), solved by back substitution on the upper triangular system \\(R\\mathbf{x}=Q^T\\mathbf{b}\\). This avoids forming \\(A^TA\\) (which squares the condition number) and is the standard approach in practice.",
    "The QR algorithm for eigenvalues iterates \\(A_k=Q_kR_k\\), \\(A_{k+1}=R_kQ_k\\). Each step is an orthogonal similarity transformation, preserving eigenvalues. With shifts, it converges cubically and is the standard algorithm for dense eigenvalue problems (used in LAPACK's \\texttt{dgeev}).",
    "QR decomposition is used in signal processing (QR-based adaptive filters), statistics (orthogonal regression), and numerical linear algebra (computing pseudoinverses, solving constrained least-squares problems). Its stability makes it preferable to normal equations in almost all practical applications."
))]

EXTRA3["linear-algebra/subspace"] = [sec("indepth","In Depth", p(
    "A subspace of a vector space \\(V\\) is a subset \\(W\\subseteq V\\) that is itself a vector space: it contains \\(\\mathbf{0}\\), is closed under addition, and closed under scalar multiplication. Equivalently, \\(W\\) is closed under linear combinations.",
    "The four fundamental subspaces of an \\(m\\times n\\) matrix \\(A\\): column space \\(\\text{Col}(A)\\subseteq\\mathbb{R}^m\\), null space \\(\\text{Null}(A)\\subseteq\\mathbb{R}^n\\), row space \\(\\text{Row}(A)\\subseteq\\mathbb{R}^n\\), left null space \\(\\text{Null}(A^T)\\subseteq\\mathbb{R}^m\\). The column space and null space of \\(A^T\\) are orthogonal complements in \\(\\mathbb{R}^m\\).",
    "The span of a set \\(S\\) is the smallest subspace containing \\(S\\) — all linear combinations of elements of \\(S\\). The intersection of subspaces is a subspace; the union generally is not. The sum \\(U+W=\\{u+w:u\\in U,w\\in W\\}\\) is the smallest subspace containing both.",
    "Affine subspaces (cosets) are translates of subspaces: \\(\\mathbf{x}_0+W=\\{\\mathbf{x}_0+w:w\\in W\\}\\). The solution set of \\(A\\mathbf{x}=\\mathbf{b}\\) (when consistent) is an affine subspace: a particular solution plus the null space.",
    "In abstract algebra, subspaces generalize to submodules (over rings) and ideals (in rings). In functional analysis, closed subspaces of Hilbert spaces are the natural setting for projection theorems and spectral theory. Every closed subspace of a Hilbert space has an orthogonal complement."
))]

EXTRA3["linear-algebra/basis"] = [sec("indepth","In Depth", p(
    "A basis of a vector space \\(V\\) is a linearly independent set that spans \\(V\\). Every vector in \\(V\\) has a unique representation as a linear combination of basis vectors. The number of basis vectors is the dimension of \\(V\\), which is the same for all bases (the dimension theorem).",
    "The standard basis of \\(\\mathbb{R}^n\\) is \\(\\{\\mathbf{e}_1,\\ldots,\\mathbf{e}_n\\}\\). Other useful bases: eigenvector bases (diagonalize linear maps), orthonormal bases (simplify inner products), and wavelet bases (localize in both time and frequency). The choice of basis affects computational efficiency.",
    "Change of basis: if \\(B=\\{\\mathbf{b}_1,\\ldots,\\mathbf{b}_n\\}\\) is a basis, the change-of-basis matrix \\(P=[\\mathbf{b}_1|\\cdots|\\mathbf{b}_n]\\) converts coordinates: \\([\\mathbf{v}]_{\\text{std}}=P[\\mathbf{v}]_B\\). A linear map \\(T\\) has matrix \\(P^{-1}AP\\) in basis \\(B\\) if it has matrix \\(A\\) in the standard basis.",
    "Ordered bases and coordinates: fixing an ordered basis \\(B\\) gives an isomorphism \\(V\\cong\\mathbb{R}^n\\) via coordinate vectors. This is why abstract vector spaces can be studied concretely using matrices — every finite-dimensional vector space over \\(\\mathbb{R}\\) is isomorphic to \\(\\mathbb{R}^n\\) for some \\(n\\).",
    "In numerical analysis, the choice of basis affects conditioning. Monomial bases for polynomials are ill-conditioned; Chebyshev bases are much better. In signal processing, the Fourier basis diagonalizes convolution operators, making frequency-domain analysis efficient via the FFT."
))]

# ── STATISTICS HUB ────────────────────────────────────────────────────────────
EXTRA3["statistics"] = [sec("indepth","In Depth", p(
    "Statistics is the science of collecting, analyzing, interpreting, and presenting data. It divides into descriptive statistics (summarizing data with measures of center, spread, and shape) and inferential statistics (drawing conclusions about populations from samples using probability theory).",
    "The central objects of statistics are random variables and their distributions. A random variable \\(X\\) assigns a numerical value to each outcome of a random experiment. Its distribution is characterized by the probability mass function (discrete) or probability density function (continuous), along with summary statistics: mean \\(\\mu=E[X]\\), variance \\(\\sigma^2=E[(X-\\mu)^2]\\), and higher moments.",
    "Estimation theory asks: given a sample \\(X_1,\\ldots,X_n\\) from a distribution with unknown parameter \\(\\theta\\), how do we estimate \\(\\theta\\)? Maximum likelihood estimation (MLE) chooses \\(\\hat\\theta\\) to maximize the likelihood \\(L(\\theta)=\\prod f(X_i;\\theta)\\). Under regularity conditions, MLE is consistent, asymptotically normal, and efficient (achieves the Cramér–Rao lower bound).",
    "Hypothesis testing formalizes decision-making under uncertainty. A null hypothesis \\(H_0\\) is tested against an alternative \\(H_1\\). The p-value is the probability of observing data at least as extreme as the sample, assuming \\(H_0\\). A small p-value (typically \\(<0.05\\)) is evidence against \\(H_0\\). The significance level \\(\\alpha\\) controls the Type I error rate.",
    "Modern statistics increasingly uses computational methods: bootstrap resampling estimates sampling distributions without parametric assumptions; Markov chain Monte Carlo (MCMC) samples from complex posterior distributions in Bayesian analysis; cross-validation estimates predictive performance. These methods extend classical statistics to high-dimensional and complex data settings."
))]
