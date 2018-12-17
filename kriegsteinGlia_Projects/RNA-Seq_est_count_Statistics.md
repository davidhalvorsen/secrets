Untitled
================

apparently kallisto is a program for quantifying RNA-seq experiments ... cool!
==============================================================================

<https://pachterlab.github.io/kallisto/starting>
================================================

Abundances are reported in “estimated counts” (est\_counts) and in Transcripts Per Million (TPM).
=================================================================================================

goal of code is to print out a list of est\_counts that are 3 times above the standard deviation
================================================================================================

``` r
# reading in the table. there's a way to get row 1 as the column headers, but I can't remember ... it doesn't matter
abundance_table = read.table("/media/david/Terabyte/Altering_CIRM_Scripts/kriegsteinRadialGliaStudy1/Submitted_Many_Directoies/kallistoOut/Hi_GW16_1/abundance.tsv")
# abundance_table
```

``` r
# I'm only interested in est_counts and data labels here
# it's simpler to just be working with columns 1 and 4
est_counts <- abundance_table$V4
target_id <- abundance_table$V1
# row 1 is text and the rest are #s, so we gotta remove row 1 cause #math
est_counts[1]
```

    ## [1] est_counts
    ## 17354 Levels: 0 0.000100653 0.000103811 0.000104508 ... est_counts

``` r
# list slicing index position 2 (R indexes start at 1, not 0) and going to length of est_counts
est_count_numbers <- est_counts[2:length(est_counts)]
target_id_labels <- target_id[2:length(target_id)]
# est_count_numbers should be 1 less than est_counts ... yup, the math checks out
length(target_id)
```

    ## [1] 197045

``` r
length(target_id_labels)
```

    ## [1] 197044

``` r
length(est_counts)
```

    ## [1] 197045

``` r
length(est_count_numbers)
```

    ## [1] 197044

``` r
#est_count_numbers
length <- length(est_count_numbers)
sum <- 0
# did I mess up the lists? I should get ENST00000461467.1 1.13596; yup :)
# print(est_count_numbers[6])
# print(target_id_labels[6])
highest_number <- 0
for (number in est_count_numbers) {
  # print(number)
  sum <- as.integer(number) + sum
  if(as.integer(number) > highest_number) {
    highest_number <- as.integer(number)
  }
}
# est_count_numbers
print(sum)
```

    ## [1] 3593232

``` r
print(highest_number)
```

    ## [1] 106553

``` r
average <- sum/length
print(average)
```

    ## [1] 18.23568

``` r
#standard_deviation <- sqrt(sum((x - mean(x))^2) / (n - 1))
#sd(est_count_numbers)
#est_count_numbers <- as.integer(est_count_numbers)
standard_deviation <- sqrt(sum((as.integer(est_count_numbers) - mean(as.integer(est_count_numbers)))^2) / (length - 1))
print(standard_deviation)
```

    ## [1] 3047.757

``` r
# using the R standard deviation to make sure that I did the formula right
print(sd(as.integer(est_count_numbers)))
```

    ## [1] 3047.757

``` r
# how many est_counts are above 3Xstandard_deviation + average?
counter <- 0
for (number in est_count_numbers) {
  if (number > (3*standard_deviation+average)) {
    counter <- counter + 1
  }
}
# this is the number that are above 3Xstandarddev + average
print(counter)
```

    ## [1] 463

``` r
# this is the percentage that are 3Xstandarddev + average
# AWESOME! It follows the 68-95-99.7 rule :D
print(100*counter/length(est_count_numbers))
```

    ## [1] 0.2349729

``` r
# Let's print some of the highest #s
# I fiddled a bit and found that 5.4*sd + average filters down to a set of numbers that we can manually check the tsv file for
i <- 1
for (number in est_count_numbers) {
  if (as.integer(number) > (5.40*standard_deviation+average)) {
    print(paste0("The sample titled ", target_id_labels[i], " has a value of ", est_count_numbers[i]))
  }
  i <- i + 1
}
```

    ## [1] "The sample titled ENST00000534336.1 has a value of 19719.3"
    ## [1] "The sample titled ENST00000619449.1 has a value of 23912.9"
    ## [1] "The sample titled ENST00000301071.11 has a value of 30360.3"
    ## [1] "The sample titled ENST00000322002.4 has a value of 58567.5"
    ## [1] "The sample titled ENST00000296755.11 has a value of 23648.3"
    ## [1] "The sample titled ENST00000244745.2 has a value of 106553"
    ## [1] "The sample titled ENST00000607016.1 has a value of 17165.2"
    ## [1] "The sample titled ENST00000612661.1 has a value of 16591"
    ## [1] "The sample titled ENST00000543693.5 has a value of 31955"
    ## [1] "The sample titled ENST00000387347.2 has a value of 23439.8"
    ## [1] "The sample titled ENST00000361624.2 has a value of 37822"

``` r
# print(i)
# SOLID!!! LibreOffice's sort function agrees w/ my math :D
```
