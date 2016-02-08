CFLAGS=-Wall -O3 `pkg-config --cflags glib-2.0`
LDFLAGS= -L.
LDLIBS=`pkg-config --libs glib-2.0`

OBJS=main.o
BLOOM_OBJS=hash.o bloom.o

all: main

main: $(OBJS)
	$(CC) $(LDFLAGS) -o $@ $^ $(LDLIBS)

libbloom.a: $(BLOOM_OBJS)
	ar rcs $@ $^


.PHONY: clean
clean:
	-rm main libbloom.a *.o
