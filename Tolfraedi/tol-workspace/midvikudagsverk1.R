library(tidyverse)
library(forcats)
library(ggplot2)

#1
AS <- read.table("https://notendur.hi.is/ahj/pulsAll.csv", sep = ";", header = T)

#2
glimpse(AS)
AS <- mutate(AS, kyn = factor(kyn))
glimpse(AS)
AS <- mutate(AS, kyn = fct_recode(kyn, kvk = "1", kk = "2"))
glimpse(AS)
levels(AS$kyn)

#3
ggplot(AS, aes(x=thyngd)) + geom_histogram(binwidth=2) 

#4
#bins fyrir fjölda súlna
#geom_bar = stöplarit fyrir flokkabreytu

ggplot(AS, aes(x=kyn)) + geom_histogram(stat="count") + labs(x = "Kyn", y = "Fjöldi")

#5
ggplot(AS, aes(x=haed)) + geom_histogram(stat="count") + labs(x = "Hæð", y = "Fjöldi")

#6
ggplot(AS, aes(x = kyn, y = haed)) + geom_boxplot() + labs(x = "Kyn", y = "Hæð")

#7
ggplot(AS, aes(x = thyngd, y = haed)) + geom_point() + labs(x = "Þyngd", y="Hæð")

#8



# ggplot(AS, aes(x = haed, y = thyngd)) + geom_bar(stat='identity' ) + labs(x = "Hæð", y="Þyngd")
# + facet_grid(~kyn) til að skipta mynd upp eftir kyni