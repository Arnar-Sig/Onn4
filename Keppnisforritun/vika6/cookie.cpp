#define PARENT(i) ((i−1)/2)
#define LEFT(i) ((i)∗2+1)
#define RIGHT(i) ((i)∗2+2)



int h[3000], hn=0;
voidswap(int∗x,int∗y){intt=∗x;∗x=∗y;∗y=t;}
voidfix_down(inti)//Hjálparfall.
{//Ferðastniðurtréðoglagarhrúguskilyrðiðáleiðinni.
intmx=i;
if(RIGHT(i)<hn&&h[mx]<h[RIGHT(i)])mx=RIGHT(i);
if(LEFT(i)<hn&&h[mx]<h[LEFT(i)])mx=LEFT(i);
if(mx!=i)swap(&h[i],&h[mx]),fix_down(mx);
}

voidfix_up(inti)//Hjálparfall.
{//Ferðastupptréðoglagarhrúguskilyrðiðáleiðinni.
if(i==0||h[i]<=h[PARENT(i)])return;
swap(&h[i],&h[PARENT(i)]),fix_up(PARENT(i));
}

voidpop()
{//Fjarlægirstærstastakið.
h[0]=h[−−hn];
fix_down(0);
}

intpeek(){returnh[0];}//Skilarstærstastakinu.
intsize(){returnhn;}//Skilarstærðhrúgurnar.
voidpush(intx)
{//Bætirxviðhrúguna.
h[hn++]=x;
fix_up(hn−1);
}