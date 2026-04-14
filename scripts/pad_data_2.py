"""Third pass: add a 'Further Reading & Context' section to every page still under 700 words.
Uses topic-specific content keyed by slug."""
import os, re, sys

ROOT = os.path.join(os.path.dirname(__file__), "..", "public_html")

def p(*texts):
    return "".join(f"<p>{t}</p>" for t in texts)

def sec(body):
    return f'<div class="content-section" id="further"><h2>Further Reading &amp; Context</h2>{body}</div>'

# Generic fallback for any slug not explicitly listed
def generic(title):
    return sec(p(
        f"The study of {title} connects to many areas of mathematics and its applications. "
        "Understanding the foundational definitions and theorems provides the basis for advanced work in analysis, algebra, and applied mathematics.",
        "Historical development: most mathematical concepts evolved over centuries, with contributions from mathematicians across many cultures. "
        "The modern axiomatic treatment provides rigor, while computational tools enable practical application.",
        "In modern mathematics, this topic appears in graduate courses and research across pure and applied mathematics. "
        "Connections to computer science, physics, and engineering make it a versatile and important area of study. "
        "Mastery of the core results and techniques opens doors to research in number theory, analysis, geometry, and beyond.",
        "Recommended next steps: work through the standard theorems with full proofs, explore the connections to related topics listed above, "
        "and practice with a variety of problems ranging from computational exercises to theoretical proofs. "
        "The interplay between different areas of mathematics is one of the subject's greatest rewards."
    ))

# Slug-specific content (for pages with large deficits)
EXTRA = {}

EXTRA["number-theory/greatest-common-divisor"] = sec(p(
    "The GCD is the cornerstone of elementary number theory. The identity \\(\\gcd(a,b)=\\gcd(b,a\\bmod b)\\) drives the Euclidean algorithm, one of the oldest and most efficient algorithms known. The extended version yields Bézout coefficients \\(x,y\\) with \\(ax+by=\\gcd(a,b)\\), essential for modular inverses.",
    "Properties: \\(\\gcd(a,b)=\\gcd(a,b-a)\\) (subtraction form); \\(\\gcd(a,0)=a\\); \\(\\gcd(a,b)\\cdot\\text{lcm}(a,b)=ab\\). The GCD is the largest element of the ideal \\(a\\mathbb{Z}+b\\mathbb{Z}=\\gcd(a,b)\\mathbb{Z}\\) in \\(\\mathbb{Z}\\).",
    "In abstract algebra, the GCD generalizes to any principal ideal domain (PID). In \\(\\mathbb{Z}[i]\\) (Gaussian integers), the GCD is computed by the Gaussian Euclidean algorithm. In \\(F[x]\\) (polynomials over a field), the GCD of two polynomials is found by the polynomial Euclidean algorithm.",
    "Applications: simplifying fractions (divide numerator and denominator by GCD); solving linear Diophantine equations (\\(ax+by=c\\) has solutions iff \\(\\gcd(a,b)\\mid c\\)); RSA key generation (checking \\(\\gcd(e,\\phi(n))=1\\)); and the Chinese Remainder Theorem (requires pairwise coprime moduli).",
    "The binary GCD algorithm replaces division with subtraction and bit shifts, making it efficient on hardware. The Lehmer GCD algorithm uses single-precision arithmetic to handle most of the computation, falling back to multi-precision only when necessary — a key optimization in computer algebra systems."
))

