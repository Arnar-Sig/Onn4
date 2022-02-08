#5.5.14
#1
qnorm(0.975) #lausn á z0.975 t.d.
qnorm(0.1)
qnorm(0.05)
qnorm(0.95)

#2
qt(0.95,40)
qt(0.90,3)
qt(0.975,17)
qt(0.05,12)

#3
qchisq(0.95,1) #q finnur töluna, p prósentuna til vinstri?
qchisq(0.05, 2)
qchisq(0.975,17)
qchisq(0.99,3)

#4
qf(0.95,10,20)
qf(0.90,20,10)
qf(0.975,3,17)
qf(0.99,5,5)

#5.5.15
#qnorm ef maður hefur prósentu, pnorm ef maður hefur töluna
pnorm(-0.82)
pnorm(1.96)
pnorm(1.65)
pnorm(0)


#5.5.18
#1
pnorm(20, 21, 2.8)

#2
1 - pnorm(30, 21, 2.8)

#3
pnorm(19, 21, 2.8) - pnorm(17, 21, 2.8)

#4
pnorm(27, 21, 2.8) - pnorm(25, 21, 2.8)

#5 # ekki hægt að fá nákvæmlega 1 gildi?
pnorm(30, 21, 2.8) - pnorm(29, 21, 2.8)


#5.5.20

#1
# ekki hægt að fá nákvæmlega eitt gildi

#2
1 - pnorm(10, 8.2, 2.2)

#3
pnorm(12, 8.2, 2.2) - pnorm(10, 8.2, 2.2)

#4
pnorm(3.7, 8.2, 2.2)

#5
qnorm(0.9, 8.2, 2.2)

#6
qnorm(0.2, 8.2, 2.2)
