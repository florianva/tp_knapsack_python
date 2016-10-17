df.time <- read.table("time.csv", sep=";")
names(df.time) <- c("nbeval", "seconds")
plot(seconds ~ nbeval, data = df.time)

df.time2 <- read.table("time2.csv", sep=";")
names(df.time2) <- c("nbeval", "seconds")
points(seconds ~ nbeval, data = df.time2)