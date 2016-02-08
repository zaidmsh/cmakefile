#include <stdio.h>
#include <glib.h>

int main(){
  GString * s;
  char hello[] = "Hello World";

  printf("Hello World\n");
  s = g_string_new (hello);
  printf("%s\n", s->str);
  hello[0] = 'A';
  printf("%s\n", s->str);
  g_string_free(s, TRUE);

  return 0;
}
