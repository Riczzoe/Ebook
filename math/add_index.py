from PyPDF2 import PdfReader, PdfWriter

def add_hierarchical_bookmarks(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # 复制页面
    for page in reader.pages:
        writer.add_page(page)

    writer.add_bookmark("Contents", 6)

    # 根目录
    chapter1 = writer.add_bookmark("1 Let's Count!", 1 + 9)
    chapter2 = writer.add_bookmark('2 Combinatorial Tools', 25 + 9)
    chapter3 = writer.add_bookmark("3 Binomial Coefficients and Pascal's Triangle", 43 + 9)
    chapter4 = writer.add_bookmark("4 Fibonacci Numbers", 65 + 9)
    chapter5 = writer.add_bookmark("5 Combinatorial Probability", 77 + 9)
    chapter6 = writer.add_bookmark("6 Integers, Divisors, and Primes", 87 + 9)
    chapter7 = writer.add_bookmark("7 Graphs", 125 + 9)
    chapter8 = writer.add_bookmark("8 Trees", 141 + 9)
    chapter9 = writer.add_bookmark("9 Finding the Optimum", 157 + 9)
    chapter10 = writer.add_bookmark("10 Matchings in Graphs", 165 + 9)
    chapter11 = writer.add_bookmark("11 Combinatorics in Geometry", 179 + 9)
    chapter12 = writer.add_bookmark("12 Euler's Formula", 189 + 9)
    chapter13 = writer.add_bookmark("13 Coloring Maps and Graphs", 197 + 9)
    chapter14 = writer.add_bookmark("14 Finite Geometries, Codes, Latin Squares, and Other Pretty Creatures", 211 + 9)
    chapter15 = writer.add_bookmark("15 A Glimpse of Complexity and Cryptography", 239 + 9)
    chapter16 = writer.add_bookmark("16 Answers to Exercises", 251 + 9)
    index = writer.add_bookmark("Index", 287 + 9)

    # 1. Let's Count!
    writer.add_bookmark('1.1 A Party', 1 + 9, parent=chapter1)
    writer.add_bookmark('1.2 Sets and the Like', 4 + 9, parent=chapter1)
    writer.add_bookmark('1.3 The Number of Subsets', 9 + 9, parent=chapter1)
    writer.add_bookmark('1.4 The Approximate Number of Subsets', 14 + 9, parent=chapter1)
    writer.add_bookmark('1.5 Sequences', 15 + 9, parent=chapter1)
    writer.add_bookmark('1.6 Permutations', 17 + 9, parent=chapter1)
    writer.add_bookmark('1.7 The Number of Ordered Subsets', 19 + 9, parent=chapter1)
    writer.add_bookmark('1.8 The Number of Subsets of a Given Size', 20 + 9, parent=chapter1)

    # 2. Combinatorial Tools
    writer.add_bookmark('2.1 Induction', 25 + 9, parent=chapter2)
    writer.add_bookmark('2.2 Comparing and Estimating Numbers', 30 + 9, parent=chapter2)
    writer.add_bookmark('2.3 Inclusion-Exclusion', 32 + 9, parent=chapter2)
    writer.add_bookmark('2.4 Pigeonholes', 34 + 9, parent=chapter2)
    writer.add_bookmark('2.5 The Twin Paradox and the Good Old Logarithm', 37 + 9, parent=chapter2)

    # 3. Binomial Coefficients and Pascal's Triangle
    writer.add_bookmark('3.1 The Binomial Theorem', 43 + 9, parent=chapter3)
    writer.add_bookmark('3.2 Distributing Presents', 45 + 9, parent=chapter3)
    writer.add_bookmark('3.3 Anagrams', 46 + 9, parent=chapter3)
    writer.add_bookmark('3.4 Distributing Money', 48 + 9, parent=chapter3)
    writer.add_bookmark("3.5 Pascal's Triangle", 49 + 9, parent=chapter3)
    writer.add_bookmark("3.6 Identities in Pascal's Triangle", 50 + 9, parent=chapter3)
    writer.add_bookmark("3.7 A Bird's-Eye View of Pascal's Triangle", 54 + 9, parent=chapter3)
    writer.add_bookmark("3.8 An Eagle's-Eye View: Fine Details", 57 + 9, parent=chapter3)

    # 4. Fibonacci Numbers
    writer.add_bookmark("4.1 Fibonacci's Exercise", 65 + 9, parent=chapter4)
    writer.add_bookmark("4.2 Lots of Identities", 68 + 9, parent=chapter4)
    writer.add_bookmark("4.3 A Formula for the Fibonacci Numbers", 71 + 9, parent=chapter4)

    # 5. Combinatorial Probability
    writer.add_bookmark("5.1 Events and Probabilities", 77 + 9, parent=chapter5)
    writer.add_bookmark("5.2 Independent Repetition of an Experiment", 79 + 9, parent=chapter5)
    writer.add_bookmark("5.3 The Law of Large Numbers", 80 + 9, parent=chapter5)
    writer.add_bookmark("5.4 The Law of Small Numbers and the Law of Very Large Numbers", 83 + 9, parent=chapter5)

    # 6. Integers, Divisors, and Primes
    writer.add_bookmark("6.1 Divisibility of Integers", 87 + 9, parent=chapter6)
    writer.add_bookmark("6.2 Primes and Their History", 88 + 9, parent=chapter6)
    writer.add_bookmark("6.3 Factorization into Primes", 90 + 9, parent=chapter6)
    writer.add_bookmark("6.4 On the Set of Primes", 93 + 9, parent=chapter6)
    writer.add_bookmark("6.5 Fermat's 'Little' Theorem", 97 + 9, parent=chapter6)
    writer.add_bookmark("6.6 The Euclidean Algorithm", 99 + 9, parent=chapter6)
    writer.add_bookmark("6.7 Congruences", 105 + 9, parent=chapter6)
    writer.add_bookmark("6.8 Strange Numbers", 107 + 9, parent=chapter6)
    writer.add_bookmark("6.9 Number Theory and Combinatorics", 114 + 9, parent=chapter6)
    writer.add_bookmark("6.10 How to Test Whether a Number is a Prime?", 117 + 9, parent=chapter6)

    # 7. Graphs
    writer.add_bookmark("7.1 Even and Odd Degrees", 125 + 9, parent=chapter7)
    writer.add_bookmark("7.2 Paths, Cycles, and Connectivity", 130 + 9, parent=chapter7)
    writer.add_bookmark("7.3 Eulerian Walks and Hamiltonian Cycles", 135 + 9, parent=chapter7)

    # 8. Trees
    writer.add_bookmark("8.1 How to Define Trees", 141 + 9, parent=chapter8)
    writer.add_bookmark("8.2 How to Grow Trees", 143 + 9, parent=chapter8)
    writer.add_bookmark("8.3 How to Count Trees?", 146 + 9, parent=chapter8)
    writer.add_bookmark("8.4 How to Store Trees", 148 + 9, parent=chapter8)
    writer.add_bookmark("8.5 The Number of Unlabeled Trees", 153 + 9, parent=chapter8)

    # 9. Finding the Optimum
    writer.add_bookmark("9.1 Finding the Best Tree", 157 + 9, parent=chapter9)
    writer.add_bookmark("9.2 The Traveling Salesman Problem", 161 + 9, parent=chapter9)

    # 10. Matchings in Graphs
    writer.add_bookmark("10.1 A Dancing Problem", 165 + 9, parent=chapter10)
    writer.add_bookmark("10.2 Another Matching Problem", 167 + 9, parent=chapter10)
    writer.add_bookmark("10.3 The Main Theorem", 169 + 9, parent=chapter10)
    writer.add_bookmark("10.4 How to Find a Perfect Matching", 171 + 9, parent=chapter10)

    # 11. Combinatorics in Geometry
    writer.add_bookmark("11.1 Intersections of Diagonals", 179 + 9, parent=chapter11)
    writer.add_bookmark("11.2 Counting Regions", 181 + 9, parent=chapter11)
    writer.add_bookmark("11.3 Convex Polygons", 184 + 9, parent=chapter11)

    # 12. Euler's Formula
    writer.add_bookmark("12.1 A Planet Under Attack", 189 + 9, parent=chapter12)
    writer.add_bookmark("12.2 Planar Graphs", 192 + 9, parent=chapter12)
    writer.add_bookmark("12.3 Euler's Formula for Polyhedra", 194 + 9, parent=chapter12)

    # 13. Coloring Maps and Graphs
    writer.add_bookmark("13.1 Coloring Regions with Two Colors", 197 + 9, parent=chapter13)
    writer.add_bookmark("13.2 Coloring Graphs with Two Colors", 199 + 9, parent=chapter13)
    writer.add_bookmark("13.3 Coloring Graphs with Many Colors", 202 + 9, parent=chapter13)
    writer.add_bookmark("13.4 Map Coloring and the Four Color Theorem", 204 + 9, parent=chapter13)

    # 14. Finite Geometries, Codes, Latin Squares, and Other Pretty Creatures
    writer.add_bookmark("14.1 Small Exotic Worlds", 211 + 9, parent=chapter14)
    writer.add_bookmark("14.2 Finite Affine and Projective Planes", 217 + 9, parent=chapter14)
    writer.add_bookmark("14.3 Block Designs", 220 + 9, parent=chapter14)
    writer.add_bookmark("14.4 Steiner Systems", 224 + 9, parent=chapter14)
    writer.add_bookmark("14.5 Latin Squares", 229 + 9, parent=chapter14)
    writer.add_bookmark("14.6 Codes", 232 + 9, parent=chapter14)

    # 15. A Glimpse of Complexity and Cryptography
    writer.add_bookmark("15.1 A Connecticut Class in King Arthur's Court", 239 + 9, parent=chapter15)
    writer.add_bookmark("15.2 Classical Cryptography", 242 + 9, parent=chapter15)
    writer.add_bookmark("15.3 How to Save the Last Move in Chess", 244 + 9, parent=chapter15)
    writer.add_bookmark("15.4 How to Verify a Password—Without Learning It", 246 + 9, parent=chapter15)
    writer.add_bookmark("15.5 How to Find These Primes", 246 + 9, parent=chapter15)
    writer.add_bookmark("15.6 Public Key Cryptography", 247 + 9, parent=chapter15)

    with open(output_pdf, "wb") as f_out:
        writer.write(f_out)

# 路径设置
input_pdf_path = 'Discrete mathematics.pdf'  # 输入文件路径
output_pdf_path = 'Discrete mathematics.pdf'    # 输出文件路径
add_hierarchical_bookmarks(input_pdf_path, output_pdf_path)