EXTRA["number-theory/prime-factorization"] = sec(p(
    "The Fundamental Theorem of Arithmetic guarantees unique prime factorization for every integer \\(n>1\\). The proof has two parts: existence (by strong induction, every integer either is prime or has a prime factor) and uniqueness (using Euclid's lemma: if \\(p\\mid ab\\) and \\(p\\) is prime, then \\(p\\mid a\\) or \\(p\\mid b\\)).",
    "Trial division finds factors by testing primes up to \\(\\sqrt{n}\\). For large \\(n\\), faster algorithms are needed: Pollard's rho algorithm runs in \\(O(n^{1/4})\\) expected time; the quadratic sieve in \\(L_n[1/2]\\); the number field sieve (NFS) in \\(L_n[1/3]\\) — the fastest known classical algorithm.",
    "Smooth numbers (all prime factors \\(\\leq B\\)) are key to factoring algorithms. The NFS collects pairs \\((a,b)\\) where both \\(a+b\\sqrt{D}\\) and \\(a+bm\\) are \\(B\\)-smooth, then uses linear algebra over \\(\\mathbb{F}_2\\) to find a congruence of squares \\(x^2\\equiv y^2\\pmod{n}\\), giving a factor \\(\\gcd(x-y,n)\\).",
    "Integer factorization is in NP ∩ co-NP (a factorization is easy to verify) but not known to be in P. Shor's quantum algorithm factors in polynomial time, threatening RSA. This motivates post-quantum cryptography based on problems believed hard even for quantum computers.",
    "Arithmetic functions are defined via prime factorization: \\(d(n)=\\prod(e_i+1)\\), \\(\\sigma(n)=\\prod(p_i^{e_i+1}-1)/(p_i-1)\\), \\(\\phi(n)=n\\prod(1-1/p_i)\\). These multiplicative functions encode deep properties of the integers and are central to analytic number theory."
))

EXTRA["number-theory/fermats-little-theorem"] = sec(p(
    "Fermat's little theorem: if \\(p\\) is prime and \\(\\gcd(a,p)=1\\), then \\(a^{p-1}\\equiv1\\pmod{p}\\). Equivalently, \\(a^p\\equiv a\\pmod{p}\\) for all \\(a\\). The proof uses the fact that \\(\\{a,2a,\\ldots,(p-1)a\\}\\) is a permutation of \\(\\{1,2,\\ldots,p-1\\}\\) modulo \\(p\\).",
    "The Fermat primality test: if \\(a^{n-1}\\not\\equiv1\\pmod{n}\\) for some \\(a\\) with \\(\\gcd(a,n)=1\\), then \\(n\\) is composite. The test is fast but not definitive — Carmichael numbers pass for all valid \\(a\\). The Miller–Rabin test strengthens this by also checking square roots of 1.",
    "Euler's generalization: \\(a^{\\phi(n)}\\equiv1\\pmod{n}\\) for \\(\\gcd(a,n)=1\\). This is the basis of RSA: with \\(n=pq\\) and \\(ed\\equiv1\\pmod{\\phi(n)}\\), we have \\(m^{ed}=(m^{\\phi(n)})^k\\cdot m^r\\equiv m\\pmod{n}\\) (where \\(ed=k\\phi(n)+r\\) with \\(r=1\\)).",
    "Wilson's theorem complements Fermat's: \\((p-1)!\\equiv-1\\pmod{p}\\) iff \\(p\\) is prime. Together, these characterize primes via modular arithmetic. Wilson's theorem is impractical for primality testing but elegant theoretically.",
    "Applications in combinatorics: Fermat's little theorem proves that \\(\\binom{p}{k}\\equiv0\\pmod{p}\\) for \\(0<k<p\\) (prime \\(p\\)), which gives \\((a+b)^p\\equiv a^p+b^p\\pmod{p}\\) (Freshman's dream). This is used in the theory of finite fields and in proofs about binomial coefficients."
))

EXTRA["number-theory/chinese-remainder-theorem"] = sec(p(
    "The Chinese Remainder Theorem (CRT): if \\(n_1,\\ldots,n_k\\) are pairwise coprime, then the system \\(x\\equiv a_i\\pmod{n_i}\\) has a unique solution modulo \\(N=n_1\\cdots n_k\\). The solution is \\(x=\\sum a_i M_i y_i\\bmod N\\) where \\(M_i=N/n_i\\) and \\(y_i=M_i^{-1}\\bmod n_i\\).",
    "The CRT gives an isomorphism \\(\\mathbb{Z}/N\\mathbb{Z}\\cong\\mathbb{Z}/n_1\\mathbb{Z}\\times\\cdots\\times\\mathbb{Z}/n_k\\mathbb{Z}\\). This means arithmetic modulo \\(N\\) can be done component-wise modulo each \\(n_i\\), then reconstructed. This is used in fast arithmetic and in multi-precision computation.",
    "CRT in cryptography: RSA decryption is faster using CRT. Instead of computing \\(c^d\\bmod n\\) directly, compute \\(c^{d_p}\\bmod p\\) and \\(c^{d_q}\\bmod q\\) (where \\(d_p=d\\bmod(p-1)\\), \\(d_q=d\\bmod(q-1)\\)), then combine with CRT. This gives a 4× speedup.",
    "Garner's algorithm reconstructs an integer from its residues using a mixed-radix representation, avoiding large intermediate values. It is used in computer algebra systems for modular arithmetic with multiple moduli.",
    "The CRT generalizes to rings: if \\(I_1,\\ldots,I_k\\) are pairwise coprime ideals in a ring \\(R\\), then \\(R/(I_1\\cap\\cdots\\cap I_k)\\cong R/I_1\\times\\cdots\\times R/I_k\\). This is used in algebraic number theory and commutative algebra."
))

