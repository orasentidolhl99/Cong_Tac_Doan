INCLUDE=`pkg-config --cflags opencv`
LIBS=`pkg-config --libs opencv`
g++ ${INCLUDE} write.cpp ${LIBS} -o write -std=c++11 && ./write && rm write