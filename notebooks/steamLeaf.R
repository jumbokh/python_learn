data <- c(1, 35, 57, 40, 73, 82, 68, 69, 52, 1, 23, 35, 55, 65, 48, 93, 59, 87, 2, 64)

stem(data)

battery <- read.csv(file = "stemnleaf.txt", header=FALSE)
# remove na in r - test for missing values (is.na example)
battery <- battery[!is.na(battery)]
stem(battery)
