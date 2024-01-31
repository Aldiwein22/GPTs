# Formelsammlung

- **Gaussche Summenformel**:
  $$ \Delta_n = \sum_{i=1}^{n} i = \frac{n(n+1)}{2} $$

- **Binomialkoeffizient**:
  $$ {n\choose k} = \frac{n!}{k!(n-k)!} $$

- **Binomischer Lehrsatz**:
  $$ (a + b)^n = \sum_{k=0}^{n} {n\choose k} a^{n-k} b^k $$

- **Permutation von n Objekten**:
  Wenn Objekte in Gruppen mit unterschiedlichen Größen eingeteilt werden, verwendet man die Formel \( \frac{n!}{n_1! \ldots n_k!} \), um die Anzahl der möglichen Anordnungen zu berechnen.

- **Variation mit Zurücklegen**:
  Bei dieser Art der Auswahl kann jedes Objekt mehrmals gewählt werden. Die Anzahl der Möglichkeiten wird mit \( n^k \) berechnet.

- **Variation ohne Zurücklegen**:
  Hier wird jedes Objekt nur einmal gewählt, und die Formel \( \frac{n!}{(n-k)!} \) gibt die Anzahl der möglichen Anordnungen an.

- **Kombination mit Zurücklegen**:
  Diese Formel \( \binom{n+k-1}{k} \) wird verwendet, wenn die Reihenfolge der Auswahl nicht wichtig ist und jedes Objekt mehrmals gewählt werden kann.

- **Geometrische Reihe**:
  Die Summe einer geometrischen Reihe wird mit der Formel \( S_n = \sum_{i=0}^{n}a_0 \cdot q^i = \frac{a_0(1 - q^{n+1})}{1 - q} \) berechnet, wobei \( a_0 \) der erste Term der Reihe und \( q \) der gemeinsame Quotient ist.

- **Quotientenregel**:
  Die Ableitung eines Quotienten von Funktionen \( \left(\frac{f}{g}\right)'(x) \) wird mit der Formel \( \frac{f'(x)g(x) - f(x)g'(x)}{(g(x))^2} \) gefunden.

- **Kettenregel**:
  Die Ableitung einer Verkettung von Funktionen \( (f \circ g)'(x) \) wird mit der Formel \( f'(g(x)) \cdot g'(x) \) berechnet.

- **Ableitung der Umkehrfunktion**
  Die Formel \( (f^{-1}(x))' = \frac{1}{f'(f^{-1}(x))} \) beschreibt, wie man die Ableitung einer Umkehrfunktion \( f^{-1} \) findet. Wenn \( f \) eine differenzierbare Funktion ist und \( f^{-1} \) ihre Umkehrfunktion, dann ist die Ableitung von \( f^{-1} \) an einem Punkt \( x \) der Kehrwert der Ableitung von \( f \) am entsprechenden Punkt \( f^{-1}(x) \).

- **Das Newton-Verfahren**
  Das Newton-Verfahren, gegeben durch \( x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)} \), ist eine Methode zur näherungsweisen Bestimmung von Nullstellen einer Funktion. Hierbei ist \( x_k \) ein Näherungswert und \( x_{k+1} \) der verbesserte Näherungswert.

- **Taylorpolynom**
  Das Taylorpolynom \( T_n(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k \) dient der Approximation von Funktionen. Es entwickelt eine Funktion \( f \) in eine Potenzreihe um den Entwicklungspunkt \( x_0 \) bis zum Grad \( n \).

Die Formeln, die Sie in Ihrem Bild haben, sind grundlegende Konzepte der Integralrechnung. Hier ist eine kurze Erklärung für jede:

- **Partielle Integration**:
  Diese Methode wird verwendet, wenn das Integral das Produkt zweier Funktionen ist. Die Formel lautet:
  $$\int_a^b u(x) \cdot v'(x) \, dx = [u(x)\cdot v(x)]_a^b - \int_a^b u'(x) \cdot v(x) \, dx$$
  Sie ermöglicht es, das Integral durch Integration der einen und Ableitung der anderen Funktion zu vereinfachen.

- **Integration durch Substitution**:
  Diese Technik ist nützlich, wenn eine Substitution die Integration erleichtert. Die Formel ist:
  $$\int_a^b f(\phi(x)) \cdot \phi'(x) \, dx = \int_{\phi(a)}^{\phi(b)} f(z) \, dz$$
  Dabei wird eine neue Variable \( z \) eingeführt, die eine Funktion von \( x \) ist, um das Integral zu vereinfachen.

- **Fehlerverstärkung**:
  Diese Formel wird in der Fehlerrechnung verwendet, um zu verstehen, wie sich Fehler in den Eingangsdaten auf das Ergebnis auswirken. Die Formel ist:
  $$\frac{\Delta y}{y} \approx \left| \frac{z f'(x)}{y} \right| \cdot \frac{\Delta x}{x}$$
  für \( y = f(x) \), wobei \( x,y \neq 0 \). Sie gibt an, wie sich relative Fehler in \( x \) auf \( y \) auswirken.