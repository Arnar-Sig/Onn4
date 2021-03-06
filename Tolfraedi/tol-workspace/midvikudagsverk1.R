---
  title: "Fasteign"
author: "Arnar Sigurðsson"
output: html_document
---
  ```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

# Hluti 1
a)
Lesum inn gögn.

```{r}
install.packages("tidyverse",dependencies = TRUE)
library(tidyverse)
library(ggplot2)
library(dplyr)
library(ggpubr)
as <- read.table("https://notendur.hi.is/~ahj/husnaedisverd_2017_21.csv", sep = ";", header = T, encoding = "UTF-8")
hverfi <- c(200, 220, 270)
```

b)
Veljum þrjú hverfi til að skoða.

```{r}
hverfi <- c(200, 220, 270)
as <- filter(as, matssvaedi%in%hverfi)
glimpse(as)
```
c)
Allar breytur virðast vera af réttri gerð.

d)
```{r}
as <- mutate(as, fermetraverd = kaupverd/birtm2)
as <- mutate(as, fermetraverd = as.integer(fermetraverd))
glimpse(as)
```

e)
```{r}
teg_eign_ser_ib <- factor(c("Einbýlishús", "Íbúðareign", "Parhús", "Raðhús"))
fct_recode(teg_eign_ser_ib, Ibud = "Íbúðareign", Serbyli = "Einbýlishús", Serbyli = "Parhús", Serbyli = "Raðhús")
```

f)
```{r}
hverfi <- c("Kópavogur", "Hafnarfjörður", "Mosfellsbær")
```

# Hluti 2

g)
```{r}
#ggplot(as, aes(fermetraverd)) + geom_histogram(binwidth =55, stat="count") + labs(x = "Fermetraverð", y = "Fjöldi")
ggplot(as, aes(x=fermetraverd)) + geom_histogram(bins = 30) + labs(x = "Fermetraverð", y = "Fjöldi")

ggplot(as, aes(x=birtm2)) + geom_histogram(bins = 30) + labs(x = "Birt m2", y = "Fjöldi")

```


h)
```{r}
#ggplot(as, aes(x = haed, y = thyngd)) + geom_bar(stat='identity' ) + labs(x = "Hæð", y="Þyngd") + facet_grid(~kyn)

#ggplot(as, aes(x = teg_eign, y = matssvaedi)) + geom_bar(stat='identity' ) + labs(x = "Hæð", y="Þyngd")

#ggplot(as, aes(x = byggar, y = matssvaedi, color = as.factor(teg_eign))) + geom_point() 

ggplot(as, aes(x = byggar, y = matssvaedi, fill = teg_eign)) + geom_bar(stat='identity') + labs(x = "Byggingarár", y = "Matssvæði")



```

i)
```{r}
ggboxplot(as, x = "matssvaedi", y = "fermetraverd",
          color = "darkgreen", palette = "jco") + labs(x = "Póstnúmer", y = "Fermetraverð")
```





