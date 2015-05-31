install.packages('agricolae')
library('agricolae')

ftdata <- read.csv("./data/time.csv")
ftdata <- ftdata[c('Type','Time')]
data(ftdata)

# ANOVA test
fit <- aov(Time ~ Type, data=ftdata)

layout(matrix(c(1,2,3,4),2,2))
LSD.test(fit,"Type", console=TRUE)
summary(fit)
plot(fit)

