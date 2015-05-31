if ("agricolae" %in% installed.packages() == FALSE) {install.packages('agricolae')}
library('agricolae')

ftdata <- read.csv("./data/time.csv")
ftdata <- ftdata[c('Type','Time')]

# ANOVA and LSD test
sink(file("results.md"), append=FALSE)

cat("## ANOVA TEST\n\nResults from the ANOVA test\n\n```R\n")
anovafit <- aov(Time ~ Type, data=ftdata)
summary(anovafit)
cat("```")

cat("\n\n## LSD TEST\n\nResults from the LSD test\n\n```R")
LSD.test(anovafit,"Type", console=TRUE)
cat("```")


