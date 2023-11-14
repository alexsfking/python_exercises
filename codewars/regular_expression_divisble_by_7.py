'''
Regular Expression - Check if divisible by 0b111 (7)

Create a regular expression capable of evaluating binary strings (which consist of only 1's and 0's) and determining whether the given string represents a number divisible by 7.

Note:

Empty strings should be rejected.
Your solution should reject strings with any character other than 0 and 1.
No leading 0's will be tested unless the string exactly denotes 0.
'''

solution = r'^(0|1((1(01*00)*01*01|(0|1(01*00)*01*011)((0|1(1|0(01*00)*01*01))1)*(0|1(1|0(01*00)*01*01)))0)*(1|(0|1(01*00)*01*011)((0|1(1|0(01*00)*01*01))1)*10)(01*00)*1)+$'

r'''
dfa divisble by 7
\documentclass[12pt]{article}
\usepackage{tikz}

\begin{document}

\begin{center}
\begin{tikzpicture}[scale=0.2]
\tikzstyle{every node}+=[inner sep=0pt]
\draw [black] (16.1,-12.7) circle (3);
\draw (16.1,-12.7) node {$0$};
\draw [black] (28.2,-20.1) circle (3);
\draw (28.2,-20.1) node {$1$};
\draw [black] (28.2,-32.9) circle (3);
\draw (28.2,-32.9) node {$2$};
\draw [black] (35,-12.1) circle (3);
\draw (35,-12.1) node {$3$};
\draw [black] (11.2,-32.9) circle (3);
\draw (11.2,-32.9) node {$4$};
\draw [black] (43.7,-32.9) circle (3);
\draw (43.7,-32.9) node {$5$};
\draw [black] (28.2,-4.4) circle (3);
\draw (28.2,-4.4) node {$6$};
\draw [black] (5.5,-13.6) -- (13.11,-12.95);
\fill [black] (13.11,-12.95) -- (12.27,-12.52) -- (12.36,-13.52);
\draw [black] (14.777,-10.02) arc (234:-54:2.25);
\draw (16.1,-5.45) node [above] {$0$};
\fill [black] (17.42,-10.02) -- (18.3,-9.67) -- (17.49,-9.08);
\draw [black] (18.66,-14.27) -- (25.64,-18.53);
\fill [black] (25.64,-18.53) -- (25.22,-17.69) -- (24.7,-18.54);
\draw (21.15,-16.9) node [below] {$1$};
\draw [black] (28.2,-23.1) -- (28.2,-29.9);
\fill [black] (28.2,-29.9) -- (28.7,-29.1) -- (27.7,-29.1);
\draw (27.7,-26.5) node [left] {$0$};
\draw [black] (30.14,-17.81) -- (33.06,-14.39);
\fill [black] (33.06,-14.39) -- (32.16,-14.67) -- (32.92,-15.32);
\draw (32.15,-17.54) node [right] {$1$};
\draw [black] (14.119,-32.211) arc (100.48606:79.51394:30.668);
\fill [black] (14.12,-32.21) -- (15,-32.56) -- (14.81,-31.57);
\draw (19.7,-31.2) node [above] {$0$};
\draw [black] (31.2,-32.9) -- (40.7,-32.9);
\fill [black] (40.7,-32.9) -- (39.9,-32.4) -- (39.9,-33.4);
\draw (35.95,-33.4) node [below] {$1$};
\draw [black] (33.01,-9.85) -- (30.19,-6.65);
\fill [black] (30.19,-6.65) -- (30.34,-7.58) -- (31.09,-6.92);
\draw (32.14,-6.8) node [right] {$0$};
\draw [black] (32,-12.2) -- (19.1,-12.6);
\fill [black] (19.1,-12.6) -- (19.91,-13.08) -- (19.88,-12.08);
\draw (25.53,-11.87) node [above] {$1$};
\draw [black] (13.6,-31.1) -- (25.8,-21.9);
\fill [black] (25.8,-21.9) -- (24.86,-21.99) -- (25.47,-22.79);
\draw (20.7,-27) node [below] {$0$};
\draw [black] (25.297,-33.652) arc (-78.52742:-101.47258:28.141);
\fill [black] (25.3,-33.65) -- (24.41,-33.32) -- (24.61,-34.3);
\draw (19.7,-34.71) node [below] {$1$};
\draw [black] (42.54,-30.13) -- (36.16,-14.87);
\fill [black] (36.16,-14.87) -- (36.01,-15.8) -- (36.93,-15.41);
\draw (40.09,-21.57) node [right] {$0$};
\draw [black] (41.498,-34.934) arc (-51.10753:-128.89247:22.375);
\fill [black] (13.4,-34.93) -- (13.71,-35.83) -- (14.34,-35.05);
\draw (27.45,-40.39) node [below] {$1$};
\draw [black] (31.188,-4.622) arc (81.08753:-24.00756:18.39);
\fill [black] (45.14,-30.27) -- (45.92,-29.74) -- (45.01,-29.34);
\draw (45.17,-12.82) node [right] {$0$};
\draw [black] (25.52,-5.723) arc (324:36:2.25);
\draw (20.95,-4.4) node [left] {$1$};
\fill [black] (25.52,-3.08) -- (25.17,-2.2) -- (24.58,-3.01);
\end{tikzpicture}
\end{center}

\end{document}

'''