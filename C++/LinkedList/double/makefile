CC = g++
CFLAGS = -Wall -g

linked: main.o dll.o
	$(CC) $(CFLAGS) -o linked main.o dll.o

main.o: main.cpp
	$(CC) $(CFLAGS) -c main.cpp

dll.o: dll.cpp dll.h
	$(CC) $(CFLAGS) -c dll.cpp

clean:
	$(RM) linked *.o *~
