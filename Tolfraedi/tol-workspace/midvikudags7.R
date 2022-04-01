library(kableExtra)
library(tidyverse)
library(ggplot2)
library(dplyr)
library(ggpubr)

#1
as <- read.table("https://notendur.hi.is/~ahj/alcho.txt", sep = ";", header = T, encoding = "UTF-8")

#2

ggplot(as, aes(x=alk, y=thyngd)) + geom_point() + labs(x = "Alkahól", y = "þyngd")


ut <- lm(alk~thyngd, data=as)
summary(ut)
