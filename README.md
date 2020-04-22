# hana
A small project exploring means to factor products quicker.

Start from command line.
Enter cutoff time (in minutes) as a raw integer
Enter the product to factor, without commas or other groupings.

And then wait for the result

Some example integers to factor:

Tested on i3, 8gb, so values will vary depending on platform and hardware specs.

429254299  #29 bit product (bp), 0.084s
3042682187 #32 bp, 0.018s
12726373969 #34 bp, 0.196s
356889940171 #39 bp, 1.074s
357743275661 #39 bp, 0.009s
187059223843 #39 bp, 1.032s
47830882408963 #46 bp,  14.29s
116689160461591 #47 bp, 2.26s
174135918609547 #48 bp, 8.21s
51387724749645829 #56 bp, 619.38s
44625110273700793 #56 bp, 139.02s - 182.37s
1047334517890082159 #60 bp, 
15113860026906136319 #64 bp,
107196521941992871667 #67 bp, 5645.70s (about 94 minutes).

Take measurements with a grain of salt.

Will be posting other exploratory or ideas here as time goes on.

Let me know if there are problems, as well as what your results are.
Open to suggestions, improvements, bugs etc.

Made in Python 3.7.2




