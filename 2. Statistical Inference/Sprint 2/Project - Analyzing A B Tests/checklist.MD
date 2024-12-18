A/B Test project: (transfer to DS notebook later)

- [ ] Do Cookie cats EDA
    - [x] Goal
    - [x] Target metric
    - [x] Sample Size
    - [x] Variant proportions
    - [x] Statistical tests (describe which test you have chosen for each metric and why)
        - [x] Student’s t-test, binomial test and the chi-square test. Here are some good resources on them (links in
          Turing)

    * [Student’s t-test](https://www.youtube.com/watch?v=pTmLQvMM-1M)
      and [Scipy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
    * [Chi-square test](https://www.youtube.com/watch?v=jABsbNBPXIk)
      and [Scipy documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html)

        - [ ] feel free to check your numbers against those given by
          the [Evan Miller A/B Test Calculator.](https://www.evanmiller.org/ab-testing/)

    - [x] Report the estimated treatment effect
    - [x] compute the confidence interval
        - [x] analytically
        - [ ] using bootstrap
        - [ ] report both intervals
    - [x] Describe clearly what your calculations imply and which decision you recommend
    - [x] Use visualizations to show differences in the metric between groups and confidence intervals
    - [ ] Create a dashboard with at least two plots