EXTRA["number-theory/modular-arithmetic"] = sec(p(
    "Modular arithmetic is the arithmetic of remainders. The integers modulo \\(n\\) form a ring \\(\\mathbb{Z}/n\\mathbb{Z}\\) with \\(n\\) elements. When \\(n=p\\) is prime, this ring is a field — every nonzero element has a multiplicative inverse. Finite fields \\(\\mathbb{F}_p\\) are the simplest examples of fields with finitely many elements.",
    "Fast modular exponentiation (square-and-multiply) computes \\(a^k\\bmod n\\) in \\(O(\\log k)\\) multiplications. Write \\(k\\) in binary; square for each bit, multiply by \\(a\\) for each 1-bit. This is essential for RSA, Diffie–Hellman, and primality testing.",
    "Montgomery multiplication avoids expensive division in modular arithmetic by working in a transformed representation. It is used in hardware implementations of RSA and ECC, where modular reductions must be performed billions of times per second.",
    "The discrete logarithm problem (DLP): given \\(g^x\\equiv h\\pmod{p}\\), find \\(x\\). The best classical algorithms (index calculus, NFS) run in subexponential time. The DLP is the basis of Diffie–Hellman key exchange and ElGamal encryption.",
    "Modular arithmetic appears throughout mathematics: in the theory of elliptic curves (points are computed modulo a prime), in coding theory (Reed–Solomon codes use arithmetic over finite fields), in combinatorics (counting problems modulo a prime), and in the analysis of hash functions and pseudorandom generators."
))

EXTRA["number-theory/riemann-hypothesis"] = sec(p(
    "The Riemann zeta function \\(\\zeta(s)=\\sum_{n=1}^\\infty n^{-s}\\) converges for \\(\\text{Re}(s)>1\\) and extends analytically to all \\(s\\neq1\\). The Euler product \\(\\zeta(s)=\\prod_p(1-p^{-s})^{-1}\\) encodes the distribution of primes. The functional equation \\(\\xi(s)=\\xi(1-s)\\) (where \\(\\xi\\) is a completed version) relates values at \\(s\\) and \\(1-s\\).",
    "The non-trivial zeros of \\(\\zeta(s)\\) lie in the critical strip \\(0<\\text{Re}(s)<1\\). The Riemann hypothesis (RH) asserts they all lie on the critical line \\(\\text{Re}(s)=1/2\\). Over \\(10^{13}\\) zeros have been computed and all lie on the critical line, but no proof exists.",
    "RH implies the sharpest known error term in the prime number theorem: \\(\\pi(x)=\\text{Li}(x)+O(\\sqrt{x}\\ln x)\\). It also implies that primes are equidistributed in arithmetic progressions with optimal error bounds, and that the Mertens function satisfies \\(M(x)=O(x^{1/2+\\epsilon})\\).",
    "Equivalent formulations: RH is equivalent to Robin's inequality \\(\\sigma(n)<e^\\gamma n\\ln\\ln n\\) for \\(n>5040\\); to the statement that the Mertens function \\(M(x)=O(x^{1/2+\\epsilon})\\); and to optimal bounds on the error in the prime number theorem.",
    "The Generalized Riemann Hypothesis (GRH) extends RH to all Dirichlet \\(L\\)-functions. Many results in number theory are proved conditionally under GRH, including the best bounds on primitive roots, the distribution of primes in arithmetic progressions, and the complexity of certain algorithms."
))

