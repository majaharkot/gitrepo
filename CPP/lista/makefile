CXX=g++
CXXFLAGS=-Wall -I.
OBJS=lista.o main.o

pong: lista.o main.o
	$(CXX) $(CXXFLAGS) $(OBJS) -o main.exe

.PHONY: clean

clean:
	rm -f *.o *~ core *~
