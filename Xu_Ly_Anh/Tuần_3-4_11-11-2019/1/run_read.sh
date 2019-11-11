INCLUDE=`pkg-config --cflags opencv`
LIBS=`pkg-config --libs opencv`
g++ ${INCLUDE} read.cpp ${LIBS} -o read -std=c++11 && ./read && rm read