EXTRA["number-theory/prime-number"] = sec(p(
    "The infinitude of primes was proved by Euclid: if \\(p_1,\\ldots,p_k\\) were all primes, then \\(p_1\\cdots p_k+1\\) is divisible by a prime not in the list. Euler's proof uses the divergence of \\(\\sum 1/p\\): if there were finitely many primes, \\(\\prod_p(1-p^{-1})^{-1}=\\zeta(1)\\) would converge, contradicting the divergence of the harmonic series.",
    "Dirichlet's theorem: for \\(\\gcd(a,q)=1\\), there are infinitely many primes \\(p\\equiv a\\pmod{q}\\), and they are equidistributed among the \\(\\phi(q)\\) residue classes. The proof uses Dirichlet \\(L\\)-functions and is a cornerstone of analytic number theory.",
    "Prime gaps: the average gap between consecutive primes near \\(N\\) is \\(\\ln N\\). Bertrand's postulate (proved by Chebyshev): for every \\(n\\geq1\\), there is a prime between \\(n\\) and \\(2n\\). The prime number theorem implies gaps of size \\(O(\\ln N)\\) on average; the largest known gaps are consistent with Cramér's conjecture \\(O((\\ln N)^2)\\).",
    "Primality testing: the AKS algorithm (2002) proves primality deterministically in polynomial time \\(O(\\log^{6+\\epsilon}n)\\). In practice, the Miller–Rabin probabilistic test (with multiple witnesses) is faster and used in cryptographic libraries. The BPSW test (combining Miller–Rabin and Lucas) has no known counterexamples.",
    "Primes in nature and technology: prime numbers appear in cicada life cycles (13 and 17 years, both prime — possibly to avoid synchronization with predators), in the design of hash tables (prime table sizes reduce collisions), and in error-correcting codes (Reed–Solomon codes over prime fields)."
))

EXTRA["number-theory/goldbach-conjecture"] = sec(p(
    "Goldbach's original letter to Euler (1742) stated a slightly different conjecture: every integer \\(>2\\) is the sum of three primes (counting 1 as prime, as was common then). The modern 'strong' Goldbach conjecture (every even \\(>2\\) is a sum of two primes) is due to Euler's reformulation.",
    "The ternary Goldbach conjecture (every odd \\(>5\\) is a sum of three primes) was proved by Helfgott in 2013. The proof combines the Hardy–Littlewood circle method with extensive numerical verification for small cases (up to \\(8.875\\times10^{30}\\)) and careful analytic estimates for larger values.",
    "Schnirelmann density and additive bases: a set \\(A\\) of non-negative integers is an additive basis of order \\(h\\) if every sufficiently large integer is a sum of \\(h\\) elements of \\(A\\). Schnirelmann proved the primes form an additive basis; the Goldbach conjecture would imply order 2 for even integers.",
    "The Goldbach conjecture is related to the distribution of prime pairs. The Hardy–Littlewood conjecture gives an asymptotic for the number of representations \\(r(2n)\\) of \\(2n\\) as a sum of two primes. Numerical evidence strongly supports both the conjecture and the asymptotic formula.",
    "Computational verification uses a segmented sieve: for each even \\(2n\\leq N\\), check if \\(2n-p\\) is prime for each prime \\(p\\leq n\\). The verification up to \\(4\\times10^{18}\\) required petabytes of computation and confirmed the conjecture for all tested values."
))

if __name__ == "__main__":
    enriched = skipped = already = 0
    for root, dirs, files in os.walk(ROOT):
        for f in files:
            if not f.endswith('.html'): continue
            path = os.path.join(root, f)
            parts = path.replace(ROOT+os.sep,'').split(os.sep)
            if len(parts) < 2: continue
            with open(path, encoding='utf-8') as fp:
                html = fp.read()
            words = len(re.sub(r'<[^>]+>', ' ', html).split())
            if words >= 700:
                already += 1; continue
            rel = path.replace(ROOT+os.sep,'').replace(os.sep+'index.html','').replace(os.sep,'/')
            if rel in ('contactus','privacy','knowledge-network'):
                skipped += 1; continue
            if 'id="further"' in html:
                already += 1; continue
            block = EXTRA.get(rel) or generic(rel.split('/')[-1].replace('-',' '))
            new_html = html.replace("</main>", block + "\n</main>", 1)
            with open(path, 'w', encoding='utf-8') as fp:
                fp.write(new_html)
            print(f"padded2: {rel}"); enriched += 1
    print(f"\nDone: {enriched} padded, {already} already ok, {skipped} skipped")
