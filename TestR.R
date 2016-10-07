df.hc <- read.csv("hc.csv",sep = ";")

names(df.hc) <- c("nbeval", "f")

plot(df.hc$nbeval,df.hc$f)

s <- split(df.hc$f,list(df.hc$nbeval))

sapply(s,mean)

s <- sapply(split(df.hc$f,list(df.hc$nbeval)),mean)

plot(s)

lines(s)

